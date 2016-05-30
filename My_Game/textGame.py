"""
"""
import time
#character and dictionary
susie = {'name':'Susie', 'hair_color':'brown', 'eye_color':'brown', 'health':5, 'endurance':5, 'speed':5, 'strength':5, 'defense':5, 'agility':5}
#create an enemy
enemy1 = {'name':'wild boar', 'health':9, 'endurance':1, 'speed':1, 'strength':9, 'defense':9, 'agility':1}

#function to print out any characteristic, created through applying abstraction
def print_char(player, char):
    print("          " + str(player[char]));

def betterInfoOf(player):
    for key in player:
        print(str(key).upper() + " : " + str(player[key]));
    print('\n');
#calling info functions
betterInfoOf(susie);
betterInfoOf(enemy1);

#character interaction functions
def fight_between(hero,villian):
    #simple fight
    compare = villian['strength'] > hero['defense'];
    if(compare):
        hero['health'] -= 2;
        print("You get away from the " + villian['name'] + ", but with a few scratches.");
        time.sleep(4);
        print("Your health is now", hero['health'], ".");
        time.sleep(2);
    if(not compare):
        print("You are able to fend off the " + villian['name'] + "!");
        time.sleep(4);
        print("You get away with just a scratch.");
        time.sleep(4);

def chase_between(hero,villian):
    print("run!");



#point1 functions:
def event1(hero, villian):
    print("As you stand there on the beach, a " + villian['name'] + " appeared out of nowhere.");
    time.sleep(6);
    print("The boar decides to charge!");
    time.sleep(4);
    option = input("Do you run(R) or fight(F)?");
    if(option.lower() == 'f'):
        fight_between(hero, villian);
    elif(option.lower() == 'r'):
        chase_between(hero,villian);


#game intro functions
def begin_game():
    print("You awaken on a strange island.");
    time.sleep(4)
    print("You remember being on a boat, waves rocking back and forth hasrshly in the summer storm.");
    time.sleep(6);
    print("Someone called out to you, screaming, yelling to 'get down'.");
    time.sleep(4);
    print("Then something hit you in the back of the head.");
    time.sleep(4);
    print("How...");
    time.sleep(2);
    print("How did I get here?");
    time.sleep(4);

def start():
    ready = input("Are you ready to play a game?(Y/N)");
    if(ready.lower()=='y'):
        begin_game();

start();
event1(susie, enemy1);
