import threading
import datetime

class myThread(threading.Thread):
    def __init__(self, name, counter):
        super().__init__()
        self.name = name
        self.counter = counter
    
    def run(self):
        print('start')
        print_date(self.name, self.counter)
        print('end')


def print_date(threadName, counter):
        today = datetime.date.today()
        print('hi, {}'.format(counter))

thread1 = myThread('th', 1)
thread2 = myThread('th', 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

