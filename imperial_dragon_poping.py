no_of_terms=int(input("enter the number of value:"))
list1=[]
for value in range(0,no_of_terms,1):
    ele=int(input("enter integer:"))
    list1.append(ele)
print("circuting then elements of list",list1)
for value in range(0,no_of_terms,1):
      ele=list1.pop(0)
      list1.append(ele)
      print(list1)
