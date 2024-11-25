user_credentials = {
    "healthMin": "123health!",
    "reliefMin": "456relief",
    "FoodMin": "1789food!",
}
admin_credentials = {'imadmin': '123'}

def user(username,password):
    if username in user_credentials and user_credentials[username]==password:
        return"user login successful"
    elif username in admin_credentials and admin_credentials[username]==password:
        return "admin login successful"
    else:
        return "invalid username or password"

username=input("Enter username: ")
password=input("Enter password: ")
result_mass=user(username,password)
print(result_mass)