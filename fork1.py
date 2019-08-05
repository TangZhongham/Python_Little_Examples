import os
import time


def child():
    """获取子程序的pid"""
    print("Hello from child, ", os.getpid())
    os._exit(0)


def parent():
    """主程序"""
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("Hello from parent, ", os.getpid(), newpid)
        time.sleep(1)
        if input(": ") == 'q':
            break


if __name__ == '__main__':
    parent()