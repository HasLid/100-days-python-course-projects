import random
# import my_module

# random_integer = random.randint(a=1, b=10)
# print(random_integer)
 
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(a=1, b=10)
# print(random_float)

# How to creat random "heads or tails"
random_heads_or_tails = random.randint(a=0, b=1)
if random_heads_or_tails == 0:
    print("heads")
else:
    print("tails")

# How to name selecting creat a random choices
list_of_friends = ["Alidce", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(list_of_friends))

random_index = random.randint(a=0, b=4)
print(list_of_friends[random_index])
