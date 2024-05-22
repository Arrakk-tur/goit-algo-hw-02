from queue import Queue
import threading
import time
import random

# Створити чергу заявок
queue = Queue()


def generate_request(request_id):
    # Створити нову заявку з унікальним ідентифікатором
    request = {'id': request_id, 'timestamp': time.time()}
    print(f"Generated request: {request}")
    # Додати заявку до черги
    queue.put(request)


def process_request():
    while True:
        if not queue.empty():
            # Видалити заявку з черги
            request = queue.get()
            # Обробити заявку
            print(f"Processing request: {request}")
            # Імітувати час обробки заявки
            time.sleep(random.uniform(0.5, 2.0))
            # Позначити заявку як оброблену
            queue.task_done()
        else:
            # Вивести повідомлення, що черга пуста
            print("No requests to process. Waiting for new requests...")
            time.sleep(1)


def main():
    request_id = 1
    # Створити окремий потік для обробки заявок
    processing_thread = threading.Thread(target=process_request, daemon=True)
    processing_thread.start()

    try:
        while True:
            # Генерувати нову заявку кожні 1-3 секунди
            generate_request(request_id)
            request_id += 1
            time.sleep(random.uniform(1, 3))
    except KeyboardInterrupt:
        print("Program terminated by user.")
        processing_thread.join()


if __name__ == "__main__":
    main()
