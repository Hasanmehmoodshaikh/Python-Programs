src = open('file-programs/append.txt','r')
dst = open('file-programs/read.txt','w')

data = src.read()
dst.write(data)

print('file copied succesfully')