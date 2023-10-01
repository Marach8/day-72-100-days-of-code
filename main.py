from replit import db
import time, os, datetime, random

def menu():
  os.system('clear')
  print('\033[4mWELCOME TO MY TWEETER\033[0m')
  print()
  ask = input('Enter:\n1. Add Tweet\n2. View Tweet\n>> ')
  return ask

def add():
  while True:
    print()
    ask1 = input('Enter the Tweet here: ')
    timest = datetime.datetime.now()
    db[timest] = ask1
    time.sleep(1)
    print('\033[32mTweet Added Succesfully😊\033[0m')
    print()
    ask2 = input('Do you want to add another tweet? y/n: ')
    if ask2 == 'y':
      os.system('clear')
      continue
    else:
      break

def view():
  print()
  ask3 = input('Enter:\n1. View from a particular date\n2. View Latest\n>> ')
  if ask3 == '1':
    list2 = []
    year = int(input('Enter the year: ').strip())
    month = int(input('Enter the month: ').strip())
    day = int(input('Enter the date: ').strip())
    date1 = datetime.datetime(year, month, day, 00, 00, 00)
    keys = db.keys()
    for k in keys:
      if type(db[k]) != str:
        continue
      else:
        v = datetime.datetime.strptime(k, '%Y-%m-%d %H:%M:%S.%f')
        if v >= date1:
          list2.append(db[k])
        else:
          print()
          print('\033[31mSorry, You do not have Tweets from that time!\033[0m')
          time.sleep(2)
          break
    if len(list2) == 0:
      pass
    else:
      time.sleep(2)
      printer(list2)
        
  elif ask3 == '2':
    list = []
    keys = db.keys()
    for i in keys:
      if type(db[i]) != str:
        continue
      else:
        list.append(db[i])
    printer(list)
  else:
    print('Invalid Selection!')

def printer(t):
  print()
  t = t[::-1]
  for j in t:
    if type(j) != str:
      continue 
    else:
      print()
      print(j)
      time.sleep(1)
    print()
    view_again = input('Want to view previous? y/n: ')
    if view_again == 'y':
      continue
    else:
     break


def add_user():
  os.system('clear')
  time.sleep(1)
  print ('\033[4mCreate Your Account\033[0m')
  print()
  username = input('Enter Your Username: ')
  password = input('Enter your password: ')
  salt = random.randint(1000, 9999)
  password = hash(f'{password}{salt}')
  db[username] = {'password': password, 'salt': salt}
  print()
  time.sleep(2)
  print('\033[32mAccount Created Successfully\033[0m')
  time.sleep(2)
  body()

def login():
  os.system('clear')
  print('\033[4mLogin with your Username and password\033[0m')
  print()
  user_name = input('Enter your Username: ')
  pass_word = input('Enter Your password: ')
  print()
  if user_name in list(db.keys()):
    salt = db[user_name]['salt']
    p = hash(f'{pass_word}{salt}')
    if p == db[user_name]['password']:
      print('LOGIN SUCCESSFUL!')
      time.sleep(2)
      body()
    else:
      print('INVALID PASSWORD')
  else:
    print('INVALID USERNAME')

def body():
  while True:
    g = menu()
    if g == '1':
      add()
    elif g == '2':
      view()
    else:
      print()
      print('Invalid Selection!')
      time.sleep(2)
      os.system('clear')
      continue
    
while True:   
  user4 = input('1. New User\n2. Existing User\n>> ')
  if user4 == '1':
    add_user()
  elif user4 == '2':
    login ()
  else:
    print()
    print('Please Select 1 or 2 to proceed!')
    time.sleep(2)
    os.system('clear')
    continue 