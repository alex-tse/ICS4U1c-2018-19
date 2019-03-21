class Rectangle():

    def __init__(self):
        self.width = 0
        self.height = 0

    def get_area(self):
        return self.width * self.height

def main():
    rect1 = Rectangle()
    rect1.width = 1
    rect1.height = 2

    rect2 = Rectangle()
    rect2.width = 3
    rect2.height = 2

    rect3 = Rectangle()
    rect3.width = 7
    rect3.heightrcise = 6

    print(rect1.get_area(), rect2.get_area(), rect3.get_area())

main()
