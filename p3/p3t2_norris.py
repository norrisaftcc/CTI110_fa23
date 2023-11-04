"""
CTI 110
P3T2 - Choices and Menus
norrisa
9/26/23
"""
# The most simple program, with main()
def main():
  # Print the menu
  print("-"*10, "Main Menu", "-"*10)
  print("1. Order lunch")
  print("2. Option two")
  print("3. Option three")

  # Let the user choose
  print("Your choice? ", end="")
  choice = int(input())
  print("You chose:", choice)

  # branch (if) on choice
  if choice == 1:
    option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
    print("Sorry, that's not an option.")


def option_1():
  print ("Ordering Lunch")
  print("Would you like a burger or a salad?")
  food = input()
  if food == "burger":
    print("One burger, coming up")
  elif food == "salad":
    print("Dressing on the side")
  else:
    print("We don't have any", food)

def option_2():
  print("This is option 2")

def option_3():
  print("Option 3")

# start the program
main()
  
