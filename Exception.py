# try except else finally


try:
    print("Enter x value: ")
    x = int(input())

    print("Enter y value: ")
    y = int(input())
    print(x / y)
except:
    print("please enter other than zero denominator ")

else:
    print("printing else block ")
finally:
    print("Always executing finally block ")

