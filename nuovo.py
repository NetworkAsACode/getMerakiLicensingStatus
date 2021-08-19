'''
with open("textfile.txt", "a") as data:
    data.write ('\t dove')

with open("textfile.txt", "r") as data:
    print (data.read())
def luca(*inserimenti):
    for quantinevuoi in inserimenti:
        print("hello", quantinevuoi, "you're a f**king mother fuc***r")

input (luca())
import sys
import xmltodict
'''
#import netmiko

#help (netmiko.cisco)

from math import pi
def area_of_circle(r = int(input("Fornire il raggio : "))):
    if r <=0:
        print ("il raggio deve essere >= 0") 
    else:
        area = pi*(r**2)
        print (area)

area_of_circle()

