## BANK MANAGEMENT SYSTEM

print("****CENTRAL BANK OF BHARAT****")
print()

##creating database
import mysql.connector as c
con=c.connect (host="localhost",user="root", passwd="1234")
cursor=con.cursor()
cursor.execute("create database if not exists CENTRAL_BANK_OF_BHARAT")
cursor.execute("use CENTRAL_BANK_OF_BHARAT")
print()

##CREATING REQUIRED TABLES
cursor.execute("create table if not exists user_details(ACCOUNT_NO varchar(20) primary key, USER_NAME varchar(30) NOT NULL, CITY varchar(20) NOT NULL, MOBILE_NO char(10) NOT NULL, BALANCE int(10))")
cursor.execute("create table if not exists transactions(ACCOUNT_NO varchar(20),AMOUNT int(6), DATE_OF_TRANSACTION date, TRANSACTION_TYPE varchar(20),foreign key (ACCOUNT_NO) references user_details(ACCOUNT_NO))")
con.commit()
while True:
    print("1 --> CREATE ACCOUNT")
    print("2 --> DEPOSIT MONEY")
    print("3 --> WITHDRAW MONEY")
    print("4 --> DISPLAY ACCOUNT")
    print("5 --> DISPLAY TRANSACTION")
    print("6 --> DELETE ACCOUNT")
    print("7 --> EXIT")
    ch=int(input("Enter your choice:"))
    print()
    
##PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        print("ALL INFORMATION PROMPTED ARE MANDATORY TO BE FILLED!!")
        acno=str(input("Enter account number: "))
        name=input("Enter name(limit 30 characters): ")
        city=str(input("Enter city name: "))
        mn=str(input("Enter mobile no.: "))
        balance=0
        cursor.execute("INSERT INTO user_details values({},'{}','{}','{}',{})".format(acno,name.upper(),city.upper(),mn,balance))
        con.commit()
        print("Account is successfully created!!!")
        print()
        
##PROCEDURE FOR UPDATIONG DETAILS AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
    elif(ch==2):
        acno=str(input("Enter account number:"))
        dp=int(input("Enter amount to be deposited:"))
        dot=str(input("Enter date of Transaction: YYYY-MM-DD "))
        ttype="DEPOSIT"
        cursor.execute("insert into transactions values({},{},'{}','{}')".format(acno,str(dp),dot,ttype))
        cursor.execute("update user_details set balance=balance + {} where ACCOUNT_NO = {}".format(str(dp),acno))
        con.commit()
        print("Money has been deposited successfully!!!")
        print()
        
##PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT
    elif(ch==3):
        acno=str(input("Enter account number:"))
        wd=int(input("Enter amount to be withdrawn:"))
        dot=str(input("enter date of transaction: YYYY-MM-DD "))
        ttype="WITHDRAWL"
        cursor.execute("insert into transactions values({},{},'{}','{}')".format(acno,str(wd),dot,ttype))
        cursor.execute("update user_details set balance=balance - {} where ACCOUNT_NO = {}".format(str(wd),acno))
        con.commit()
        print("Money has been withdrawn successfully!!!")
        print()
        
##PROCEDURE FOR DISPLAYING THE ACCOUNT OF THE ACCOUNT HOLDER AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif(ch==4):
        acno=str(input("Enter account number:"))
        print("(ACCOUNT_NO, NAME, CITY, MOBILE_NO, BALANCE)")
        cursor.execute("select * from user_details where ACCOUNT_NO = {}".format(acno))
        for i in cursor:
            print(i)
            print()
            
##PROCEDURE FOR DISPLAYING THE USER TRANSCTIONS AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif(ch==5):
        acno=str(input("Enter account number:"))
        print("(ACCOUNT_NO, AMOUNT, TRANSACTION_DATE, TRANSACTION_TYPE)")
        cursor.execute("select * from transactions where ACCOUNT_NO = {}".format(acno))
        for i in cursor:
            print(i)
            print()

##PROCEDURE FOR CLOSING AN ACCOUNT
    elif (ch==6):
        acno=str(input("Enter account number:"))
##        cursor.execute("delete from user_details where ACCOUNT_NO = {}".format(acno))
        cursor.execute("delete from transactions where ACCOUNT_NO = {}".format(acno))       
        print("Your account has been deleted successfully!!!")
        print()

##PROCEDURE FOR EXIT
    elif (ch==7):
        print("THANKS FOR VISITING!!")
        break

##PROCEDURE IF USER ENTERS NUMBER > 7
    else:
        print("INVALID SELECTION!!")
