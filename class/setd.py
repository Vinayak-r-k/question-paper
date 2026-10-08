# n=int(input("enter number:"))
# if n>0:

#     if n%2==0:
#         print("even")
#     else:
#         print("odd")



# count=0
# n=input("enter string:")
# for i in n:
#     if i in "aeiouAEIOU":
#         count+=1
# print("count of vovel is:",count)



# for i in range(1,11):
#     print(i**2)



# a=10
# while a>0:
#     print(a)
#     a-=1




# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print(sum)


# found=False
# t=(10,20,15,16,22,1,2,3)
# n=int(input("enter element to search:"))
# for i in t:
#     if i==n:
#         print("found")
#         found=True

# if found==False:
#     print("not found")



# fruit=["apple","banana","mango"]
# fruit.insert(1,"grape")
# fruit.pop()
# print(fruit)





# person={"name":"rahul","age":25,"city":"kochi"}
# print(person.get("age"))
# person.pop("city")
# person["profession"]="engineer"
# print(person)




# lis=[12,2,1,-3,2,-7,14,-4]
# for i in lis:
#     if i<0:
#         continue
#     print(i)



# n=input("enter a string:")
# print(len(n))


# total=0
# for i in range(5):
#     n=int(input("enter price:"))
#     total+=n
# if total>5000:
#     total=total-(total*0.1)
# print("total=",total)



# while True:
#     passw=input("enter password:")
#     if len(passw)<8:
#         print("invalid password,password must have more than 8 character")
#         continue
#     elif passw.isalpha():
#         print("password invalid,must contain numbers")
#     elif passw.isalnum():
#         print("valid password")




# p,n,e,o=[],[],[],[]
# l=[]
# for i in range(10):
#     num=int(input("enter numbers:"))
#     l.append(num )

# for i in l:
#     if i>0:
#         p.append(i)
#     elif i<0:
#         n.append(i)
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print("positive",p)
# print("negative",n)
# print("even",e)
# print("odd",o)




# tup=(10,20,30,25,25)
# total=sum(tup)
# average=total/5
# highest=max(tup)
# lowest=min(tup)
# top=0
# for i in tup:
#     if i>75:
#         top+=1
# print("total is:",total)
# print("highest is:",highest)
# print("average",average)
# print("lowest",lowest)
# print("above 75",top)




# av_seat=10
# booked=0
# while True:
    
#     print("1)view seat")
#     print("2)book ticket")
#     print("3)cancel ticket")
#     print("4)exit")
#     n=int(input("enter option:"))
#     if n==1:
#         print("available seat",av_seat)
#     elif n==2:
#         if av_seat>0:
#             av_seat-=1
#             booked+=1
#             print("booked")
#         else:
#             print("no seat available")
#     elif n==3:
#         if booked>0:
#             av_seat+=1
#             booked-=1
#             print("booking cancelled")
#         else:
#             print("not booked")
#     else:
#         break








total=0
products={"laptop":50000,"phone":20000,"mouse":1000}
while True:
    
    print("1)add product:")
    print("2)remove product:")
    print("3)view cart:")
    print("4)calculate total:")
    print("5)exit:")

    n=int(input("enter choice:"))
    if n==1:
        product=input("enter product:")
        price=int(input("enter price:"))
        
        products.update({product:price})
    elif n==2:
        n=input("enter item to delete:")
        products.pop(n)
    elif n==3:
        print(products)
    elif n==4:
        for i in products.values():
            total=total+i
        print(total)
    elif n==5:
        break
    






