from game import game
from intro import intro_loading
from menu import menu


if __name__ == "__main__":
	debug = False
	Intro = intro_loading()
	Intro.run()
	Menu = menu()
	Menu.run()
	ismousedown = Menu.run()
	Menu.close()
	Game = game(debug)
	while True:
		if(ismousedown == True):
			Game.run()
			break




#this is the main point of entry for the program
