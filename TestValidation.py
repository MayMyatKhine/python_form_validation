
print("Attention-Name must be not more than 30 alphabet,shouldn't have any symbol,shouldn't have any number");

n =  input("Please enter your name: ")


SpecialSym =['$', '@', '#', '%']
val = True
if (n.isalpha()) == True:
  print('Name must be alphabets');
  val = False
if len(n) > 30:
  print('length should be not be greater than 30')
  val = False
if any (char in SpecialSym for char in n):
  print('Name cannot have any symbol $@#')
  val = False
if (n.isdigit()) == True:
  print('Cannot have any number')
  val = False
for character in n:
  if character.isdigit():
     print('Cannot have any number')
     val = False
if val:
  print("Success Name",n)




print("Attention-Mobile Number must be Not more than 15 number,must include Country code and + sign,should not have any other symbol and alphaet");
# Mobile Number  validation in Python
import re
mno = int(input("Please enter your mobile number: "))
 
	
SpecialSym =['$', '@', '#', '%']
chars_to_check = ['+']
val = True
 
if (mno > 15)==False:
  print('length should be not be greater than 15')
  val = False
if  any(char in chars_to_check for char in str(mno)):
 print("+ sing character was not found")
 val = False

Pattern = re.compile("(0|99)? {15}")
if( Pattern.match(str(mno)))==True:
  print ("InValid Number")  
  val = False
if val:
   print("Success Mobile Number",mno)



print("Attention-Password must have Min 8 character, but not more than 15 character,must have at least 1 capital Letter and 1 number,allow at least one symbols of$#@,should not have spacing.");
#Password  validation in Python
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<8 or len(p)>15):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")


