from sys import exit

#game starts with no locations known to player except start:
locations = []
#game starts with nothing in your inventory:
inventory_list = []
#here is a place to track death counts (will be displayed at end):
death_count = []
#characters begin alive:
kraken = True
prisoner_alive = True
#prisoner is not with you in beginning:
prisoner_with_you = False
#bear is still blocking south door in beginning:
bear_moved = False

def welcome():
    print("\n\nWelcome to Oliver's treasure hunt!\n")
    print("In the world you are about to enter, there are many, many ways to die,")
    print("and only ONE path that leads to a glorious escape with treasure in hand.\n")
    print("Interact with this game by responding to the program with your best guess")
    print("at what actions would lead your fearless hero to victory, but do not worry;")
    print("type HELP at any point if you get stuck.")
    print("If you die, there are multiple checkpoints you can return to.\n")
    print("Please press ENTER to begin your adventure...")
    input()
    start()

### SCENES WITHOUT PRISONER COMPANION ###
def start():
    locations.append("Start Room")
    ## SCENE w/ PRISONER ##
    if "key" in inventory_list:
        print("You take a minute to calm your racing heart,")
        print("and enjoy the familiar darkness of this empty room.")
        print("You know the door on the left leads to the maddening Cthulu. There is also a door to the right.")
        print("Which one do you take?")

        choice = input(">>> ")

        if "right" in choice:
            bear_room_scene()
        elif "left" in choice:
            cthulu_room_scene()
        elif "cheat" in choice:
            inventory_list.append("key")
            gold_room_scene()
        else:
            dead("\nYou stumble around the room until you starve.","")

    ## SCENE W/O PRISONER ##
    else:
        print("\nYou are in a dark room.")
        print("There is a door to your right and left on the south wall of the room.")
        print("Which one do you take?")

        choice = input(">>> ")

        if "right" in choice:
            bear_room_scene()
        elif "left" in choice:
            cthulu_room_scene()
        elif "cheat" in choice:
            inventory_list.append("key")
            gold_room_scene()
        else:
            dead("\nYou stumble around the room until you starve.","")

def bear_room_scene():
    #registers the Bear Room as being "discovered" for respawn purposes
    locations.append("Bear Room")
    #pulling in the "bear_moved" variable:
    global bear_moved
    ## SCENE w/ PRISONER ##
    if prisoner_with_you == True:
        print("this scene and onwards is still in progress...")
    ## SCENE W/O PRISONER ##
    else:
        #if bear remains in front of North door:
        if bear_moved == False:
            print("\nThere is a bear here.")
            print("The bear has a bunch of honey.")
            print("There is a door on the east side of the room.")
            print("The fat bear is in front of another door along the south wall.")
            print("What would you like to do?")
            while True:
                choice = input(">>> ").lower()
                if ("take" in choice) or ("honey" in choice):
                    dead("\nThe bear looks at you then slaps your face off.","")
                elif ("start" in choice) or ("back" in choice):
                    print("\nYou retreat back to the starting room.")
                    start()
                elif "east" in choice:
                    cthulu_room_scene()
                elif (("wave" in choice) or ("smile" in choice) or ("pet" in choice) or ("sing" in choice) or ("play")) and not bear_moved:
                    print("\nThe bear has moved from the door.")
                    print("You can go through it now.")
                    bear_moved = True
                elif "bear" in choice and bear_moved:
                    dead("\nWhy are you still messing with the bear? He gets pissed off and chews your leg off.","")
                elif (("door" in choice) or ("open" in choice) or ("south" in choice) or ("through" in choice)) and not bear_moved:
                    print("\nThe bear is in the way of the door on the South wall. What are you going to do?")
                elif (("door" in choice) or ("open" in choice) or ("south" in choice) or ("through" in choice)) and bear_moved:
                    silver_forest_scene("North")
                elif("help" in choice):
                    help("bear")
                else:
                    print("\nI don't understand, please try a different action.")
        #if bear has moved in front of East door:
        elif bear_moved == True:
            print("\nYou return to see the bear plopped near the east door.")
            print("The bear has a bunch of honey.")
            print("There is a door on the south wall.")
            print("What would you like to do?")
            while True:
                choice = input(">>> ").lower()
                if (("door" in choice) or ("open" in choice) or ("south" in choice) or ("through" in choice)) and bear_moved and ("east" not in choice):
                    silver_forest_scene("North")
                elif (("door" in choice) or ("open" in choice) or ("east" in choice) or ("through" in choice)) and bear_moved and ("south" not in choice):
                    cthulu_room_scene()
                elif ("take" in choice) or ("honey" in choice):
                    dead("\nThe bear looks at you then slaps your face off.","")
                elif (("wave" in choice) or ("smile" in choice) or ("pet" in choice) or ("sing" in choice)):
                    print("\nThe bear smiles and waves at you.")
                    print("He continues to eat honey.")
                elif("help" in choice):
                    help("bear")
                else:
                    print("\nI don't understand, please try a different action.")

def cthulu_room_scene():
    #registers the Cthulu Room as being "discovered" for respawn purposes
    locations.append("Cthulu's Chamber")
    #pulling in the prisoner variable to see if he's with you:
    global prisoner_with_you
    global prisoner_alive
    ## SCENE w/ PRISONER ##
    if prisoner_with_you == True:
        print("\n\t~~When Cthulu captured me, I had tried to conquer him.")
        print("\t~~Now I think it best we just run away before I lose a limb.")
        print("\n\t~~What say you?")
        while True:
            choice = input(">>> ").lower()
            if ("run" in choice) or ("flee" in choice) or ("return" in choice) or ("start" in choice) or ("agree" in choice) or ("yes" in choice) or ("sure" in choice) or ("okay" in choice) or ("yep" in choice):
                print("\nYou and the prisoner run for the nearest door.")
                print("Over your shoulder, you see the prisoner frozen, caught in the grip of Cthulu.")
                print("With the last of his strength, he reaches in his pocket and tosses you something small.")
                print("Press ENTER to continue...")
                input()
                global name
                print(f"\n\t~~Take this, and go get the treasure for the both of us, {name}!")
                print("\nThe prisoner dissolves as the shadow of Cthulu engulfs him.")
                #prisoner dies
                prisoner_alive = False
                prisoner_with_you = False
                print("Running back to the start room, you open your hand and see you've caught a heavy iron key...")
                inventory_list.append("key")
                start()
            elif ("fight" in choice) or ("conquer" in choice) or ("kill" in choice):
                dead("Cthulu murders both of you swiftly and aimlessly.")
            elif("help" in choice):
                help("cthulu")
            else:
                print("\nI don't understand, please try a different action.")
    ## SCENE W/O PRISONER ##
    else:
        print("\nHere you see the great evil Cthulu.")
        print("He, it, whatever stares at you and you go insane.")
        print("Do you flee for you life or eat your head?")

        while True:
            choice = input(">>> ")
            if "flee" in choice:
                print("\nYou run for your life like a headless chicken.")
                print("You go through a door you didn't even notice under")
                print("the guise of Cthulu.\n")
                bear_room_scene()
            elif "start" in choice:
                print("\nYou retreat to a place of safety.")
                start()
            elif ("head" in choice) or ("eat" in choice):
                print("\nAs your head begins to turn inside out, your remaining eye")
                print("notices a slightly ajar window with a musty scent flowing from")
                print("it appear on the west side of the chamber.\n")
                print("Do you complete your meal, or make a dive for the window?")
                while True:
                    choice = input(">>> ")
                    if ("window" in choice) or ("dive" in choice) or ("crawl" in choice):
                        prisoner_room_scene()
                    elif("help" in choice):
                        help("cthulu")
                    else:
                        dead("\nYum, that was tasty.","")
            elif("help" in choice):
                help("cthulu")
            else:
                print("\nI don't understand, please try a different action.")

def prisoner_room_scene():
    #registers the Prisoner Room as being "discovered" for respawn purposes
    locations.append("The Prison")
    #Prisoner begins alive...
    global prisoner_alive
    global prisoner_with_you
    prisoner_alive = True
    #this function is referenced if player wants to kill the character
    def kill():
        print("\nYou lunge forward with the tooth of the Kraken, and drive it deep in the chest of this... *creepy* individual.")
        print("The prisoner grunts and slumps to the ground. You hear a metal clanking hit the ground.")
        input("ENTER to continue...")
        print("\nFeeling over the ground in dim light, your hands come across the metal, and make it out to be a key.")
        print("You stick the key in your pocket, and decide what to do next.")
        #the prisoner has died:
        prisoner_alive = False
        #adding key to the inventory:
        inventory_list.append("key")
        while True:
            choice = input(">>> ")
            if (("no" in choice) or ("bad" in choice) or ("horrible" in choice) or ("leave" in choice) or ("return" in choice) or ("back" in choice) or ("cthulu" in choice)):
                    print("\nYou return to Cthulu's lair.")
                    cthulu_room_scene()
            elif (("prisoner" in choice) or ("body" in choice) or ("loot" in choice)):
                print("The prisoner is dead, and there is no more loot to be found.") 
                print("You have no more purpose in this room; you should go back to Cthulu's Chamber.")
            elif("help" in choice):
                help("prisoner")
            else:
                print("\nI don't understand, please try a different action.")
    if prisoner_alive == False:
        print("\nYou return to see the shadow of a collapsed pile of flesh.")
        print("There is nothing left for you here.")
        while True:
            choice = input(">>> ")
            if (("no" in choice) or ("bad" in choice) or ("horrible" in choice) or ("leave" in choice) or ("return" in choice) or ("back" in choice) or ("cthulu" in choice)):
                print("\nYou return to Cthulu's lair.")
                cthulu_room_scene()
            elif("help" in choice):
                help("prisoner")
            else:
                    print("\nI don't understand, please try a different action.")
    else:    
        print("\nYou tumble into a narrow corridor and, without much thought,")
        print("sprint down the passage distancing yourself from the unspeakable")
        print("Cthulu encounter.\nBefore long, as the musty smell quickly turns to")
        print("a sulphuric stench that burns the nostrils, the passage opens to a small, dark room.\n")
        print("\t~~Hello?\n")
        print("The voice, sounding like marbles are stuck in the vocal chords, makes you jump.")
        print("How do you respond?")

        while True:  
            choice = input(">>> ").lower()     
            if ("flee" in choice) or ("return" in choice) or ("run" in choice):
                print("Scared out of your mind, you run back down the corridor,")
                print("preferring the evil Cthulu to the uncertainy of this situation.")
                cthulu_room_scene()

            elif (("kill" in choice) or ("murder" in choice) or ("stab" in choice)) and ("weapon" in inventory_list):
                kill()

            elif (("kill" in choice) or ("murder" in choice) or ("stab" in choice)) and ("weapon" not in inventory_list):
                        print("\nYou do not have a weapon (...yet), and can do no harm here (...for now).")
                        print("Please try a different action.")

            elif ("hello" in choice) or ("who" in choice) or ("what" in choice) or ("where" in choice) or ("hey" in choice) or ("sup" in choice) or ("hi" in choice):
                print("\t~~I am the prisoner")
                print("\t~~Hear I stand, tongue-tied and sinister.")
                print("\nFrom the darkness emerges a tattered little man,")
                print("skin as dark as could be, eyes as bright as the sea.")
                input("ENTER to continue...")
                print("\n\t~~For the mighty Cthulu may have overthrown me,")
                print("\t~~but together, the two of us could have the strength of three!")
                print("\t~~For my key knowledge is valuable, and your strength is infallible.")
                print("\t~~What is your name, my fair dame?")
                global name
                name = input("\n>>> ")

                print(f"\nSo, {name}, you too have fallen prey to Cthulu?")
                print("I would have tried to escape, but without two, 'tis bad ju-ju.")
                print(f"\nWhat do you say, {name}, to escaping as two bold")
                print("explorers, intent to lay eyes on gold?")
                while True:
                    choice = input("\n> ").lower()
                    if ("agree" in choice) or ("good" in choice) or ("great" in choice) or ("let's" in choice) or ("yes" in choice) or ("sure" in choice) or ("okay" in choice):
                        prisoner_with_you = True
                        print("\nWith your new companion, you return to Cthulu's chamber.")
                        cthulu_room_scene()
                    elif (("kill" in choice) or ("murder" in choice) or ("stab" in choice)) and ("weapon" in inventory_list):
                        kill()
                    elif (("kill" in choice) or ("murder" in choice) or ("stab" in choice)) and ("weapon" not in inventory_list):
                        print("\nYou do not have a weapon (...yet), and can do no harm here (...for now).")
                        print("Please try a different action.")
                    elif (("no" in choice) or ("bad" in choice) or ("horrible" in choice) or ("leave" in choice) or ("return" in choice) or ("back" in choice)) and (prisoner_alive == True):
                        print(f"\n\t~~Suit yourself, {name}, but know that you may never get the") 
                        print("\t~~gold without my key knowledge.")
                        print("\nSkeptically, you back out of the room keeping an eye on the prisoner, and return to Cthulu's lair.")
                        cthulu_room_scene()
                    elif (("no" in choice) or ("bad" in choice) or ("horrible" in choice) or ("leave" in choice) or ("return" in choice) or ("back" in choice)) and (prisoner_alive == False):
                        print("\nYou return to Cthulu's lair.")
                        cthulu_room_scene()
                    elif("help" in choice):
                        help("prisoner")
                    else:
                        print("\nI don't understand, please try a different action.")
            elif("help" in choice):
                help("prisoner")
            else:
                print("I don't understand, please try a different action.")
    
def silver_forest_scene(direction):
    #registers the Silver Forest Room as being "discovered" for respawn purposes
    locations.append("Silver Forest")
    if direction == "North":
        print("\nThe door opens and you are blinded by a flash of bright light.")
        print("As your eyes adjust, the light breeze and whiff of green air tells you you are outside!")
        input("ENTER to continue...")
        print("\nYou wander forward and look around, noting you are surrounded by a grove of silver aspen trees,")
        print("leaves flashing and fluttering in the wind.")
        print("What direction will you venture in?")
    else:
        print("You arrive back in the lush greenery of stunning silver trees,")
        print("a lively display of animal chirping, and a sense of peace.")
        print("What direction will you go now?")

    while True: 
        choice = input("\n> ").lower()
        if ("south" in choice) and (prisoner_with_you == False):
            sea_of_despair_scene()
        elif ("south" in choice) and (prisoner_with_you == True):
            print("\n\t~~Ooohhhh I've been to the Sea of Despair, but I am NOT going back there again.")
            print("I'll wait for you right here when you're back; good luck!")
            print("Press ENTER to continue...")
            input()
            sea_of_despair_scene()
        elif ("east" in choice):
            gold_room_scene()
        elif ("west" in choice):
            magic_portal_scene()
        elif ("north" in choice) or ("bear" in choice):
            bear_room_scene()
        elif("help" in choice):
                help("silver")
        else:
            print("I don't understand, please use a cardinal direction (north, west, east, south).")

def sea_of_despair_scene():
    #registers the Sea of Despair as being "discovered" for respawn purposes
    locations.append("Sea of Despair")
    global prisoner_with_you
    global kraken
    #death of kraken scene:
    def kraken_scene():
        print("\nYou remember the water being still... large drops of rain now hit it,")
        print("and you realize the dark clouds overhead are releasing their fury.")
        print("This Kraken may carry valuable resources; do you stay and fight,")
        print("Or back away from the shore?")
        while True:
            choice = input(">>> ").lower()
            if ("stay" in choice) or ("fight" in choice) or ("kill" in choice) or ("slay" in choice):
                print("\nYou approach the Kraken, unsure of how to defeat the beast at least 100 times your size.")
                print("The Kraken, not even noticing your miniature presence, erects itself out of the water,")
                dead("and crushes you as it meanders near the shoreline.","")
            elif("retreat" in choice) or ("run" in choice) or ("back" in choice):
                print("\nJust as you reach the edge of the forest, a thunderous CRASH")
                print("rattles your bones. Curious, you turn around just as another CRASH")
                print("carries a lightning bolt from the clouds down to... the Kraken!")
                input("ENTER to continue...")
                print("The monster is seared from the top down, and collapses dead on the rocky shoreline.")
                print("You debate whether to continue your retreat to the Silver Forest, or inspect the body")
                print("of the Kraken?")
                #kraken has died:
                kraken = False
                while True:
                    choice = input(">>> ").lower()
                    if ("inspect" in choice) or ("kraken" in choice) or ("body" in choice):
                        print("\nYou find yourself standing in the gaping mouth of the Kraken, feeling very uncomfortable.")
                        print("Prodding around, the thousands of teeth in several rows catch your attention.")
                        print("Each tooth is approximately the size of a large dagger.")
                        input("ENTER to continue...")
                        print("\nLooking away in disgust, you firmly grasp a tooth and pull hard,")
                        print("hearing a 'hhtthhhwwuck' as the tooth's suction releases from the gum.")
                        #add weapon to inventory
                        inventory_list.append("weapon")
                        print("Tooth of the Kraken in hand, you eagerly head back to the Silver Forest...")
                        print("Press ENTER to continue")
                        input()
                        silver_forest_scene("South")
                    elif ("forest" in choice) or ("back" in choice) or ("silver" in choice) or ("retreat" in choice):
                        print("\nYou return, unharmed, to the Silver Forest.")
                        silver_forest_scene("south")
                    elif("help" in choice):
                        help("sea")
                    else:
                        print("\nI don't understand, please try a different action.")
            elif("help" in choice):
                help("sea")
            else:
                print("\nI don't understand, please try a different action.")   
    #if kraken is dead and you discovered the weapon:
    if (kraken == False) and ("weapon" in inventory_list):
        print("\nYou return to the Sea of Despair, barely able to stand")
        print("the stench of the Kraken's formidable carcass strewn along the shore.")
        print("There is nothing left for you here.")
        while True:
            choice = input(">>> ")
            if (("return" in choice) or ("silver" in choice) or ("forest" in choice) or ("leave" in choice) or ("back" in choice)):
                print("\nYou return to the Silver Forest.")
                silver_forest_scene("South")
            elif("help" in choice):
                        help("sea")
            else:
                print("\nI don't understand, please try a different action.")
    #if kraken is dead and you didn't find the weapon: 
    elif (kraken == False) and ("weapon" not in inventory_list):
        print("\nYou return to the Sea of Despair, barely able to stand")
        print("the stench of the Kraken's formidable, charred carcass strewn along the shore.")
        input("ENTER to continue...")
        print("\nDigusted, you approach the mouth of the Kraken, wondering if you could salvage anything")
        print("useful from the beast.")
        print("What would you like to explore?")
        while True:
            choice = input(">>> ")
            if (("return" in choice) or ("silver" in choice) or ("forest" in choice) or ("leave" in choice) or ("back" in choice)):
                print("\nYou return to the Silver Forest.")
                silver_forest_scene("South")
            elif (("mouth" in choice) or ("look" in choice) or ("inspect" in choice) or ("body" in choice)):
                print("\nYou find yourself standing in the gaping mouth of the Kraken, feeling very uncomfortable.")
                print("Prodding around, the thousands of teeth in several rows catch your attention.")
                print("Each tooth is approximately the size of a large dagger.")
                input("ENTER to continue...")
                print("\nLooking away in disgust, you firmly grasp a tooth and pull hard,")
                print("hearing a 'hhtthhhwwuck' as the tooth's suction releases from the gum.")
                #add weapon to inventory
                inventory_list.append("weapon")
                print("Tooth of the Kraken in hand, you eagerly head back to the Silver Forest...")
                print("Press ENTER to continue")
                input()
                silver_forest_scene()
            elif("help" in choice):
                        help("sea")
            else:
                print("\nI don't understand, please try a different action.")
    # If Kraken is alive:
    print("\nThe padded forest floor begins to depart as the ground turns rocky.")
    print("The trees thin, and the life of the forest dies behind you.")
    print("You've reached the edge of the world, the end of reality, the place where dreams go to die.")
    input("ENTER to continue...")
    print("\nStopped, staring, a body of water that stretches past the horizon stands before you.")
    print("The water is as still as glass, and you can't tell where the sea ends and the sky begins.")
    print("You look down and the shoreline is made of smooth rocks and pebbles.")
    print("What would you like to do?")
    while True:
        choice = input(">>> ")
        #if player enters water
        if (("swim" in choice) or ("water" in choice) or ("enter" in choice) or ("wade" in choice) or ("drink" in choice) or ("sea" in choice)) and (("rock" not in choice) and ("pebble" not in choice)):
            print("\nYou enter the water, it's a comfortable tempature on your skin.")
            print("As you wade deeper and look down towards your feet, a tiny ripple of water")
            print("hits your body. Looking up, you realize the ripples grow larger farther out at sea.")
            print("Before you can react, the gargantuan reddish-brown head of the Kraken emerges from the sea.")
            input("ENTER to continue...")
            kraken_scene()
        #if the player throws a rock in the water
        elif (("rock" in choice) or ("pebble" in choice)) and (("water" in choice) or ("sea" in choice)):
            print("\nYou pick up a small rock, tossing it lightly up and down in one hand.")
            print("Swiftly, you toss it into the water and watch the ripples.")
            print("Suddenly, as if the ripples have awakened a great power,")
            print("the gargantuan reddisn-brown head of the Kraken emerges from the sea.")
            kraken_scene()
        elif (("return" in choice) or ("silver" in choice) or ("forest" in choice) or ("leave" in choice) or ("back" in choice)):
                print("\nYou return to the Silver Forest.")
                silver_forest_scene("South")
        elif("help" in choice):
                        help("sea")
        else:
            print("\nI don't understand, please try a different action.")
 
def magic_portal_scene():
    #registers the Gold Room as being "discovered" for respawn purposes
    locations.append("The Magic Portal")
    
    def note():
        print("You approach the tree on the right to discover a note on the tree:")
        print("\n\t\t~Have you been to the gold?")
        print("\t\t~Sometimes, the only way to the near dead")
        print("\t\t~Is to eat one's own head")
        print("\n\t\t~Let the portal between the trees")
        print("\t\t~be a gift for your journey.")
        print("\nA tad confused, you ponder over these words.")
        print("What would you like to do next?")
        while True:
            choice = input(">>> ").lower()
            if (("between" in choice) or ("curve" in choice) or ("space" in choice) or ("walk" in choice) or ("portal" in choice)) and (("silver" not in choice) and ("back" not in choice)):
                portal()
            elif ("silver" in choice) or ("forest" in choice) or ("back" in choice) or ("return" in choice):
                silver_forest_scene("west")
            elif("help" in choice):
                help("magic")
            else:
                print("\nI don't understand, please try a different action.")
    def portal():
        print("\nYou approach the distorted space between the trees,")
        print("and as soon as your head passes between them, you are")
        print("bamboozled by a portal! The forest is no more; you see different pathways")
        print("in front of you, each representing the places in this world you have discovered:")
        location_tracking(locations)
        print("\nWhere would you like to go?")
        while True:
            teleport = input(">>> ").lower()
            if "start" in teleport:
                start()
            elif "bear" in teleport:
                bear_room_scene()
            elif "cthulu" in teleport:
                cthulu_room_scene()
            elif "prisoner" in teleport:
                prisoner_room_scene()
            elif ("sea" in teleport) or ("despair" in teleport):
                sea_of_despair_scene()
            elif ("magic" in teleport) or ("portal" in teleport):
                magic_portal_scene()
            elif ("forest" in teleport) or ("silver" in teleport):
                silver_forest_scene("west")
            elif "gold" in teleport:
                gold_room_scene()
            elif("help" in choice):
                help("magic")
            else:
                print("I don't understand, please try again")
                
    print("\nThe forest grows dense as you walk this way,")
    print("Dimming the bright sunlight to an earthy glow.")
    print("Just before the brush becomes too thick to travel through,")
    print("A puzzling sight catches your eye.")
    input("ENTER to continue...")
    print("\nTwo large aspens curve toward each other to form a circle.")
    print("Everything inside this circle is unnaturely distorted as well;")
    print("The branches, the trees in the background, it seems even the air.")
    print("A piece of paper is pinned to the tree on the right.")
    print("What would you like to do?")
    while True:
        choice = input(">>> ").lower()
        if (("paper" in choice) or ("note" in choice) or ("read" in choice) or ("right" in choice)):
            note()
        elif (("between" in choice) or ("curve" in choice) or ("space" in choice) or ("walk" in choice)) and (("silver" not in choice) and ("back" not in choice)):
            portal()
        elif ("silver" in choice) or ("forest" in choice) or ("back" in choice) or ("return" in choice):
            silver_forest_scene("west")
        elif("help" in choice):
            help("magic")
        else:
            print("\nI don't understand, please try a different action.")

def gold_room_scene():
    #registers the Gold Room as being "discovered" for respawn purposes
    locations.append("Golden Pyrmaid")
    gold = 1
    
    print("You walk east... you keep walking east.")
    print("After a longer-than-you-want walk, a small gold shape appears in the distance.")
    print("You run towards it, hopes high. The small shape develops into a triangular shaped")
    print("gold building 60 feet high at it's tip.")
    input("ENTER to continue...")
    print("\nTwo massive, ebony wood doors guard the entrance, with a keyhole in one.")
    print("What do you do?")
    while True:
        choice = input("\n> ").lower()
        if (("open" in choice) or ("door" in choice) or ("pull" in choice) or ("key" in choice)) and ("key" in inventory_list):
                print("\nYou slide your key into the door, and with a turn, hear a series of latches click within.")
                print("The gargauntuan doors silently swing open.")
                print("This room is full of gold. How much do you take?")
                #choose how much gold to take. If you take less than 50, you win the game. If you take more, booby trap kills you
                while True:
                    try:
                        gold = int(input(">>> "))
                        if gold <= 50:
                            print("Nice, you're not greedy, you win!")
                            print(f"Gold collected: {gold}")
                            #calculates total deaths:
                            total_deaths = sum(death_count)
                            print(f"Deaths: {total_deaths}")
                            final_score = gold - (total_deaths*2)
                            print(f"Final Score: {final_score}")
                            print("\nPress ENTER to end the program.")
                            input()
                            exit(0)
                        else:
                            dead("You greedy bastard!","")
                    except ValueError:
                        print("Please enter a positive whole number.")

        elif (("open" in choice) or ("door" in choice) or ("pull" in choice) or ("key" in choice)) and ("key" not in inventory_list):
                print("The gargauntuan doors don't budge. It appears a key is needed.")
        elif("back" in choice) or ("west" in choice) or ("walk" in choice):
                print("You saunter, defeated, back to the silver forest.")
                silver_forest_scene("East")
        elif("help" in choice):
                        help("gold")
        else:
                print("I don't understand, please try another action.")

### NON-SPAWN SCENES ###
def location_tracking(locations):
    list_set = set(locations)
    unique_list = (list(list_set))
    for x in unique_list:
        print("-",x)

def dead(why,location):
    death_count.append(1)
    print(why, "You died!")
    print("Where would you like to respawn?")
    location_tracking(locations)

    while True: 
        respawn = input('> ').lower()
        if "start" in respawn:
            start()
        elif "bear" in respawn:
            bear_room_scene()
        elif "cthulu" in respawn:
            cthulu_room_scene()
        elif "prisoner" in respawn:
            prisoner_room_scene()
        elif ("sea" in respawn) or ("despair" in respawn):
            sea_of_despair_scene()
        elif ("magic" in respawn) or ("portal" in respawn):
            magic_portal_scene()
        elif ("forest" in respawn) or ("silver" in respawn):
            silver_forest_scene("Respawn")
        elif "gold" in respawn:
            gold_room_scene()
        else:
            print("I don't understand, please try again")

def help(location):
    if("bear" in location):
        print("The bear is very protective of his honey,")
        print("but is generally responds well to friendly activities.")
        print("Press ENTER to return to the Bear Room...")
        input()
        bear_room_scene()
    elif("cthulu" in location):
        print("Cthulu has transcended this game, and deleted any help.")
        print("You are on your own to face this force.")
        print("Press ENTER to return to Cthulu's Chamber...")
        input()
        cthulu_room_scene()
    elif("prisoner" in location):
        print("The prisoner has something you need.")
        print("There are friendly and... not so friendly ways to")
        print("Obtain what you need from him.")
        print("Press ENTER to return to the Prisoner's Room...")
        input()
        prisoner_room_scene()
    elif("silver" in location):
        print("At the center of the world, the Silver Forest is the gateway")
        print("to many things. Feeling stuck? Try walking north, south, east, or west.")
        print("Press ENTER to return to the Silver Forest...")
        input()
        silver_forest_scene("Help")
    elif("sea" in location):
        print("What is in the Sea holds a possible key to the key.")
        print("Press ENTER to return to the Sea of Despair...")
        input()
        sea_of_despair_scene()
    elif("magic" in location):
        print("Confused by the message? Cthulu has been known to drive some insane.")
        print("Press ENTER to return to the Magic Portal Room...")
        input()
        magic_portal_scene()
    elif("gold" in location):
        print("Locked out of the Pyramid? The key lies beyond your fears of Cthulu.")
        print("Once inside, do not take too many cookies from the cookie jar.")
        print("Press ENTER to return to the Golden Pyramid...")
        input()
        gold_room_scene()

welcome()
