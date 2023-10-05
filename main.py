import random


class Hero():
    __numb = 0 #номер объекта
    __team = 0 #свойство принадлежности к команде
    __damage = 0
    __speed = 0
    def __init__(self, numb, team):
        self.numb = numb
        self.team = team


    def __del__(self):#метод удаляющий ненужный экземпляры, когда на них больше нет внешних ссылок
        print(f"Удаление экземпляра {self}")

    def __str__(self):
        return f"Hero: {self.numb}, {self.team}, {self.damage}, {self.speed}"
   # @property
    def numb(self):
        return self.numb
  #  @property
    def team(self):
        return self.team
  #  @property
    def damage(self):
        return self.damage
   # @property
    def speed(self):
        return self.speed


class Wizard(Hero):
    __lvl = 0
    @property
    def lvl(self):#уровень мага. по условию этот свойсто есть только у мага
        return self.lvl

class Paladin(Hero):
    __follow = 0#Номер мага за которым будет следовать
    def get_follow(self, item):#свойство следования, зависит от номера мага, за которым будет следовать
        return self.__follow

    def set_follow(self, follow):
        self.__follow = follow



FirstWiz = Wizard(11,0)
SecondWix = Wizard(21,1)
ThirdWiz = Wizard(31,2)

for i in range(2):
    a = random.randint(0,2)
    Palads = Paladin(int(f"{a+1}"+"2"), a)

