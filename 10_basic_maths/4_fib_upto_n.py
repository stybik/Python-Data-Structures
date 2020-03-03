def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    
    n = int(input())
    if n <= 0:
        print("Please enter a positive integer")
    else:
        for i in range(n):
            print(fib(i)) 