myfile = open('file-programs/sample.txt','w')
data = input('Enter your data to be written in the file - ')

myfile.write(data)
print('data saved in your file succecfully')