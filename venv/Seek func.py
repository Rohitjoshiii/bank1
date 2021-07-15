with open("alphafile.py","r") as file:
    print(file.tell())          # tell()
   #print(ile.readline())
    print(file.readlines())

## seek()

    print(file.seek(8))
    print(file.readline())                   # here we learn how we can read file from where we want and skip tghe text here