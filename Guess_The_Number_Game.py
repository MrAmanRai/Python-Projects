HN = 57
print("\nWelcome! to the Guessing the number game.\n")
print("You have to guess the number which the developer has hidden.\n"
      "Number is positive and from 0 to 150 only\n"
      "If you guessed it right. Your guessing game is great.\n"
      "If not? Then you might have to work on it.\n"
      "You will get total of 9 guesses, and with each answer one guess will be deducted.\n"
      "************************So, LETS BEGIN THE GAME!**********************\n")
while 1:
    print("1: Start the game!\n"
          "2. Exit\n")
    feed = int(input("Enter your choice:\n"))
    if feed == 1:
        i = 9
        while i > 0:
            num = int(input("Mujhe Khojo!\n"))
            if ((num > 0) and (num < 10)) or (num > 100 and num < 150):
                print("Bhot Dur ho tum mujhse. Kuch chota ya bada Socho")
            elif ((num >= 10) and (num < 20)) or ((num > 90) and (num <= 100)):
                print("Faasle abhi bhi bhot hai.")
            elif (num >= 20) and (num < 35):
                print("Toda or bada socho")
            elif (num > 75) and (num <= 90):
                print("Toda chota bhi soch liya karo")
            elif (num >= 35) and (num < 45):
                print("Mai tumhe Mehsus kar rha hu... Tum yahi kahi aas paas ho. Toda or upar dekho")
            elif (num > 65) and (num <= 75):
                print("Mai tumhe Mehsus kar rha hu... Tum yahi kahi aas paas ho. Toda or dekho dekho")
            elif (num >= 45) and (num < 55):
                print("Milne Ka samay aa gya... Mai upar hi hu")
            elif (num > 59) and (num <= 65):
                print("Aa gyi milan ki bella... Mai niche tumhara intzaar kar rha hu")
            elif (num >= 55) and (num <= 56):
                print("Aage baadho or mere gale lag jao")
            elif (num >= 58) and (num <= 59):
                print("Peeche to dekho")
            elif num == 57:
                print("Tumne mujhe Doondh Liya...!!!\n"
                      "CONGRATS!...YOU WON!!!\n")
                break
            else:
                print("Graden me Ghumne nikla hai kya? Jo itni dur nikal gya.")

            i -= 1
            print("Number of guess Left: ", i,"\n")

        if i == 0 and num != HN:
            print("GAME OVER!!!\n")

    elif feed == 2:
        print("Ending the Game... See you next time!")
        break
    else:
        print("Abey akal ke andhe...padhne nhi aata kya? '1' ya '2' daba\n")
        continue
