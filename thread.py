#same function work at a time 
import threading
import time
def numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)
# numbers()
# numbers()
thread=threading.Thread(target=numbers)
thread1=threading.Thread(target=numbers)
thread.start()
thread1.start()
thread.join()
thread1.join()
print("the numbers are printed")

#different function works at a time
'''import threading
import time 
def numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)
def letters():
    for char in ['A','B','C','D','E',]:
        print(char)
        time.sleep(1)
thread1=threading.Thread(target=numbers)
thread2=threading.Thread(target=letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished")'''
