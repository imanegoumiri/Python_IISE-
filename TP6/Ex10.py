def read_file(filename):
    try:
        with open(filename, "r") as fichier:
            contenu = fichier.read()
            return contenu  
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier n'a pas été trouvé !")  

def get_positive_integer():
    while True:
        try:
            value = int(input("Saisir un entier positif : "))
            if value <= 0:
                print("Erreur : L'entier doit être positif.")
            else:
                return value
        except ValueError:
            print("Erreur : L'entier invalide.")

def main():
    while True:  
        filename = input("Saisir le nom du fichier : ")
        try:
            contenu = read_file(filename)  
            print("\nContenu du fichier :")
            print(contenu)
            break  
        except FileNotFoundError as e:
            print(e)  
    
    while True:
        try:
            value = get_positive_integer()  
            print(f"\nL'entier saisi est : {value}")
            break  
        except ValueError as e:
            print(e)

    print("\nFin !")

if __name__ == "__main__":
    main()
