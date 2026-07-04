#drawing shapes triangle using print statement

print('   /|')
print('  / | ')
print(' /  |' )
print('/___|')

#variable is like like a container that stores the value

#understanding imp of variable 

print("my name is john ")
print("john  age is 30 ")
print("john wants make fell like to play and sing ")
 
#if i want to change john name into another i have to find and change but if we use variable we can change it by 
#by just chaning name variable

char_name = "jossh"
print("my name is "+ char_name )
print(char_name +"  age is 30 ")
print(char_name+" wants make fell like to play and sing ")

#working with strings
#fun is named block of code that it gets executed when it is called 

print(char_name.upper().isupper())
print(char_name[3])
#starts with zero and ends with len-1 last num is not called
print(char_name[0:3])
print(char_name.index("sh"))

#working with numbers
x=10
#basic arthemetic
print((x+x) , " " ,(x-x), " " ,(x*x), " " ,(x/(x+1)), " " ,(x%(x+1)))
#basic fun
print(abs(-10.87))
print(round(10.89))
print(min(10,2,3,4))

#input fromuser
name = input("enter your name :")
age = int(input("enter your age"))
print(f"my name is :{name}")
print(f"my age is :{age}")