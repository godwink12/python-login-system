import string

# Login System 

print('Welcome to our  Website Glad to Have You here Login For more More Access!!')

users = {}

while True:
  user_choice = input("Do you Want to 'register' , 'login' or 'Exit' ")

  if user_choice == 'Exit':
    print('Thank you!')
    break
  elif user_choice == 'register':
    username = input("Enter a username: ")
    password = input('Enter Password: ')
    if username in users:  # Check if user already exists in the dictionary
      print('username Already existed')
    elif len(password) < 6:
      print('Too Weak')
    elif not any(char.isupper() for char in password):
      print('Needs a Capital Letter')
    elif not any(char.isdigit() for char in password):
      print('Needs a Number')
    elif not any(char in string.punctuation for char in password):
      print('Needs a symbol')
    else:
      users[username] = password
      if len(password) >= 10:
        print('Excellent')
      else:
        print('Saved')
  elif user_choice == 'login':
    username = input("Enter a username: ")
    passwordL = input('Enter Password: ')
    # Check User input Exist 
    if username in users and passwordL == users[username]:
      print('Welcome')
    elif username in users and passwordL != users[username]:
      print('Wrong Password')
    else :
      print('USER NOT FOUND!!')
  else:
    print("Invalid choice, try again.")
 
    
     

