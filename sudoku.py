import pygame


def main():
    pygame.init()
    display_width=800
    display_height=600
    pygame.display.set_caption("Sudoku Solver")
    screen=pygame.display.set_mode((display_width,display_height))
	
    white=(255,255,255)
    clock=pygame.time.Clock()
    running=True
    while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode == 'q':
                        running=False
                
            screen.fill(white)
            pygame.display.update()
    pygame.quit()			
if __name__ =="__main__":
	main()
