
# import regex
import re

"""
findall	--> Returns a list containing all matches
search --> 	Returns a Match object if there is a match anywhere in the string
split	--> Returns a list where the string has been split at each match
sub	--> Replaces one or many matches with a string
"""


txt = "The rain in Spain in floor"
x = re.search("in", txt)

print(x) # <re.Match object; span=(6, 8), match='in'>

if x:
  print("YES! We have a match!")
else:
  print("No match")

a = re.findall("a" , txt)
print(a)

b = re.split("in",txt)
print(b)

c = re.sub("in","out",txt)
print(c)


"""
The Match object has properties and methods used to retrieve information--

.span() --> returns a tuple containing the start-, and end positions of the match.
.string --> returns the string passed into the function
.group() --> returns the part of the string where there was a match

"""

string = "lets play in the rain in the ground above the cloud"
s = re.search("the",string)
print(s) # if not present -> None will printed

print(s.span())
print(s.string)
print(s.group())


"""
Metacharacters

[] --> A set of characters between user defined range	"[a-m]"	
\	 --> Signals a special sequence --> print digits	"\d"	
.	 --> Any character (except newline character)	"he..o"	
^	 --> Starts with	"^hello"	
$	 --> Ends with	"planet$"	
*	 --> Zero or more occurrences	"he.*o"	
+	 --> One or more occurrences	"he.+o"	
?	 --> Zero or one occurrences	"he.?o"	
{} --> Exactly the specified number of occurrences	"he.{2}o"

"""



