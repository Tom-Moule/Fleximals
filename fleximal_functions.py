from fleximal_object import Fleximal
def get_valid_user_base():

  user_input = input("\nplease select a whole number between 2 and 10 inclusive as your base")

  while True:

    try:

      user_input = int(user_input)

      if user_input < 2 or user_input > 10:
        raise Exception

      break



    except:

      user_input = input("\nplease select a whole number between 2 and 10 inclusive as your base")


  return user_input


def get_valid_user_number(base):

  user_input = input("\nselect a positive integer that's valid for your base.\n(i.e. don't use any digits that are greater than or equal to your base)")

  while True:

    try:

      user_input = int(user_input)

      if user_input < 0:
        raise ValueError

      digits = [int(x) for x in list(str(user_input))]

      forbidden_digits = list(range(base,10))

      for forbidden_digit in forbidden_digits:
        if forbidden_digit in digits:
          raise ValueError

      break



    except:
      user_input = input("\nselect a positive integer that's valid for your base.\n(i.e. don't use any digits that are greater than or equal to your base)")


  return user_input


def get_user_fleximal():

  base = get_valid_user_base()

  number = get_valid_user_number(base)

  fleximal = Fleximal(number, base)

  return fleximal