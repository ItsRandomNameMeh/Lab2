import random
import Wizard
import Paladin
from collections import Counter #метод для получения нужных данных об объектах класса

Wizards = {}#Магит будут храниться в словаре, первое число - номер мага, второе - команда
for i in range(3):
    Wizards[f'{i+1}1'] = i


Palads = {}#Паладины будут храниться в словаре. Ключ - номер паладина, значение - команда

for i in range(12): #случайное определение 10 паладинов в одну из трех команд
    a = random.randint(0,2)
    Palads[f'{i+1}2'] = a

value_counts = Counter(Palads.values())
max_value = max(value_counts.values())
max_elements = [key for key, value in Palads.items() if value_counts[value] == max_value]
print(Palads)

print(f'Команда, в которой оказалось макисмальное количество паладинов - {Palads[max_elements[0]]}\n'
      f'В нее входят паладины:')
for elem in max_elements:
    print(elem)
#делаем лист из всех значений словаря Паладинов и считаем количество паладинов на каждую команду
#где команда - числовое значение от 0 до 2 включительно
print(f'В первой(нулевой) команде {list(Palads.values()).count(0)} паладинов,\n'
      f'Во второй команде {list(Palads.values()).count(1)} паладинов, \n'
      f'В третьей команде {list(Palads.values()).count(2)}  паладинов')








print(f"Паладин из команды №1 следует за своим магом с номером 11")


