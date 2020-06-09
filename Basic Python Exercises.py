#Isiah Larose
#CS100 2019F Section 037
# HW01, Sept 9 2019

#Exercise 1.1
print('Question #1: If one or both parentheses are left out, a syntax error will occour.\n'
      'Question #2 You will also get a synta error. Parenthesis must match in order to for the output to be shown. Either single or double quotes, not both.\n'
      'Qustion #3: Putting a plus sign before a number genrall does nothing.\n'
      'as numbers are represented as positive without signs in python. 2++2 will rperform arithmetic and return a value of 4\n')

#Exercise 1.2
#1
mySec=60
myTime = 42*mySec
myTot = myTime + 42
print ("There are",myTot, "seconds in 42 minutes and 42 seconds\n")

#1.2, Question 2
myKM=10
myMile=1.61
myDist= myKM/myMile
print ('There are',myDist, "miles in 10 kilometers\n")

myFTime = myKM/myTot
myMTime = myFTime/10
print ("If you run a 10 KM race in 42 minutes and 42 seconds,your average pace would be\n"
       , myFTime,"KM,or",myMTime,"miles\n" )

#Exercise 2.1

print('42=n is illegal because variables cannot be named as numbers as it deifes logic.\n'
      "You cannot assign numbers to literals\n")

x=y=1
print("x=y=1 is legal as it will return a value of 1\n")

print("A semi colon has no effect at the end of a python statement. It can however\n",
      "be used as a separator when declaring variables in the same line"," a period returns a syntax error\n")

print("Printing xy will return an error because an operator is always need in order to perform arithmetic in Python\n")

#Exercise 2.2
Volume = 4/3*3.14*5**3
print ("The volume of a sphere whose radius is 5 is\n",Volume)

#2.2 Question 2

myBook = 24.95
myDisc = 0.40
myShipp= 3
myBook2 =24.95 - myBook*myDisc 
myBook3= myBook2 + myShipp
myBook4 = .75*57
myBook5 = myBook4+myBook3
myBook6 = myBook2*60
myCost = myBook5+myBook2+myBook6
print ( "The total cost is\n", myCost)


#2.2 Question 3
print ('7:30')

