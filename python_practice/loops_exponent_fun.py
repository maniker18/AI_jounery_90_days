i=10
while(i>=0):
    print(i)
    i-=1

for i in range(5):
    print(i)


j="kiokiloskjd"
for i in range(len(j)):
    print(j[i])

# exponent fun

def exponent_fun(base,power):
    result = 1
    for i in range(power):
        result = base*result
    print(result)

exponent_fun(4,2)

#nested loops

list = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [0]]

print(list)

for i in list:
    
    for j in i:
        print(j,end=' ')