count = 0
total = 0
input = 1
while True:
    try:
        num = input("Enter a number")
        if number == 'done':
            break
        input = int(number)
        count = count + 1
        total = total + input
    except:
        print("Enter a valid number")
        print(count,total/count)
