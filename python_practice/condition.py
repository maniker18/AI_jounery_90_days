#condtions if else elif 
wakeup_early = False
use_phone = False

if wakeup_early and use_phone:
    print( "go to gym  worry about  time ")

elif wakeup_early and(not use_phone):
    print( "go to gym doesnt worry about time ")
else:
    print("study")


def game(studyhrs,freindscall):
    if studyhrs>=8 and freindscall  == True:
        return "play game"
   
    elif studyhrs<8 and freindscall  == False:
        return " then study "
    elif studyhrs<=8 or freindscall  == True:
        return "play game then study "

print(game(5,True))