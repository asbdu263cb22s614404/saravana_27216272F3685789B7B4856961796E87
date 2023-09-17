class bankaccount:
    
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self,amount):
      if amount > 0:
          self.__account_balance += amount
          print("Deposited{}. New balance:{}",format(amount,self.__account_balance))

      else:
          print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self,amount):
      if amount > 0 and amount <= self.__account_balance:
          self.__account_balance-=amount
          print("withdraw{}. New balance:{}",format(amount,self.__account_balance))

      else:
          print("Invalid withdraw")

  def display_balance(self):
      print("Account balance for{}(account {}):{}",format(self.__account_holder_name,self.__account_number,self.__account_balance))

account = bankaccount(account_number="324424424424",class bankaccount:
    
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self,amount):
      if amount > 0:
          self.__account_balance += amount
          print("Deposited{}. New balance:{}",format(amount,self.__account_balance))

      else:
          print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self,amount):
      if amount > 0 and amount <= self.__account_balance:
          self.__account_balance-=amount
          print("withdraw{}. New balance:{}",format(amount,self.__account_balance))

      else:
          print("Invalid withdraw")

  def display_balance(self):
      print("Account balance for{}(account {}):{}",format(self.__account_holder_name,self.__account_number,self.__account_balance))

account = bankaccount(account_number="324424424424",