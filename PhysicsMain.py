# Name: Amyn Jiwani
# Date: June 15/20
# main.py
# Description: This program is an extention of the previous one, whose function is to show the Doppler Effect (by printing Concentric Circles).

#libraries needed to run the code
import turtle
import time

#write about Doppler...
t = turtle.Turtle() 
print("Glad you found your way here!")

print("So, you might be wondering, what exactly is the Doppler Effect?\n")
time.sleep(1)
print("Well, the Doppler Effect is the change in the frequency of sound as an object passes by an observer. Watch as how the \"waves\" (circles) get bigger and bigger, simulating the object passing by the observer (you!)") 

while True:   
  try:
    radius = float(input("\nBut first, What's the radius of the set of waves:")) # radius of the circle
    break
  except:
    print("Invalid Input, try again")  
    
# Loop needed for printing circles within themselves 
for i in range(20): 
  t.circle(radius * i) 
  t.up() 
  t.sety((radius * i)*(-1)) 
  t.down() 
print("I can go forever, but I hope you understand, and want to learn more!")
