"""a = input("Enter your Name")

b= " Good Afternoon!!" 

print(a+b)"""



letter = '''Dear <|Name|>, 
You are selected!

Date: <|Date|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n") 

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)