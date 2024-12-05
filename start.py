import pygame

from display import *

class Start():
    isActive = True
    screen = (1200,900)
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("codingnow.co.kr")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen)
        self.display = Display(self.screen)
        
    
    def eventProcess(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.isActive = False
            
    def run(self):
        while self.isActive:
            self.screen.fill((0, 255, 255))
            self.eventProcess()
            self.display.draw()
            pygame.display.update()
            self.clock.tick(100)

if __name__ == '__main__':
    game = Start()
    game.run()