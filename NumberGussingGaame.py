import random

top_of_range = input("Type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please write number grater the 0')
        quit()

else:
    print('Please write positive number next time')

randum_number = (random.randint(1,top_of_range))
# print(randum_number)

# print('guess the number in defined range by You ')
No_of_Guesses = 0
while True:
    guess_number = int(input("Guess: "))
    No_of_Guesses += 1
    if guess_number == randum_number:
        print("Congragulations!")
        break
    if guess_number > randum_number:
        print("number is smaller then guessed number")
    else:
        print("number is Grater then guessed number")

    
print("You took "+str(No_of_Guesses)+ " terns to guess correct number")