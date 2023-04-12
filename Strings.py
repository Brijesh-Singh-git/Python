"""b = "Aman's"
print(b)
print(type(b))"""

"""greeting ="Good Morning,"
name = " Aman"

c= greeting + name
#print(c) 
#print(c[19]) """

"""name = "Aman"

print(name[3]) # Indexing starts from 0 

#name[3] = 'd' ----> We cannot change the character of string it will NOT WORK

#SLICING IN PYTHON
print(name[0:3])  #---> It will exllide the last number it will only print till 0,1,2
"""

"""name = "Harry"
print(name[:3]) #----> It is same as name[0:3] 
print(name[1:]) # ---> It is same as name[1:5]

#Negative Indexing ----> Negative index starts from last character of the string and mive on to left side like -5,-4,-3,-2,-1

print(name[-4:-1]) #-----> This is same as name[1:4]"""



"""name = "Amazing"

d = name[1:6:1]  #---> It will not skip anything  #OUTPUT -- mazin

d= name[1:6:2]  #---> It will skip 1-1 value in betwwen #OUTPUT -- mzn
print(d)""" 

"""
story ="once upon a time there was a developer who used to love to build amazing website and work with amazing new tools in the development"

#String Fucntions 

print(len(story))   #------>It will return the length of the String 

print(story.endswith("vdhgvhd"))  # ------>This function tells whether the string ends with "vdhgvhd" this or not and it will return TRUE or FALSE

print(story.count("d"))   #-----> It will count the total number of occurance in the string 

print(story.capitalize())  #----> It will capitalize the first character of the string  

print(story.find("developer"))  #----->This fucntion finds the word and returns the index of (first) occurance of that word in the String

print(story.replace("to","HELLOTHIS")) #---> It will replace all the occurances with the new word in the string


"""



story ="Amna is a good.\nHe is very good boy" 
print(story)