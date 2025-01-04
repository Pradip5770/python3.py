
#list
# string is inmutabale(means  change is not allwod)
mark="pradip"
print(mark)
#mark[0]="y"
print(mark[0])


# list is mutabal


marks =[64,646,664,664,64,64,64,6]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
studant=[64,'pradip',33.4,"fjernfger","fnerjb"]   
print(studant)

#we can change
# studant=[64,'pradip',33.4,"fjernfger","fnerjb"]   

studant[1]="harsh"
print(studant)

#slicing in list
# studant=[64,'pradip',33.4,"fjernfger","fnerjb"]   


cut=studant[0:2]
print(cut)

print("\n")
print("\n")
print("\n1")


#list method

#1 
#add into the list
#studant=[64,'pradip',33.4,"fjernfger","fnerjb"]   
studant.append(5)
studant.append("jay")
print(studant)



print("\n")
print("\n")
print("\n2")

#2
#sorts in asscending order
mark=[3,35,37,86,57,56,44]
print(mark.sort())
print(mark)
print(mark.sort(reverse=True))
print(mark)

name=["pradip","naman","ghanshyambhai"]
name.sort()
print(name)


print("\n")
print("\n")
print("\n3")

#3
#revers the list
#[64, 'harsh', 33.4, 'fjernfger', 'fnerjb', 5, 'jay']
studant.reverse()
print(studant)


print("\n")
print("\n")
print("\n4")

#4
#add in list at indexing
#[64, 'harsh', 33.4, 'fjernfger', 'fnerjb', 5, 'jay']
studant.insert(4,"pradip")
print(studant)


print("\n")
print("\n")
print("\n5")

#5
#remove from in list
#[64, 'harsh', 33.4, 'fjernfger', 'fnerjb', 5, 'jay']

studant.remove("harsh")
print(studant)


print("\n")
print("\n")
print("\n6")

#6
#remove from at index
#['jay', 5, 'fnerjb', 'fjernfger', 'pradip', 33.4, 64]
studant.pop(2)
print(studant)




print("\n")
print("\n")
print("\n7")

#7
#practic   wap to ask the user names their favorite movie & store them in a list
movielist=[]
movielist.append(input("enter 1 movie :"))
movielist.append(input("enter 2 movie :"))
movielist.append(input("enter 3 movie :"))
print(movielist)



print("\n")
print("\n")
print("\n8")

#8
#wap to check if a list contains a palindrom of element of element use copy() method

x=["p","aba",1,1,"aba","p"]
p=x.copy()
p.reverse()
print(x)
print(p)

if(p==x):
    print("yes")
else:
    print("no")

