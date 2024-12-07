""""
x = input('your name: ')

print("your name is " + x + "!")

print("la longueur du character est", (len(x)))


print("START")

welcome = "Welcome to the Band Name Generator."

print (welcome)

city_name = input("What's the name of the city you grew up in \n ")

pet_name = input("What's your pet's name ? \n ")

print("Your band name could be " + city_name + " " + pet_name)

print("END")
"""""

"""
name = input("What's your name? ")

name_length = len(name)

print("Name length: ", name_length)

print ("Name length type: ", type(name_length))

age = input("What's your age? ")

print("Age type: ", type(age))

age_converter = int(age)

print("Age converter type: ", type(age_converter))

score = age_converter + name_length

print(f"your name is {name} and your age is {age}\n your score is {score}")
"""

"""
welcome = "Welcome to the tip calculator!"

print(welcome)

print("START")

bill_mount = input("What was the total bill? $")

bill_mount_converter = int(bill_mount)

much_tip = input("What percentage tip would you like to give?: 10, 12, 15 $")

much_tip_converter = int(much_tip)

tip = (bill_mount_converter * much_tip_converter) / 100

pay_total = bill_mount_converter + tip

people = input("How many people to split the bill? ")

people_converter = int(people)

split_bill = pay_total / people_converter

split_bill_rounded = round(split_bill, 3)

pay_by_each_person = f"Each person should pay: ${split_bill_rounded}"

print(pay_by_each_person)

print("END")
"""
"""
welcome = "Welcome number check app"

your_number = input("What is your number? ")

your_number_converter = int(your_number)

modulo_check = your_number_converter % 2

division = your_number_converter / 2

if modulo_check == 0:
    print(f"Your number is good and it division is {division}")
else:
    print(f"Your number is not good and it rest is {modulo_check}")
"""
""""
welcome = "Welcome to my program"

print(welcome)

height = input("Your height? ")

height_converter = int(height)

if height_converter > 120:
    print("Can ride")

    age = input("Your age? ")

    age_converter = int(age)

    if age_converter < 12:
        print("$5")

    elif 12 < age_converter < 18:
        print("$7")

    else:
        print("$12")
else:
    print("Can't ride")
"""

""""
welcome = "Welcome to python pizza deliveries"

print(welcome)

bill = 0
S = 15
print("S = ", S)
M = 20
print("M = ", M)
L = 25
print("L = ", L)

size = input("What size pizza do you want? S, M or L: ")

pepperoni = input("Dou you want pepperoni on your pizza?: Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N: ")

if pepperoni == "Y":
    if extra_cheese == "Y":
        if size == "S":
            bill = 15 + 2 + 1
            print(f"your amount is ${bill}")
        if size == "M":
            bill = 20 + 2 + 1
            print(f"your amount is ${bill}")
        if size == "L":
            bill = 25 + 2 + 1
            print(f"your amount is ${bill}")
    else:
        if size == "S":
            bill = 15 + 2
            print(f"your amount is ${bill}")
        if size == "M":
            bill = 20 + 2
            print(f"your amount is ${bill}")
        if size == L:
            bill = 25 + 2
            print(f"your amount is ${bill}")
else:
    if size == "S":
        bill = 15
        print(f"your amount is ${bill}")
    if size == "M":
        bill = 20
        print(f"your amount is ${bill}")
    if size == L:
        bill = 25
        print(f"your amount is ${bill}")
"""
"""
a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
"""

"""
print(''' Alice's Adventures in Wonderland: 'Through the Looking Glass'
    ,--._                      _
    "'.  '.                  ,';
       )   '.              ,' /
     _/      '.          ,'   '.
   -"__        '.;  /  ,`'    ,-`
       \        /  ( ,===.  _`. )
       /__      `.__//.' \\/_.-`
          '-,._.-    \ \_/\\ ,-.
              \.-     /  \_\\/||
             _/\\    :o o :-'/;.`.
          _,";-,;|   :/"\ : // ||))
     _..."((|_//||-.._\"//  `` ;;''
    /,-----"||" ''    \`._
   //      ,'|         `-.`-..._
  ::     ,','             '.__.=
  ::     |||  _
   \\_   ""   ))     'Beware the jabberwock, my son!'
    \_"--....';
      '""---"' ''')

welcome = "Welcome to Treasure Island."
mission = "Your mission is to find the treasure."
question = "You're at a cross road. Where do you to go? type \n "
left_message = "You've come a lake, There is an island in the middle of lake.\n Type 'wait' to wait for a boat. Type 'swim' to swim across "
right_message = "Fall into a hole. GAME OVER"
door_message = "Thanks for your choice. Type 'red', 'blue', 'yellow' or anythings to continue..."

print(welcome)
print(mission)
print(question)

position = input("'left' or 'right'? ")
swim_message = "Attacked by angry trout . GAME OVER"
print (f"Your position is {position}")

if position == "left":
    print(left_message)
    your_choice = input("Type your choice: ")
    if your_choice == "wait":
        print(door_message)
        which_door = input("Which door? ")
        if which_door == "red":
            print("Burned by fire. GAME OVER")
        elif which_door == "blue":
            print("Eaten by beasts.GAME OVER")
        elif which_door == "yellow":
            print("YOU WIN")
        else:
            print("GAME OVER")
    else:
        print(swim_message)
else:
    print(right_message)
"""

#import  random
#import my_module

#print(my_module.my_random_number)

""""
a = input("your first number: ")
b = input("your second number > your first number: ")

a_converter = int(a)
b_converter = int(b)

my_number = random.randint(a_converter, b_converter)
"""""

""""
a = input("your first number: ")
b = input("your second number > your first number: ")

a_converter = int(a)
b_converter = int(b)

uniform_random = random.uniform(a_converter, b_converter)

if (a_converter + 1) < uniform_random < b_converter:
    print(f"random number is {uniform_random} and you have: Heads")
else:
    print(f"random number is {uniform_random} and you have: Tails")

#my_random = random.random()

#print(f"the random number is {my_random}")

"""

""""
import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america))
choice = random.choice(states_of_america)

print(choice)

tail = len(states_of_america)

print(tail)
print(states_of_america.index(choice))
"""

"""
import random

welcome = "Welcome to my Rock Paper Scissors Game!"

rock = '''
     _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
 '''

paper = '''
     _______
 ---'   ____)____
           ______)
           _______)
          _______)
 ---.__________)
 '''

scissors =  '''
     _______
 ---'   ____)____
           ______)
        __________)
       (____)
 ---.__(___)
'''

choice_table = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

#print(computer_choice)

#print(choice_table.index(rock))

print(welcome)

print("What do you want to choose?")

message = "Type 0 for Rock, 1 for Paper or 2 for Scissors."

print(message)

choice = input("You choice? ")

choice_converter = int(choice)

if choice_converter == choice_table.index(rock) and computer_choice == 0:
    print(f"You choose:\n {rock}")
    print(f" computer choose({computer_choice}):\n {rock}")
    print("It's a draw")
elif choice_converter == choice_table.index(rock) and computer_choice == 1:
    print(f"You choose:\n {rock}")
    print(f" computer choose({computer_choice}):\n {paper}")
    print("You lose")
elif choice_converter == choice_table.index(rock) and computer_choice == 2:
    print(f"You choose:\n {rock}")
    print(f" computer choose({computer_choice}):\n {scissors}")
    print("You win")
elif choice_converter == choice_table.index(paper) and computer_choice == 0:
    print(f"You choose:\n {paper}")
    print(f" computer choose({computer_choice}):\n {rock}")
    print("You win")
elif choice_converter == choice_table.index(paper) and computer_choice == 1:
    print(f"You choose:\n {paper}")
    print(f" computer choose({computer_choice}):\n {paper}")
    print("It is a draw")
elif choice_converter == choice_table.index(paper) and computer_choice == 2:
    print(f"You choose:\n {paper}")
    print(f" computer choose({computer_choice}):\n {scissors}")
    print("You lose")
elif choice_converter == choice_table.index(scissors) and computer_choice == 0:
    print(f"You choose:\n {scissors}")
    print(f" computer choose({computer_choice}):\n {rock}")
    print("You lose")
elif choice_converter == choice_table.index(scissors) and computer_choice == 1:
    print(f"You choose:\n {scissors}")
    print(f" computer choose({computer_choice}):\n {paper}")
    print("You win")
elif choice_converter == choice_table.index(scissors) and computer_choice == 2:
    print(f"You choose:\n {scissors}")
    print(f" computer choose({computer_choice}):\n {scissors}")
    print(computer_choice)
    print("It is a draw")
else:
    print("Type number between 0 to 2")
"""
""""
students_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 69, 89]

#max_number = 0

#number = range(len(students_scores))

#print(number)
total_number = 0
numbers = range(1, 101)

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 ==0:
        print("Fizz")
    else:
        print(number)
"""

import  random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
password = ""

if nr_letters > 51:
    print("Chose number <= 51")
else:

    for letter in range(0, nr_letters):
        random_letter = letter
        letter_generate = letters[random_letter]
        password_list.append(letter_generate)
    print(password_list)


    nr_symbols = int(input(f"How many symbols would you like?\n"))

    if nr_symbols > 8:
        print("Choose number <= 8")
    else:

        for symbol in range(0, nr_symbols):
            random_symbol = symbol
            symbol_generate = symbols[random_symbol]
            password_list.append(symbol_generate)
        print(password_list)

        nr_numbers = int(input(f"How many numbers would you like?\n"))

        if nr_numbers > 9:
            print("Choose number <= 9")
        else:

            for number in range(0, nr_numbers):
                random_number = number
                number_generate = numbers[random_number]
                password_list.append(number_generate)
            print(password_list)

            random.shuffle(password_list)

            password_generate = password_list

            print(password_generate)

            for i in password_list:
                password += i

            password_generate = f"Your password is: {password}"

            print(password_generate)