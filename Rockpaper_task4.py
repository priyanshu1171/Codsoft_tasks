while(True): 
    n = input("Enter Your Choice :- ") 
    list1= ['rock','paper','scissor'] 
    p = 'you loose' 
    r = 'you win' 
    import random 
    l = random.choice(list1) 
    print(f"computer choose-{l}") 
    if n=='rock' and l=='paper': 
        print(p) 
    elif n=='paper' and l=='scissor': 
        print(p) 
    elif n=='scissor' and l == 'rock': 
        print(p) 
    elif n==l: 
        print("Tie") 
    else: 
        print(r) 
    a = input("Do you want to play again yes/no = ") 
    if (a == "yes"): 
        continue 
    else: 
        break