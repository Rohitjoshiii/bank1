filename=input("enter file name :")   # this is file name want from user
lines=[]                              # here  we stored the data into that file which we want from user
print("enter content")
while True:
    line=input()
    if line=="exit":
        break
    else:
        lines.append(line +'\n')
print(lines)

#open
file=open(filename,"w")

#write
file.writelines(lines)

#close
file.close()

