
import subprocess

# Spécifiez les informations du référentiel et du fichier à pousser
repository_url = "https://github.com/enupten/serveur.git"
file_path = "data/test.txt"
commit_message = "Mise à jour du fichier depuis Python"

# Effectuez un "git add" pour ajouter le fichier
subprocess.run(["git", "add", file_path])

# Effectuez un "git commit" avec un message de commit
subprocess.run(["git", "commit", "-m", commit_message])

# Effectuez un "git push" pour pousser les modifications vers GitHub
subprocess.run(["git", "push", repository_url, "master"])