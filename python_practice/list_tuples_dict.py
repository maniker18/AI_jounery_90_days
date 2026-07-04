#working with list
num = [1,2,2,2,3,4,7,5,6]
freinds =["ram","kam","sam","sur"]
print(freinds)
#removes an insert new item
freinds[1]="kiren"
#adds last item to existing list
freinds.append("jam")
#remove the elements
freinds.remove("ram")
print(freinds)
#finds the index of given item
print(freinds.index("sam"))
print(freinds[0:len(freinds):2])

print(num)
#sort the item in ascending order
num.sort()
print(num)
#removes the last element
y=num.pop()
print(y)
print(num)
#Extension extends list by appending elements from the iterable
freinds.extend(num)
print(freinds)
print(num.count(2))
num.reverse()
print(num)



#tuples are immutable nd list are mutbale
coordinates=(10,20)

#dict are key value pairs key should be unique
dic = {
    "hello" : "greetings",
    "silent" : "not_speaking",
    "attitude": "not_respectfull"
}

print(dic.get("helldo","notvalid"))