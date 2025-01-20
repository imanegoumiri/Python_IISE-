import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message):
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, "r") as fichier:
            contenu = fichier.read()
    except FileNotFoundError:
        log_error(f"Le fichier '{filename}' n'a pas été trouvé.")
        print("Le fichier n'a pas été trouvé !")
    else:
        print("Contenu du fichier :")
        print(contenu)
    finally:
        print("Fin !")

read_file("exemple.txt")
