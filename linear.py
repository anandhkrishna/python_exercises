def LS():
    list1=[]
    vldl=0
    N=input("enter:")
   
    for i in range (0,N):
        a=input ("enter")
        list1.append (a)
    print list1
    key =input ("enter value:")
    for i in range (0,N):
        if key ==list1[i]:
         vldl=1
         break
    if vldl ==1:
        print ("u found")
    else:
        print ("get away")
LS()