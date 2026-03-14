c=int(input("Guess the Number:"))
a=10
while True:
    if(c==a):
        print ("Correct Guess")
        break
    elif (c!=a):
        print ("Try Again")
        c=int(input ("Guess the Number again :"))
        while True:
           if(c==a):
             print ("Correct Guess")
             break
           elif (c!=a):
             print ("Try Again")
             c=int(input ("Guess the Number again :"))
             while True:
                if(c==a):
                  print ("Correct Guess")
                  break 
                elif (c!=a):
                  print ("Guess Again")
                break
             break
        break
 
