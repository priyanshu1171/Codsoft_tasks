list1 = ['a', 'b', 'c', 'd', 'e', 
         'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o', 
         'p', 'q', 'r', 's', 't', 
         'u', 'v', 'w', 'x', 'y', 
         'z', '0', '1', '2', '3', 
         '4', '5', '6', '7', '8',
         '9', '0', 'A', 'B', 'C',
         'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 
         'X', 'Y', 'Z', '!', '@',
         '#', '$', '%', '^', '&',
         '*', '+', '-', '/', '=',
         '~', '?'] 
import random 
x = int(input("Length the of password ?  ")) 
y = " "
for i in range(x): 
    y+= random.choice(list1) 
print("Password is : ",y)