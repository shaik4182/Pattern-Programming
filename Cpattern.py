def c_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 1):
            #print two columns
            if i==0 and j!=0 or i==n-1 and j!=0 or j==0 and i!=0 and i!=n-1:
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the size="))
if num > 7:
    c_pattern(num)
else:
    print("Enter a size minimum of 8")
