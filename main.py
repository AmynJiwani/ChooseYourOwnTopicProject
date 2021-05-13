# Name: Amyn Jiwani
# Date: June 15/20
# main.py
# Description: This program's function is to create a "Choose Your Own Science Topic" simulator, similar to the "Choose Your Own Adventure" series, with each path being controlled by user input.

#libraries needed to run the code
import random # library used to generate random figures
import sys # imports the 'sys' library (used for system exit)
import os # a package for use of keyboard
os.system('cls||clear') # to refresh the output screen, to see that generated values are different each time. 
import time # imports the variable needed to pause the code
import matplotlib.pyplot as plt #used to graph various functions

#NOTE: Slide the ouput screen up to clearly see the text in the console

def main(): #main function, used to run the main code
  introduction() #introduction function

def introduction(): #function used for the introduction
  print("\nHi there! Welcome to the \"Choose Your Own Science Topic\" program, where you get to choose a topic you want to review or learn more about! The topics are as follows:\n")
  time.sleep(1)
  print("1. Math\n")
  print("2. Physics\n")
  print("3. Chemistry\n")
  print("4. Biology\n")
  print("Keep in mind these concepts will be based at a high-school level, with the majority of these being Grade 11 topics.\n")
  time.sleep(1)
  print("It's also worth noting that this is simply to serve as a review. As such, this program only contains the most essential and important concepts of their respective areas, and requires at least a rutementary knowledge of these topics for understanding...\n")
  time.sleep(2)
  print("Oh, one more thing. Whenever the option of numbers is given, unless otherwise indicated, please type the corresponding number to the option you want to choose. Thanks!")
  
  while (True):
    time.sleep(1)
    topicselection = (input("\nChoose a topic by entering the corresponding number: ")) 
    #error handling
    if topicselection.isdigit() == False: #boolean to declare that it'll go through the rest of the conditionals if requirement isn't met
      if topicselection[0] == "-": # if-statement stating that if there's a negative sign, it's invalid 
        print ("Invalid Input, Try Again...")
        continue # continues through the loop
      elif any(i.isalpha() for i in topicselection): # elif statement using the isalpha() function for integers ("i") accounting for capital letters for potential strings- if there are any present, it's invalid 
        print ("Invalid Input, Try Again...")
        continue # continues through the loop

    if topicselection.isdigit():
      if (topicselection == "1"):  
        mathsection()
        break
      elif (topicselection == "2"):
        physicssection()
        break
      elif (topicselection == "3"):
        chemistrysection()
        break
      elif (topicselection == "4"): 
        biosection() 
        break
      else:
        print("Invalid, Try again...")

#---------------------------------------------

def mathsection(): #function used in the Math section
  print("\nGreat, let's get started!")
  time.sleep(1) #delays for time within brackets (in seconds)
  print("\nSo you've chosen math, a very interesting subject indeed.\nLike physics, there are many facets of knowledge one can choose to explore. But for the sake of the program (and your sanity), the following is what I offer:\n")
  time.sleep(0.5)
  print("1. Pythagorean Theorem Checker")
  print("2. Nature of Roots Calculator")
  print("3. Graph Generator")
  print("4. Interest Calculator")
  
  while (True):
    time.sleep(1)
    topicselection = (input("\nChoose a topic by entering the corresponding number: ")) #input statement used to get number
    if topicselection.isdigit() == False: # conditional using boolean to declare that it'll go through the rest of the conditionals if requirement isn't met
      if topicselection[0] == "-": # if-statement stating that if there's a negative sign, it's invalid 
        print ("Invalid Input, Try Again...")
        continue # continues through the loop
      elif any(i.isalpha() for i in topicselection): # elif statement using the isalpha() function for integers ("i") accounting for capital letters for potential strings- if there are any present, it's invalid 
        print ("Invalid Input, Try Again...")
        continue # continues through the loop

    #conditionals resposible for deciding which subpath to take
    if topicselection.isdigit():
      if (topicselection == "1"): 
        pythagoreantheorem()
        break
      elif (topicselection == "2"):
        natureofroots()
        break
      elif (topicselection == "3"):
        graphgenerator()
        break
      elif (topicselection == "4"): 
        interestcalculator() 
        break

def pythagoreantheorem(): #function used for the first path of the Math Topic

  print("Welcome to the Right Triangle Calculator!") 
  while True:
    try:
      time.sleep(0.5)
      num1 = int (input("Enter the value of the first side: ")) 
    except:
      print("Invalid Input")
    try:
      num2 = int (input("Enter the value of the second side: ")) 
    except:
      print("Invalid Input")
    try:
      num3 = int (input("Enter the value of the hypotenuse (the longest side): ")) 
      break
    except:
      print("Since one of the values was an Since one of the values was an Invalid Input, let's try this again...")
      
  square = num1*num1
  square2 = num2*num2
  square3 = num3*num3
  # add two numbers to determine if variables follow Pythagorean Theorem
  sum = float(square) + float(square2) 

  if (sum == square3):
    print("It would seem like you have a right triangle")
    #condtional that acts as a repeat button at the end of each path, asking if the user wants to reinitiate the code
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!") 
      
  else:
    print("It would seem like you don't have a right triangle") 
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!")
            
def natureofroots(): #function used for the second path of the Math Topic
  print("\nThe nature of roots/zeroes (of a function) are essentially the types of solutions of quadratic functions, when they're in the form of: ax^2+bx+c")
  time.sleep(1)
  print("\nYou might be thinking that the quadratic equation is a good way of solving these types of equations. Well, what if I were to tell you there was an easier way...")
  time.sleep(1)
  print("\nI will now prove (using the above format) whether the roots are:")
  time.sleep(1)
  print("1. Unequal and Real")
  print("2. Equal and Real")
  print("3. Imaginary")
  
  while True:
    try:
      avalue= float(input("In the form of ax^2+bx+c, what's the value of a: \n"))
    except:
      print("Invalid Input")
    try:
      bvalue= float(input("In the form of ax^2+bx+c, what's the value of b: \n"))
    except:
      print("Invalid Input")
    try:
      cvalue= float(input("In the form of ax^2+bx+c, what's the value of c: \n"))
      break
    except:
      print("Since one of the values was an Since one of the values was an Invalid Input, let's try this again...")
      
  
  calcformula= (((bvalue)**2)-4*avalue*cvalue) #formula used to determine the nature of the roots

  if calcformula > 0:
    print("The roots are Unequal and Real")
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!")
  elif calcformula == 0:
    print("The roots are Equal and Real")
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!")
  elif calcformula < 0:
    print("The roots are imaginary")
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!")
  
def graphgenerator(): #function used for the third path of the Math Topic
  print("So you decided to go with the Graph Generator. So, as you know, when you have any kind of function, by substituting values for x, you can come up with y-values.\n")
  time.sleep(2)
  print("That's the function of this branch! It creates a graph using certain values, but keep in mind that due to the limited set of data I have to work with, the graph may not look complete./n")
  time.sleep(1)
  print("Ultimately, your function has to be either:\n")
  time.sleep(1)
  print("1. Linear (involving something like y=mx+b)")
  print("2. Quadratic (involving something like y=mx^2+b)")
  print("3. Exponential (involving something like y=ma^x+b)")
  
  while(True):
    time.sleep(1)
    topicselection = (input("\nSo tell me, what equation do you want to explore?: ")) 
    if topicselection.isdigit() == False: 
      if topicselection[0] == "-":  
        print ("Invalid Input...")
        continue
      elif any(i.isalpha() for i in topicselection): 
        print ("Invalid Input...")
        continue 

    #if-elif-else statement guiding user to different paths depending on choice
    if topicselection.isdigit():
      if (topicselection == "1"):  
        linearequation()
        break
      elif (topicselection == "2"):
        quadraticequation()
        break
      elif (topicselection == "3"):
        exponentialequation()
        break
      else:
        print("Invalid Input")
      
def linearequation(): # function used in the Linear path of the thrid path of the Math Section
  print("Alright, so you chose the linear equation.\n")
  while(True):
    time.sleep(1)
    #try-except statements serving as error handling to expect a certain type of user input
    try:
      horizontal = float(input("What's your horizontal stretch/compress coefficient (that goes before the x)- type 1 if you don't want one): \n"))
    except:
      print("Invalid Input")
    try:
      time.sleep(1)
      vertical= float(input("What's your vertical translation coefficient (that goes after the x)- type 0 if you don't want one): \n"))
      #different x-values are applied to the formula to create a certain set of y-values
      yneg3=(horizontal*-3)+vertical
      yneg2=(horizontal*-2)+vertical
      yneg1=(horizontal*-1)+vertical
      y0=horizontal*0+vertical
      y1=horizontal*1+vertical
      y2=horizontal*2+vertical
      y3=horizontal*3+vertical  
      x = [-3,-2,-1,0,1,2,3] # values for the x-axis (always constant)
      y = [yneg3,yneg2,yneg1,y0,y1,y2,y3] # values for the y-axis
      plt.plot(x, y) # plots the points   
      plt.xlabel('x - axis') # labels the x-axis
      plt.ylabel('y - axis')  # labels the y-axis 
      plt.title('Linear Graph:') #names the graph
      plt.show() #displays the graph
      break 
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    except:
      print("Since one of the values was an Invalid Input, let's try this again...")
            
              
def quadraticequation(): # function used in the Quadratic path of the thrid path of the Math Section
  print("Alright, so you chose the Quadratic Equation.\n")
  while(True):
    time.sleep(1)
    try:
      horizontal = float(input("What's your horizontal stretch/compress coefficient (that goes before the x)- type 1 if you don't want one:\n "))
    except:
      print("Invalid Input")
    try:
      time.sleep(1)
      vertical= float(input("What's your vertical translation coefficient (that goes after the x)- type 0 if you don't want one: "))
      yneg3=(horizontal*(-3**2))+vertical
      yneg3=(horizontal*(-2**2))+vertical
      yneg3=(horizontal*(-1**2))+vertical
      y0=(horizontal*(0**2))+vertical
      y1=(horizontal*(1**2))+vertical
      y2=(horizontal*(2**2))+vertical
      y3=(horizontal*(3**2))+vertical 
      x = [-3,-2,-1,0,1,2,3]  
      y = [yneg3,yneg2,yneg1,y0,y1,y2,y3]   
      plt.plot(x, y)
      plt.xlabel('x - axis')
      plt.ylabel('y - axis') 
      plt.title('Quadratic Graph:') 
      plt.show() 
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!") 
    except:
      print("Since one of the values was an Invalid Input, let's try this again...")

def exponentialequation(): # function used in the Exponential path of the thrid path of the Math Section
  print("Alright, so you chose the Exponential Equation.\n")
  while(True):
    time.sleep(1)
    try:
      a = float(input("What's your horizontal stretch/compress coefficient (that goes before the x)- type 1 if you don't want one): \n"))
    except:
      print("Invalid Input")
    try:
      time.sleep(1)
      horizontal = float(input("What's your horizontal stretch/compress coefficient (that goes before the x)- type 1 if you don't want one):\n "))
    except:
      print("Invalid Input")
    try:
      time.sleep(1)
      vertical= float(input("What's your vertical translation coefficient (that goes after the x)- type 0 if you don't want one): "))
      yneg3=horizontal(a**-3)+vertical
      yneg2=horizontal(a**-2)+vertical
      yneg1=horizontal(a**-1)+vertical
      y1=horizontal(a**1)+vertical
      y2=horizontal(a**2)+vertical
      y3=horizontal(a**3)+vertical
      x = [-3,-2,-1,0,1,2,3] 
      y1 = [yneg3,yneg2,yneg1,y0,y1,y2,y3] 
      plt.plot(x, y) 
      plt.xlabel('x - axis')  
      plt.ylabel('y - axis')  
      plt.title('Exponential Graph:') 
      plt.show() 
      break 
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    except:
      print("Since one of the values was an Invalid Input, let's try this again...")

def interestcalculator(): #function used for the fourth path of the Math Topic
  time.sleep(1)
  print("\nSo you decided to choose the Interest Calculator. This is a very useful tool, as it has practical application (everyone has money!)")
  print("There are 2 main equations nessessary to understand/look at:")
  print("1. I = Prt")
  print("2. A = P(1+i)^n")
  while(True):
    time.sleep(1)
    topicselection = (input("\nSo tell me, what equation do you want to explore?: ")) 
    if topicselection.isdigit() == False: 
      if topicselection[0] == "-": 
        print ("Invalid Input...")
        continue
      elif any(i.isalpha() for i in topicselection): 
        print ("Invalid Input...")
        continue 
    
    if topicselection.isdigit():
      if (topicselection == "1"): 
        firstinterestequation()
        break
      elif (topicselection == "2"):
        secondinterestequation()
        break
      else:
        print("Invalid Input")
      
def firstinterestequation(): # function used in the Simple Interest path of the fourth path of the Math Section
  time.sleep(1)
  print("Alright, so you chose I = Prt.\n")
    
  while(True):
    time.sleep(1)
    print("Type in the corresponding letter:\n")
    choice= input(str("Do you want to solve for I (Simple Interest), P (Principle Value), r (Interest Rate) or t (Time Period)?: ")) #input statement used to get variable
    
    if choice.isdigit() == True: 
      if choice[0] == "-":  
        print ("Invalid Input...")
        continue 
      elif any(i.isdigit() for i in choice): 
        print ("Invalid Input...")
        continue 

    if choice.isalpha():
      time.sleep(1)
      #conditionals to ask a set of questions to acquire variable values based on what path is taken
      if (choice == "I" or choice == "i"): 
          try:
            P = float(input("What's your value for P?: "))
          except:
            print("Invalid Input")
          try: 
            r= float(input("What's your value for r?: "))
          except:
            print('Invalid Input')
          #try-except statement used to determine if all values comply to the type they're supposed to be in, and if not, to start the collection of variables again. This is to help the user understand the repercussions of mistyping values in the real-world 
          try:
            time.sleep(1)
            t = float(input("What's your positive value for t?: "))
            formula= P*r*t
            roundedformula= round(formula, 2)
            print("Your interest is $", roundedformula)
            break
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!")
          except:
            print("Since one of the values was invalid, let's try this again, shall we...")
        
      elif (choice == "P" or choice == "p"): 
          try:
            time.sleep(1)
            I = float(input("What's your value for I?: "))
          except:
            print("Invalid Input")
          try:  
            time.sleep(1)
            R = float(input("What's your value for r?: "))
          except:
            print('Invalid Input')
            
          try:
            time.sleep(1)
            t = float(input("What's your positive value for t?: "))
            formula= I/(R*t)
            roundedformula= round(formula, 2)
            print("Your principle value is $", roundedformula)
            break
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!")
          except:
            print("Since one of the values was invalid, let's try this again, shall we...")
      
      elif (choice == "R" or choice == "r"): 
          try:
            time.sleep(1)
            I = float(input("What's your value for I?: "))
          except:
            print("Invalid Input")  
          try:  
            time.sleep(1)
            P = float(input("What's your value for P?: "))
          except:
            print('Invalid Input')
            
          try:
            t = float(input("What's your positive value for t?: "))
            formula= (I/(P*t))*100
            roundedformula= round(formula, 2)
            #conditional used to indicate an impossibility in the logic; if the rate is less than 0 and prints an appropriate statement in response
            if roundedformula>0:
              print("Your rate is", roundedformula, "%")
              break
              repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
              if (repeat == "1"):
                introduction()
              else:
                print("Alrighty then, see ya next time! Keep on learning!")
            else:
              print("That can't be right, rate can't be negative...") 
              break
              repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
              if (repeat == "1"):
                introduction()
              else:
                print("Alrighty then, see ya next time! Keep on learning!")
          except:
            print("Since one of the values was invalid, let's try this again, shall we...")

      elif (choice == "T" or choice == "t"): 
          try:
            time.sleep(1)
            I = float(input("What's your value for I?: "))
          except:
            print("Invalid Input") 
          try:  
            P = float(input("What's your value for P?: "))
          except:
            print('Invalid Input') 
          try:
            R = float(input("What's your value for R?: "))
            formula= I/PR
            roundedformula= round(formula, 2)
            if roundedformula>0:
              print("Your time is", roundedformula, "years")
              break
              repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
              if (repeat == "1"):
                introduction()
              else:
                print("Alrighty then, see ya next time! Keep on learning!")
            else:
              print("That can't be right, time can't be negative...") 
              break
              repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
              if (repeat == "1"):
                introduction()
              else:
                print("Alrighty then, see ya next time! Keep on learning!")
          except:
            print("Since one of the values was invalid, let's try this again, shall we...")
              
def secondinterestequation(): # function used in the Compound Interest path of the fourth path of the Math Section
  time.sleep(1)
  print("Alright, so you chose A = P(1+i)^n.\n")
  time.sleep(2)
  print("Generally, when dealing with compound interest, we almost always know n (the number of compounding periods), and variables like P (Principle Ammount) and i (interest rate) are either already given, or can be found from other formulas (like simple interest)\n")
  time.sleep(2)
  print("Because this is supposed to simulate practical applications, we're going to be solving for the ammount of money one has after compound interest.\n")
    
  try:
    time.sleep(1)
    P = float(input("What's your positive, whole number value for P (in dollars)?: "))
    time.sleep(1)
  except:
    print("Invalid Input")  
  try:  
    i = float(input("What's your positive, whole number value for i (as a percent)?: "))
    time.sleep(1)
  except:
    print('Invalid Input')
            
  try:
    n = float(input("What's your value for n (in years)?: \n"))
    formula= P(1+i)^n
    roundedformula= round(formula, 2)
    print("Your accumulated amount is $", roundedformula)
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!")     
  except:
    print("You know what, because you typed in a variable incorrectly, I can't do much about it.\n")
    print("You should care more about what values you enter, especially when dealing with money!")
    repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
    if (repeat == "1"):
      introduction()
    else:
      print("Alrighty then, see ya next time! Keep on learning!")  
    

#------------------------------------------------------------

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") #used for declaring subscripts
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹") #used for declaring superscripts (exponents)

def physicssection(): #function used for the Physics Topic
  print("\nGreat, let's get started!")
  time.sleep(0.5)
  print("\nSo you've chosen physics, a very interesting subject indeed.\nLike math, there are many facets of knowledge one can choose to explore. But for the sake of the program (and your sanity), the following is what I offer:\n")
  time.sleep(0.5)
  print("1. Kinematic Equation Solver")
  print("2. Electricity Equation Solver")
  print("3. Doppler Effect Demonstator")
  
  
  while (True):
    time.sleep(1)
    topicselection = (input("\nChoose a topic by entering the corresponding number: ")) 
    if topicselection.isdigit() == False: 
      if topicselection[0] == "-":  
        print ("Invalid Input...")
        continue 
      elif any(i.isalpha() for i in topicselection): 
        print ("Invalid Input...")
        continue 
    if topicselection.isdigit():
      if (topicselection == "1"): 
        kinematicequation()
        break
      elif (topicselection == "2"):
        electricitysolver()
        break
      elif (topicselection == "3"):
        dopplereffect()
        break   

def kinematicequation(): # function used in the first path of the Physics Section
  SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
  SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
  time.sleep(1)
  print("So you decided to choose the Kinematic Equation path. But before we continue, what are the Kinematic Equations?\n")
  time.sleep(1)
  print("The Kinematic Equations are a set of 5 equations integral to accelerated and projectile motion, these can help us find variables like:\n")
  print("a (acceleration)")
  time.sleep(1)
  print("\u0394d (displacement)")
  time.sleep(1)
  print("V2".translate(SUB),"(Final Velocity)")
  time.sleep(1)
  print("\u0394t (time)")
  time.sleep(1)
  print("V1".translate(SUB), "(Initial Velocity)")
  time.sleep(1)
    
  print("However, for the sake of simplicity, the equation we're going to be taking a look at is:\n")
  print("\u0394d =", "(V1".translate(SUB),"+","V2".translate(SUB),")/2 x \u0394t\n") #uses special unicode to generate symbols needed for equations (although at times, they might be referrenced without thesse special symbols)
  time.sleep(1)
  print("The reason as to why we're looking at this one in particular is that it's the most common kinematic equation in Physics.\n")
  displacementequation()
  
  
def displacementequation(): # function used in the first path of the Physics Section
  time.sleep(1.5)
  print("The variables you'll have to solve for are: ")
  print("1. \u0394d")
  print("2.", "V1".translate(SUB))
  print("3.","V2".translate(SUB))
  print("4. \u0394t")
  
  while (True):
    time.sleep(1)
    variableselection = input(str("\nWhat variable do you want to specifically solve for?: "))
    if variableselection.isdigit() == False: 
      if variableselection[0] == "-": 
        print ("Invalid Input...")
        continue 
      elif any(i.isdigit() for i in variableselection): 
        print ("Invalid Input...")
        continue 
    
    if variableselection.isdigit():
      if (variableselection == "1"):
        #try-except statement for each variable so that it's easier to error catch and handle at many parts in the program
        try:
          time.sleep(1)
          V1 = float(input("What's your value for V1: "))
        except:
          print("Invalid Input")
        try:
          time.sleep(1)
          V2 = float(input("What's your value for V2: "))
        except:
          print("Invalid Input")
        try:
          time.sleep(1)
          t = float(input("What's your positive value for t?: "))
          formula= ((V1+V2)/2)*t
          roundedformula= round(formula, 2)
          print("Your distance is", roundedformula, "m")
          break
          repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
          if (repeat == "1"):
            introduction()
          else:
            print("Alrighty then, see ya next time! Keep on learning!")    
        except:
          print("Since one of the values was invalid, let's try this again, shall we...")
            
  
      elif (variableselection == "2"): 
        try:
          time.sleep(1)
          d = float(input("What's your value for displacement (d)?: "))
          time.sleep(1)
        except:
          print("Invalid Input")
        try:
          time.sleep(1)
          t = float(input("What's your positive value for time(t)?: "))
        except:
          print('Invalid Input')
               
        try:
          V2 = float(input("What's your value for","V2?: ".translate(SUB)))
          formula= ((2*d)/t)-V2
          roundedformula= round(formula, 2)
          print("Your velocity is", roundedformula, "m/s".translate(SUP)) 
          break 
          repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
          if (repeat == "1"):
            introduction()
          else:
            print("Alrighty then, see ya next time! Keep on learning!")   
        except:
          print("Since one of the values was invalid, let's try this again, shall we...")
          

      elif (variableselection == "3"): 
        try:
          d = float(input("What's your value for displacement (d)?: "))
          time.sleep(1)
        except:
          print("Invalid Input")
        try:
          t = float(input("What's your positive value for time(t)?: "))
          time.sleep(1)
        except:
          print('Invalid Input')     
        try:
          V1 = float(input("What's your value for","V1?: ".translate(SUB)))
          formula= ((2*d)/t)-V1
          roundedformula= round(formula, 2)
          print("Your velocity is", roundedformula, "m/s")
          break  
          repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
          if (repeat == "1"):
            introduction()
          else:
            print("Alrighty then, see ya next time! Keep on learning!")   
        except:
          print("Since one of the values was an Invalid Input, let's try this again...")
            
      elif (variableselection == "4"): 
        try:
          d = float(input("What's your value for displacement (d)?: "))
          time.sleep(1)
        except:
          print("Invalid Input")
        try:
          V2 = float(input("What's your value for","V2?: ".translate(SUB)))
          time.sleep(1)
        except:
          print('Invalid Input')       
        
        try:
          V1 = float(input("What's your value for","V1?: ".translate(SUB)))
          formula= (2*d/(V1+V2))
          roundedformula= round(formula, 2)
          print("Your time is", roundedformula, "s") 
          repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
          if (repeat == "1"):
            introduction()
          else:
            print("Alrighty then, see ya next time! Keep on learning!")    
        except:
          print("Since one of the values was an Invalid Input, let's try this again...")      
      else:
        print("Invalid Input")

def electricitysolver(): # function used in the first path of the Physics Section
  print("So you decided to choose the Electricity Equation Solver. In this path, we will solve for various elements related to power and electricity.")
  print("For now, the following equations are what I offer:")
  print("1. V = IR")
  print("2. P = IV")
  
  while(True):
    time.sleep(1)
    topicselection = (input("\nSo tell me, what equation do you want to explore?: ")) 
    if topicselection.isdigit() == False: 
      if topicselection[0] == "-": 
        print ("Invalid Input...")
        continue 
      elif any(i.isalpha() for i in topicselection): 
        print ("Invalid Input...")
        continue 

    if topicselection.isdigit():
      if (topicselection == "1"):  
        firstequation()
        break
      elif (topicselection == "2"):
        secondequation()
        break
      else:
        print("Invalid Input")
      
def firstequation(): # function used in the Voltage Equation path of the second path of the Physics Section
  time.sleep(1)
  print("Alright, so you chose V = IR.")
    
  while(True):
    time.sleep(1)
    choice= input(str("Do you want to solve for V, I or R (type the corresponding letter)?: ")) 
    if choice.isdigit() == True: 
      if choice[0] == "-": 
        print ("Invalid Input...")
        continue 
      elif any(i.isdigit() for i in choice): 
        print ("Invalid Input...")
        continue 

    if choice.isalpha():
      if (choice == "V" or choice == "v"): 
        try:
          time.sleep(1)
          I = float(input("What's your value for Current (I)?: "))
        except:
          print('Invalid Input')

        try:
          time.sleep(1)
          R = float(input("What's your value for Resistance (R)?: "))
          formula= I*R
          roundedformula= round(formula, 2)
          print("Your voltage is", roundedformula, "V")
          repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
          if (repeat == "1"):
            introduction()
          else:
            print("Alrighty then, see ya next time! Keep on learning!")
            break
        except:
          print("Since one of the values was invalid, let's try this again, shall we...")
        
      if (choice == "I" or choice == "i"): 
          try:
            time.sleep(1)
            V = float(input("What's your value for Voltage (V)?: "))
          except:
            print('Invalid Input')
          try:
            time.sleep(1)
            R = float(input("What's your value for Resistance (R)?: "))
            formula= V/R
            roundedformula= round(formula, 2)
            print("Your current is", roundedformula, "A")
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!")
              break
          except:
            print('Invalid Input')
      
      if (choice == "R" or choice == "r"): 
          try:
            time.sleep(1)
            V = float(input("What's your value for Voltage (V)?: "))
          except:
            print('Invalid Input')
          try:
            I = float(input("What's your value for Current (I)?: "))
            formula= V/I
            roundedformula= round(formula, 2)
            print("Your voltage is", roundedformula, "A")
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!") 
              break
          except:
            print('Invalid Input')
          
def secondequation(): # function used in the Power Equation path of the second path of the Physics Section
  print("Alright, so you chose P = IV.")
  while(True):
    time.sleep(1)
    choice= input(str("Do you want to solve for P, I or V (type the corresponding letter)?")) 
    if choice.isdigit() == True: 
      if choice[0] == "-": 
        print ("Invalid Input...")
        continue 
      elif any(i.isdigit() for i in choice): 
        print ("Invalid Input...")
        continue 
    
    if choice.isalpha():
      time.sleep(1)
      if (choice == "P" or choice == "p"): 
          try:
            I = float(input("What's your value for Current (I)?: "))
            time.sleep(1)
          except:
            print('Invalid Input')
          try:
            V = float(input("What's your value for Voltage (V)?: "))
            time.sleep(1)
            formula= I*V
            roundedformula= round(formula, 2)
            print("Your power is", roundedformula, "J")
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!")
              break
          except:
            print("Since one of the values was an Invalid Input, let's try this again...") 
      
      elif (choice == "I" or choice == "i"): 
          try:
            P = float(input("What's your value for Power (P)?: "))
            time.sleep(1)
          except:
            print('Invalid Input')

          try:
            V = float(input("What's your value for Voltage (V)?: "))
            time.sleep(1)
            formula= P/V
            roundedformula= round(formula, 2)
            print("Your voltage is", roundedformula, "V")
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!")
              break
          except:
            print("Since one of the values was an Invalid Input, let's try this again...")      
      
      elif (choice == "V" or choice == "v"): 
          try:
            time.sleep(1)
            I = float(input("What's your value for Current (I)?: "))
          except:
            print('Invalid Input')
          
          try:
            time.sleep(1)
            P = float(input("What's your value for Power (P)?: "))
            formula= P/I
            roundedformula= round(formula, 2)
            print("Your voltage is", roundedformula, "V")
            repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
            if (repeat == "1"):
              introduction()
            else:
              print("Alrighty then, see ya next time! Keep on learning!")
              break
          except:
            print("Since one of the values was an Invalid Input, let's try this again...") 
      
def dopplereffect(): # function used in the third path of the Physics Section
  print("So, you decided to choose the Doppler Effect Demonstator")
  print("Well, I decided to take a different approach to this one.. I'm going to show you!")
  print("Why don't you head on over to the 'PhysicsMain.py' python program, and we can continue!")
  repeat= str(input("Do you want to run the program again? Type 1 for Yes and anything if not."))
  if (repeat == "1"):
    introduction()
  else:
    print("Alrighty then, see ya next time! Keep on learning!")

#----------------------------------------------------------- 

def chemistrysection(): # function used in the Chemistry Section
  SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
  print("Great, let's get started!\n")
  time.sleep(0.5)
  print("So, there are indeed many different facets of knowledge in chemistry, and many different concepts associated. But before attepmting any of these, it's important to understand chemical reactions.\n")
  time.sleep(0.5)
  print("Now, there are thousands of possibilities for chemical reactions, but I'm just here to reaffirm your knowledge of the basic ones.\n")
  time.sleep(0.5)
  print("And what better way to do that than by creating your own!")
  time.sleep(0.5)
  print("These are the most common types of reactions in chemistry:\n")
  print("1. Synthesis (A + B --> AB)")
  print("2. Decomposition (AB --> A + B)\n")
    
  while (True):
    time.sleep(1)
    # checks and accepts user input
    conformation= str(input("What type of reaction do you want to solve/create?: ")) 
    time.sleep(1)
    if conformation.isdigit() == False: 
      if conformation[0] == "-":  
        print ("Invalid Input, Try Again...")
        continue 
      elif any(i.isalpha() for i in conformation):  
        print ("Invalid Input, Try Again...")
        continue 
    # different conditionals that guides different reactions based on the choices they make
    if conformation.isdigit():
      if (conformation == "1"): 
        synthesis()
        break
      elif (conformation == "2"):
        decomposition()
        break
      else:
        print("Invalid Input")

def synthesis(): #function used for the first path of the Chemistry section
  print()
  # assigns metals and non-metals to values within dictionaries
  metallist = dict([(1, "Na"), (2, "Ca"), (3, "Mg"), (4, "Al")])
  nonmetallist= dict([(5, "P"), (6, "H"), (7, "Cl"), (8, "O")])
  SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") #used for subscripts of elements by subbing in list to their respective number values
  
  # prints metals and non-metals using for loops
  print("Metals:")
  for y, value in metallist.items():
    print(y,":", value)

  print("\nNon-metals:")
  for z, value in nonmetallist.items():
    print(z, ':', value)
  
  while (True):
    time.sleep(1) 
    try:
      choice1= int(input("Choose your first element: "))
      if choice1 > 4 or choice1 < 1:
        print("Let's try that again")
        continue
    except:
      print("Let's try that again")
      continue
    choice2= int(input("\nChoose your second element: "))
    if choice2 > 8 or choice2 < 5:
      print("Let's try that again")
      continue 
    # different conditionals that display different reactions based on the choices the user makes
    if (choice1 == 1 and choice2 == 5):
      print("Your balanced equation is, 9Na +","P3".translate(SUB), "--> 3", "Na3P".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 1 and choice2 == 6):
      print("Your balanced equation is, 2Na +","H2".translate(SUB), "--> 2NaH")
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 1 and choice2 == 7):
      print("Your balanced equation is, Na +","Cl2".translate(SUB), "--> NaCl")
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 1 and choice2 == 8):
      print("Your balanced equation is, Na +","O2".translate(SUB), "-->", "NaO".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 2 and choice2 == 5):
      print("Your balanced equation is, 3Ca + 3P --> ", "Ca3P2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 2 and choice2 == 6):
      print("Your balanced equation is, Ca +", "H2".translate(SUB), " --> ", "CaH2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 2 and choice2 == 7):
      print("Your balanced equation is, Ca + 2Cl --> ", "CaCl2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 2 and choice2 == 8):
      print("Your balanced equation is, 2Ca + " "O2".translate(SUB)," --> 2CaO")
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 3 and choice2 == 5):
      print("Your balanced equation is, 3Mg + 2P --> ", "Mg3P2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 3 and choice2 == 6):
      print("Your balanced equation is, Mg +","H2".translate(SUB)," --> ","MgH2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 3 and choice2 == 7):
      print("Your balanced equation is, Mg + 2Cl --> ", "MgCl2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 3 and choice2 == 8):
      print("Your balanced equation is", "2Mg + ", "O2".translate(SUB)," --> 2MgO")
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 4 and choice2 == 5):
      print("Your balanced equation is, Al + P --> AlP")
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 4 and choice2 == 6):
      print("Your balanced equation is, 2Al + 3","H2".translate(SUB)," --> 2","AlH3".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 4 and choice2 == 7):
      print("Your balanced equation is, 2Al + 3","Cl2".translate(SUB), " --> 2", "AlCl3".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (choice1 == 4 and choice2 == 8):
      print("Your balanced equation is, 4Al + 3" "O2".translate(SUB), " --> 2", "Al2O3".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    else:
      print("Invalid Input, Try Again")
  

def decomposition(): #function used in the second path of the Chemistry section
  print()
  SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
  # assigns compoundss to values within dictionary
  compoundlist = dict([(1, "CO2".translate(SUB)), (2, "NH3".translate(SUB)), (3, "NaCl"), (4, "H2O".translate(SUB))])
  
  print("Compound:")
  for y, value in compoundlist.items():
    print(y,":", value)
  
  while (True):
    time.sleep(1)
    try:
      compoundchoice= int(input("Choose your compound by typing in the corresponding number: \n"))
      if compoundchoice > 4:
        print("Let's try that again")
        continue
    except:
      print("Let's try that again")
      continue
    
    # different conditionals that display different reactions based on the choices the user makes
    if (compoundchoice == 1):
      print("Your balanced equation is", "CO2".translate(SUB), "--> C + O2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (compoundchoice == 2):
      print("Your balanced equation is", "2NH3".translate(SUB), "--> N2 + 3", "H2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
    elif (compoundchoice == 3):
      print("Your balanced equation is", "2NaCl --> 2Na +", "Cl2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")

    elif (compoundchoice == 4):
      print("Your balanced equation is 2", "H2O".translate(SUB), "--> 2","H2 + O2".translate(SUB))
      break
      repeat= str(input("\nDo you want to run the program again? Type 1 for Yes and anything if not."))
      if (repeat == "1"):
        introduction()
      else:
        print("Alrighty then, see ya next time! Keep on learning!")
       
#-----------------------------------------------------------

def biosection(): #function for the biology section
  score = 0 #variable used to keep track of score
  time.sleep(1)
  print("\nSo you decided to choose Biology, eh? Well, although Biology isn't one of my favourite subjects, one aspect I do enjoy are disections!\n")
  time.sleep(1)
  print("But in order to enjoy and understand disections, one must look at the different parts of an animal.\n")
  time.sleep(1)
  print("One disection I really enjoyed and believe you'll benefit from is the Frog Disection!\n")
  time.sleep(0.5)
  print("Look to the File Labelled \"Bio Frog Label Diagram\". In case it's not there, check the file attached with the program submission. There, you'll find a blank diagram of a frog with numbers.")
  time.sleep(1)

  # assigns list of frog parts to values within dictionary
  partslist = dict([(1, "Vomerine Teeth"), (2, "Internal Nares"), (3, "Eustacian Tubes"), (4, "Tongue"), (5, "Liver"), (6, "Gall Bladder"), (7, "Small Intestine"), (8, "Anus"), (9, "Large Intestine"), (10, "Fatty Bodies"), (11, "Spleen"), (12, "Pancreas"), (13, "Stomach"), (14, "Glottis"), (15, "Gullet"), (16, "Maxillary Teeth")])
  # randomized list of frog parts
  randompartslist = dict([(1, "Tongue"), (2, "Gall Bladder"), (3, "Maxillary Teeth"), (4, "Vomerine Teeth"), (5, "Liver"), (6, "Intenal Nares"), (7,"Stomach"), (8, "Glottis"), (9, "Spleen"), (10, "Fatty Bodies"), (11, "Large Intestine"), (12, "Pancreas"), (13, "Small Intestine"), (14, "Anus"), (15, "Gullet"), (16, "Eustacian Tubes")])
  print("Word Bank:")

  # prints frog list using for loop
  for x in randompartslist:
    print(randompartslist[x])
    time.sleep(0.5)

  numlist= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  randNum = random.choice(numlist) # chooses random number from list
  time.sleep(1)
  partscount = 0 # variable to keep track of number of parts chosen
  score = 0 # variable to keep track of score
  
  while (True):
    print("Using the word bank, make your best guess at Part #", randNum, "on the next line (capitilization matters!): ")
    partsguess= input(str())
    #if-else statement indicating if the user got the name correct and removes the number from the list and part from its list so it can't be asked again
    if (partsguess== partslist.get(randNum)):
      print("\nCorrect!")
      score += 1
      numlist.remove(randNum) #removes number from respective list
      partslist.pop(randNum) #removes part from respective list
      partscount += 1 #adds one to parts count each loop
      if partscount > 15:
        break
      randNum = random.choice(numlist)

    else:
      print("Sorry, the answer was", partslist.get(randNum))
      partscount += 1
      numlist.remove(randNum)
      partslist.pop(randNum)
      if partscount > 15:
        break
      randNum = random.choice(numlist)
  
  time.sleep(1)
  print("Your score is", score," /16") # prints score
  #condtional that acts as a repeat button at the end of each path, asking if the user wants to reinitiate the code
  repeat= str(input("Do you want to run the program again? Type 1 for Yes and anything if not."))
  if (repeat == "1"):
    introduction()
  else:
    print("Alrighty then, see ya next time! Keep on learning!")

main()