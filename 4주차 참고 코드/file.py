
# f = open('test.txt', 'w')
#
# f.write("hello")
# f.close()

# f = open('test.txt', 'a')
#
# f.write("hello world!")
# f.close()

f = open('test.txt', 'r')
lines = f.readlines()

for line in lines:
    print(line)

f.close()
