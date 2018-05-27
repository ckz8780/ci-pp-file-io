# 'w' mode overwrites
f = open('newfile.txt', 'w')
f.write("Hello")
f.close()

# 'a' mode appends
f = open('newfileappend.txt', 'a')
f.write("Hello\n")
f.close()

# Using writelines:
f = open('writelines.txt', 'a')
lines = ['Hello', 'World!', 'Welcome', 'To', 'File', 'IO']
f.writelines(lines)
f.close()

# Using writelines with join method to append newlines:
f = open('writelinesjoin.txt', 'a')
lines = ['Hello', 'World!', 'Welcome', 'To', 'File', 'IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()