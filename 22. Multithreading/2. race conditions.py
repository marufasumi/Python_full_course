import threading
import time

balance = 1000
lock = threading.Lock()


def withdraw(amount):
    global balance
    with lock:
        temp = balance  # read
        time.sleep(0.0001)
        balance = temp - amount  # write back


t1 = threading.Thread(target=withdraw, args=(100,))
t2 = threading.Thread(target=withdraw, args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()

print("── Bank Transfer ──")
print(f"Expected balance: 800  →  Got: {balance}")
