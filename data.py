def legalAges():
    lifeEvent = {
          "drivingAge": 16,
          "votingAge": 18,
          "drinkingAge": 21,
          "retirementAge": 65
      }
    listlen = len(lifeEvent)
    
    for i in range(listlen):
        print("The legal {}  age is{} ",format(lifeEvent[i])
    #print("The legal voting age is ", str(lifeEvent[1]) + ".")
    #print("The legal drinking age is " + str(lifeEvent[2]) + ".")
    #print("The legal retirement age is "+ str(lifeEvent[3]) + ".")
 
legalAges()
