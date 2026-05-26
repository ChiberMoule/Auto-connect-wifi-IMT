# 📡 Wi-Fi IMT Auto-Reconnect

Script Python qui maintient automatiquement la connexion au portail Wi-Fi IMT en se reconnectant toutes les 60 secondes si nécessaire.

---

## 📋 Prérequis

- Python 3.x installé
- Le fichier `auto-connect.py` présent sur ton Bureau

---

## 🐍 1. Installer Python

### macOS
1. Va sur [https://python.org](https://python.org)
2. Télécharge la dernière version pour macOS
3. Lance l'installateur et suis les étapes

Vérifie l'installation dans le Terminal :
\```bash
python3 --version
\```

### Windows
1. Va sur [https://python.org](https://python.org)
2. Télécharge la dernière version pour Windows
3. Lance l'installateur
4. ⚠️ **Coche bien "Add Python to PATH"** avant de cliquer sur Install

Vérifie l'installation dans l'invite de commandes :
\```cmd
python --version
\```

---

## 📦 2. Installer la dépendance

### macOS
\```bash
pip3 install requests
\```
Si erreur :
\```bash
python3 -m pip install requests
\```

### Windows
\```cmd
pip install requests
\```
Si erreur :
\```cmd
python -m pip install requests
\```

---

## ▶️ 3. Lancer le script

### macOS

**Mode normal** (logs visibles dans le Terminal) :
\```bash
cd ~/Desktop
python3 auto-connect.py
\```
> ⚠️ Fermer le Terminal arrête le script.

**Mode arrière-plan** (survit à la fermeture du Terminal) :
\```bash
cd ~/Desktop
nohup python3 auto-connect.py > /dev/null 2>&1 &
\```
> Les logs sont enregistrés dans `~/Desktop/wifi_imt.log`.

### Windows

**Mode normal** (logs visibles dans l'invite de commandes) :
\```cmd
cd %USERPROFILE%\Desktop
python auto-connect.py
\```
> ⚠️ Fermer la fenêtre cmd arrête le script.

**Mode arrière-plan** (survit à la fermeture de cmd) :
\```cmd
cd %USERPROFILE%\Desktop
start /B pythonw auto-connect.py
\```
> Les logs sont enregistrés dans `%USERPROFILE%\Desktop\wifi_imt.log`.

---

## ⏹️ 4. Arrêter le script

### macOS

Mode normal :
\```
Ctrl + C
\```

Mode arrière-plan :
\```bash
pkill -f auto-connect.py
\```

Vérifier si le script tourne :
\```bash
ps aux | grep auto-connect.py
\```

### Windows

Mode normal :
\```
Ctrl + C
\```

Mode arrière-plan :
\```cmd
taskkill /F /IM pythonw.exe
\```

Vérifier si le script tourne :
\```cmd
tasklist | findstr python
\```

---

## 📄 5. Consulter les logs

### macOS

Voir les dernières lignes :
\```bash
tail -n 30 ~/Desktop/wifi_imt.log
\```

Suivre en direct :
\```bash
tail -f ~/Desktop/wifi_imt.log
\```

Vider le log :
\```bash
> ~/Desktop/wifi_imt.log
\```

### Windows

Voir le contenu du log :
\```cmd
type %USERPROFILE%\Desktop\wifi_imt.log
\```

Vider le log :
\```cmd
type nul > %USERPROFILE%\Desktop\wifi_imt.log
\```

---

## 💤 6. Comportement selon l'état de la machine

| Action | macOS | Windows |
|---|---|---|
| Réduire la fenêtre | ✅ Continue | ✅ Continue |
| Verrouiller l'écran | ✅ Continue | ✅ Continue |
| Fermer le capot / mise en veille | ⏸️ Pause, reprend au réveil | ⏸️ Pause, reprend au réveil |
| Fermer Terminal / cmd (mode normal) | ❌ Arrêt | ❌ Arrêt |
| Fermer Terminal / cmd (mode arrière-plan) | ✅ Continue | ✅ Continue |
| Redémarrer / éteindre | ❌ Arrêt, à relancer | ❌ Arrêt, à relancer |

---

## 🗂️ 7. Fichiers du projet

| Fichier | Description |
|---|---|
| `auto-connect.py` | Script principal |
| `wifi_imt.log` | Fichier de logs (créé automatiquement au premier lancement) |
| `README.md` | Ce fichier |

---

## 🆘 En cas de problème

1. Lance le script en **mode normal** pour voir les logs dans le terminal
2. Copie les messages d'erreur
3. Vérifie que tu es bien connecté au réseau **Wi-Fi IMT** avant de lancer le script
# Auto-connect-wifi-IMT
Dans ce Git, vous trouverez la procédure et le script pour automatiser la connexion au réseau wifi de l'IMT.
