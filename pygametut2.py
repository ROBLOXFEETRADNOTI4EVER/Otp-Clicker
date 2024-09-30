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
        self.autoclickvalue = 1 #for hand left
        self.autoclickvalue2 = 2 #for hand right
        self.ofshorevalue = 5 #for company
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
        self.AutomultipCost = 10
        self.AutomultipCost2 = 1
        self.offshorecompany = 10
        self.ShowImg = True
        self.show_coin_time = None 
        self.show_coin_time1 = None 
        self.autoclick_On = False
        self.autoclick_On2 = False
        self.autoclick_On3 = False
        self.show_coin_time2 = None
        self.Enableauto2 = False
        self.Enablecompany = False

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
                self.autoclick22()
                self.companylogicauto()
                #self.button4()
                #self.button5()


    def image(self,x,y,IMG_FILE):
        self.x = x
        self.y = y
        self.imagee = pygame.image.load(IMG_FILE)
        screen.blit(self.imagee, (self.x,self.y))

    def updateMultipCost(self):
        self.multipCost = round(self.multipCost * 2.5)
    
    def incraseClickWorth(self):
        self.clickworth += 2
        self.updateMultipCost()
    
    def autoupdateMultipCost(self):
        self.AutomultipCost = round(self.AutomultipCost * 2.5)
        
    
    def autoincraseClickWorth(self):
        self.autoclickvalue += 2
        self.autoupdateMultipCost()

    def incraseClickWorth2(self):
        self.clickworth += 7
        self.autoupdateMultipCost2()

    def autoupdateMultipCost2(self):
        self.AutomultipCost2 = round(self.AutomultipCost2 * 1.5)
        
    
    def autoincraseClickWorth1(self):
        self.autoclickvalue2 += 7
        self.autoupdateMultipCost2()



    def getPos(self):
        return pygame.mouse.get_pos()

    def clickshop1(self):
        self.bt1 = self.button(f"Törvény rendelet", y=130)
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
        
        if current_time - self.last_autoclick_time >= 500:  
            self.playsounds("pop.mp3",3,0.01)
            self.cookies += self.autoclickvalue 
            self.totalclicks += self.autoclickvalue
            self.last_autoclick_time = current_time  
            self.show_coin_time = current_time + 250
        
        if self.show_coin_time is not None and current_time < self.show_coin_time:
            self.image(680, 450, "Clickermouse.png")

        else:
            self.show_coin_time = None  


    def logicautoclick2(self):
        current_time2 = pygame.time.get_ticks()  

        if not hasattr(self, 'last_autoclick_time2'):
            self.last_autoclick_time2 = current_time2  
        
        if current_time2 - self.last_autoclick_time2 >= 500:  
            self.playsounds("pop.mp3",3,0.01)
            self.cookies += self.autoclickvalue2 
            self.totalclicks += self.autoclickvalue2
            self.last_autoclick_time2 = current_time2  
            self.show_coin_time1 = current_time2 + 250
        
        if self.show_coin_time1 is not None and current_time2 < self.show_coin_time1:
            self.image(1025, 450, "mouseright.png")

        else:
            self.show_coin_time1 = None  
            

    def autoclick(self):
        #logic start
        
        #logic end
        self.bt2 = self.button(f"Választó 1 ", y=190)
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
                    self.Enableauto2 = True




    def autoclick22(self):
        if self.Enableauto2 == True:
            self.bt3 = self.button(f"Választó 1 (premium)", x=1660, y=190)
            self.shopUI = False
            if self.bt3.collidepoint(self.getPos()):
                self.bt3 = self.button(f" Cost: [{self.AutomultipCost2}] | Multiplier: x{self.autoclickvalue2}", x=1660, y=190, color="#71797E")
                if pygame.mouse.get_pressed()[0]:
                    self.shopUI = True
                    if self.cookies >= self.AutomultipCost2:
                        self.playsounds("kozpenz.mp3", 1, 0.4)
                        self.cookies -= self.AutomultipCost2
                        self.autoincraseClickWorth1()
                        self.Enablecompany = True
                        self.autoclick_On2 = True  
                         

 

    def incraseClickWorthOfshore(self):
        self.clickworth += 1982
        self.autoupdateMultipCost2()

    def autoupdatecompanycost(self):
        self.offshorecompany = round(self.offshorecompany * 4)
        
    
    def autoincresecompanyclickworth(self):
        self.ofshorevalue += 1982 #need to fix it rn
        self.autoupdatecompanycost()


    def companyautoclick(self):
        current_time3 = pygame.time.get_ticks()

        # Ensure the last autoclick time is initialized
        if not hasattr(self, 'last_autoclick_time3'):
            self.last_autoclick_time3 = current_time3

        # Perform autoclick action every 500ms
        if current_time3 - self.last_autoclick_time3 >= 5000:
            generated_amount = self.ofshorevalue  
            self.playsounds("pop.mp3", 3, 0.01)
            self.cookies += generated_amount  
            self.totalclicks += generated_amount
            self.last_autoclick_time3 = current_time3
            self.show_coin_time2 = current_time3 + 350  

            
            self.generated_text = f"Közpénz:{generated_amount} generated!"  
        
        
        self.image(-30, 818, "company.png")  

        # Display the generated text for 350ms
        if self.show_coin_time2 is not None and current_time3 < self.show_coin_time2:
            text_font = pygame.font.SysFont(None, 40)  
            self.maintxt = text_font.render(self.generated_text, True, "black") 
            screen.blit(self.maintxt, (30, 800))  
        else:
            self.show_coin_time2 = None  

    def companylogicauto(self):
        #logic start
        if self.Enablecompany == True:
            #logic end
            self.bt4 = self.button(f"Offshoreceg",x=1660 , y=130)
            self.shopUI = False
            if self.bt4.collidepoint(self.getPos()):
                self.bt4 = self.button(f" Cost: [{self.offshorecompany}] | Multiplier: x{self.ofshorevalue}",x=1660 ,y=130, color="#71797E")
                if pygame.mouse.get_pressed()[0]:
                    self.shopUI = True
                    if self.cookies >= self.offshorecompany:
                        self.playsounds("kozpenz.mp3",1,0.4)
                        self.cookies -= self.offshorecompany
                        self.autoincresecompanyclickworth()
                        self.autoclick_On3 = True
                        


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
    if game.autoclick_On2 == True:
        game.logicautoclick2()
    if game.autoclick_On3 == True:
        game.companyautoclick()

    pygame.display.update()
    clock.tick(600) 