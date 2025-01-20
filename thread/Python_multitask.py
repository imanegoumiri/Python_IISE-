import multiprocessing
import matplotlib.pyplot as plt
import random
import time

def simulate_arduino_data(data_queue):
    """Processus pour simuler les données d'Arduino"""
    while True:
        pot_value = random.randint(0, 1023)  # Simule une lecture
        data_queue.put(pot_value)
        time.sleep(0.1)  # Pause avant la prochaine lecture

def plot_data(data_queue):
    """Processus pour afficher les données en temps réel"""
    plt.ion()  # Mode interactif
    fig, ax = plt.subplots()
    x_data = []
    y_data = []
    start_time = time.time()

    while True:
        if not data_queue.empty():
            pot_value = data_queue.get()
            elapsed_time = time.time() - start_time
            x_data.append(elapsed_time)
            y_data.append(pot_value)

            ax.clear()
            ax.plot(x_data, y_data, label="Potentiometer Value")
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Potentiometer Value")
            ax.legend()
            plt.pause(0.1)

if __name__ == "__main__":
    # File partagée entre les processus
    data_queue = multiprocessing.Queue()

    # Processus pour simuler les données série
    serial_process = multiprocessing.Process(target=simulate_arduino_data, args=(data_queue,))
    serial_process.start()

    # Processus pour tracer les données
    plot_process = multiprocessing.Process(target=plot_data, args=(data_queue,))
    plot_process.start()

    try:
        # Attente de la fin des processus
        serial_process.join()
        plot_process.join()
    except KeyboardInterrupt:
        print("Programme terminé.")
        serial_process.terminate()
        plot_process.terminate()
