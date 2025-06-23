# username = "admin"
# password = "12345678"
user_input = str(input("Enter your Username : "))
pass_input = complex(input("Enter your Password : "))

if user_input == "admin" and pass_input == complex("12345678"):
    print("login Success !!!!")
else:
    print("invalid Username or password")