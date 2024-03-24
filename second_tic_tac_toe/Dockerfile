# Utiliser une image de base Python
FROM python:3.9-slim

# Installer les dépendances nécessaires pour Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
 && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port 4616
EXPOSE 4616

# Commande pour exécuter l'application
CMD ["python3", "test.py"]