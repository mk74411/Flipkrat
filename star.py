num_row=int(input("enter the number of rows"))
x=1
for i in range(0,num_row):
    for j in range(0,x):
      print("*",end="")
    x=x+1
    print()

num_rows=int(input("enter the number of rows"))
for a in range(num_rows+1,0,-1):
    for b in range(0,a-1):
      print("*",end="")
    print()
