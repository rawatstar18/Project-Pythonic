#User-Defined Functions

#structure of function
#def function_name(parameter1, parameter2): 
    # Function body
    # ...
#    return result

# We use the def keyword to define the function, followed by the function name and a set of parentheses. 
# The parentheses () may contain parameters, and a colon : at the end of the line that indicates the start of the function body. 
# The return keyword is used to specify the value that the function should return.

#lets create a fuction for our app
def add_number(num1,num2):
    # body of the function
    sum = num1 + num2
    return  sum

print (add_number(1,5))

#fuction is working good lets work with our previous file and make fuctions.
def print_question(digit,op,digit2):
    print() # We add this here because we want to add blank line so that we can read question comfortably
    #body of fuction
    question = 'what is ' + str(digit) + op + str(digit2) + ' ?'
    print (question)

def answer(user_answer,correct_answer):
    #body of fuction
    print('Your answer is' , user_answer)
    print('Correct answer is' , correct_answer)
    
n1 = 40
n2 = 5
print_question ( n1 , '+' , n2)
user_answer = input ('Ans :')
correct_ans = n1 + n2
answer (user_answer , correct_ans)

print_question (n1 , ' - ' ,n2)
user_answer = input ( 'Ans : ')
correct_ans = n1 - n2
answer (user_answer , correct_ans)

print_question (n1 , ' * ' ,n2)
user_answer = input ( 'Ans : ')
correct_ans = n1 * n2
answer (user_answer , correct_ans)

print_question (n1 , ' / ' ,n2)
user_answer = input ( 'Ans : ')
correct_ans = int(n1 / n2)
answer (user_answer , correct_ans)

