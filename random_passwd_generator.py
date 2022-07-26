#python 3.7.1
import random
import string

print ("Hello, Dcoder!")
print('Welcome to Password generator!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

all = lower + upper + num

temp = random.sample(all,length)
password = "".join(temp)

print(password)