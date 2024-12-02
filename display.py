import pygame

class Display():
    
    
    def __init__(self,screen):
        self.screen = screen
        self.Font = pygame.font.SysFont('malgungothic', 50)
        self.Font2 = pygame.font.SysFont('malgungothic', 100)
        self.printnumder =''
        self.numderlist = []
        self.listset = 1
        
    def clickchick(self):
        self.buttonFontlist = [self.button0,self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9,self.button10,self.button11,self.button12,self.button13,self.button14]
        pos = pygame.mouse.get_pos()
        for i in range(15):
            if self.buttonFontlist[i].collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                if self.lock == 0:
                    self.lock = 1
                    if i< 10:
                        self.printnumder += str(i)
                        if self.listset == 1:
                            self.numderlist.append(str(i))
                            self.listset = 0
                        else: 
                            self.numderlist[len(self.numderlist)-1] += str(i)
                            self.listset = 0
                            
                    if self.listset == 0:
                        if i == 10:
                            self.printnumder += '+'
                            self.numderlist.append('+')
                            self.listset = 1
                        elif i == 11:
                            self.printnumder += '-'
                            self.numderlist.append('-')
                            self.listset = 1
                        elif i == 12:
                            self.printnumder += '*'
                            self.numderlist.append('*')
                            self.listset = 1
                        elif i == 13:
                            self.printnumder += '/'
                            self.numderlist.append('/')
                            self.listset = 1
                        elif i == 14:
                            self.printnumder = ''
                            self.numderlist = []
                            self.listset = 1
                        
        if pygame.mouse.get_pressed()[0] == False:
            self.lock = 0

    
    def draw(self):
        pygame.draw.rect(self.screen,(127,127,127),[250,100,700,100])
        self.button0 = self.screen.blit(self.Font.render('0',True,(255,255,255)),(575,800))
        self.button1 = self.screen.blit(self.Font.render('1',True,(255,255,255)),(375,350))
        self.button2 = self.screen.blit(self.Font.render('2',True,(255,255,255)),(575,350))
        self.button3 = self.screen.blit(self.Font.render('3',True,(255,255,255)),(775,350))
        self.button4 = self.screen.blit(self.Font.render('4',True,(255,255,255)),(375,500))
        self.button5 = self.screen.blit(self.Font.render('5',True,(255,255,255)),(575,500))
        self.button6 = self.screen.blit(self.Font.render('6',True,(255,255,255)),(775,500))
        self.button7 = self.screen.blit(self.Font.render('7',True,(255,255,255)),(375,650))
        self.button8 = self.screen.blit(self.Font.render('8',True,(255,255,255)),(575,650))
        self.button9 = self.screen.blit(self.Font.render('9',True,(255,255,255)),(775,650))
        self.button10 = self.screen.blit(self.Font.render('+',True,(255,255,255)),(125,425))
        self.button11 = self.screen.blit(self.Font.render('-',True,(255,255,255)),(225,425))
        self.button12 = self.screen.blit(self.Font.render('*',True,(255,255,255)),(125,575))
        self.button13 = self.screen.blit(self.Font.render('/',True,(255,255,255)),(225,575))
        self.button14 = self.screen.blit(self.Font.render('초기화',True,(255,255,255)),(900,500))
        self.screen.blit(self.Font.render(self.printnumder,True,(255,255,255)),(300,120))
        self.clickchick()
        