value = int(input("Enter numbers: "))
reverse = int(str(value)[::-1])
times = 0
while True:
    total = value + reverse

    print(value, "+", reverse, "=", total)
    value = total
    reverse = int(str(total)[::-1])
    times += 1

    if value == reverse:
        print(total, 'is a palindrome number and take', times, 'times to reverse')
        break