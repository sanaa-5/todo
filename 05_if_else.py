# if , else , elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# Short Hand If ... Else
a = 2
b = 330
c = 500
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# The and keyword is a logical operator, and is used to combine 
# conditional statements:
if a > b and c > a:
  print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine 
# conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# The not keyword is a logical operator, and is used to reverse the 
# result of the conditional statement:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")




























