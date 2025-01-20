from multiprocessing import Process, current_process

# détermine si le nombre donné est premier 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# calcule tous les nombres premiers dans une plage donnée
def calculate_primes(start, end):
    primes = [n for n in range(start, end) if is_prime(n)]
    process_name = current_process().name
    print(f"{process_name} - Nombres premiers entre {start} et {end} : {primes}")

if __name__ == "__main__":
    # définir les plages
    ranges = [(2, 1000), (1000, 2000), (3000, 4000)]
    processes = []

    # créer processus pour chaque plage
    for start, end in ranges:
        process = Process(target=calculate_primes, args=(start, end))
        processes.append(process)
        process.start()

    # attendre tous les processus se terminent
    for process in processes:
        process.join()

    print("Calcul des nombres premiers terminé.")
