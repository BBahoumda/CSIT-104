def collatz(n):
        while n!=1:
            print(n)
            if n%2 == 0:
                 n = n // 2
            else:
                 n= ((n*3) +1) // 2 
def main():
    n = int(input("Enter a number"))
    collatz(n)

main()
        
        
