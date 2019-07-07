def getSum(n): 
   
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum
  
for i in range (1,4):
    n=input("enter")
    print(getSum(n)) 
