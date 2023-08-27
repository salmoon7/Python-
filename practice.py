# my_dog=2
# my_dog=["boy", "girl"]
# print(my_dog)

# for number in range(1,13):
#     print(number +0.5)

#Function in python uses def then the name of the function

# def greetUser(name):
#     print(f"hello {name} you are welcome to pydevelopment")
# greetUser("Tope")
# greetUser("Ade")

# def sumNumber(n1,n2):
#     return n1 + n2

# answer1=sumNumber(2,3)
# print(answer1)


def listNumber(n1,n2):
    numbers=[]
        
    for i in range(n1,n2):
        numbers.append(i)
    return numbers


a=listNumber(2,660)
print(a)