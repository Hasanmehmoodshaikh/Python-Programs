import os

try:
    os.remove('file-programs/append.txt')
    os.rmdir('file-programs/myfolder')
    print('file delete successfully')


except FileNotFoundError as e:
    print('file you want do delete does not exist')    
