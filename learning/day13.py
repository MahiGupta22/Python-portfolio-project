#degging errors
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

age = int(input("How old are you?"))
if age >= 18:
    print("You can drive at age {age}.")
else:
    print("You can't drive at age {age}.")

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

import maths
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)
mutate([1, 2, 3, 5, 8, 13])
