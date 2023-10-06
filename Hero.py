class Hero():
    __numb = 0 #номер объекта
    __team = 0 #свойство принадлежности к команде
    __damage = 0
    __speed = 0
    instances = []
    def __init__(self, numb, team):
        self.numb = numb
        self.team = team
        self.instances.append(self)


    def __del__(self):#метод удаляющий ненужный экземпляры, когда на них больше нет внешних ссылок
        #print(f"Удаление экземпляра {self}")
        pass

    #def __str__(self):
    #    return f"Hero: {self.numb}, {self.team}, {self.damage}, {self.speed}"
    def get_numb(self):
        return self.__numb
    def get_team(self):
        return self.__team
    def get_damage(self):
        return self.__damage
    def get_speed(self):
        return self.__speed