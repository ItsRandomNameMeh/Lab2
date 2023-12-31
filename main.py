import random
import Hero
import Wizard
import Paladin
from collections import Counter #метод для получения нужных данных об объектах класса


Wizards = {}#Маги будут храниться в словаре, первое число - номер мага, второе - команда
for i in range(3):
    Wizards[f'{Wizard.Wizard(i+1,i)}1'] = i

all_obj_W = Wizard.Wizard.instances[0:3]#срезы нужны, т.к в instances записаны все наследники Hero
print(all_obj_W)


Palads = {}#Паладины будут храниться в словаре. Ключ - номер паладина, значение - команда
for i in range(12): #случайное определение 10 паладинов в одну из трех команд
    a = random.randint(0,2)
    Palads[f'{Paladin.Paladin(i+1,a)}'] = a

all_obj_P = Paladin.Paladin.instances[3::]
print(all_obj_P)
print(Palads)
for i in all_obj_P:
    print(f'Paladin{Paladin.Paladin.get_numb(i)}: team {Paladin.Paladin.get_team(i)}')


def MaxTeam():
    value_counts = Counter(Palads.values())#считаем количетсво повторений каждого значения
    max_value = max(value_counts.values())#Запоминаем максимальное число повторений
    #смотрим, какое значение является максимальным
    max_elements = [key for key, value in Palads.items() if value_counts[value] == max_value]
    print(Palads)
    print(f'Команда, в которой оказалось макисмальное количество паладинов - {Palads[max_elements[0]]}\n'
          f'В нее входят паладины:')
    for elem in max_elements:
        print(elem)
    return max_elements




def CommandCounts():
    #делаем лист из всех значений словаря Паладинов и считаем количество паладинов на каждую команду
    #где команда - числовое значение от 0 до 2 включительно
    print(f'В первой(нулевой) команде {list(Palads.values()).count(0)} паладинов,\n'
          f'Во второй команде {list(Palads.values()).count(1)} паладинов, \n'
          f'В третьей команде {list(Palads.values()).count(2)}  паладинов')
def Move():
    a = 0
    for j in all_obj_P:
        if Paladin.Paladin.get_team(j) == 1:
            a = j
    print(f"Паладин {Paladin.Paladin.get_numb(a)} из команды №1 следует за своим магом с номером 11")

def KillTop():
    print("Увольняем мага из команды с максимальным числом паладинов")
    for i in Wizards:
        if Wizards[i] == Palads[max_elem[0]]:
            Wizards[i] = None



max_elem = MaxTeam()
CommandCounts()
Move()
KillTop()