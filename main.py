
class Hero():
    __numb = 0 #номер объекта
    __team = 0 #свойство принадлежности к команде
    __damage = 0
    __speed = 0
    def __init__(self, numb, team):
        self.numb = numb
        self.team = team
        pass

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
    __follow = 0
    @property
    def follow(self):#свойство следования, зависит от номера мага, за которым будет следовать
        return self.follow

ls = Hero(1,4)
print(ls.__dict__)