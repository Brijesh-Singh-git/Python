'''Write a Python program that displays a message as follows for a given number:

If it is a multiple of 3, display "Zip"

If it is a multiple of 5, display "Zap"

If it is a multiple of both 3 and 5, display "Zoom"

If it does not satisfy any of the above given conditions, display "Invalid'''


a =55 
if(a%3==0): 
    print("Zip")
elif(a%5==0):
    print("Zap")
elif(a%3==0 and a%5==0):
    print("Zoom")
else: 
    print("Invalid")