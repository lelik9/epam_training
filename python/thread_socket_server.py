import socket
from threading import Thread
from queue import Queue


conn_queue = Queue()


class SockWorker(Thread):
    def __init__(self, queue, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self._queue = queue

    def run(self):
        while True:
            conn = self._queue.get()
            if isinstance(conn, str):
                if conn == 'close':
                    break
            try:
                while True:
                    data = conn.recv(4000).strip()

                    if not data or data == b'close':
                        break
                    else:
                        print(data)
            except Exception as e:
                print(str(e))
            finally:
                conn.close()


def thread_pool(thread_num):
    pool = []

    for _ in range(thread_num):
        th = SockWorker(conn_queue)
        th.start()
        pool.append(th)
    return pool


def start_server(conn_count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 9000))
    sock.listen(conn_count)

    return sock


if __name__ == '__main__':
    pool = thread_pool(4)

    try:
        sock = start_server(4)

        while True:
            conn, addr = sock.accept()
            conn_queue.put(conn)
    except Exception as e:
        print(str(e))
    finally:
        for _ in range(len(pool)):
            conn_queue.put('close')

        for thread in pool:
            thread.join()
