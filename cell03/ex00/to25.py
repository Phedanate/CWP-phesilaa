a = int(input("Enter a number less than 25: "))

if a > 25:
    print("ERROR")
else:
    for i in range(a, 26):
        print(i)