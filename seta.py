# n=int(input("enter number:"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# elif n==0:
#     print("zero")






# n=input("enter character:")
# if n in "aeiouAEIOU":
#     print("vovel")
# else:
#     print("consonant")





# n=int(input("enter a number:"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")







# sum=0
# for i in range(1,51):
#     if i%2==0:
#         sum+=i
# print(sum)







# n=int(input("enter number:"))
# for i in range(1,11):
#     print(i,"*",n,"=",n*i)







# count=0
# n=input("enter strings:")
# for i in n:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)








# fruits=["apple","banana","orange","mango","grape"]
# fruits.append("guava")
# fruits.insert(2,"cherry")
# fruits.pop()
# print(fruits)





# l=(12,2,1,233,33)
# print(len(l))
# print(min(l))
# print(max(l))





# n=input("enter a string:")
# upp=0
# low=0
# for i in n:
#     if i.isupper():
#         upp+=1
#     elif i.islower():
#         low+=1
# print("lowercase:",low)
# print("uppercase:",upp)





# for i in range(1,31):
#     if i%3==0:
#         continue
#     print(i)






# fail=False
# total=0
# marks=[]
# for i in range(5):
#     n=int(input("enter marks"))
#     marks.append(n)
#     total+=n
# average=total/5
# if average>90:
#     print("A")
# elif average>=75 and average<=89:
#     print("B")
# elif average>=60 and average<=74:
#     print("C")
# elif average>50 and average<=59:
#     print("D")
# else:
#     print("fail")
#     fail=True

# if not fail:
#     print("passed")







# balance=5000
# while True:
#     print("1) balance")
#     print("2) deposit")
#     print("3) withdraw")
#     print("4) exit")


#     n=int(input("enter choice from 1-4:"))
#     if n==1:
#         print(balance)
#     elif n==2:
#         deposit=int(input("enter number to deposit:"))
#         balance+=deposit
#     elif n==3:
#         withdraw=int(input("enter amount to withdraw:"))
#         if withdraw<=balance:
#             balance=balance-withdraw
#         elif withdraw>balance:
#             print("insufficient balance")
#         else:
#             print("amount cannot be negative")
#     elif n==4:
#         break




# incorrect=False
# password="python123"
# for i in range(3):
#     n=input("enter password")
#     if n==password:
#         print("password correct")
#         break
#     else:
#         print("incorrect passsword")
#         incorrect=True
# if incorrect:
#     print("account locked")





# odd=[]
# even=[]
# five=[]
# numbers=[10,15,20,25,30,35,40,45]
# for i in numbers:
#     if i%5==0:
#         five.append(i)
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd number",odd)
# print("even numbers",even)
# print("sum of even",sum(even))
# print("divisible by 5",len(five))








# t=(1,232,223,322,123,13,2,111,123,116)
# while True:
#     print("1) display tuple")
#     print("2) length of tuple")
#     print("3) search element")
#     print("4) count element")
#     print("5) sum of even")
#     print("6) second largest number")
#     print("7) exit")

#     n=int(input("enter choice from 1-7:"))
#     if n==1:
#         print(t)
#     elif n==2:
#         print(len(t))
#     elif n==3:
#         found=False
#         s=int(input("enter element to search"))
#         for i in t:
#             if i==s:
#                 print("found")
#                 found=True
#                 break
#         if found==False:
#             print("not found")
#     elif n==4:
#         count=0
#         n=int(input("enterr element to find count"))
#         for i in t:
#             if n==i:
#                 count+=1
#         print("count=",count)
#     elif n==5:
#         soe=0
#         for i in t:
#             if i%2==0:
#                 soe+=i
#         print("sum of even number is",soe)
#     elif n==6:
#         l=list(t)
#         l.sort()
#         print(l[-2])
#     elif n==7:
#         break






marks=[]
student = dict()
name=input("enter name:")
age=int(input("enter age:"))
for i in range(5):
    mark=int(input("enter marks:"))
    marks.append(mark)
student.update({"name":name,"age":age,"marks":marks})
total=sum(marks)
average=total/5
high=max(marks)
low=min(marks)
fail=False
if average>90:
    grade="A"
elif average >=75 and average<90:
    grade="B"
elif average >=60 and average<75:
    grade="C"
elif average>=50 and average<60:
    grade="D"
elif average<50:
    grade="fail"
    fail=True
if fail:
    result="failed"
else :
    result="passed"
student.update({"total":total,"average":average,"grade":grade,"result":result})
print(student)




