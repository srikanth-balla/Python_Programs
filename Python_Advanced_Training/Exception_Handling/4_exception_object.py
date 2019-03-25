# try:
#     # this code is expected to throw exception
# except ExceptionType as ex:
#     # code to handle exception
try:
    number = eval(input("Enter a number: "))
    print("The number entered is", number)
except NameError as ex:
    print("Exception:", ex)