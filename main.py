#Maru Puran
#October 12, 2023
#Create a calculator using if statements, subroutines, and input statements; get a better understanding of what can be done when they are combined together or alone as well as how they're used individually and how they work

#assign variables and have users type in numbers to be remembered, assigned to those variables
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

#store third number the user enters between 1-4 to decide what operation to use
calc_num = int(input("Please enter a number between 1 and 4, inclusive! 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))

def add(n1,n2): #create subroutine for addition, puts parameters for arguments to be inserted
  return n1+n2 #return the sum of two numbers inputted

def subtract(n1,n2): #create subroutine for subtraction, puts parameters for arguments to be inserted
  return n1-n2 #return the difference of the first number and second number inputted

def multiply(n1,n2): #create subroutine for multiplication, puts parameters for arguments to be inserted
  return n1*n2 #returns product of two numbers inputted

def divide(n1,n2): #create subroutine for division, puts parameters for arguments to be inserted
  return n1/n2 #returns quotient of the first number by the second number inputted


#create if and elseif and else statements for conditionals to correctly choose and output the chosen operation by the user
if calc_num == 1: #check if 1, if 1 do addition
  print("\nYou added!") #alert user they've selected addition
  print("The sum is", add(num1,num2)) #provide the sum
elif calc_num ==2: #check if 2, if 2 do subtraction
  print("\nYou subtracted!") #alert user they've selected subtraction
  print("The difference is", subtract(num1,num2)) #provide the difference
elif calc_num == 3: #check if 3, if 3 do multiplication
  print("\nYou multiplied!") #alert user they've selected multiplication
  print("The product is", multiply(num1,num2)) #provide the product
elif calc_num == 4: #check if 4, if 4 do division
  print("\nYou divided!") #alert user they've selected division
  print("The quotient is", divide(num1,num2)) #provide the quotient
else: #if none of the above, user hasn't entered a number between 1-4
  print("\nThat is not a number between 1 and 4 :(") #alert user they haven't entered a number, print