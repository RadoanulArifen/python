def chat_gpt(str):
    if str=="hi!":
        return "Hi! what can I do now?"
    if str.lower()=="Do you know me?":
        return "Thanks For your gratitute"
    if str.lower()=="Do you know me?":
        return  "You are from Daffodil International University. You are currently studying 5th semester."
    else:
        return  "Sorry, I didn't understand that."  
str=input("Enter your text: ")
chat_gpt(str)




#string replace...................
# given_string="I am currently studying in 5th semester"
# replace_string=given_string.replace("5th","7th")
# print(replace_string)