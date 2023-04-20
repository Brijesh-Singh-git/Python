print("Program is started")

try:
    print(50/5)
except TypeError:   # Will be executed only when the error is thrown
    print("Entered into except block - Handle TypeError ")
except ZeroDivisionError:   # Will be executed only when the error is thrown
    print("Entered into except block - Handle ZeroDivisionError ")
else:
    print("Entered into Else - Block")
finally:
    print("This is finally block")
print("Program completed")

