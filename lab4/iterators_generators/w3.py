#создать итератор

class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

it = MyIterator(5)
for x in it:
    print(x)  






#создать генератор
def my_generator(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

gen = my_generator(5)
for x in gen:
    print(x)  


gen = (x**2 for x in range(5))
for x in gen:
    print(x) 



'''Методы работы с итераторами и генераторами
next(iterator) — возвращает следующий элемент или вызывает StopIteration.
iter(object) — преобразует объект в итератор, если возможно.

lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # 1
print(next(it))  # 2


фильтрация 

def even_numbers(limit):
    for num in range(1, limit + 1):
        if num % 2 == 0:
            yield num

for x in even_numbers(10):
    print(x)  # Вывод: 2 4 6 8 10


    
сумма чисел
gen = (x for x in range(1, 101))
print(sum(gen))  # Вывод: 5050


'''