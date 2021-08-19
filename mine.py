def hello(*luca):
    for z in luca:
        print ("Ciao", z,"!")

#names = input ("dammi i valori:")
# creating an empty list 
lst = []
mylist = []
# number of elements as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = input('Name Number {}): '.format(i+1))
    lst.append(ele) 
    mylist = list(sorted(set(lst)))

hello(mylist)


class Router:
    def __init__(self, model,swversion, ip_add)
    self.model = model
    self.swversion = swversion
    self.ip_add = ip_add


