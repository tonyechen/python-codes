# thread =  a flow of execution. Like a separate order of instructions
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global intrepreter lock)
#           allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#               use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
#               use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")
def drink_coffee(num):
    time.sleep(num)
    print("You drank coffee")
def study():
    time.sleep(5)
    print("You finished studying")

x = threading.Thread(target = eat_breakfast, args=())
x.start()

y = threading.Thread(target = drink_coffee, args=(4,))
y.start()

z = threading.Thread(target = study, args=())
z.start()

#x.join()  # synchornize with another thread, wait for the thread to finish
#y.join()
#z.join()

#eat_breakfast()
#drink_coffee()
#study()

print(threading.activeCount())
print(threading.enumerate())
print(time.perf_counter())