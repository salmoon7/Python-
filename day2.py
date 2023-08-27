#Conversion of data types from one from to another.

'''
num_string = '345'
num_int=int(num_string)
print(type(num_int))
'''
#Accepting input from users

'''
username= input('Enter your name : ')
age= input('Enter your age : ')
age=int(age)
print(f'Your user name is {username} and your age will be {age + 10} in 10 years.')
'''

# Handling Errors in your code

# try:
#     print('trying to convert')
#     to_numb=int('happy')
#     print('moving on after converting')
# except Exception as e:
#     print('error occurred in the program')
#     print ('e')


# print('\n noe my program continues')

#Comparison operatoors
# >   <  <=   =

#COMpound doolean expressio  operator:



#conditiinal execution of code if, elif, else


# if 5<4:
#     print('first if block ran')
# elif len('boy')==3:
#     print('first eleif block ran')
# elif len('girl')==4:
#     print('sedond elif block ran')
# else:
#     print('else block ran')

'''
the eval function

c= "3 + 4j"
print(type(eval(c)))
'''

#Basic loops in python for primitive and simple data type 
# for while loops
'''
#looping over numbers
for number in range(1,10,2):
    print(number)

#looping over strings

username='johnah'
for alphabet in username:
    print(alphabet)
    #another method

for index in range(len(username)):
    print(username[index])

    '''
#The while loop

# i=0
# while True:
#     quit= input('do you want to quit the porgram? press 1 or yes to quit \n Otherwise any other to continue: ')
#     if quit.replace('  ','')=='1' or quit.replace('  ','')[0].lower()=='y':
#         print('user exiting the porgram')
#         break
#     else:
#         print('user has not exit the porgram')


#str Manipulation

text = "The adventure of zoro"

#print Upper case
print(text.islower())
print(text.find("adventure"))
print(text.replace("zoro","ednut"))
print(text.startswith('the'))











