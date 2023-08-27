#string slicing
# name= 'hello world'
# print(name[2:])
# print(name[:3])

# letters='abcdefgijklmno'
# print(letters[3:6])
# print(letters[::-1
#               ])

#string formatting and functions

# boy='Sam'
# #can't change boy name as boy[0]='P'
# #Therefore yoou use the string concatination

# print('P'+boy[1:])

# x='hello world'
# x=x+  ("  It is beautiful ooutside")
# print(x)

#Dont conactenate a string and a number

#CREATING A CLASS 
class Dog():
        def __init__(self,breed):
            self.breed = breed

            his_Dog = Dog(breed='Huskey')
            print(his_Dog.breed)