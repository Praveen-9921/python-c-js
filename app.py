# user_input =int (input("Enter your age"))
# if user_input >= 18:
#     {
#         print("You are eligible")
#     }
# else:
#     {
#         print("You are not eligible")
#     }


user_input =int (input("Enter time  "))
user_input1 =input("Enter am or pm  ")
user_input1= user_input1.lower()
time=f"{user_input} : {user_input1}"
print(user_input1)
if user_input>=0 and user_input <=12 and user_input1 =="am":
    {   
        print(f"Hello its, {time} Good Morning" )
       
    }
elif user_input>=0  and user_input <=12 and user_input1 =="pm":
    {   
        print(f"Hello its, {time} Good Night" )
    }
else:
    {
        print("Enter valid input")
    }
