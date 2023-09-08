import threading
import random
import time

def gerar_numeros_aleatorios():
    return random.randint(1, 5)

def esperar(segundos):
    time.sleep(segundos)

def realizar_corrida(identificador_thread):
    posicao_atual = 0
    total_passos = 0

    print(f'Thread {identificador_thread} - Iniciando')

    while posicao_atual < 50:
        passos = gerar_numeros_aleatorios()
        total_passos += passos
        posicao_atual += passos

        print(f'Vez da thread {identificador_thread}')
        print(f'Numero sorteado: {passos}')
        print(f'Thread {identificador_thread} Andou {passos} casas')
        print(f'Posição atual da thread {identificador_thread}: {posicao_atual}')

        esperar(1)

    print(f'Thread {identificador_thread} - Chegou a posição 50! Total de passos: {total_passos}')
    return total_passos

def iniciar_corrida():
    num_threads = 2
    threads = []
    resultados = []

    def thread_func(identificador):
        total_passos = realizar_corrida(identificador)
        resultados.append(total_passos)

    for i in range(num_threads):
        thread = threading.Thread(target=thread_func, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    indice_vencedor = resultados.index(min(resultados))
    id_thread_vencedora = indice_vencedor + 1
    print(f'Thread {id_thread_vencedora} venceu com {resultados[indice_vencedor]} passos')

if __name__ == "__main__":
    iniciar_corrida()
