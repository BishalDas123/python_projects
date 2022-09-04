import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                        user="root",
                        passwd="A#@01wrft45",
                        database='bank_management_system')



def openAcc():
    n=input("Enter Name Of Customer : ")
    ac=input("Enter Account Number : ")
    db=input("Enter Date of Birth : ")
    add=input("Enter Address of customer : ")
    cn=input("Enter Contact Number : ")
    ob=int(input("Enter the Opening Balance : "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x= mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("successfull.......")
    main()

def depoAmo():
    amount=input("Enter the amount you want to deposit : ")
    ac=input("Enter Account Number : ")
    a=('select balance from amount where account_no=%s')
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0] +  amount
    sql=('update amount set balance where account_no=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()



def withdrawAmount():
    amount=input("Enter the amount you want to withdraw : ")
    ac=input("Enter Account Number : ")
    a='select balance from account where account_no=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result= x.fetchone()
    t=result[0]- amount
    sql=('update amount set balance where account_no=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()



def balEnq():
     ac=input('Enter Account No : ')
     a='select * from amount where account_no=%5'
     data=(ac,)
     x=mydb.cursor()
     x.execute(a,data)
     result=x.fetchone()
     print("Balance for Account :", ac , result[-1])
     main()


def DisDetails():
     ac=input('Enter Account No : ')
     a='select * from account where account_no=%5'
     data=(ac,)
     x=mydb.cursor()
     x.execute(a,data)
     result=x.fetchone()
     for i in result:
         print(i)
     main()
     

def CloseAcc():
    ac=input('Enter Account No : ')
    sql1='delete from account where account_no=%s'
    sql2='delete from amount where account_no=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()



def main():
    print('''
                        1.Open New Account
                        2.Deposite Amount
                        3.Withdraw Amount
                        4.Balance Enquary
                        5.Display Customer Details
                        6.Close An Account''')
    choice = input("Enter the Task 1/2/3/4/5/6 : ")
    if (choice == '1'):
        openAcc()
    elif (choice == '2'):
        depoAmo()
    elif (choice == '3'):
        withdrawAmount()
    elif (choice == '4'):
        balEnq()
    elif (choice == '5'):
        DisDetails()
    elif (choice == '6'):
        CloseAcc()
    else:
        print("invalid choise")
        main()
main()
