def phase1 (PM, Qs):
    print ("Price Money :", PM)
    print ("Question :", Qs)


print ("Welcome to KBC!")
print('Are you excited to play KBC?')
usreq = input("(yes/no)")

if usreq == "yes":
    playername = input("Enter your full name: ")
    print("So", playername, "There are 10 levels in this KBC. In each level you will get 1 question and 4 options. If you hit the correct answer you will be capable for next level. If you hit the wrong in any level then your journey will be finish on that level, that's mean GAME OVER. You will get only 1 chance to answer the correct and as the level increase the price money will be increase. Press any key to begin the GAME!")
    a = input()


    print("LEVEL-1")
    phase1 ("10,000/- BDT", "Which color is commonly associated with the sky on a clear day?")
    option1 = ["a) Green", "b) Blue", "c) Red", "d) Yellow"]
    print("Press any key for Options")
    b = input()
    print(option1)
    ans1 = input("Answer :")

    if (ans1=="b"):
        print("Correct Answer! You won 10,000/- BDT")
        ch1 = int(input("Press 1 for Next Level"))
        while ch1 == 1 :
            print("Your Current Balance is: 10,000/- BDT")
            print("LEVEL-2")
            phase1 ('50,000/- BDT', "How many days are there in a week?")
            option2 = ["a) 5", "b) 6", "c) 7", "d) 8"]
            print("Press any key for Options")
            b2 = input()
            print(option2)
            ans2 = input("Answer :")

            if (ans2=="c"):
                print("Correct Answer! You won 50,000/- BDT")
                ch2 = int(input("Press 1 for Next Level"))
                while ch2 == 1 :
                    print("Your Current Balance is: 60,000/- BDT")
                    print("LEVEL-3")
                    phase1 ('1,00,000/- BDT', "Which animal is known as the king of the jungle?")
                    option3 = ["a) Elephant", "b) Tiger", "c) Lion", "d) Horse"]
                    print("Press any key for Options")
                    b3 = input()
                    print(option3)
                    ans3 = input("Answer :")

                    if (ans3=="c"):
                        print("Correct Answer! You won 1,00,000/- BDT")
                        ch3 = int(input("Press 1 for Next Level"))
                        while ch3 == 1 :
                           print("Your Current Balance is: 1,60,000/- BDT")
                           print("LEVEL-4")
                           phase1 ('5,00,000/- BDT', "Which device is mainly used to make phone calls?")
                           option4 = ["a) Television", "b) Phone", "c) Fridge", "d) Fan"]
                           print("Press any key for Options")
                           b4 = input()
                           print(option4)
                           ans4 = input("Answer :")

                           if (ans4=="b"):
                               print("Correct Answer! You won 5,00,000/- BDT")
                               ch4 = int(input("Press 1 for Next Level"))
                               while ch4 == 1 :
                                  print("Your Current Balance is: 6,60,000/- BDT")
                                  print("LEVEL-5")
                                  phase1 ('10,00,000/- BDT', "Which month usually has 28 days in a non-leap year?")
                                  option5 = ["a) March", "b) January", "c) February", "d) April"]
                                  print("Press any key for Options")
                                  b5 = input()
                                  print(option5)
                                  ans5 = input("Answer :")

                                  if (ans5=="c"):
                                     print("Correct Answer! You won 10,00,000/- BDT")
                                     ch5 = int(input("Press 1 for Next Level"))
                                     while ch5 == 1 :
                                        print("Your Current Balance is: 16,60,000/- BDT")
                                        print("LEVEL-6")
                                        phase1 ('50,00,000/- BDT', "What do plants absorb from the atmosphere for photosynthesis?")
                                        option6 = ["a) Oxygen", "b) Hydrogen", "c) Carbon Dioxide", "d) Nitrogen"]
                                        print("Press any key for Options")
                                        b6 = input()
                                        print(option6)
                                        ans6 = input("Answer :")

                                        if (ans6=="c"):
                                          print("Correct Answer! You won 50,00,000/- BDT")
                                          ch6 = int(input("Press 1 for Next Level"))
                                          while ch6 == 1 :
                                            print("Your Current Balance is: 66,60,000/- BDT")
                                            print("LEVEL-7")
                                            phase1 ('70,00,000/- BDT', "Which planet is known as the Red Planet?")
                                            option7 = ["a) Venus", "b) Mars", "c) Jupiter", "d) Mercury"]
                                            print("Press any key for Options")
                                            b7 = input()
                                            print(option7)
                                            ans7 = input("Answer :")

                                            if (ans7=="b"):
                                              print("Correct Answer! You won 70,00,000/- BDT")
                                              ch7 = int(input("Press 1 for Next Level"))
                                              while ch7 == 1 :
                                                print("Your Current Balance is: 1,36,60,000/- BDT")
                                                print("LEVEL-8")
                                                phase1 ('1,00,00,000/- BDT', "Which gas is most abundant in the Earth’s atmosphere?")
                                                option8 = ["a) Oxygen", "b) Hydrogen", "c) Nitrogen", "d) Carbon Dioxide"]
                                                print("Press any key for Options")
                                                b8 = input()
                                                print(option8)
                                                ans8 = input("Answer :")

                                                if (ans8=="c"):
                                                  print("Correct Answer! You won 1,00,00,000/- BDT")
                                                  ch8 = int(input("Press 1 for Next Level"))
                                                  while ch8 == 1 :
                                                    print("Your Current Balance is: 2,36,60,000/- BDT")
                                                    print("LEVEL-9")
                                                    phase1 ('5,00,00,000/- BDT', "What is the capital city of Australia?")
                                                    option9 = ["a) Sydney", "b) Canberra", "c) Melbourne", "d) Perth"]
                                                    print("Press any key for Options")
                                                    b9 = input()
                                                    print(option9)
                                                    ans9 = input("Answer :")

                                                    if (ans9=="b"):
                                                       print("Correct Answer! You won 5,00,00,000/- BDT")
                                                       ch9 = int(input("Press 1 for Next Level"))
                                                       while ch9 == 1 :
                                                         print("Your Current Balance is: 7,36,60,000/- BDT")
                                                         print("LEVEL-10")
                                                         phase1 ('7,00,00,000/- BDT', "Which instrument measures atmospheric pressure?")
                                                         option10 = ["a) Barometer", "b) Thermometer", "c) Hygrometer", "d) Ammeter"]
                                                         print("Press any key for Options")
                                                         b10 = input()
                                                         print(option10)
                                                         ans10 = input("Answer :")

                                                         if (ans10=="a"):
                                                            print("Correct Answer! You won 7,00,00,000/- BDT")
                                                            print ("You Won the KBC! Your total Prize Money is 14,36,60,000/- BDT")
                                                            break
                                                         else:
                                                              print("Wrong answer! Better luck next time")
                                                         break
                                                       break
                                                    break

                                                else:
                                                      print("Wrong answer! Better luck next time")
                                                break
                                              break
                                            break

                                        else:
                                          print("Wrong answer! Better luck next time")
                                        break
                                     break
                                  break

                           else:
                             print("Wrong answer! Better luck next time")
                             break
                           break
                        break
                          
                    else:
                        print("Wrong answer! Better luck next time")
                        break
                  
                break

            else:
                print("Wrong answer! Better luck next time")
            break
            

    else :
        print("Wrong answer! Better luck next time")

else :
    print("Thanks you better next time!")








        #         print("LEVEL-2")
        #     phase1 (50000, "How many days are there in a week?")
        #     option2 = ["5", "6", "7", "8"]
        #     print("Press any key for Options")
        #     b2 = input()
        #     print(option2)
        #     ans3 = input("Answer :")

        #     if (ans3 == 7):
        #        print("Correct Answer! You won 50,000/- BDT")
        #        ch2 = int(input("1. Check Balance or 2. Next Level"))
        #        if ch2 == 1 :
        #           print("Your Current Balance is: 60,000/- BDT")
        #         # break







        # elif ch1 == 2:
        #     print("LEVEL-2")
        #     phase1 (50000, "How many days are there in a week?")
        #     option2 = ["5", "6", "7", "8"]
        #     print("Press any key for Options")
        #     b2 = input()
        #     print(option2)
        #     ans3 = input("Answer :")

        #     if (ans3 == 7):
        #        print("Correct Answer! You won 50,000/- BDT")
        #        ch2 = int(input("1. Check Balance or 2. Next Level"))
        #        if ch2 == 1 :
        #           print("Your Current Balance is: 60,000/- BDT")

            #    elif ch2 == 2:
       
    # else :
    #     print("Wrong answer! Better luck next time")
       

    
# else :
#     print("Thanks you better next time!")
    
