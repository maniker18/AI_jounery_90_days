secerat_name = "dragon"
user_input = ""
limit =0

out_of_limit = False
while secerat_name != user_input and not(out_of_limit):
    print("limit =", limit)
    if limit < 3:
        user_input = input("enter a animal name ")
        limit +=1
        score =100
    elif (limit >= 3) and (limit < 6):
        print(" hint! : it can fly and breate fire")
        user_input = input("enter a animal name ")
        limit +=1
        score = 60
        
    else:
        out_of_limit = True


if secerat_name == user_input:
    print(user_input + " you guessed it correct with score :" +str( score))
else:
    print("out of limt")