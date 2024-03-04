class TextAdventure:
    def __init__(self):
        self.intro()

    def intro(self):
        print("Hello my friend! this is a beta, text-based adventure game i tried to code with very few knowledge about Python and other languages in general.")
        print("You find yourself locked in a very dimly lit room, all you can see is some light spreading out of the doorway. Do you want to get closer to the only source of light?")
        self.first_choice()

    def first_choice(self):
        choice1 = input('Enter "yes" or "no": ').lower()
        if choice1 == "yes":
            self.explore_door()
        elif choice1 == "no":
            self.stay_in_room()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            self.first_choice()

    def explore_door(self):
        print("You get closer to the door and see that it's unlocked. Exit the room?")
        choice2 = input('Enter "yes" or "no": ').lower()
        if choice2 == "yes":
            self.exit_room()
        elif choice2 == "no":
            self.stay_in_room()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            self.explore_door()

    def stay_in_room(self):
        print("You spent a couple of hours in a cold room without any supplies, you feel an upcoming exhaustion, your desire for food and water becomes stronger and stronger with every passing minute.")
        choice4 = input('Enter "stay" or "leave": ').lower()
        if choice4 == "leave":
            self.taiga()
        elif choice4 == "stay":
            print("You spent another couple of hours in the room, you feel hopeless, broken and devastated.")
            print("Maybe there are no point of trying to fulfil your basic needs at all?")
            choice5 = input('Enter "yes" or "no": ')
            if choice5 == "yes":
                print("You decided not to resist your fate. Your cold, lifeless body is now rotting in some God's forgotten place.")
        else:
            print("Invalid choice. Please enter 'stay' or 'leave'.")
            self.stay_in_room()

    def exit_room(self):
        print("Once you open the door the first thing you see is an endless taiga. Cold wind blows onto your face, making it painful to breathe.")
        print("You have a choice, either you stay in the room in hope of a miracle or go investigating without any food, water, clothes or proper equipment on you in hope to find something that might help you to survive.")
        choice3 = input('Enter "stay" or "leave": ').lower()
        if choice3 == "leave":
            self.taiga()
        elif choice3 == "stay":
            self.stay_in_room()
        else:
            print("Invalid choice. Please enter 'stay' or 'leave'.")
            self.exit_room()
    
    def taiga(self):
        print("As you're walking, leaving deep trails behind you notice a wooden hut in the middle of a forest")
        print("What would you like to do?")
        choice6 = input('Enter "go inside" or "go around": ')
        if choice6 == "go inside":
            self.wooden_hut()
        elif choice6 == "go around":
            self.deep_forest()
        else:
            print("Invalid choice. Please enter 'go inside' or 'go around'.")
            self.taiga()

    def wooden_hut(self):
        print("You enter the wooden hut. Inside you find a bed, a table and a tiny kitchen. Maybe that's the safest place around. You check the kitchen, but unfortunately find nothing but dust. As you check the bedroom you hear some noises coming out of outside the hut.")
        choice7 = input('Enter "stay" or "leave": ')
        if choice7 == "leave":
            self.predator_1()
        elif choice7 == "stay":
            self.progressing_hunger()
        else:
            print("Invalid choice. Please enter 'stay' or 'leave'.")
            self.wooden_hut()
    
    def deep_forest(self):
        print("You venture deeper into the forest, encountering nothing but trees after trees. You found a a sharp, hard stick that could serve as a spear. Maybe it's better to go back?")
        choice8 = input('Enter "go further" or "turn around": ')
        if choice8 == "turn around":
            self.predator_2()
        elif choice8 == "go further":
            self.watch_tower()
        else:
            print("Invalid choice. Please enter 'go further' or 'turn around'.")
            self.deep_forest()

    def predator_1(self):
        print("As you step out of the hut something with a size of a dog immedietly tuckles you onto the ground. The unknown animal starts ripping off the remaining clothes you have.")
        choice9 = input('Enter "fight" or "escape to the hut": ')
        if choice9 == "fight":
            self.painful_death
        elif choice9 == "escape to the hut":
            self.progressing_hunger1
        else:
            print("Invalid choice. Please enter 'fight' or 'escape to the hut'.")
            self.predator_1

    def progressing_hunger(self):
        print("Not leaving the only place where you're safe is definetly the best option, you think. You stay in the hut until the noises are gone, but instead you start to hear the growling of your own stomach. You're hungry.")
        choice10 = input('Enter "stay" or "leave": ')
        if choice10 == "leave":
            self.deep_forest()
        elif choice10 == "stay":
            self.evening()
        else:
            print("Invalid choice. Please enter 'stay' or 'leave'.")
            self. progressing_hunger

    def predator_2(self):
        print("As you return to the hut something with a size of a dog immedietly tuckles you onto the ground. The unknown animal starts ripping off the remaining clothes you have.")
        choice11 = input('Enter "fight" or "run away": ')
        if choice11 == "fight":
            self.prey
        elif choice11 == "run away":
            self.painful_death
        else:
            print("Invalid choice. Please enter 'fight' or 'run away'.")
            self.predator_2()

    def watch_tower(self):
        print("You coninue walking deper and deeper into the forest, until eventually you face a huge watch tower.")
        choice12 = input('Enter "go inside" or "go around": ')
        if choice12 == "go upstairs":
            self.tower_cabin()
        elif choice12 == "go around":
            self.desparation()
        else:
            print("Invalid choice. Please enter 'go inside' or 'go around'.")
            self.watch_tower()
    pass

game = TextAdventure()
