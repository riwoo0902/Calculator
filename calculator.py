import pygame

class Calculator():
    



    def math(self,numlist:list):
        list = numlist.copy()
        multiplication = 0
        if len(numlist) > 2:
            while True:
                for i in range(len(list)):
                    if list[i] == '*':
                        list[i] = str(float(list[i-1]) * float(list[i+1]))
                        del list[i+1]
                        del list[i-1]
                        break
                    if list[i] == '/':
                        list[i] = str(float(list[i-1]) / float(list[i+1]))
                        del list[i+1]
                        del list[i-1]
                        break
                    if i == len(list)-1:
                        multiplication = 1
                        
                if multiplication == 1:
                    for i in range(len(list)):
                        if list[i] == '+':
                            list[i] = str(float(list[i-1]) + float(list[i+1]))
                            del list[i+1]
                            del list[i-1]
                            break
                        if list[i] == '-':
                            list[i] = str(float(list[i-1]) - float(list[i+1]))
                            del list[i+1]
                            del list[i-1]
                            break
                
                if len(list) < 3:
                    return list[0]
        return numlist[0]


        