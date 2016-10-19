import pygame
import sys
from extractor import *
screen_size=(640, 480)
num_colours=6
extract_size=(200, 200)
difference=1

def main():
    pygame.init()
    screen=pygame.display.set_mode(screen_size)
    colours=extract_colours_from_image(str(sys.argv[1]), num_colours, extract_size, difference)
    print(colours)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                break
        screen.fill((0, 0, 0))

        for i in range(len(colours)):
            this_rect=pygame.Rect(i*screen_size[0]/len(colours), 0, screen_size[0]/len(colours), screen_size[1])
            pygame.draw.rect(screen, colours[i], this_rect)


        pygame.display.flip()
    pygame.quit()

if __name__=='__main__':
    sys.exit(main())