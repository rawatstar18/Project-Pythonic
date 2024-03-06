from random import randint

def greetings(user_name,):
    welcome_message = 'Hello! ' + user_name + ' welcome to math quiz.' + ' Please provide answers of the following questions.'
    print (welcome_message)

def result(result):
    result_message = 'Thanks!' + user_name + ' Result will be declare soon '
    print(result_message)


user_name = input('Please enter your name : ')
greetings(user_name)

#question 1
num1 = randint(1,10)
num2 = randint(1,10)
op = '+'
Q = 'what is ' + str(num1) + op + str(num2) + '?'
print (Q)
ans = input('Your answer is: ')
correct_answer = num1 + num2
print('Correct answer is: ', correct_answer)

#question 2 
num1 = randint(1,10)
num2 = randint(1,10)
op = '-'
Q = 'what is ' + str(num1) + op + str(num2) + '?'
print (Q)
ans = input('Your answer is: ')
correct_answer = num1 - num2
print('Correct answer is: ', correct_answer)

#question 3
num1 = randint(1,10)
num2 = randint(1,10)
op = '*'
Q = 'what is ' + str(num1) + op + str(num2) + '?'
print (Q)
ans = input('Your answer is: ')
correct_answer = num1 * num2
print('Correct answer is: ', correct_answer)

#question 4 
num1 = randint(1,10)
num2 = randint(1,10)
op = '/'
Q = 'what is ' + str(num1) + op + str(num2) + '?'
print (Q)
ans = input('Your answer is: ')
correct_answer = int(num1 / num2)
print('Correct answer is: ', correct_answer)

result(result)
