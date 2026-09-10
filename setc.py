# age=int(input("enter age:"))
# if age<13:
#     print("child")
# elif age>=13 and age<=19:
#     print("teenager")
# elif age>=20 and age<59:
#     print("adult")
# elif age>=60:
#     print("senior citizen")1




# n= int(input("enter number:"))
# if n%5==0 and n%3==0:
#     print(n,"is multiple of 5 and 3")
# elif n%3==0:
#     print(n,"is multiple of 3")
# elif n%5==0:
#     print(n,"is multiple of 5")

# else:
#     print(n,"is not multiple of 3or 5")




# for i in range(1,51):
#     if i%2!=0:
#         print(i)



# n= int(input("enter number:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)



# count=0
# n=input("enter a string:")
# for i in n:
#     if i.isdigit():
#         count+=1
# print(count,"digitsab")



# t=(1,23,4,5,3,45,15,2)
# l=list(t)
# l.sort()
# print(l[-2])




# movie=["titanic","avatar","terminator","spiderman","iron man"]
# print(movie[0])
# print(movie[-1])
# movie[1]="batman"
# print(movie)




# d={"amraz":15,"fayis":20,"adil":17}
# d["adith"]=11
# del d["fayis"]
# print(d)




# for i in range(1,21):
#     if i==12:
#         break
#     print(i)





# sum=0
# lis=[1,23,67,63,23,11]
# for i in lis:
#     sum=sum+i
# print(sum)



# balance=10000
# while True:
#     try:
        
#         withdraw=int(input("enter number"))
#         if withdraw<0:
#             print("amount should be positive:")
#             continue
#         elif withdraw>balance:
#             print("amount should not  exceed balance")
#         else:
#             balance=balance-withdraw
#             print("balance:",balance)
#     except:
#         print("an error occured")






# def student(*marks):
#     total=sum(marks)
#     average=total/5
#     if average>90:
#         grade="A"
#     elif average>80:
#         grade="B"
#     elif average>70:
#         grade="C"
#     elif average>60:
#         grade="D"
#     else:
#         grade="F"
#     return f"total={total},average={average},grade={grade}"

  
# print(student(80,30,70,60,50))





# numbers=[10,20,10,30,20,40,50,30]
# lis=[]
# for i in numbers:
#     if i not in lis:
#         lis.append(i)
# print(lis)
# count=len(lis)
# print(count)






# inventory={
#     "apple":10,"banana":20,"orange":15}

# inventory["mango"]=30
# inventory["banana"]+=10
# del inventory["orange"]
# for key,values in inventory.items():
#     print(key,values)






# while True:
#     print("1)addition")
#     print("2)substraction")
#     print("3)multiplication")
#     print("4)division")
#     print("5)exit")


#     try:
#         n=int(input("enter choice from 1-5:"))
#         if n !=5:
#             a=int(input("enter number:"))
#             b=int(input("enter number:"))
#         if n==1:
#             print(a+b)
#         elif n==2:
#             print(a-b)
#         elif n==3:
#             print(a*b)
#         elif n==4:
#             try :
#                 div=a/b
#                 print(a/b)
#             except ZeroDivisionError:
#                 print("division by zero not possible")
#         elif n==5:
#             break
#         else:
#             print("invalid input")
#     except:
#         print("error occureed")






# pf="pass"
# marks=[20,30,20,22,27]
# student={"name":"akhil","age":25,"course":"bca","marks":marks}
# total=sum(marks)
# average=total/5
# highest=max(marks)
# lowest=min(marks)
# if average>40:
#     grade="A"
# elif average>30:
#     grade="B"
# elif average>20:
#     grade="D"
# else:
#     grade="F"
#     pf="fail"

# student.update({"total":total,"average":average,"highest":highest,"lowest":lowest})
# print(student)



            


