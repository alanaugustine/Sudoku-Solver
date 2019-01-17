import pygame


def main():
    pygame.init()
    display_width=800
    display_height=600
    pygame.display.set_caption("Sudoku Solver")
    screen=pygame.display.set_mode((display_width,display_height))
	
    white=(255,255,255)
    black=(0,0,0)
    green=(0,255,0)
    red=(255,0,0)
    yellow=(255,255,153)
    running=True
    while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode == 'q':
                        running=False
                
            screen.fill(yellow)
            mouse=pygame.mouse.get_pos()
            for row in range(9):
                for col in range(9):
                    if ((mouse[0]<=row*50++50 and mouse[0]>=row*50 ) and (mouse[1]<= col*50+50 and mouse[1]>=col*50)):
                        pygame.draw.rect(screen,red,(row*50,col*50,50,50),1)
                    else:
                        pygame.draw.rect(screen,black,(row*50,col*50,50,50),1)
            pygame.display.update()
            
    pygame.quit()			
if __name__ =="__main__":
	main()
