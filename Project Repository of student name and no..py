#We make two list one for name and second for numbers according to question....
list1=["Rudra","Krishna","Shivang","Dev","Shyam","Aman","Himanshu","Prashant","Anchal"
       ,"Shubham","Anurag","Bassam","Ankit","Sahil","Shiv"]
list2=[7896543781,9897546973,8735439472,9675432962,8768906532,6547891234,8764219061,9655486543
       ,6667889564,9863459673,6316568763,7774656688,9874345432,8898778871,9998734685]
#here we print name and contact number with the help of for loop....
for i in range(len(list1)):
    print("{} <--> {}".format(list1[i],list2[i]))

#we use while loop for yes(to continue) and no(to break)....
while(True):
    num=int(input("Enter the Number: "))  #to find the name of user we have to take input the-
    if len(str(num))!=10:                 #--number from the user....
        print("Invalid Number")
    else:
#for loop to print the name and the contact number of the student according to user demand....

        for i in range(len(list2)):  
            if(list2[i]==num):
                print("{} <--> {}".format(list1[i],list2[i]))
#Yes and No condition to continue or break the execution....
    x=input("Is you want to extract more (Y/N): ")
    if x=="N":
        print("Have a nice day")
        break                    # use break to break the execution
    else:
        continue                 # use continue to continue the execution



