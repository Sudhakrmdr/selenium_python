# read - r
# write - w
# apeend - a
fil = open("C:\\Users\\Shiva\\PycharmProjects\\pythonProject\\HelloWorld\\Python.txt", 'w')
fil.write("Banana")
fil.write("Mangoes")
# fil.close()

filread = open("C:\\Users\\Shiva\\PycharmProjects\\pythonProject\\HelloWorld\\Python.txt", 'r')
print(filread.readline())
