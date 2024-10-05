








import pygame , sys , threading
from pygame import mixer 
import os
from pygame.locals import *  
from time import sleep
import random
import math
from time import sleep
import json
import atexit

class Game:
   







    def __init__(self):
        self.cookie = pygame.Rect(950 - 150, 400 - 150, 300, 300)
        self.slider_rect = pygame.Rect(20, 20, 200, 10)
        self.slider_button_rect = pygame.Rect(self.slider_rect.x, self.slider_rect.y - 5, 20, 20)
        self.cookie_color = "#f6871f"

        self.backgrounds = ['idk.jpeg', 'citybackground.jpeg', 'background3.jpg', 'background4.jpg', 'background5.png', 'background6.png']
        self.current_background = self.backgrounds[0]  
        self.purchased_backgrounds = [False] * 6 
        self.selected_background = 0  
        self.show_buy_ui = False  
        self.game_completed = False
        self.cookies = 0
        self.totalclicks = 0
        self.clickworth = 1
        self.autoclickvalue = 1
        self.autoclickvalue2 = 2
        self.ofshorevalue = 5
        self.ofshorevalue2nd = 7
        self.volume = 1.0
        self.muted = False
        self.multipCost = 20
        self.AutomultipCost = 1000
        self.AutomultipCost2 = 10000
        self.offshorecompany = 500000
        self.offshorecompany2nd = 1000000
        self.maximumclicks = 100000000
        self.show_coin_time = None
        self.show_coin_time1 = None
        self.show_coin_time2 = None
        self.show_coin_time3 = None
        self.show_coin_time4 = None
        self.base_value = 100  
        self.base_value2company = 200  
        self.offshorecompany_orban = 5000000 
        self.ofshorevalue_orban = 10 
        self.coolmusicplay = True

                
        self.autoclick_On = False  
        self.autoclick_On2 = False  
        self.autoclick_On3 = False
        self.autoclick_On4 = False
        self.autoclick_On_orban = False
        self.show_dropdown = False  
        self.selected_channel_index = 0  
        self.current_channel = 0  
        self.confirm_selection = False  
        self.BetterBackground = False
        self.font = pygame.font.SysFont(None, 36)  
        self.Enableauto2 = False
        self.Enablecompany = False
        self.EnableCompany2start = False
        self.EnableOrbánpalotaStart = False
        self.clicked = False
        self.channels = ["Channel 0", "Channel 1", "Channel 2", "Channel 3","Channel 4", "Channel 5", "Channel 6", "Channel 7"]
        self.selected_channel_index = 0 
        self.current_channel = 0  


        self.show_save_prompt = False
        self.save_decision_made = False
        self.load_save = False

        self.check_for_save()


        self.shopUI = True
        self.fonts = pygame.font.get_fonts()
        self.randomsound = ["cash1.mp3", "cash2.mp3", "cash3.mp3"]
        self.colorlist = ["#FFA07A", "#FF8C00", "#FF6347", "#FF7F50", "#FFB347", "#E9967A", "#F08080", "#FFA500", "#FF4500", "#FF7043", "#FF6F00", "#FF9E80"]

    def check_for_save(self):

        save_file = "game_save.json"
        if os.path.exists(save_file):
            self.show_save_prompt = True  
        else:
            print("No save file found. Starting a new game.")

    def save_game_state(self):
        data = {
            "cookies": self.cookies,
            "totalclicks": self.totalclicks,
            "clickworth": self.clickworth,
            "autoclickvalue": self.autoclickvalue,
            "autoclickvalue2": self.autoclickvalue2,
            "ofshorevalue": self.ofshorevalue,
            "ofshorevalue2nd": self.ofshorevalue2nd,
            "volume": self.volume,
            "muted": self.muted,
            "slider_position": self.slider_button_rect.x,
            "multipCost": self.multipCost,
            "AutomultipCost": self.AutomultipCost,
            "AutomultipCost2": self.AutomultipCost2,
            "offshorecompany": self.offshorecompany,
            "offshorecompany2nd": self.offshorecompany2nd,
            "purchased_backgrounds": self.purchased_backgrounds,  
            "selected_background": self.selected_background, 
        }

        with open("game_save.json", "w") as file:
            json.dump(data, file)

    def load_game_state(self):
        try:
            with open("game_save.json", "r") as file:
                data = json.load(file)
                self.cookies = data.get("cookies", 0)
                self.totalclicks = data.get("totalclicks", 0)
                self.clickworth = data.get("clickworth", 1)
                self.autoclickvalue = data.get("autoclickvalue", 1)
                self.autoclickvalue2 = data.get("autoclickvalue2", 2)
                self.ofshorevalue = data.get("ofshorevalue", 5)
                self.ofshorevalue2nd = data.get("ofshorevalue2nd", 7)
                self.volume = data.get("volume", 1.0)
                self.muted = data.get("muted", False)
                self.slider_button_rect.x = data.get("slider_position", self.slider_rect.x)
                self.multipCost = data.get("multipCost", 20)
                self.AutomultipCost = data.get("AutomultipCost", 1000)
                self.AutomultipCost2 = data.get("AutomultipCost2", 10000)
                self.offshorecompany = data.get("offshorecompany", 500000)
                self.offshorecompany2nd = data.get("offshorecompany2nd", 1000000)
                self.purchased_backgrounds = data.get("purchased_backgrounds", [False] * 6)
                self.selected_background = data.get("selected_background", 0)
                self.current_background = self.backgrounds[self.selected_background]  
                print("Game loaded successfully.")
        except FileNotFoundError:
            print("No save file found. Starting a new game.")

    def draw_save_prompt(self, screen):
        prompt_text = self.font.render("Load previous game?", True, (255, 255, 255))
        screen.blit(prompt_text, (800, 500))

       
        yes_button = pygame.Rect(800, 550, 100, 50)
        pygame.draw.rect(screen, (0, 255, 0), yes_button)
        yes_text = self.font.render("Yes", True, (0, 0, 0))
        screen.blit(yes_text, (830, 560))

       
        no_button = pygame.Rect(950, 550, 100, 50)
        pygame.draw.rect(screen, (255, 0, 0), no_button)
        no_text = self.font.render("No", True, (0, 0, 0))
        screen.blit(no_text, (980, 560))

        return yes_button, no_button
    def handle_save_prompt(self, event):
        
        yes_button, no_button = self.draw_save_prompt(screen)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if yes_button.collidepoint(event.pos):
               
                self.load_save = True
                self.load_game_state()
                self.show_save_prompt = False  
                self.save_decision_made = True
            elif no_button.collidepoint(event.pos):
               
                save_file = "game_save.json"
                if os.path.exists(save_file):
                    os.remove(save_file)
                self.show_save_prompt = False  
                self.save_decision_made = True

    def handle_volume_slider(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.volume = max(0, self.volume - 0.01)
        if keys[pygame.K_RIGHT]:
            self.volume = min(1, self.volume + 0.01)


        self.slider_button_rect.x = self.slider_rect.x + int(self.slider_rect.width * self.volume)

        mixer.Channel(self.current_channel).set_volume(self.volume)



    def draw_volume_slider(self):
        red_value = int(255 * self.volume)
        green_value = 192 - int(192 * self.volume)  
        blue_value = 60 - int(60 * self.volume) 
        slider_color = (red_value, green_value, blue_value) 

        pygame.draw.rect(screen, "grey", self.slider_rect)
        pygame.draw.rect(screen, slider_color, self.slider_button_rect)

        font = pygame.font.SysFont(None, 24)
        instructions_text = font.render("Press CTRL+ESC to change channel", True, "white")
        screen.blit(instructions_text, (self.slider_rect.x, self.slider_rect.y + 30))


    def create_slider(self):
        self.slider_rect = pygame.Rect(50, 50, 200, 10)
        self.slider_button_rect = pygame.Rect(self.slider_rect.x, self.slider_rect.y - 5, 10, 20)
        self.volume = 0.5
        self.muted = False
    def handle_channel_selection(self):
        if self.show_dropdown:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.selected_channel_index = min(self.selected_channel_index + 1, len(self.channels) - 1)
                pygame.time.wait(150)  
            if keys[pygame.K_UP]:
                self.selected_channel_index = max(self.selected_channel_index - 1, 0)
                pygame.time.wait(150)  
            if keys[pygame.K_RETURN]:
                self.current_channel = self.selected_channel_index
                self.confirm_selection = True
                self.playsounds("selectionsound.mp3", 0, 1)  
                pygame.time.wait(150)  
            if keys[pygame.K_RETURN] and self.confirm_selection:
                self.show_dropdown = False

    def draw_dropdown(self):
        if self.show_dropdown:
            dropdown_height = len(self.channels) * 25
            dropdown_width = 120 
            dropdown_rect = pygame.Surface((dropdown_width, dropdown_height), pygame.SRCALPHA)
            dropdown_rect.fill((255, 255, 255, 128)) 
            screen.blit(dropdown_rect, (self.slider_rect.x, self.slider_rect.y + 50))

            for i, channel in enumerate(self.channels):
                color = "black"
                if i == self.selected_channel_index:
                    color = "red"
                text = pygame.font.SysFont(None, 30).render(channel, True, color)
                screen.blit(text, (self.slider_rect.x + 10, self.slider_rect.y + 55 + i * 25))

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
        screen.blit(progress_text, (830, 850))

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
                self.companylogicauto2nd()
                self.companylogicauto_orbanpalota()
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
            self.bt3 = self.button(f"Választó 1 (premium)", x=1660, y=130)
            self.shopUI = False
            if self.bt3.collidepoint(self.getPos()):
                self.bt3 = self.button(f" Cost: [{self.AutomultipCost2}] | Multiplier: x{self.autoclickvalue2}", x=1660, y=130, color="#71797E")
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
        self.ofshorevalue += 4 #need to fix it rn
        self.autoupdatecompanycost()


    def companyautoclick(self):
        current_time3 = pygame.time.get_ticks()

        if not hasattr(self, 'last_autoclick_time3'):
            self.last_autoclick_time3 = current_time3

        if current_time3 - self.last_autoclick_time3 >= 5000:  
            
            generated_amount = self.base_value * self.ofshorevalue 
            self.playsounds("factory.mp3", 4, 0.04)
            self.cookies += generated_amount
            self.totalclicks += generated_amount
            self.last_autoclick_time3 = current_time3
            self.show_coin_time2 = current_time3 + 350  

            self.generated_text = f"{generated_amount} Közpénz generated!"  
        self.image(-30, 818, "company.png")

        if self.show_coin_time2 is not None and current_time3 < self.show_coin_time2:
            text_font = pygame.font.SysFont(None, 40)
            self.maintxt = text_font.render(self.generated_text, True, "black")
            screen.blit(self.maintxt, (30, 800))
        else:
            self.show_coin_time2 = None


    def companylogicauto(self):
        if self.Enablecompany == True:
            
            self.bt4_company1 = self.button(f"Offshoreceg", x=1660, y=190)
            self.shopUI = False
            if self.bt4_company1.collidepoint(self.getPos()):
                self.bt4_company1 = self.button(f" Cost: [{self.offshorecompany}] | Multiplier: x{self.ofshorevalue}", x=1660, y=190, color="#71797E")
                if pygame.mouse.get_pressed()[0]:
                    self.shopUI = True
                    if self.cookies >= self.offshorecompany:
                        self.cookies -= self.offshorecompany
                        self.playsounds("kozpenz.mp3", 1, 0.4)
                        self.autoincresecompanyclickworth()
                        self.autoclick_On3 = True
                        self.EnableCompany2start = True
























    def incraseClickWorthOfshorecompany2nd(self):
        self.clickworth += 1982
        self.autoupdateMultipCost2()

    def autoupdatecompanycost2end(self):
        self.offshorecompany2nd = round(self.offshorecompany2nd * 4)
        
    
    def autoincresecompanyclickworth2nd(self):
        self.ofshorevalue2nd += 4 #need to fix it rn
        self.autoupdatecompanycost2end()


    def companyautoclick2nd(self):
        current_time4 = pygame.time.get_ticks()

        if not hasattr(self, 'last_autoclick_time4'):  
            self.last_autoclick_time4 = current_time4

        if current_time4 - self.last_autoclick_time4 >= 5000:  
            
            generated_amount2nd = self.base_value2company * self.ofshorevalue2nd 
            self.playsounds("factory.mp3", 5, 0.04)
            self.cookies += generated_amount2nd
            self.totalclicks += generated_amount2nd
            self.last_autoclick_time4 = current_time4  
            self.show_coin_time3 = current_time4 + 500 

            self.generated_text1 = f"{generated_amount2nd} Közpénz generated!"  
        self.image(120, 818, "company.png")  

        if self.show_coin_time3 is not None and current_time4 < self.show_coin_time3:
            text_font = pygame.font.SysFont(None, 40)
            self.maintxt2 = text_font.render(self.generated_text1, True, "black")
            screen.blit(self.maintxt2, (100, 850))  
        else:
            self.show_coin_time3 = None


    def companylogicauto2nd(self):
        if self.EnableCompany2start == True:
            self.bt5_company2 = self.button(f"Offshoreceg 2nd", y=250)
            self.shopUI = False
            if self.bt5_company2.collidepoint(self.getPos()):
                self.bt5_company2 = self.button(f" Cost: [{self.offshorecompany2nd}] | Multiplier: x{self.ofshorevalue2nd}", y=250, color="#71797E")
                if pygame.mouse.get_pressed()[0]:
                    self.shopUI = True
                    if self.cookies >= self.offshorecompany2nd:
                        self.autoclick_On4 = True
                        self.cookies -= self.offshorecompany2nd
                        self.playsounds("kozpenz.mp3", 1, 0.4)
                        self.autoincresecompanyclickworth2nd()
                        self.autoclick_On4 = True
                        self.EnableOrbánpalotaStart = True



    def incraseClickWorthOrbánpalota(self):
        self.clickworth += 1982
        self.autoupdateMultipCostOrbánpalota()

    def autoupdateMultipCostOrbánpalota(self):
        self.offshorecompany_orban = round(self.offshorecompany_orban * 4)
        
    def autoincreseOrbánpalotaclickworth(self):
        self.ofshorevalue_orban += 5 
        self.autoupdateMultipCostOrbánpalota()

    def orbanpalotaautoclick(self):
        current_time5 = pygame.time.get_ticks()

        if not hasattr(self, 'last_autoclick_time5'): 
            self.last_autoclick_time5 = current_time5

        if current_time5 - self.last_autoclick_time5 >= 5000:  
            generated_amount_orban = self.base_value2company * self.ofshorevalue_orban 
            self.playsounds("factory.mp3", 7, 0.05)
            self.cookies += generated_amount_orban
            self.totalclicks += generated_amount_orban
            self.last_autoclick_time5 = current_time5 
            self.show_coin_time4 = current_time5 + 350  

            self.generated_text_orban = f"{generated_amount_orban} Közpénz generated!"  
        self.image(80, 418, "orbanpalotareal.png") 

        if self.show_coin_time4 is not None and current_time5 < self.show_coin_time4:
            text_font = pygame.font.SysFont(None, 40)
            self.maintxt_orban = text_font.render(self.generated_text_orban, True, "black")
            screen.blit(self.maintxt_orban, (150, 450))  
        else:
            self.show_coin_time4 = None

   
    def companylogicauto_orbanpalota(self):
        if self.EnableOrbánpalotaStart == True:
            self.bt6 = self.button(f"Orbánpalota", x=1660, y=250)
            self.shopUI = False
            if self.bt6.collidepoint(self.getPos()):
                self.bt6 = self.button(f" Cost: [{self.offshorecompany_orban}] | Multiplier: x{self.ofshorevalue_orban}", x=1660, y=250, color="#71797E")
                if pygame.mouse.get_pressed()[0]:
                    self.shopUI = True
                    if self.cookies >= self.offshorecompany_orban:
                        self.cookies -= self.offshorecompany_orban
                        self.playsounds("kozpenz.mp3", 1, 0.4)
                        self.autoincreseOrbánpalotaclickworth()
                        self.autoclick_On_orban = True  
                        self.EnableOrbánpalotaStart = True
                        self.BetterBackground = True
                        if self.coolmusicplay == True:
                            self.playsounds("fluet.mp3", 6, 0.5) 
                            self.coolmusicplay = False









    def bacgkround(self):
        if self.current_background: 
            self.background = pygame.image.load(self.current_background)  
        else:
            self.background = pygame.image.load('default_background.jpg') 

        screen.blit(self.background, (0, 0)) 




    def button4(self):
        self.bt4 = self.button("tes", y=310)
        self.shopUI = False
        if self.bt4.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                self.bt4 = self.button("tes", y=310, color="#848884")
            else:
                self.bt4 = self.button("tes", y=310, color="#71797E")

    def draw_buy_background_ui(self):
       
        transparent_bg = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        transparent_bg.fill((255, 255, 255, 77))  
        screen.blit(transparent_bg, (0, 0))

        background_prices = [1000, 20000, 30000, 42000, 50000, 69000]  
        
        for i in range(len(self.backgrounds)):
            button_width = 350 
            button_height = 60  
            button_x = 400 
            button_y = 200 + i * 80 
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            
            if self.purchased_backgrounds[i]:
                if i == self.selected_background:
                    pygame.draw.rect(screen, (0, 255, 0), button_rect) 
                    text = self.font.render(f"Background {i + 1}: Owned", True, (255, 255, 255))
                else:
                    pygame.draw.rect(screen, (128, 128, 128), button_rect)
                    text = self.font.render(f"Background {i + 1}: Owned", True, (255, 255, 255))
            else:
                pygame.draw.rect(screen, (0, 128, 0), button_rect)
                text = self.font.render(f"Background {i + 1}: {background_prices[i]} cookies", True, (255, 255, 255))
            text_rect = text.get_rect(center=button_rect.center)
            screen.blit(text, text_rect)


    def handle_buy_background(self, event):
        background_prices = [1000, 20000, 30000, 42000, 50000, 69000]
        
        for i in range(len(self.backgrounds)):
            button_width = 350
            button_height = 60
            button_x = 400
            button_y = 200 + i * 80
            
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    if self.purchased_backgrounds[i]:  
                        self.selected_background = i
                        self.playsounds("selectionsound.mp3", 0, 1)
                        self.current_background = self.backgrounds[self.selected_background]
                    elif self.cookies >= background_prices[i]:
                        self.cookies -= background_prices[i]
                        self.playsounds("fluet.mp3", 6, 0.5)
                        self.purchased_backgrounds[i] = True

    def button5(self):
        self.bt5 = self.button("tes", y=370)
        self.shopUI = False
        if self.bt5.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.shopUI = True
                self.bt5 = self.button("tes", y=370, color="#848884")
            else:
                self.bt5 = self.button("tes", y=370, color="#71797E")
                     


    def click_button(self):
        self.onCokkie = False
        if self.cookie.collidepoint(self.getPos()):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                
            else:
                if self.clicked:
                    self.totalclicks += self.clickworth
                    self.cookies += self.clickworth
                    self.totalclicks 
                    self.clicked = False
                    self.cookie_color = random.choice(self.colorlist)
                    self.playsounds(random.choice(self.randomsound),0,0.1) 


            self.onCokkie = True
                    

        else: 
            self.cookie_color = "#f6871f"
            
            
        pygame.draw.rect(screen,self.cookie_color,self.cookie,border_radius=150)


    def check_for_game_completion(self):
        if self.totalclicks >= self.maximumclicks:
            self.game_completed = True

    def draw_congrats_prompt(self):
        font = pygame.font.SysFont(None, 60)
        
        
        congrats_text = font.render("Congratulations! You've completed the game!", True, (255, 255, 255))
        screen.blit(congrats_text, (400, 250))  

       
        play_again_button = pygame.Rect(400, 400, 300, 100) 
        pygame.draw.rect(screen, (0, 128, 0), play_again_button) 
        play_again_text = font.render("Play Again", True, (255, 255, 255)) 

        
        play_again_text_rect = play_again_text.get_rect(center=play_again_button.center)
        screen.blit(play_again_text, play_again_text_rect)

        
        quit_button = pygame.Rect(800, 400, 300, 100) 
        pygame.draw.rect(screen, (128, 0, 0), quit_button) 
        quit_text = font.render("Quit", True, (255, 255, 255)) 

        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_text_rect)

        self.handle_congrats_prompt(play_again_button, quit_button)


    def handle_congrats_prompt(self, play_again_button, quit_button):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_again_button.collidepoint(event.pos):
                    self.restart_game() 
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def restart_game(self):
        self.cookies = 0
        self.totalclicks = 0
        self.game_completed = False

    def render(self):
        if self.game_completed:  
            screen.fill((0, 0, 0))  
            self.draw_congrats_prompt() 
        elif self.show_save_prompt and not self.save_decision_made: 
            self.draw_save_prompt(screen)
        else:
            self.textfidesz()
            self.bacgkround()
            self.shop()
            self.lvlsysm()
            self.moneyonscreen()
            self.draw_score()
            
           
            if not self.show_buy_ui:
                self.click_button()
            
            self.draw_volume_slider()
            self.handle_volume_slider()
            self.draw_dropdown()
            self.drawotp()

        
            if self.show_buy_ui:
                self.draw_buy_background_ui()

        self.check_for_game_completion()

pygame.init()
widt = 1920
height = 1820

game = Game()

fs = pygame.RESIZABLE
screen = pygame.display.set_mode((widt, height), fs)
pygame.display.set_caption("OTP Clicker")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
title = text_font.render("OTP Clicker", True, "orange")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                game.show_buy_ui = not game.show_buy_ui  
            if event.key == pygame.K_ESCAPE and pygame.key.get_mods() & pygame.KMOD_CTRL:
                game.show_dropdown = not game.show_dropdown

        if event.type == pygame.QUIT:
            game.save_game_state()
            pygame.quit()
            sys.exit()

        if game.show_save_prompt and not game.save_decision_made:
            game.handle_save_prompt(event)

        if game.show_buy_ui:
            game.handle_buy_background(event) 
    game.render()  

    game.handle_channel_selection() 

    if game.autoclick_On:  
        game.logicautoclick()
    if game.autoclick_On2:
        game.logicautoclick2()
    if game.autoclick_On3:
        game.companyautoclick()
    if game.autoclick_On4:
        game.companyautoclick2nd()
    if game.autoclick_On_orban:
        game.orbanpalotaautoclick()

    pygame.display.update()
    clock.tick(600)
