correct_password='Cisco123'
name=raw_input('Enter your Name: ')
password=raw_input('Enter the password : ')

while correct_password != password:
    raw_input("wrong password ! enter the password again:  ")

print ('Hi {} you are logged in').format( name)