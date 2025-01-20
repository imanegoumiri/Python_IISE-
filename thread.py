import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Téléchargement terminé : {filename}")

urls = [
    ("https://example.com/file1", "file1.txt"),
    ("https://example.com/file2", "file2.txt"),
    ("https://example.com/file3", "file3.txt")
]

threads = []
for url, filename in urls:
    t = threading.Thread(target=download_file, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Tous les fichiers ont été téléchargés.")