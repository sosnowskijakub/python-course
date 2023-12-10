from robot import Robot

class Robot_Cat(Robot):

    def make_noise(self):
        print('Meow meow!')

my_robot_cat = Robot_Cat('Kitku')
my_robot_cat.walk(10)
my_robot_cat.make_noise()