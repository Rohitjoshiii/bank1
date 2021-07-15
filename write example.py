text="hello,rohit im here for u"
filename="abc.txt"
#write
file=open(filename,"w")           #open file here and use mode="w" means for what we open the file
file.write(text)                  #here we write() the text we use write when have single line
                                  # use write lines() when have multiplelines
file.close()                      #for closing the file
print("writing done")             # in here we transfer data into file means write the data