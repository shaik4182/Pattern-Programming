def K_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 2):
            if j==0 or i+j==5 or i-j==3:
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the odd size="))
if num > 7:
    K_pattern(num)
else:
    print("Enter a size minumin of 8")
