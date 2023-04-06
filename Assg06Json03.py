class Dog:
    def _init_(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")

class JackRussellTerrier(Dog):
    def _init_(self, name, age, coat_color):
        super()._init_(name, age, coat_color)

    def bark(self):
        print("bhow bhow")

class Bulldog(Dog):
    def _init_(self, name, age, coat_color):
        super()._init_(name, age, coat_color)

    def sit(self):
        print(f"{self.name} sits down.")

dog1 = JackRussellTerrier("Tommy", 4, "Grey")
dog2 = Bulldog("Tiger", 6, "Black")

dog1.description()
dog1.get_info()
dog1.bark()

dog2.description()
dog2.get_info()
dog2.sit()