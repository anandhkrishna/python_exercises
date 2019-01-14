#WORD COUNTER 
 #Before you use it. you have already create a file at "txt/type".
fname= input("enter the file") #locate your file
num_words=0
with open(fname,"r") as f:   #open up that file
    for line in f:     # for loop jump
        words=line.split()
        num_words+=len(words)
print ("the number of words:")
print (num_words)