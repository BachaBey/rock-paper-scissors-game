import random

def prog_choice():
    x=random.randint(1,3)
    match x:
        case 1: return "rock"
        case 2: return "paper"
        case 3: return "scissors"

def result(pc,b):
    if pc=="rock":
        if b=="scissors" :
            res="you lose!"
        elif b=="paper":
            res="you win!"
        else:
            res="draw"
    elif pc=="scissors":
        if b=="paper" :
            res="you lose!"
        elif b=="rock":
            res="you win!"
        else:
            res="draw"
    else:
        if b=="rock" :
            res="you lose!"
        elif b=="scissors":
            res="you win!"
        else:
            res="draw"
    return res

def paper(*ags, **kws):
    user="paper"
    pc=prog_choice()
    pyscript.write("chose", pc)
    res=result(pc,user)
    pyscript.write("res", res)
    
def scissors(*ags, **kws):
    user="scissors"
    pc=prog_choice()
    pyscript.write("chose", pc)
    res=result(pc,user)
    pyscript.write("res", res)
    

def rock(*ags, **kws):
    user="rock"
    pc=prog_choice()
    pyscript.write("chose", pc)
    res=result(pc,user)
    pyscript.write("res", res)
