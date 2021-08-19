a = input("Digita qualcosa:")

#print ("hai inserito una variabile di tipo: ", type(a))

if type(a) == str:
    print ("hai inserito una variabile di tipo STRINGA")
elif type(a) == int:
    print ("hai inserito una variabile di tipo INTEGER")
elif type(a) == bool:
    print ("hai inserito una variabile di tipo BOOLEAN")
elif type(a) == float:
    print ("hai inserito una variabile di tipo FLOAT")
else:
    print("non ho capito cosa hai inserito")
