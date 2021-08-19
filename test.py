def primeNumb():
    testNum = int(input("Enter an integer to test for prime: "))
    if testNum > 1:
        for i in range(2,testNum):
            #print(i)
            if (testNum % i) == 0:
                print(testNum, "is not a prime number")
                print(i,"times",testNum//i,"is",testNum)
                break
        else:
            print(testNum, "is a prime number",i)
    else:
        print("You must enter an integer.")

def stampa():
    print ("ecco quello che cercavi")

if __name__ == "__main__": 
    stampa()
    