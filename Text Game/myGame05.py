"""



"""
import time
#character and dictionary
susie = {'name':'Susie', 'hair_color':'brown', 'eye_color':'brown', 'health':5, 'endurance':5, 'speed':5, 'strength':5, 'defense':5, 'agility':5}
#create an enemy
enemy = {'name':'Ogre', 'health':9, 'endurance':1, 'speed':1, 'strength':9, 'defense':9, 'agility':1}

#function to print out any characteristic, created through applying abstraction
def print_char(player, char):
	print("          " + str(player[char]));

def betterInfoOf(player):
	for key in player:
		print(str(key).upper() + " : " + str(player[key]));
	print('  ');
#calling info functions
betterInfoOf(susie);
betterInfoOf(enemy);

def begin_game():
	print("You awaken on strange island. \nYou remember being on a boat, waves rocking back and forth hasrshly in the summer storm.");
	time.sleep(2);
	print("Someone called out to you, screaming, yelling to 'get down'.");
	time.sleep(2);
	print("Then something hit you in the back of the head");
	time.sleep(2);
	print("How...");
	time.sleep(1);
	print("How did I get here?");

ready = raw_input("Are you ready to play a game?(Y/N)");

def start():
	if(ready.lower()=='y'):
		begin_game();

start();
