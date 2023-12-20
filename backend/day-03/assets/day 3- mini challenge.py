print("<Positive or Negative>")
Number = int(input("Enter an integer: "))

if Number > 0:
    print(f"Your integer {Number} is a Positive Number")
elif Number < 0:
    print(f"Your integer {Number} is a Negative Number")
else:
    print(f"Your integer {Number} is neither positive nor negative (it is zero)")
    
