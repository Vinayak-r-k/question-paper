# n=int(input("enter a number:"))
# if n%3==0 and n%5==0:
#     print("divisible by both 3 and 5")
# else:
#     print("not divisible by both 3 and 5")




# n=input("enter a character:")
# if n.isupper():
#     print("uppercase")
# elif n.islower():
#     print("lowecase")
# elif n.isdigit():
#     print("digit")
# elif n in "!@#$%^&*()":
#     print("special character")




# for i in range(20,0,-1):
#     print(i)




# n=int(input("enter a nuumber:"))
# sum=0
# for i in range(n+1):
#     sum+=i
# print("sum=",sum)




# n=input("enter a word:")
# for i in range(len(n)):
#     print(n[i],"position=",i)


# odd=0
# even=0
# n=(1,24,3,2,34,27,21,23)
# for i in n:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even :",even)
# print("odd:",odd)




# student=["adith ","abhi","akhil","adi","dani"]
# student[2]="fayis"
# del student[0]
# print(student)





# student={"name":"abhi","age":21,"course":"bca"}
# student["grade"]="A"
# print(student)





# for i in range(1,21):
#     if i%4==0:
#         continue
#     print(i)




# a=int(input("enter number:"))
# b=int(input("enter number:"))
# print(max(a,b))





# correct_password = "admin123" 
# for i in range(3,0,-1):
#     n=input("enter password:")
#     if n==correct_password:
#         print("password accepted")
#         break
#     else:
#         print("incorrect password ,remaining attempts",i-1)
# print("account locked")







# total=0
# products=["chair","table","tv","fan"]
# price=[1000,3000,50000,4000]
# while True:
#     print("choose an option betweem 1 to 4")
#     print("1) display product")
#     print("2) add product price")
#     print("3)total")
#     print("4) exit")
#     n=int(input("enter choice:"))
#     if n==1:
#         for i in range(len(products)):
#             print(products[i] ,price[i])
#     elif n==2:
#         pro=input("enter a product")
#         indx=products.index(pro)
#         total=total+price[indx]
#     elif n==3:
#         print(total)
#     elif n==4:
#         break







# pas=0
# marks=[]
# for i in range(5):
#     mark=int(input("enter marks"))
#     marks.append(mark)


# print("highest",max(marks))
# print("lowest",min(marks))
# print("total=",sum(marks))
# print("average=",sum(marks)/5)
# for i in marks:
#     if i>=50:
#         pas+=1
# print("no of passed",pas)








# l=[]
# n= input("enter sentence")
# for i in n:
#     if i not in "!@#$%^&*()-=+":
#         l.append(i)
# a="".join(l)
# print(a)








# incorrect=True
# for i in range(5,0,-1):
#     secret=25
#     n= int(input("enter number:"))
#     if n>secret:
#         print("number too high")
#     elif n<secret:
#         print("number too low")

#     else:
#         print("correct")
#         incorrect=False
#         break
#     print("attempts remaining",i-1)
# if incorrect:
#     print("game over")








# order=dict()
# menu = { "burger": 150, "pizza": 300, "juice": 80, "pasta": 200 } 
# while True:
#     print("1)view menu")
#     print("2)order food")
#     print("3)view bill")
#     print("4)exit")
#     n= int(input("enter a choice from 1-4:"))
#     if n==1:
#         for food,price in menu.items():
#             print(food ,price)
#     elif n==2:
#         ord=input("enter item to order:")
#         print("ordered")
#         order[ord]=menu[ord]
#     elif n==3:
#         print("total=",sum(order.values()))
#     elif n==4:
#         break










    



