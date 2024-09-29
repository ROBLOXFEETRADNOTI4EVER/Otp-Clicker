import pygame , sys , threading
from pygame import mixer 
import os
from pygame.locals import *  
from time import sleep
import random
import math
from time import sleep

    
class Game:
   





    def __init__(self):
        self.shopUI = True
        self.fonts = pygame.font.get_fonts()
        self.maximumclicks = 10000000
        self.randomsound = ["cash1.mp3","cash2.mp3","cash3.mp3"]
        self.colorlist = ["#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043", "#FF6F00", "#FF9E80", "#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043", "#FF6F00", "#FF9E80", "#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043"]
        self.totalclicks = 0 
        self.cookies = 0
        self.autoclickvalue = 1 #for auto bot 
        self.clickworth = 1 #for maunyl 
        self.times = 1
        self.cookie = pygame.Rect(950 - 150,400 - 150,300,300)
        self.clicked = False
        self.cookie_color = "#9A3334"
        self.multipCostume_immage = pygame.image.load('fidesz.png')
        self.onCokkie = False
        self.python = pygame.image.load('fidesz.png')
        self.cooinnumb = 10
        self.multipCost = 20
        self.AutomultipCost = 50
        self.ShowImg = True
        self.show_coin_time = None 
        self.autoclick_On = False
        

    def drawotp(self):
        self.python = pygame.image.load('fidesz.png')
        screen.blit(self.python, (650,120))
    
    def textfidesz(self):
        self.maintxt = text_font.render("Fidesz  Clicker","True","black")
        screen.blit(self.maintxt, (400,500))
    
    def lvlsysm(self): 
        Pwidt = 600
        Pheight = 20
        porgress_ratio = self.totalclicks / self.maximumclicks
        porgress_ratio = min(porgress_ratio ,1)
        gbw = porgress_ratio * Pwidt
        rbw = Pwidt - gbw

        pygame.draw.rect(screen,"white", (650,850,gbw,Pheight))
        pygame.draw.rect(screen, "black", (650 + gbw, 850, rbw,Pheight))
        font = pygame.font.SysFont("timesnewroman Bold", 30)
        progress_text = font.render(f"Progress: {self.totalclicks}/{self.maximumclicks}", True, "#e04c16")
        screen.blit(progress_text, (850, 850))

    def draw_score(self):
        #self.maintxt = text_font.render("Közpénz  Clicker","True","black")  
        #screen.blit(self.maintxt, (800,100))
        text_font = pygame.font.SysFont("", 60)
        if self.cookies < 10:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","purple")
            screen.blit(self.display_cookies, (750,200))
        if self.cookies >= 10:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","purple")
            
            screen.blit(self.display_cookies, (750,200))
        if self.cookies >= 50:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","purple")
            screen.blit(self.display_cookies, (750,200))
        if self.cookies >= 100:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","purple")
            screen.blit(self.display_cookies, (750,200))
        if self.cookies >= 500:
            self.display_cookies = text_font.render(f"Közpénz score: {str(self.cookies)}","True","purple")
            screen.blit(self.display_cookies, (750,200))
    


    def playsounds(self,soundpath,channel,volume):
        mixer.init()
        mixer.Channel(channel).play(pygame.mixer.Sound(soundpath))
        mixer.Channel(channel).set_volume(volume)

    def displaycoins(self,x,y,unit):
        #for a in range(unit):
            #screen.blit(pygame.image.load('coin.png'), (x,y + a * 100))
            pass

    def moneyonscreen(self):
        #if self.cookies <= self.cooinnumb * 100:
            #unit = self.cooinnumb - math.floor(self.cookies / 100)
            #self.displaycoins(1800,0,unit)
            #if self.cookies % 10 == 9 and self.cookies > 0:
                #self.playsounds("kozpenz.mp3",1,0.4)
                #self.isplayingsound = True
                pass
    def button(self, txt, x = 1430, y = 100, width = 200, height = 50, color = "grey", txt_color = "black", txt_size = 20):
        button_rect = pygame.Rect(x, y, width, height)

        pygame.draw.rect(screen, color, button_rect)
        text_font = pygame.font.SysFont("", txt_size)
        progress_text = text_font.render(txt, True, txt_color)
        screen.blit(progress_text, (x + 15, y + 10))
        
        return button_rect

    def shop(self):
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_TAB:
                self.shopgui = pygame.Rect(1400 ,100,500,750)
                self.shopcolor = "#536878"
                pygame.draw.rect(screen,self.shopcolor,self.shopgui,)
                self.python = pygame.image.load('orban.png')
                screen.blit(self.python, (1425,125))
                self.display_cookies = text_font.render("SHOP","True","black")
                screen.blit(self.display_cookies, (1600,97))
                
                self.clickshop1()
                self.autoclick()
               #self.button3()
                #self.button4()
                #self.button5()


    def image(self,x,y,IMG_FILE):
        self.x = x
        self.y = y
        self.imagee = pygame.image.load(IMG_FILE)
        screen.blit(self.imagee, (self.x,self.y))

    def updateMultipCost(self):
        self.multipCost = round(self.multipCost * 1.5)
    
    def incraseClickWorth(self):
        self.clickworth += 1
        self.updateMultipCost()
    
    def autoupdateMultipCost(self):
        self.AutomultipCost = round(self.AutomultipCost * 1.5)
        
    
    def autoincraseClickWorth(self):
        self.autoclickvalue += 1
        self.autoupdateMultipCost()

    def getPos(self):
        return pygame.mouse.get_pos()

    def clickshop1(self):
        self.bt1 = self.button(f"Cost: [{self.multipCost}] | Multiplier: x{self.clickworth}", y=130)
        self.shopUI = False

        if self.bt1.collidepoint(self.getPos()):
            self.bt1 = self.button(f"Cost: [{self.multipCost}] | Multiplier: x{self.clickworth}", y=130, color="#71797E")
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                if self.cookies >= self.multipCost:
                    self.playsounds("kozpenz.mp3",1,0.4)
                    self.cookies -= self.multipCost
                    self.incraseClickWorth()

    

    def logicautoclick(self):
        current_time = pygame.time.get_ticks()  

        if not hasattr(self, 'last_autoclick_time'):
            self.last_autoclick_time = current_time  
        
        if current_time - self.last_autoclick_time >= 1000:  
            self.playsounds("pop.mp3",3,0.01)
            self.cookies += self.autoclickvalue 
            self.totalclicks += self.autoclickvalue
            self.last_autoclick_time = current_time  
            self.show_coin_time = current_time + 500
        
        if self.show_coin_time is not None and current_time < self.show_coin_time:
            self.image(680, 450, "Clickermouse.png")

        else:
            self.show_coin_time = None  
            

    def autoclick(self):
        #logic start
        
        #logic end
        self.bt2 = self.button(f"Cost: [{self.AutomultipCost}] | Multiplier: x{self.autoclickvalue}", y=190)
        self.shopUI = False
        if self.bt2.collidepoint(self.getPos()):
            self.bt2 = self.button(f" Cost: [{self.AutomultipCost}] | Multiplier: x{self.autoclickvalue}", y=190, color="#71797E")
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                if self.cookies >= self.AutomultipCost:
                    self.playsounds("kozpenz.mp3",1,0.4)
                    self.cookies -= self.AutomultipCost
                    self.autoincraseClickWorth()
                    self.autoclick_On = True
 


    def button3(self):
        self.bt3 = self.button("tes", y=250)
        self.shopUI = False
        if self.bt3.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                self.bt3 = self.button("tes", y=250, color="#848884")

            else:
                self.bt3 = self.button("tes", y=250, color="#71797E")


    def button4(self):
        self.bt4 = self.button("tes", y=310)
        self.shopUI = False
        if self.bt4.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                self.bt4 = self.button("tes", y=310, color="#848884")
            else:
                self.bt4 = self.button("tes", y=310, color="#71797E")


    def button5(self):
        self.bt5 = self.button("tes", y=370)
        self.shopUI = False
        if self.bt5.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                self.bt5 = self.button("tes", y=370, color="#848884")
            else:
                self.bt5 = self.button("tes", y=370, color="#71797E")
                     


    def bacgkround(self):
        self.background = pygame.image.load('idk.jpeg')
        screen.blit(self.background, (0,0))

    def click_button(self):
        self.onCokkie = False
        if self.cookie.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                
            else:
                if self.clicked:
                    self.totalclicks += self.clickworth #another value to track how many cookies later i have to change this 
                    self.cookies += self.clickworth
                    self.totalclicks 
                    self.clicked = False
                    self.cookie_color = random.choice(self.colorlist)
                    self.playsounds(random.choice(self.randomsound),0,0.1) #annyonig game sound


            self.onCokkie = True
                    

        else: 
            self.cookie_color = "#f6871f"
            
            
        pygame.draw.rect(screen,self.cookie_color,self.cookie,border_radius=150)

    def render(self):
    
        self.textfidesz()
        self.bacgkround()
        self.shop()
        self.clickshop1()
        self.lvlsysm()
        self.moneyonscreen()
        self.draw_score()
        self.click_button()
        
        self.drawotp()

pygame.init()
widt = 1920
height = 1820

game = Game()

fs = pygame.RESIZABLE
screen = pygame.display.set_mode((widt, height), fs)
pygame.display.set_caption("OTP Clicker")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None,50)
title = text_font.render("OTP Clicker",True,"orange")
keeeys = pygame.key.get_pressed()

while True:
    
    
    
    
    #screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                game.shop()
                print("t")
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(title, (850,90))
    
    game.render()
    if game.autoclick_On == True:
        game.logicautoclick()

    pygame.display.update()
    clock.tick(600) 