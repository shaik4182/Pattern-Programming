def J_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 1):
            if i==0 or j==n//4 or i==n-1 and j<n//4 or j==0 and i>n-3:
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the odd size="))
if num > 7:
    J_pattern(num)
else:
    print("Enter a size minumin of 8")
