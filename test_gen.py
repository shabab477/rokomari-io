import random

file = open("testcase.txt", "w")
tc = 100
file.write(str(tc) + "\n")
for i in range(tc) :
    #Lets just test for 6 random values cause its pretty hard to cross check more than it using
    #brute force
    n = 6
    file.write(str(n) + "\n")

    for i in range(n) :
        file.write(str(random.randrange(1, 501)) + " ")
    
    file.write("\n")


file.close()