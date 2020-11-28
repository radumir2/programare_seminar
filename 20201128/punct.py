x = None

y = None

def Punct(x_,y_):
    global x,y 
    x = x_
    y = y_

def __str__():
  return f"Punct[{x},{y}]"


if __name__ == "__main__":
  Punct(1,2)
  print(__str__())
  Punct(3,4)
  print(__str__())
