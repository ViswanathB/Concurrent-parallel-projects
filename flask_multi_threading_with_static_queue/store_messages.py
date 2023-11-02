from queue import Queue
from threading import Thread, Lock
import time


class StoreMessages:
    msg_q = Queue()

    message_q_lock = Lock()
    count = 0

    message_q_lock_put = Lock()
    put_count = 0

    class FileWriter:
        msg_get_count = 0
        msg_get_lock = Lock()
        log_file = open("/home/vish/Documents/python_projects/flask_test_app/file.log", "w+")

        def __init__(self) -> None:
            pass

        def write_to_file(self, msg_q: Queue) -> None:
            print("Thread started for writing")
            while True:
                time.sleep(5)
                while not msg_q.empty():
                    print(f"Q not empty: {StoreMessages.msg_q.qsize()}")
                    try:
                        next_msg = msg_q.get(block=False, timeout=1)
                        with StoreMessages.FileWriter.msg_get_lock:
                            StoreMessages.FileWriter.msg_get_count += 1
                        StoreMessages.FileWriter.log_file.write(next_msg + "\n")
                        StoreMessages.FileWriter.log_file.flush()
                    except Exception as e:
                        print(f"There is an exception {e}")

    thread = Thread(target=FileWriter().write_to_file, args=[msg_q])
    thread.start()

    def add_message(self, message: str) -> None:
        with StoreMessages.message_q_lock:
            StoreMessages.count = StoreMessages.count + 1

        try:
            StoreMessages.msg_q.put(str(StoreMessages.count) + message)
            with StoreMessages.message_q_lock_put:
                StoreMessages.put_count += 1
        except Exception as e:
            print(f"Exception while writing into msg q : {e}")
            return

        if StoreMessages.count % 10 == 0:
            print(
                f"Put count {StoreMessages.put_count}, get count {StoreMessages.FileWriter.msg_get_count}, thread count {StoreMessages.count}, q size: {StoreMessages.msg_q.qsize()}"
            )
            # thread = Thread(target=self.write_to_file)
            # thread.start()
