class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)
        

class Robot_Cat(Robot):

    def make_noise(self):
        print('Meow meow!')
def main():
    my_robot_cat = Robot_Cat('Kitku')
    my_robot_cat.walk(10)
    my_robot_cat.make_noise()

main()