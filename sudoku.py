import pygame


def main():
	pygame.init()
	pygame.display.set_caption("Sudoku Solver")
	screen=pygame.display.set_mode((240,180))
	
	
	running=True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running=false
				
if __name__ =="__main__":
	main()