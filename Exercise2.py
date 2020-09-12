#str.join()
#The join() method returns a string in which the string elements of sequence have been joined by str separator.
string = "-"
string = string.join(["abc",'def',"IJK"])
#output abc-def-IJK

#str.capitalize()	Converts the first character to upper case
string ="abcd"
string = string.capitalize()
print(string)
#output: Abcd


#casefold()	Converts string into lower case
string ="SADID"
string = string.casefold()
print(string)
#output: sadid


#center()	method will center align the string
string ="SADID"
string = string.center(10) # it will create 10 charecter storng
print(string)
#output:      sadid

#count()	Returns the number of times a specified value occurs in a string
string ="SADID"
string = string. count('D') 
print(string)
#output: 2


#encode()	Returns an encoded version of the string
string ="SA'D%ID"
string = string.encode()
print(string)
#output: b"SA'D%ID"


#endswith()	Returns true if the string ends with the specified value
string ="SADID"
string = string.endswith("D")
print(string)
#output: True



#expandtabs()	Sets the tab size of the string
string ="SADID\tTAHSIN"
string = string.expandtabs(16)
print(string)
#output: SADID           TAHSIN

#find()	Searches the string for a specified value and returns the position of where it was found
string ="SADID"
string = string.find("I")
print(string)
#output: 3


#format()	Formats specified values in a string
string = "For only {price:.2f} dollars!"
print(string.format(price = 49))
#output: For only 49.00 dollars!



#index()	Searches the string for a specified value and returns the position of where it was found
string ="SADID"
string = string.index("I")
print(string)
#output: 3


#isalnum()	Returns True if all characters in the string are alphanumeric
string ="SADID123"
string = string.isalnum()
print(string)
#output: True


#isalpha()	Returns True if all characters in the string are in the alphabet
string ="SADID123"
string = string.isalpha()
print(string)
#output: False


#isdecimal()	Returns True if all characters in the string are decimals
string ="123"
string = string.isdecimal()
print(string)
#output: True
# float number willl return false


#isidentifier()	Returns True if the string is an identifier
string ="SADID123"
string = string.isidentifier()
print(string)
#output: True
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.


#islower()	Returns True if all characters in the string are lower case
string ="Sadid"
string = string.islower()
print(string)
#output: False



#isprintable()	Returns True if all characters in the string are printable
string ="Hello!\nAre you #1?"
string = string.isprintable()
print(string)
#output: True



#isspace()	Returns True if all characters in the string are whitespaces
string ="   T   "
string = string.isspace()
print(string)
#output: False

#istitle()	Returns True if the string follows the rules of a title
string ="Welcome To Our Company"
string = string.istitle()
print(string)
#output: True

#isupper()	Returns True if all characters in the string are upper case
string ="Sadid"
string = string.isupper()
print(string)
#output: False


#ljust()	Returns a left justified version of the string
string ="Sadid"
string = string.ljust(20)
print(string, 'is my good friend')
#output: Sadid                is my good friend
#Return a 20 characters long, left justified version of the word "Sadid"

#lower()	Converts a string into lower case
string ="SaDid"
string = string.lower()
print(string)
#output: sadid  


#lstrip()	Returns a left trim version of the string
string ="       Sadid"
string = string.lstrip()
print(string)
#output: Sadid  


#partition()	Returns a tuple where the string is parted into three parts
string ="I alwys love to read books"
string = string.partition("love")
print(string)
#output: ('I alwys ', 'love', ' to read books')   


#replace()	Returns a string where a specified value is replaced with a specified value
string ="I am Sadid"
string = string.replace("Sadid","Tahsin")
print(string)
#output: I am Tahsin


#rfind()	Searches the string for a specified value and returns the last position of where it was found
string ="Sadid"
string = string.rfind("d")
print(string)
#output: 4 


#rindex()	Searches the string for a specified value and returns the last position of where it was found
string ="Sadid"
string = string.rfind("d")
print(string)
#output: 4 



#rjust()	Returns a right justified version of the string
string ="Sadid"
string = string.rjust(20)
print("Hollo", string)
#output: Hollo                Sadid 

#rsplit()	Splits the string at the specified separator, and returns a list
string = "Mango, Orange, Apple"
string = string.rsplit(", ")
print(string)
#output: ['Mango', 'Orange', 'Apple']


#rstrip()	Returns a right trim version of the string
string ="     Sadid     "
string = string.rstrip()
print(string)
#output:     Sadid


#split()	Splits the string at the specified separator, and returns a list
string = "Mango, Orange, Apple"
string = string.rsplit(", ")
print(string)
#output: ['Mango', 'Orange', 'Apple']


#splitlines()	Splits the string at line breaks and returns a list
string = "hello I am Sadid Tahsin.\n I love to read books. "
string = string.splitlines()
print(string)
#output: ['hello I am Sadid Tahsin.', ' I love to read books. ']


#startswith()	Returns true if the string starts with the specified value
string ="Sadid"
string = string.startswith('S')
print(string)
#output: True 


#strip()	Returns a trimmed version of the string
string ="      Sadid       "
string = string.strip()
print(string)
#output: Sadid 

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
string ="SadId"
string = string.swapcase()
print(string)
#output: sADiD

#title()	Converts the first character of each word to upper case
string ="welcome to our company"
string = string.title()
print(string)
#output: Welcome To Our Company 

#upper()	Converts a string into upper case
string ="SadId"
string = string.upper()
print(string)
#output: SADID

#zfill()	Fills the string with a specified number of 0 values at the beginning
string ="SadId"
string = string.zfill(10)
print(string)
#output: 00000SADID