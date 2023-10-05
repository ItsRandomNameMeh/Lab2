import Hero
class Wizard(Hero.Hero):
    __lvl = 0

    def lvlup(self): #метод увеличения уровня мага
        self.lvl += 1
    def get_lvl(self):#уровень мага. по условию этот свойсто есть только у мага
        return self.__lvl
    def set_lvl(self,lvl):#уровень мага. по условию этот свойсто есть только у мага
        self.__lvl = lvl

    lvl = property(get_lvl, set_lvl)