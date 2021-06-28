
class Robot():
    def __init__(self, name, color, age):
        self.name, self.color, self.age = name, color, age

    def selfIntroduction(self):
        print(f"My name is {self.name} and I am {self.age} old")


r1 = Robot('Tom', 'Blue', 12)
r2 = Robot('Jerry', 'Red', 10)


class Person():
    def __init__(self, name, age):
        self.name, self.age = name, age

    def getRobot(self):
        return self.robot.selfIntroduction()


p1 = Person('Alexa', 16)
p2 = Person('Katie', 16)

p1.robot = r1
p2.robot = r2

p1.getRobot()
