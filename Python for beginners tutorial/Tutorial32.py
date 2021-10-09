#Using python external & Built in modules

import random

random_number = random.randint(1,10)   #gives us a random integer
print(random_number)

rand = random.random() * 100  #gives us a random number - defalut random number it gives 0 to`1
print(rand)

lst = ["Star Plus", "Zee Cinema", "Star Utsav", "Cartoon Network", "Discovery", "National Geography"]
choice = random.choice(lst)
print(choice)


