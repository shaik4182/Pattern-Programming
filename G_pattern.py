def G_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 1):
            if (i==0 and j!=0 and j!=n//2) or (j==0 and i!=0 and i!=n-1) or (i==n-1 and j!=0 and j!=n//2) or (j==n//2 and i>n//2 and i!=n-1) or (i==n//2 and j>1) or i==1 and j==n//2:
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the size="))
if num > 7:
    G_pattern(num)
else:
    print("Enter a size minumin of 8")
