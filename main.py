import threading
import time

class Knight (threading.Thread):
    enemies = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run (self):
        days = 0
        print (f'{self.name}, на нас напали!')
        while True:
            if self.enemies > 0:
                self.enemies -= self.power
            else:
                break

            days += 1
            time.sleep(1)
            print (f'{self.name} сражается {days} дней ..., осталось {self.enemies} воинов')

        print (f'{self.name} одержал победу спустя {days} дней (дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()