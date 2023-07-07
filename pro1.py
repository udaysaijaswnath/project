import pywhatkit
import random
from datetime import datetime
table={}
totalBill=int()
personBill=[]
def sendMsg(phNum,msg):
    try:
        pywhatkit.sendwhatmsg_instantly("+91"+str(phNum),msg,5,True,6)
        print("Message went successfully")
    except:
        print("No message went")
def printingTotalData(totalData):
    if len(totalData)==0:
        print("No orders up to now")
    else:
        for i in totalData:
            abc=0
            for j in i:
                if abc==2:print("table number :",end="")
                elif abc==3:print("Mobile number :",end="")
                print(j,end="\n")
                abc+=1
def emptyTablesPrint(table):
    emptyTables=[]
    for i in table.items():
        if i[1][0]==0:emptyTables.append("Table-"+str(i[0]))
    if len(emptyTables)==0:
        pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),"All tables are reserved kindly wait for 15 mins.")
        print("There are no empty tables")
    else:
        for i in emptyTables:print(i,end="\n")
        tableNumber=int(input("Select Table:"))
        #pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),"your table "+str(tableNumber)+" is booked at our hotel.",3,True,3)
        OTP=random.sample("123456789",6)
        OTP="".join(OTP)
        #sendMsg(phoneNumber,"Your OTP is Book the Table is "+str(OTP))
        pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),"Your OTP is Book the Table is "+str(OTP),10,True,3)
        az=input("Enter Otp to book your table")
        if az==OTP:
            table[tableNumber][0]=phoneNumber
            sendMsg(phoneNumber,"Table"+str(tableNumber)+"is booked for you")

def reversedTablesPrint(table):
    reservedTables=[]
    for i in table.items():
        if i[1][0]!=0:reservedTables.append("Table-"+str(i[0]))
    if len(reservedTables)==0:print("There are no reversed tables")
    for i in reservedTables:print(i,end="\n")

def Bill():
    totalBill=0
    tableBill=int(input("For which table number you want to get the bill::"))
    Bills=""
    personBill=[]
    personBill.append(tableBill)
    personBill.append(table[tableBill][0])
    use=""
    for i in range(len(item)):
        if table[tableBill][1][i]!=0:
            totalBill+=(table[tableBill][1][i]*item[i+1][1])
            use=item[i+1][0]+str((table[tableBill][1][i]*item[i+1][1]))
            personBill.append(use)
            Bills+=use+"\n"
    personBill.append("total"+str(totalBill))
    totalData.append(personBill)
    print(Bills,end="")
    print("Your total bill is",totalBill)
item={1:["roti",20],2:["curry",50],3:["tea",10]}
for i in range(1,11):
    table[i]=[0,[0]*len(item)]
big=0
for i in item.values():
    if big<len(i[0]):big=len(i[0])
date_time = datetime.fromtimestamp(1887639468)
s=""
s+="FTS Hotel \n"
s+=str(date_time)+"\n"
for i in item.items():
    s+=str(i[0])+"."+i[1][0]+"-"*(big-len(i[1][0]))+"----"+str(i[1][1])+"\n"
ib=[]
phoneNumber=int()
totalData=list()
tableNumber=int()
selecteditem=int()
while True:
    a=input("1.book table\n2.send menu\n3.amount bill\n4.send bill\n5.send ack\n6.Exit\n7.close hotel \n")
    match a:
        case "1":
            phoneNumber=int(input("enter mobile number:"))
            print("RESERVED TABLES")
            reversedTablesPrint(table)
            print("EMPTY TABLES")
            emptyTables=[]
            for i in table.items():
                if i[1][0]==0:emptyTables.append("Table-"+str(i[0]))
            if len(emptyTables)==0:
                pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),"All tables are reserved kindly wait for 15 mins.")
                print("There are no empty tables")
            else:
                for i in emptyTables:print(i,end="\n")
                tableNumber=int(input("Select Table:"))
                #pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),"your table "+str(tableNumber)+" is booked at our hotel.",3,True,3)
                OTP=random.sample("123456789",6)
                OTP="".join(OTP)
                #sendMsg(phoneNumber,"Your OTP is Book the Table is "+str(OTP))
                lll=""
                lll="Your OTP for Book the Table is "+str(OTP)
                pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),lll)
                az=input("enter you OTP Here:: ")
                if az==OTP:
                    table[tableNumber][0]=phoneNumber
                    sendMsg(phoneNumber,"Table "+str(tableNumber)+" is booked for you")
        case "2":
            print("RESERVED TABLES")
            reversedTablesPrint(table)
            tableNumber=int(input("For which table your are sending the menu::"))
            sendMsg(table[tableNumber][0],s)
            while True:
                print("ITEMS MENU")
                print(s+"0.Exit")
                selecteditem=int(input("Select Items::"))
                if selecteditem==0:break
                table[tableNumber][1][selecteditem-1]+=int(input("how many "+str(item[selecteditem][0])+" you want::"))
        case "3":
            print("RESERVED TABLES")
            reversedTablesPrint(table)
            totalBill=0
            tableBill=int(input("For which table number you want to get the bill::"))
            Bills=""
            date_time = datetime.fromtimestamp(1887639468)
            use=""
            use+="FTS Hotel \n"
            use+=str(date_time)+"\n"
            use+="Table number"+str(tableBill)
            for i in range(len(item)):
                if table[tableBill][1][i]!=0:
                    totalBill+=(table[tableBill][1][i]*item[i+1][1])
                    use=item[i+1][0]+"---"+str((table[tableBill][1][i]*item[i+1][1])) 
                    Bills+=use+"\n"
            totalData.append(personBill)
            print(Bills,end="")
            print("Your total bill is",totalBill)
        case "4":
            print("RESERVED TABLES")
            reversedTablesPrint(table)
            totalBill=0
            tableBill=int(input("For which table number you want to send the bill::"))
            Bills=""
            personBill=[]
            personBill.append("FTS hotel")
            Bills+="Fts Hotel \n"
            date_time = datetime.fromtimestamp(1887639468)
            personBill.append(str(date_time))
            Bills+="Date and Time:"+str(date_time)+"\n"
            personBill.append(tableBill)
            personBill.append(table[tableBill][0])
            use=""
            for i in range(len(item)):
                if table[tableBill][1][i]!=0:
                    totalBill+=(table[tableBill][1][i]*item[i+1][1])
                    use=item[i+1][0]+"---"+str((table[tableBill][1][i]*item[i+1][1]))
                    personBill.append(use)
                    Bills+=use+"\n"
            personBill.append("Total Bill"+str(totalBill))
            totalData.append(personBill)
            print(Bills,end="")
            sendMsg(table[tableBill][0],Bills+"your total bill is "+str(totalBill))
            #pywhatkit.sendwhatmsg_instantly("+91"+str(phoneNumber),"your total bill is "+str(totalBill),5,True,5) 
        case "5":
            print("RESERVED TABLES")
            reversedTablesPrint(table)
            tableBill=int(input("For which table number you want to send the Acknowleadgement::"))
            sendMsg(table[tableBill][0],"your total bill is paid \n Thank You \n Visit Again\n FTS")
            
        case "6":
            print("Todays overall bill")
            printingTotalData(totalData)
        case "7":
            print("Today's orders are completed and Hotel is closed")
            break



            




