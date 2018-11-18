def computeGCD(x,y):
      if (x<y):
         x=smaller
      else:
         y=smaller
      for i in range(1,smaller+1):
              if (x%i==0) and (y%i==0):
                     gcd=i
      return gcd
x=int(input("neter"))
y=int(input(",enter"))
print("gcd of",x,"and",y,"is",computeGCD(x,y))
computeGCD(x,y)