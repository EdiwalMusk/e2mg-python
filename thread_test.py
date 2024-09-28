import threading
import time


def sing(msg):
    while True:
        print("sing!", msg)
        time.sleep(1)


def dance(msg):
    while True:
        print("dance!", msg)
        time.sleep(1)


if __name__ == '__main__':
    thread_obj = threading.Thread(target=sing, args="a")
    thread_obj.start()
    thread_obj = threading.Thread(target=dance, kwargs={"msg": "b"})
    thread_obj.start()
