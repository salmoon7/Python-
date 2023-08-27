import time
import  random
from mymodule import addNumber


print(addNumber(23,5))

struct_time = time.localtime()

print(struct_time)

formatted_date=f'{struct_time.tm_year}/{struct_time.tm_mon}/{struct_time.tm_mday}'
print(formatted_date)


for i in range(10):
    print(i)
    time.sleep(1)

item = ['rice','beans','egg','yam']
print(random.choice(item))
print(random.choices(item,k=20))



print(random.randint(3,6))
