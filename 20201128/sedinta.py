class Punct:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Punct[{self.x},{self.y}]"


if __name__ == "__main__":
    punct1 = Punct(1,2)
    punct2 = Punct(3,4)
    print(f"Punct1: {punct1}, Punct2: {punct2}")
