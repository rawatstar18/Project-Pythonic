#Introduction to Python and Programming Concepts.
#In this code, I learn Python concepts

#The built-in print() function

print(18)  # Print an integer
print(round(24.43))  # Print the rounded value of a float
print(round(24.51))  # Print the rounded value of a float
print('You managed to score 100 marks')  # Print a string
print(10 + 2)  # Print the result of an arithmetic operation
print('You managed' + ' to score 100 marks')  # Concatenate and print strings
print('You managed', 'to score 100 marks')  # Print multiple values using a comma

# here i learn how to use use text word together with + operator 
print ("The correct answer for 8 + 2 is:", 8 + 2) # Concatenate strings and print the result of an arithmetic operation


#The built-in input() function

#input("what is your name:") 
#print(input('what is your name:'))   #here i learn how to use input fuction together with print. 

#Variable assignment

#user_name = 'pankaj'  # Assign a string to a variable
#print(user_name)      # Print the value of the variable

#lets do some testing 
# print('hi', user_name, "! welcome to math quiz ")
# print(user_name , 'can you answer some math question?')
# print('congratulation' , user_name , 'to score 10 marks')

#now we will use variable and other fuction together
#take input from user and save it in a variable.

user_name = input('what is your name:')  # Prompt the user to enter their name and save it in a variable
welcome_message = 'Hello,' + user_name + '! welcome to math quiz' # Create a welcome message using concatenation
# If you use a comma instead of +, output will show in brackets like ('Hello,', 'Pankaj', '! Welcome to the math quiz')
#print ('Hi', user_name , 'welcome to math quiz')
print (welcome_message) # Print the welcome message

# Let's ask the user to answer some questions
question_1 = 'Sum of 5 + 2:'              # Define the first question
question_2 = "Subtraction of 5 - 2:"      # Define the second question
question_3 = 'Multiplication of 5 * 3:'   # Define the third question
question_4 = 'Division of 20 / 4:'        # Define the fourth question

a = input (question_1)
b = input (question_2)
c = input (question_3)
d = input (question_4)
