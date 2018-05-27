# Using readlines() method
f = open('data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

# Using read() method
f = open('data.txt', 'r')
lines = f.read()
f.close()
print(lines)