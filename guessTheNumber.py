n = 10

gusses = 1 
while(gusses<=9):
    num = input("Enter your Guess")
    num = int(num)
    
    if num > n:
        print("You have entered no greater than the guess")
        
    elif num<n:
        print("You have entered no smaller than the guess")
        
    elif num == n:
        print("you won !!!")
        print(gusses,"no of gusses took to finish this")
        break
    print(9-gusses,"no of gusses left")
    gusses = gusses+1

if gusses>9:
    print("game over")

    