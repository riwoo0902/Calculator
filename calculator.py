import pygame

class Calculator():
    
    def __init__(self,display):
        self.display = display



    def math(self):
        self.result = self.display.numderlist
        for i in range(len(self.result)):
                if self.result[i] == '*':
                    if len(self.result)-1 != i:
                        self.result[i] = str(int(self.result[i-1]) * int(self.result[i+1]))
                        del self.result[i-1]
                        del self.result[i]
                        print(self.result)
                        break
                elif self.result[i] == '/':
                    if len(self.result)-1 != i:
                        self.result[i] = str(int(self.result[i-1]) / int(self.result[i+1]))
                        del self.result[i-1]
                        del self.result[i]
                        print(self.result)
                        break



    def run(self):
        self.math()

        