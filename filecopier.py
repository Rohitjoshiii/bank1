from_filename=input("Enter source file name :")
to_filename=input("Enter destination file name")
with open(from_filename,"r") as from_filename:
     content=from_filename.readlines()
     with open(to_filename,"w")as to_filename:
         to_filename.writelines(content)



print("done")


#here we learn that how we can transfer data(text) from one file to another file
#use with keyword so need to close file again and again .the fill close automatically
#programmers used with statement with code because no need to write close()