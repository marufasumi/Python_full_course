import time
import threading


def task(name):
    print(f"{name} task is running\n")
    time.sleep(2)
    print(f"{name} task is finished\n")


print("Main Program START\n")
t1 = threading.Thread(target=task, args=("cooking",))
t2 = threading.Thread(target=task, args=("baking",))
t3 = threading.Thread(target=task, args=("running",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Program END\n")
