import threading
import requests
import time

# Fonction pour télécharger un fichier
def download_file(url, file_name):
    print(f"Début du téléchargement de {file_name} depuis {url}")
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"Terminé : {file_name}")

# Liste des fichiers à télécharger
files_to_download = [
    {"url": "https://www.example.com/file1.jpg", "file_name": "file1.jpg"},
    {"url": "https://www.example.com/file2.jpg", "file_name": "file2.jpg"},
    {"url": "https://www.example.com/file3.jpg", "file_name": "file3.jpg"},
]

# Mesurer le temps d'exécution sans multithreading
start_time = time.time()
for file_info in files_to_download:
    download_file(file_info["url"], file_info["file_name"])
print(f"Temps sans multithreading : {time.time() - start_time:.2f} secondes\n")

# Mesurer le temps d'exécution avec multithreading
start_time = time.time()
threads = []
for file_info in files_to_download:
    thread = threading.Thread(target=download_file, args=(file_info["url"], file_info["file_name"]))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads soient terminés
for thread in threads:
    thread.join()
print(f"Temps avec multithreading : {time.time() - start_time:.2f} secondes")