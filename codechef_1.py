n = int(input())

dragon = []
sloth = []

for i in range(n):
    dragon_input = input()
    dragon_input = dragon_input.split(" ")
    dragon_input = list(map(int, dragon_input))
    dragon.append(dragon_input)
    
    sloth_input = input()
    sloth_input = sloth_input.split(" ")
    sloth_input = list(map(int, sloth_input))
    sloth.append(sloth_input)
    

for i in range(len(dragon)):
    if sum(dragon[i]) > sum(sloth[i]):
        print("DRAGON")
        
    elif sum(dragon[i]) == sum(sloth[i]):
        if dragon[i][0] > sloth[i][0]:
            print("DRAGON")
            
        elif dragon[i][0] == sloth[i][0]:
            if dragon[i][1] > sloth[i][1]:
                print("DRAGON")
            elif dragon[i][1] == sloth[i][1]:
                if dragon[i][2] > sloth[i][2]:
                    print("DRAGON")
                
                if dragon[i][2] == sloth[i][2]:
                    print("TIE")
                            
                else:
                    print("SLOTH")
                
            else:
                print("SLOTH")
            
        else:
            print("SLOTH")
        
    else:
        print("sloth")