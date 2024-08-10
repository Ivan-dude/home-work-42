from threading import Thread
import time
from time import sleep

class Knight(Thread):
    warriors = 100
    days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        for warrior in range(self.warriors):
            if self.warriors > 0:
                self.warriors = self.warriors - self.power
                time.sleep(1)
                self.days = self.days + 1
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.warriors} воинов.\n', end='')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
