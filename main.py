import fleximal_object
from fleximal_functions import get_valid_user_base, get_valid_user_number, get_user_fleximal

def user_journey():

  print("A fleximal is a number in a specified base (where the base is between 2 and 10 inclusive)")
  print("\nWe're going to set up some fleximals and have some fun with them")
  print("\nLet's start by setting up your first fleximal, Fleximal_1")

  f1 = get_user_fleximal()

  if f1.base != 10:

    print(f"\nGood job. By the way, {f1.number} in base {f1.base} as a decimal is {f1.as_decimal}")
    picked_ten = False

  else:
    print("\nGood job. Next time, why not try setting the base to something other than 10")
    picked_ten = True

  print("\nNow let's convert Fleximal_1 to a different base")

  new_base = get_valid_user_base()

  while new_base == f1.base:

    print("why not pick a new base")

    new_base = get_valid_user_base()


  f1.convert_to_base(new_base)

  print(f"\nGood job. Fleximal_1 expressed in base {new_base} has a vlue of {f1.number}")
  print("\nNext, set up your second fleximal, Fleximal_2")

  f2 = get_user_fleximal()

  print("\n Good job.")

  print ("\nNow let's compare Fleximal_1 and Fleximal_2")
  print ("\nwhich of the following do you think is true:\n")
  print ("a) Fleximal_1 is greater than Fleximal_2")
  print ("b) Fleximal_1 is less than Fleximal_2")
  print ("c) Fleximal_1 is equal to Fleximal_2")

  user_response = input("type 'a', 'b' or 'c' ")

  while user_response != 'a' and user_response != 'b' and user_response != 'c':

    user_response = input("type 'a', 'b' or 'c' ")

  if f1.as_decimal > f2.as_decimal:

    answer = 'a'
    answer_description = "Fleximal_1 is greater than Fleximal_2"

  elif f1.as_decimal < f2.as_decimal:

    answer = 'b'
    answer_description = "Fleximal_1 is less than Fleximal_2"

  else:

    answer = 'c'
    answer_description = "Fleximal_1 is equal to Fleximal_2"

  if user_response == answer:

    print('Excellent', answer_description)

    



  else: 

    print('Not Quite', answer_description)

user_journey()