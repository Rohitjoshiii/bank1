# STEP1-OPEN THE FILE
file=open("abc.txt","r")


#STEP2-READ THE FILE
#result=file.read(2)        # read(2) means ir reads teo characters only

#result=file.readline()      #readline() it print one line only

#result=file.readlines()      #readlines() print all lines into list

line=file.readlines()         # for loop used when we dont want our text into list form
for result in line:

   print(result)
#STEP3-CLOSE THE FILE
file.close()