"""
Reconnexion automatique au Wi-Fi IMT-PUBLIC (portail captif).
"""
import requests
import time
import logging
import urllib3
from datetime import datetime

# Désactive les warnings SSL (le portail captif intercepte parfois le HTTPS)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# === CONFIGURATION ===
PORTAL_URL = "https://controller.access.network/portal_api.php"
LOGIN = "IMTPUBLIC"
PASSWORD = "IMTtours2526"
CHECK_INTERVAL = 60          # vérifier la connexion toutes les 60 s
RECONNECT_EVERY = 6500       # forcer reconnexion préventive toutes les ~1h48
TEST_URL = "http://neverssl.com"  # site HTTP pour détecter un portail captif

# === LOGGING ===
logging.basicConfig(
    filename="wifi_imt.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
# Affiche aussi dans la console
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logging.getLogger().addHandler(console)


def is_connected() -> bool:
    """
    Vrai si on a un vrai accès internet (pas de portail captif).
    neverssl.com renvoie une page contenant 'NeverSSL' si l'accès est libre.
    Si on est intercepté par le portail, on est redirigé ou on reçoit autre chose.
    """
    try:
        r = requests.get(TEST_URL, timeout=5, allow_redirects=False)
        # 200 direct = OK ; 3xx = redirection vers portail = pas connecté
        return r.status_code == 200 and "neverssl" in r.text.lower()
    except requests.RequestException:
        return False


def authenticate() -> bool:
    """Soumet le formulaire de connexion au portail captif."""
    data = {
        "action": "authenticate",
        "login": LOGIN,
        "policy_accept": "false",
        "private_policy_accept": "false",
        "from_ajax": "true",
        "password": PASSWORD,
        "wispr_mode": "false",
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0",
    }
    try:
        r = requests.post(
            PORTAL_URL, data=data, headers=headers,
            timeout=10, verify=False,
        )
        ok = r.status_code == 200 and '"type":"CONNECT"' in r.text
        if ok:
            logging.info("✅ Connexion réussie au portail IMT")
        else:
            logging.warning(f"⚠️ Échec connexion (HTTP {r.status_code}) : {r.text[:200]}")
        return ok
    except requests.RequestException as e:
        logging.error(f"❌ Erreur réseau lors de l'authentification : {e}")
        return False


def main():
    logging.info("=== Démarrage du keep-alive Wi-Fi IMT ===")
    last_login = 0
    while True:
        now = time.time()
        connected = is_connected()
        elapsed = now - last_login

        if not connected:
            logging.info("🔌 Pas d'accès internet, tentative de connexion...")
            if authenticate():
                last_login = now
        elif elapsed >= RECONNECT_EVERY:
            logging.info("⏰ Reconnexion préventive (avant déconnexion auto)")
            if authenticate():
                last_login = now
        else:
            logging.debug("Connexion OK")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Arrêt manuel.")
