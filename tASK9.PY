#Task1: Output for the following code
import numbers
import re


print("")
print("Output the given program:")
print("")
print("********************************************")
print("")
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter( lambda x : x>4, data)
print(list(result))
print("")
print("_____________END OF PROGRAM_____________________________")
print("")

# Output = [10, 501, 22, 37, 100, 999, 87, 351] . which prints the list of numbers greater than 4 in given list using filer and lambda function

#Task2: Check every element in the given list is an interger or string using lambda function
print("")
print("Program to check every element in the given list is an interger or string using lambda function :")
print("")
print("********************************************")
print("")
def check_item_dtype_in_list(item_range):
    if all(map(lambda x: str(x).isdigit(), item_range)):
        item_range = list(map(int, item_range))
        print('all are integer')
        print(item_range)
        return 
    elif all(isinstance(item, str) for item in item_range):
        print('all are string')
        print(item_range)
        return 
    elif any(map(lambda x: str(x), item_range)):
        print('mixed dtype')
        print(item_range)
        return 
check_item_dtype_in_list([5, 2, 3])
check_item_dtype_in_list(["python", "guvi", 'program'])
check_item_dtype_in_list([2, '5', 'Two'])
print("")
print("_____________END OF PROGRAM_____________________________")
print("")



#Task3: Create fibonacci series using lambda function
print("")
print("Program to Create fibonacci series using lambda function :")
print("")
print("********************************************")
print("")
n = 50
def fibonacci(count):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
            range(2, count)))
    return fib_list[:count]

print(fibonacci(n))
print("")
print("_____________END OF PROGRAM_____________________________")
print("")


#Task4: To validate the regular expression for email_id, mobile_number_bangladesh, telephone_numer_US, 16 character alpha-numberic password composed of alphabets of upper case_lower case_special character_numbers
print("")
print("Program to validate the regular expression: ")
print("")
print("********************************************")
print("")
print("Email_ID regular expression: ")
print("")

def verify_email(data):
    email_pattern='[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z]{2,6}'
    if re.fullmatch(email_pattern, data):
        return True
    else:
        return False
    
data = 'python@guvi.com'
print("Given email_id is: ", data, "and the value is: ",verify_email(data))
print("__________________________________________")
print("")


print("")
print("bangladesh mobile number regular expression: ")
print("")
def verify_bangladesh_number(data1):
    bangladesh_pattern='(?:\\+88|88)?(01[3-9]\\d{8})'
    if re.fullmatch(bangladesh_pattern, data1):
        return True
    else:
        return False
    
data1 = '8801996409999'
print("Given mobile number is: ", data1, "and the value is: ",verify_bangladesh_number(data1))
print("")
print("__________________________________________")
print("")

print("")
print("US mobile number regular expression: ")
print("")
def verify_us_number(data1):
    us_pattern='(^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$)'
    if re.fullmatch(us_pattern, data1):
        return True
    else:
        return False
    
data2 = '(234)-555-1234'
print("Given mobile number is: ", data2, "and the value is: ",verify_us_number(data2))
print("")
print("__________________________________________")
print("")


print("")
print("Regular expression for password: ")
print("")
def verify_password(data3):
    password_pattern='[A-Za-z0-9!@#$%^&*()_]{8,16}'
    if re.fullmatch(password_pattern, data3):
        return True
    else:
        return False
    
data3 = 'tAsd!@t'
print("Given password is: ", data3, "and the value is: ",verify_password(data3))
print("")
print("_______________END OF PROGRAM___________________________")
print("")

