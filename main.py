import numpy as np
from functions import add, minus, power

def main():
  a = 1
  b = 3
  c = add(a,b)  

  
  print(f"{a} plus {b} equals to {c}")
  c=minus(a,b)
  print(c)
  c=power(a,b)
  print(c)

  


if __name__ == "__main__":
    main()
  
