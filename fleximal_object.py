class Fleximal:

  def __init__(self,number, base):

    self.__base_fp = self.__is_base_valid(base)
    self.__number_fp = self.__is_number_valid(number)[0]
    self.__digits = self.__is_number_valid(number)[1]

    self.base = self.__does_number_match_base(self.__number_fp,self.__base_fp)[0]
    self.number = self.__does_number_match_base(self.__number_fp,self.__base_fp)[1]



  def __is_base_valid(self, base):

    if type(base) != int:
      raise TypeError ("choose an integer between 2 and 10 inclusive as your base")
    elif base < 2 or base > 10:
      raise ValueError("Choose a base that is between 2 and 10 inclusive")
    else:
      return base


  def __is_number_valid(self, number):

    if type(number) != int:
      raise TypeError("This programme is designed to work with whole numbers in a specified base")
    elif number < 0:
      raise ValueError("This programme is desinged to work with positive whole numbers in a specified base")
    else:
      digits = [int(x) for x in list(str(number))]
      return number, digits


  def __does_number_match_base(self, number, base):

    forbidden_count = []
    for i in range(base,10):
      if i in self.__digits:
          forbidden_count.append(1)
    if len(forbidden_count) != 0:
      raise ValueError ('the number you entered and its base do not match-up. There are forbidden digits')

    else:
      return base, number

  @property
  def as_decimal(self):

    n = self.number
    b = self.base

    n_as_list = [int(x) for x in list(str(n))]
    highest_power = len(n_as_list) - 1
    order_of_powers = list(range(highest_power,-1,-1))

    zipped_place_value_and_power = list(zip(n_as_list, order_of_powers))

    decimal_components = [x[0] * (b ** x[1]) for x in zipped_place_value_and_power]

    decimal_number = sum(decimal_components)

    return decimal_number


  def convert_to_base(self, new_base):

    decimal = self.as_decimal
    base = new_base

    if type(base) != int:
      raise TypeError('bases must be whole numbers')

    elif new_base < 2 or new_base >10:
      raise ValueError('This programme is desinged to convert numbers between bases 2 to 10 inclusive')

    else:
      base = base


  #find the largest power of base that can go into decimal at least once
    power = 0
    while decimal > base ** power:
      power += 1
    highest_power = power - 1

    outcome_as_list = []

    for power in range(highest_power,-1,-1):

      element = base ** power
      count_for_place_value = []

      while decimal >= element:
        count_for_place_value.append(1)
        decimal -= element

      place_value = sum(count_for_place_value)
      outcome_as_list.append(place_value)

    outcome = int(''.join(str(x) for x in outcome_as_list))

  #update fleximal number and base
    self.number = outcome
    self.base = new_base

    return outcome

  def __repr__(self):

    return f"value = {self.number}, base = {self.base}"


  def __add__(self, other):

    self_as_decimal = self.as_decimal
    other_as_decimal = other.as_decimal

    new_flex_as_decimal = self_as_decimal + other_as_decimal

    New_fleximal = Fleximal(new_flex_as_decimal, 10)

    return New_fleximal


  def __sub__(self, other):

    self_as_decimal = self.as_decimal
    other_as_decimal = other.as_decimal

    new_flex_as_decimal = self_as_decimal - other_as_decimal

    New_fleximal = Fleximal(new_flex_as_decimal, 10)

    return New_fleximal

  def __mul__(self, other):

    self_as_decimal = self.as_decimal
    other_as_decimal = other.as_decimal

    new_flex_as_decimal = self_as_decimal * other_as_decimal

    New_fleximal = Fleximal(new_flex_as_decimal, 10)

    return New_fleximal


  def __lt__(self, other):

    if self.as_decimal < other.as_decimal:
      return True
    else:
      return False

  def __gt__(self, other):

    if self.as_decimal > other.as_decimal:
      return True
    else:
      return False

  def __le__(self, other):

    if self.as_decimal <= other.as_decimal:
      return True
    else:
      return False

  def __ge__(self, other):

    if self.as_decimal >= other.as_decimal:
      return True
    else:
      return False

  def __eq__(self, other):

    if self.as_decimal == other.as_decimal:
      return True
    else:
      return False

  def __ne__(self, other):

    if self.as_decimal != other.as_decimal:
      return True
    else:
      return False