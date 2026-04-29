# Login System 

print('Welcome to our  Website Glad to Have You here Login For more More Access!!')


users = {}




while True:
  user_choice = input("Do you Want to 'register' , 'login' or 'Exit' ")

  if user_choice == 'Exit':
     print('Thank you!')
     break
  
  # Register Section
  elif user_choice == 'register':
     username = input("Enter a username: ")
     password = input('Enter Password: ')
     if username in users : # Check if User already exist in the dictionary
        print('username Already existed') 
    # Check Password Lenght
     elif len(password) < 6 : 
        print('Too Short')
     elif len(password) > 10 :
        print('Execellent')
     else :
        users[username] = password
        print('Saved')

    # Login Section
  elif user_choice == 'login':
     username = input("Enter a username: ")
     passwordL = input('Enter Password: ')
     # Check User input Exist 
     if username in users and passwordL == users[username]:
        print('Welcome')
     elif username in users and passwordL != password:
        print('Wrong Password')
     else :
        print('USER NOT FOUND!!')
  else:
    print("Invalid choice, try again.")
 
    
     

