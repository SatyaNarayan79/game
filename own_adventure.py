name = input("type your name: ")
print("wlcome",name,"to your adventure")

answer = input("you come to a dirt road, it has come to an end and you can go left or right ?").lower()

if answer == "left":
    answer = input("this path is dance with tree what you will do follow the tree or cut the tree or catch the light ?").lower()
    
    if answer == "follow the tree":
        
        print("you are loss in the forest!")
        
    elif answer == "cut the tree":
        
       answer=input("a river and mountain is come ? where you wil go(river or mountain) ?").lower()
       
       
       if answer == "river": 
            answer=input("a river come! how to cross ? swim or build a boat ?").lower()
    
            if answer == "swim":
                print("you drown and died! THE END.")
    
            elif answer=="build a boat":
                print("you reach the destination.")
        
            elif answer == "catch the light":
                print("fire the forest or leave")
             
            else:
                 print("not a valid option, you lose")        
                 
       elif answer == "mountain":
            print("you die.")
       else:
        print("not an option.")
    else:
        print("got the king's riing.")                       
elif answer == "right":
    answer=input("a river come! how to cross ? swim or build a boat ?").lower()
    
    
    if answer == "swim":
        print("you drown and died! THE END.")
    
    elif answer=="build a boat":
        print("you reach the destination.")
       
            


else:
    print("not a valid option, you lose")        