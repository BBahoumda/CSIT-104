x = int(input("Enter a value between 0-1000: "))
total =0
while(x != 0):
    digit = x % 10
    total += digit
    x = x // 10
print("The total is ", total)
