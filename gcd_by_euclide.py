
a = input("Enter the first numbers:")
a = int(a)
b = input("Enter the second numbers:")
b = int(b)

if b > a:
    a, b = b, a

    while a != b:
        if b == 0:
            break
        if a > b:
            a = a-b
        else:
            b = b-a
        print("GCD is", a)
