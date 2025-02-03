class func:
    def __init__(self):
        self.s = ""

    def get(self):
        self.s = input("string: ")

    def print(self):
        print(self.s.upper())
str = func()

str.get()  
str.print()