def A_pattern(n): 
    for i in range(n): 
        for j in range((n // 2) + 1):
            #print two column
            if ((j == 0 or j == n //2) and i != 0 or
                #print first line
                i == 0 and j != 0 and j != n // 2 or
                #print middle line
                i == n // 2): 
                print("*", end = " ") 
            else: 
                print(" ", end = " ")   
        print() 
num = int(input("Enter the size="))
if num > 7:
    A_pattern(num)
else:
    print("Enter a size minumin of 8")
