import random
import math
timeswon = (0)
con = ("")
iskindaclose = ("")
isextremelyclose = ("")

print("Welkom bij raad eens, het spel met 20 rondes waarbij je een cijfer tussen 1 en 1000 moet raden")
print("Het spel zal nu starten, veel geluk!")
print("")

for ronum in range(0, 20):
    ronum = ronum + 1
    print("Dit is ronde "+ str(ronum) +" van de 20")
    print("")
    uwon = False
    if (ronum > 1):
        print("Je hebt tot nu toe "+ str(timeswon) +" goed geraden")
        while (con.lower() != "ja" or con.lower() != "nee"):
            con = input("Nog een getal raden? (Ja/Nee) ")
            if (con.lower() == "nee"):
                quit()
            elif (con.lower() == "ja"):
                break
            else:
                print ("Oeps, verkeerde input. Geacepteerde inputs zijn Ja en Nee")
                continue

        
        
        
    ranum = random.randint(1,1000)
    for ponum in range(0, 10): 
        ponum = ponum + 1
        guess = int(input("Welk cijfer denk je dat het is? (dit is poging "+ str(ponum) +") "))
     
        if (math.isclose (guess, ranum, abs_tol= 50) == True):
            iskindaclose = True

        if (math.isclose (guess, ranum, abs_tol= 20) == True):
            isextremelyclose = True
            iskindaclose = False

        if (ponum == 10 and guess != ranum):
                break
        if (guess < int(ranum)):
                print("Het cijfer zit hoger")
                if (iskindaclose == True):
                    print("Je bent warm")
                if (isextremelyclose == True):
                    print("Je bent heel warm")
                print("")
        if (guess > int(ranum)):
                print("Het cijfer zit lager")
                if (iskindaclose == True):
                    print("Je bent warm")
                if (isextremelyclose == True):
                    print("Je bent heel warm")
                print("")
        if (guess == int(ranum )):
            print("Je hebt het goed geraden!")
            print("")
            timeswon = int(timeswon) + 1
            uwon = True
            break
    
    if (uwon == False):
        print("Sorry, je hebt het nummer niet kunnen raden...")
        print("")
    

