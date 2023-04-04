bill = 0 
size = (input("Enter the size of your pizza-example( S - M - L)"))
add_papperoni =(input("Do you want extra pepperoni serving - (Y - N)"))
extra_cheese = (input("Do you want extra Cheese Serving - (Y -N)"))

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25


if add_papperoni =="Y" :
  if size == "S" :
    bill += 2
  else:
    bill +=3
if extra_cheese  =="Y" :
    bill += 1
print(f"Your final bill is $ {bill} ")
