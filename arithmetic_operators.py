#Arithmetic Operators and Data Types

#Adding two numbers

#num1 = input("first number : ")
#num2 = input("second number: ")

#When we use input(), it takes whatever we type and stores it as a string.
#So, the numbers stored in num1 and num2 are treated as text and not as mathematical numbers.
#print ("sum of ", num1 ,'+', num2, 'is' , num1 + num2) 


#arithmetic operations

# x = 5
# y = 9

# print (x + y) #addition

# print (x-y) #subrataction

# print (x/y) #division

# Converting the result to an integer by truncating the decimal part 
print(int(6 / 3))
print(int(7 / 3))

#let take the user input and print the correct answer
n1 = 5
n2 = 4

question = 'what is ' + str(n1) + ' + ' + str(n2) + ' ? '
user_answer = input(question)
print ('Your answer is ' , user_answer)
# Computing the correct answer
print ('The correct answer is' , n1 + n2)

question = "What is " + str(n1) + "-" + str(n2) + "? "
user_answer = input(question)
print("Your answer is:", user_answer)
# Computing the correct answer
print("The correct answer is:", n1 - n2)

question = "What is " + str(n1) + "*" + str(n2) + "? "
user_answer = input(question)
print("Your answer is:", user_answer)
# Computing the correct answer
print("The correct answer is:", n1 * n2)

question = "What is " + str(n1) + "/" + str(n2) + "? "
user_answer = input(question)
print("Your answer is:", user_answer)
# Computing the correct answer
print("The correct answer is:", n1 / n2)
