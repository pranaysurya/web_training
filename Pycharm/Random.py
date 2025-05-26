# def cal (num1, num2 = 4):
#     res = num1 * num2
#     print(res)

# cal(5,6 )

def checker(num1, num2):
    if num1 * num2 > 1000:
        print(num1 + num2)
    
    elif num1 * num2 < 1000:
        print(num1 * num2)

checker(20, 30)

checker(60, 70)