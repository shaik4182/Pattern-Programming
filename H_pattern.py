def H_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 1):
            if j==0 or j==n//2 or i==n//2:
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the size="))
if num > 7:
    H_pattern(num)
else:
    print("Enter a size minumin of 8")
