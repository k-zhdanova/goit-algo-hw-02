from queue import Queue
import uuid

queue = Queue()


def get_uuid():
    return str(uuid.uuid4())


def generate_request():
    request = input("Enter request: ")
    queue.put({"id": get_uuid(), "content": request})
    print("Request added to queue")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request with id {request['id']}: {request['content']}")
    else:
        print("Queue is empty")


def main():
    while True:
        generate_request()
        process_request()

        wants_to_exit = input("Exit? (y/n): ")

        if wants_to_exit == "y":
            break


if __name__ == "__main__":
    main()
