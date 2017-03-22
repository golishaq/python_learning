#opiekun zwierzaka, ktorym nalezy sie opiekowac
class Critter(object):
    """Wirtualny zwierzak
    Minimalny poziom hunger, boredom = 0"""
    def __init__(self, name, hunger, = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    #prywatna metoda zwieksza poziom nudy i glodu
    def __pass_time(self):
        self.hunger+= 1
        self.boredom+= 1
    #wlasciwosc reprezentujaca nastroj
    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
            m = "szczesliwy"
        elif 5 <= unhapiness < 10:
            m = "zadowolony"
        elif 10 <= unhapiness <15:
            m = "podenerwowany"
        else:
            m = "wsciekly"
        return m
    #wyswietla nastroj
    def talk(self):
        print("nazywam sie", self.name, "i jestem", self.mood, "teraz \n")
        self.__pass_time()
    #zmniejsza poziom hunger o staly parametr
    def eat(self, food = 4):
        print("Mniam, mniam. Dziekuje")
        self.hunger -= food
        if self.hunger < 0
            self.hunger = 0
        self.__pass_time()
    #zmniejsza poziom boredom o staly parametr
    def play(self, fun =4):
        print("Hura")
        self.boredom -= fun
        if self.boredom <0:
            self.boredom =0
        self.__pass_time()

