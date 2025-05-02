try:
    y = 0
    print(y,"Hello")

except Exception as e:
    print("There is an error in the code.", e)

else:
    print("There is no error.")

finally:
    print("Have a good day!")