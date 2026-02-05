count = 0
maximum = None

while True:
    try:
        num = int(input("Enter an integer (or 0 to stop): "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if num == 0:
        break

    count += 1

    if maximum is None or num > maximum:
        maximum = num

if count == 1:
    print(count, "number entered")
else:
    print(count, "numbers entered")

if count > 0:
    print("Maximum number entered:", maximum)
else:
    print("No numbers were entered.")
