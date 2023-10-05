import Hero
class Paladin(Hero.Hero):
    __follow = 0#Номер мага за которым будет следовать
    def get_follow(self, item):#свойство следования, зависит от номера мага, за которым будет следовать
        return self.__follow

    def set_follow(self, wizard):
        self.__follow = wizard.get_numb()
