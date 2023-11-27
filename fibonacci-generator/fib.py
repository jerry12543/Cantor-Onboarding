def main():
    try:
        num_terms = int(input("Enter number of Fibonacci terms: "))
        a, b = 1,1
        for i in range(0,num_terms):
            print(a)
            a, b = b, a+b
    except:
        print("Invalid input. Input must be a numeric value.")
main()