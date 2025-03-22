def fours_and_fives():
    num = int(input("Enter number: "))

    step_4 = 4
    step_5 = 5
    counter_4 = 0
    counter_5 = 0

    for i in range(0, num+1, step_4):
        if i % step_4 == 0:
            counter_4 += 1

        elif i == num:
            print(num)
    
    for i in range(0, num+1, step_5):
        if i % step_5 == 0:
            counter_5 += 1

        elif i == num:
            print(num)
    
    print(counter_4 - 1)
    print(counter_5 - 1)

    fours_and_fives()
        

fours_and_fives()