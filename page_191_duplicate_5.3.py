list=[]
n=10
i=0
while i<n:
	new=int(input("Enter a number\n"))
	if new not in list:
		 list.append(new)
		 i=i+1
	
       

print("--------------------")
print("Our list without duplicates")
for i in range (len(list)):
	print("%d %d"%(i ,list[i]))
print("--------------------")
