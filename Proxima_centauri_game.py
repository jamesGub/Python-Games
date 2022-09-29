#CINF 308 Assignment 6 - Text-Based Game
#This is James Gillanders' code

#For this assignment, I wanted to go all out since we are basically creating a game!
#I will be using import functions such as time to add more nuance to the decisions
#as well as utilizing a narrative that I will try to flesh it out at multiple points. 
#We will break down the stages of the game into different functions and incorporate all
#assignment requirements.

#Game start.
import time
import random
from random import randint

score = []

#Player information, stored and returned to them.
print("Welcome to the game! Before you can start, enter your name and age! Your info and score will be returned at the end!")
player_list = [str(i) for i in input().split()]


#Title screen, a few different options to choose from. 
def title_screen():
    print("Welcome " + player_list[0])
    
    print("\n**PROXIMA CENTAURI** \nAn interactive adventure game made in Python.")
    
    print("\nSTART: Begin the adventure!")
    print("\nCREDITS: View who made the game!")
    print("\nABOUT: Learn about the story and game making process!")

title_screen()

#credits function
def game_credits():
        print("Game made by: James Gillanders")
        
        print("Thank you for playing! Did you enjoy your ending?")
     
        print("\nYou already know who made this, run the program again and start playing! :)")

        print("Your player info and score: ")
        
        print(player_list + score)
        
        title_screen()


#about function
def about():
        print("This text-based adventure game was made for CINF 308.\nI am super passionate about games, so this being an assignment is super fun!")
        print("I wanted to create an in-depth story for this game that is emblematic of all my favorites. I hope you can enjoy!")


option = input("\nType an option: ")
#Once you pick START, the basic plot of the game is outlined to you and what your mission will be on this adventure.
if(option.upper() == "START"):
    def plot():
        print("Let the game begin!")
        print("""\n***PREFACE***
        
        The throne of the once glorious Centuris dynasty awaits its next dogged contender to play the title of lord.
        Their once great Astral Flame, now snuffed to nothing but cinders once allowed them to conquer their pocket of the galaxy.
        Now they're nothing but an empire of the dead, feeding off what remains of their dying maternal star, Proxima Centauri. 

        \nThe regal Centuris family has reigned for millennia, and today is Mother's Day. 
        But on Proxima D, the day has a different meaning; for it is the day they offer a new 
        bearer for their Mother star's will, or rather, a new lord. 

        \nNext in the succession is Fraya Centuris, the green eyed princess, reluctantly obeying the will of the Mother Star. 
        She is an inquisitive royal, one not too fond of her late father's dogmatic ramblings of the Star's prosperity. 
        Fraya knows the end is nigh for this world, yet for the sake of her people, she bears the will. 
        
        You are the omnipitence, who will control Fraya through this perilous story of legacy, fate, and birthright. 
        You have allies, you have enemies, but you have no one you can trust but yourself. 
        """)
    plot()
#Simply a credit section, not much to discuss here but this is an option at the start as well as displaying after each ending like a real game. 
elif(option.upper() == "CREDITS"):
    game_credits()
#The about section tells what the game was made for and my inspiration behind it. This was a passionate assignment for me so I wanted to get that across in some way.
elif(option.upper() == "ABOUT"):
    about()
else:
    print("Invalid input, have fun playing another game!")

#Here are the functions we will use for different parts of the plot. I condensed the choices and paths the story can take into functions since it seemed the easiest. 
#They play into each other in different ways, though some are purely expository. 
    
#This is the default function that starts with the game. It is also the first instance in which there is a player choice.
def act1scene1():
    print("""The streets of the Centuris Capital, Silus, erupt with festivities. The royal city is bathed in dim, warm starlight; 
    whenever Mother's Day commences, feasts and parties are akin to wildfire, unlike any across the galaxy. At least that is how things used to be.

    \nYou gaze from the Centuris Kiln as dozens of handmaidens tend to your every need. You view the the meek festivities below from on high. 

    \nA handmaiden with fair blue skin compliments your hair and asks your thoughts on taking the throne.
    
    \n1. "I never cared much for politics...the throne, our dynasty, it can all go to waste. The mother star is dying."
    \n2. "My father died for the throne, I have to do what is best for my family and my people. I will bear her will."
    
    """)
#I went with two paths the player can take, chaotic or heroic respectively. Not exactly "good & evil" but still along those lines. 

#First plot function down the chaos path 

def act1scene2(): 
    print("""\nAs your escort approaches the historic Centuris throne room, the applause of crowds, allied houses, and your family is a lot to take in.

        \nDespite their joy of seeing a woman as lord, that is all they see. You believe there is no hope for the dynasty or its influence on the world.

        \nYour thoughts are once again occluded by the clamor of the ceremony. A new ruler, and you're forced to bear the weight. 

        \nThe Centuris family, or what remains of it is a problematic bunch. The widowed matriarch, Celine, your mother. Once a beacon of hope 
        for the dynasty is a husk of her former self following the death of her king husband, Rayga Centuris, the last lord. Through Celine's turmoil, 
        you can sense her warm approval for your bearing of the will. 

        \nYou feel eyes like daggers stabbing you from across the throne room, your brother, Reinard, father's second-born, repudiates your existence
        as the next ruler. He feels your reign is an anomaly in the face of tradition, you recall him deriding you earlier about letting the star die and by extension its people. 

        \nThe festivities commence, as the crown is placed upon your unwilling head much to the joy of your now subjects, a gruff voice yells out,

        \n"A reluctant puritan such as you has no right to rule! Think about your people, think about father!" 

        \nYou recognize the voice as your brother's, his opposition has reached a breaking point. Commotion arises, with your guard
        attempting to diffuse the situation. 

        \n"One duel, let us end this rivalry. I win, I take the throne, if you win, I will never oppose your rule again."

        \n1. *Fight Reinard*
        \n2. *Let your guards handle it*
    """)
    #Second player choice that can drastically alter the course of the story. Since the input would only take a string for 1 and 2, I had to convert them to integers. 
    #If the player chooses to fight, then this will put them down the path of a possible ending. 
    choice2 = int(input("Choose 1 or 2: "))
    time.sleep(1)
    if(choice2 == int(1)):
        
        print("""\nYou tell your guards to stand down as your watch your brother unsheath his blade. 

        \nAs shock erupts in the throne room as a result of treason, you decide to meet your brother's challenge. Not so much for the title of ruler,
        but because you wish to put him in his place once and for all. 

        \nYou ask your royal ambassadors to fetch your own blade, which has been your closest ally and friend since you were young. Shortly after, combat ensues. 

        \nReinard is a skilled fighter, but your will remains true. Despite your courage and the support of your Mother and people. You are unsure whether you will come out alive. 

        """)
        act1scene3_end()
   #The general structure of this project is pretty simple, I made functions, then chained them together if they were related.     
    elif(choice2 == int(2)):
        print("""\nYou decide to let your guards diffuse the situation. Yet Reinard refuses to let this go without a proper sibling duel. 

        \nYou possess renowned skill with a sabre, but you don't believe the throne is worth dying over. 

        \nHowever, Reinard is stronger, able to dispose of your guard effortlessly. In a shocking turn of events, guards and people all over the throne room reveal their true allegiances, this was a royal coup brewing from the start!

        \nChaos swelters all around. Your brother probably promised those that sided with him riches or guaranteed shelter when the star dies and becomes a supernova. 

        \nIf there's one thing your brother is, it's a liar. These people have been manipulated, and turned against you for false promises. You never wanted to rule, you never wanted this.

        \nAs enemies close in closer to you, your ambassador, Roland gives you your blade. Rushing for it amidst the chaos. 

        \nYou have no choice but to fight, should anything happen to your mother, you would never forgive yourself.
        """)
        act1scene3_end()
    else:
        print("Error")
def act1scene3_end():
    print(""" Your blade is knocked out of your hand, much to the surprise of your family. You're a talented fighter, but Reinard always trained harder.
    
    \nHe scoffs at his premature victory, but then you sense an opportunity to use the hair ornament the handmaiden gifted to you. 

    \nYou frantically pull it out of your hair and launch it at Reinard with full force. 

    \nHe is taken aback at the sharpness of the device, which gives you the upper hand to retrieve your blade. 

    \nThe battle returns to a neutral standoff...you're almost at your limit. But the battle presses on.
    
    """)
    #This was the hardest part of the entire program, I kept overthinking the best ways to implement a random factor. 
    #I kept using complex conditionals and trying to pull values from lists and go from there.
    #Eventually I settled on a for loop, it was the easiest approach and had randomness in a simple way.
   
    for i in range(1,6):
        print(random.randint(1,6))
        print(i)
        break
    if i in range(1,3):
            print("""You tested your luck continuing the battle and you emerge victorious, knocking your brother to the floor.
            
            \n"I will not let you do as you please! Threatening your own blood, your schemes are over!" 

            \nReinard is taken away, with a puzzled expression on his wounded visage. You are hailed as a hero and a protector of the planet. 

            \nYou begin to have a change of heart, and realize what truly matters. Not the star, nor the politics, but the people you are able to protect.

            \nThe indoctrination continues, and you bear the will of the Mother Star as the next ruler of the Centuris dynasty as the Queen Fraya.
            """)

            print("Congratulations! You got the HERO ending! Your score has been updated.")
            score.append(100)
            game_credits()
    #Yes the endings are random, but what kind of game would it be if they weren't?
    elif i not in range(1, 3):
            print("""The duel rages on, you feel yourself getting weaker with each slash and clash of your blade.

            \nReinard is nearly untouched, but you suffer from your sibling's sabre, the rending of your flesh is a precise dissection. 

            \nAs you nearly collapse, you recount the days leading up to your inauguration. You remember your grief you felt after your Father's passing, and the dread of having to take the throne. 

            \nYou're unable to fight any longer. You surrender the throne to your brother. 

            \nTime passes, new administrations are put into place. You end up a prisoner in the citadel. 

            \nYou accept the circumstances, you begin to formulate your escape for another planet, somewhere safer. Somewhere that isn't doomed. 
            """)

            print("Oh no! You got the BAD ending! Your score has been updated.")
            
            score.append(0)
            
            game_credits()
            
    else:
        print("ERROR")
        

#After the introductory function, the choices that are made are decided here. 
act1scene1()
choice1 = int(input("Choose 1 or 2: "))
time.sleep(1)
path = "route"
while(path == "route"):
    if(choice1 == int(1)):
            def next_scene():
                print("""\nYou give the handmaiden a cold remark on the state of your dynasty.

                \nThe handmaiden gently processes your statement, giving a warm smile in admiration of your honesty. She pulls out a hair ornament and gifts it to you, it is sharp to the touch.

                \n"This is native to my planet, it's a pretty ornament but if you are ever in danger, it can be relied on, my lady."

                \nAs they finish your hair and the smell of cosmic fireworks permeate your nasal cavity, your tranquility is disturbed by 
                \na cacophony of soldiers and ambassadors rushing up the staircase ready to escort you to the throne. 

                \n"They are waiting for you my lady, the whole Capital is awaiting your arrival."

                \nThe ambassador, Roland, was a cautious man. Very entwined with your father and his politics. 
                \nYou have known him since you were a child, though you've never truly trusted him. Then you remember...

                \nYou cannot trust anyone.

                \nYou are escorted from your chambers by a massive party, this is really happening. """)
            next_scene()
            act1scene2()
            break
            
    
#Originally I planned to have two entirely different paths the story could go in, but for the sake of time and getting the purpose of the assingment across, I figured I would remove it and safe it for later 
#should I want to continue it at a later point. 
    
    elif(choice1 == int(2)):
            def hero1():
                print("""\nYou tell the handmaiden about your most virtuous ambitions and how you will inherit the will as a faithful ruler.

                \n"With all due respect princess, don't you think that is a bit lofty? The Mother Star is not what it once was." 

                \nAdmonishing your privileges as ruler, you accept the handmaiden's statement with benevolence. Assuring her
                that you promise to preserve the legacy of your dynasty no matter what. 

                \nSilence permeates following your brief exchange with the handmaiden. 

                \nThe absence of sound is broken by the roars of protestors en masse, groups that call for the end to the Centuris dynasty.
                They believe the throne and dreams of prosperity are for naught following the death of your father. 

                \nYou regain your composure and relocate downstairs as a result of your counsel's beckoning. 

                \nThere is an uneasiness coursing through you. You feel as if you cannot trust anyone.""")
            hero1()
            act1scene2()
            break

    else: 
        print("Invalid input! Try again?")
        choice1 = input("Choose 1 or 2: ")
    









            

    







