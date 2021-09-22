class animes:
    """A class created to tell me when certain animes have their episodes aired"""
    def __init__(self, anime_name, episode_day):
        self.name = anime_name
        self.episode_day = episode_day


#anime = animes("Black Clover", "Tuesday")
#print(anime.name, anime.episode_day)

class calc:
    """A class created to calculate shit"""
    def __init__(self, number, other):
        self.number = number
        self.other = other

    def sum(self):
        y = self.number + self.other
        return y

    def subtract(self):
        y = self.number - self.other
        return y

    def mult(self):
        y = self.number * self.other
        return y

    def divide(self):
        y = self.number / self.other
        return y

    def power(self):
        y = self.number ** self.other
        return y


#number = float(input("Insert a number: "))
#other = float(input("Insert another one: "))
#obj = calc(number,other)

#print(obj.sum())
#print(obj.subtract())
#print(obj.mult())
#print(obj.divide())
#print(obj.power())
