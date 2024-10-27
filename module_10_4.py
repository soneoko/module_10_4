from threading import Thread
from random import choice
from time import sleep
from queue import Queue
class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        x = choice([i for i in range(3, 11)])
        sleep(x)

class Cafe:
    def __init__(self, *list):
        self.queue = Queue()
        self.tables = list

    def guest_arrival(self, *guests):
        for guest in guests:
            free_tables = [table for table in self.tables if table.guest == None]
            if len(free_tables) == 0:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
            else:
                free_tables[0].guest = guest
                print(f'{guest.name} сел(-а) за стол номер {free_tables[0].number}')

    def discuss_guests(self):
        while not(self.queue.empty()) or len([table for table in self.tables if table.guest != None]) != 0:
            for table in [table for table in self.tables if table.guest != None]:
                if not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest.start()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


