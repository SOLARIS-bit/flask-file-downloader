# Flask File Downloader

![GitHub repo size](https://img.shields.io/github/repo-size/SOLARIS-bit/flask-file-downloader)
![Docker Image Size](https://img.shields.io/docker/image-size/library/python/latest)
![GitHub last commit](https://img.shields.io/github/last-commit/SOLARIS-bit/flask-file-downloader)
![GitHub issues](https://img.shields.io/github/issues/SOLARIS-bit/flask-file-downloader)
![GitHub license](https://img.shields.io/github/license/SOLARIS-bit/flask-file-downloader)

Une application web simple qui permet de :

- Naviguer dans un répertoire de fichiers
- Rechercher un fichier
- Télécharger un fichier
- Téléverser un fichier
- Consommer une API REST avec JavaScript
- Lancer l'application via Docker

## 🌐 Interface utilisateur

L'application permet d'afficher tous les fichiers présents dans le dossier `data` avec leur taille et date de modification. Elle permet aussi de :

- Télécharger chaque fichier
- Uploader un nouveau fichier
- Rechercher dynamiquement un fichier (JavaScript)

## 🔧 Endpoints API

| Méthode | Endpoint                  | Description                                 |
|---------|---------------------------|---------------------------------------------|
| GET     | `/api/files`              | Retourne la liste des fichiers              |
| GET     | `/api/download/<filename>`| Télécharge un fichier                       |
| POST    | `/api/upload`             | Upload un fichier                           |

## 🚀 Démarrage rapide avec Docker

docker build -t flask-file-downloader .
docker run -d -p 5000:5000 flask-file-downloader

Accès via `http://localhost:5000`

## 🧪 Tests
Lance les tests unitaires avec :

pytest

## 📁 Structure

flask-file-downloader/
├── app.py
├── data/
├── templates/
├── static/
├── test_app.py
├── Dockerfile
├── requirements.txt
└── README.md

## 🐳 Technologies
1. Python 3.11
2. Flask
3. Docker
4. HTML + Bootstrap
5. JavaScript

### 🤝 Auteur
SOLARIS-bit
Projet Flask personnel — Docker + API + Interface web simple
