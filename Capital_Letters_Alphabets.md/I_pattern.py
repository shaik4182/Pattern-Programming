def I_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 1):
            if i==0 or i==n-1 or j==n//4:
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the size="))
if num > 7:
    I_pattern(num)
else:
    print("Enter a size minumin of 8")
