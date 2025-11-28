def Saadain():
  while True:
      print("Type  a  operation :\naddition,\nsubtraction,\ndivision,\nmultiplication")
      operation=input("enter the operation : ")
      a =float(input("enter first no :"))
      b =float(input("enter second no :"))
      if operation == "addition":
          print("RESULT =",a+b)
      elif operation == "subtraction":
          print("RESULT =",a-b)
      elif operation == "division":
          if b==0 :
            print("error,b can't be zero")
          else :
            print("RESULT =",a/b)
      elif operation == "multiplication" :
          print("RESULT =",a*b)
      else:
          print("invalid operation")
      again =input("Do you want another calculation: (yes/no)\n")
      if again != "yes":
        print("Good Bye !")
        break

import random

def Asad():
    print("\t***** WELCOME to \"GUESS THE NUMBER!\" *****")
    print("The number is between 1 and 50!\n")
    x = random.randint(1, 50)
    attempts = 1
    while True:
        try:
            guess = int(input("Enter a number to start playing:\n"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if 1 <= guess <= 50:
            if guess < x:
                print("Too Low! Try Higher!\n")
                attempts += 1
            elif guess > x:
                print("Too High! Try Lower!\n")
                attempts += 1
            else:
                print(f"Congratulations! You guessed the number {x}!")
                print(f"It took you {attempts} attempts.\n")
                break
        else:
            print("Invalid Input. Enter a number between 1 and 50.\n")

def main():
    print("1. Smart Calculator")
    print("2. Guessing Game")
    choice = input("Choose option: ")
    if choice == "1":
        Saadain()
    elif choice == "2":
        Asad()
    else:
        print("Invalid choice")

main()


