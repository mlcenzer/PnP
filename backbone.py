#!/usr/bin/env python3


#import modules
import user, os, sass, first_encounter, random, time#,combat


#initialize global variables

game_play='active'

while game_play=='active':# the player enters the loop. they cannot escape the loop until game_play is called not active.
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2) 
    

#game begins
    while player.hp>0:
        while player.escapeStatus==False:
            print("Your name is", player.name,", you have", player.hp, "health points. \n")
            read_statement=input("Press enter to begin.\n")

            fake_query=input("Your eyelids flutter open. You look up to see a dank, mossy ceiling and stone walls with one bleak, barred window. You sit up and look around. You see an open door in front you, candlelight flickering behind it. You stumble blearily to your feet and walk through the door.\n")
        #sample a location when we get to that
            decision_counter=1
            while decision_counter>0:
                first_query=input("You walk down the hallway and see a set of stairs leading down into the dark. Do you go down the stairs, [yes] or [no]?\n ")
                if first_query=="no":
                    decision_counter=0
                    first_encounter.first_combat()
                elif first_query=="yes":
                    decision_counter=0
                else:
                    print(sass.sample_sass(), '\n')
                #what happens at the bottom of the stairs
                print("You start creeping down the stairs. You hear a squadron of gaurds march past in the hall above. Moving as quietly as you can, you peer through the darkness.\n")
            
    print("Game Over.")#print when you escape the second while loop.
    game_play='not active' #gets you out of the outermost while loop.






    

