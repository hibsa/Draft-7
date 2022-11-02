# Hiba Hamad, hhamad
# Project Name: Bloon Battles

import math
import pygame
from sys import exit 

#initiallizing pygame
pygame.init()

#initiallizing screen display, setting color to pink
screen = pygame.display.set_mode((890,735))
screen.fill('Pink')

#naming display screen, also name of the game, 'Bloon Battles'
pygame.display.set_caption('Bloon Battles')

#initiallizing clock
clock = pygame.time.Clock()

#loading map and game bar images
test_surface = pygame.image.load('graphics/map-11.png').convert_alpha()
game_bar = pygame.image.load('graphics/game-bar2.png').convert_alpha()

#loading balloon and popped balloon images
pinkB = pygame.image.load('graphics/balloon.png').convert_alpha()
itachiB = pygame.image.load('graphics/itachii.png').convert_alpha()
b = pinkB
pop = pygame.image.load('graphics/popped-balloon.png').convert_alpha()

#setting initial health to 20
healthBar = 20

#setting initial money to 300
currentMoney = 300

# Displays a balloon
# When put in while loop, balloon moves to the end of the map
class Balloons(pygame.sprite.Sprite):
    def __init__(self,b,x):

        #initiallizing sprite class
        super().__init__()

        #initiallizing variables
        self.x = x
        self.y = 85
        self.balloon = b

    ## ROUND 1
    #displays inputted balloon on screen + makes into rectangle
    #moves balloon at a slow speed when in main loop
    def round1(self):

        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))
        screen.blit(self.balloon,self.rect)

        if self.x<495:
            self.x += 1
            
        if self.x>=494 and self.y<265:
            self.y += 1
        
        if self.y>=264 and self.x<640:
            self.x += 1
            
        if self.x>=639 and self.y<800:
            self.y += 1

    ## ROUND 2
    #displays inputted balloon on screen + makes into rectangle
    #moves balloon at a medium speed when in main loop
    def round2(self):

        self.rect = self.balloon.get_rect(topleft=(self.x,self.y))
        screen.blit(self.balloon,self.rect)
        
        if self.x<495:
            self.x += 1.5
            
        if self.x>=494 and self.y<265:
            self.y += 1.5
        
        if self.y>=264 and self.x<640:
            self.x += 1.5
            
        if self.x>=639 and self.y<800:
            self.y += 1.5

    #returns true if balloon is passing the map border,
    #otherwise, returns false
    def checkPassing(self):

        if self.rect.top>735:
            return True
        
        return False

    #returns true if balloon is colliding with given item,
    #otherwise, returns false
    def isColliding(self,item):

        if self.rect.colliderect(item):
            return True

        return False

    #returns current center position of balloon
    def balloonPos(self):

        return (self.rect.centerx,self.rect.centery)

    ## ROUND 1 Balloons
    ## Contains 15 balloons 
    def round1Balloons(self):
        
        self.dB1 = Balloons(b,100)
        self.dB2 = Balloons(b,60)
        self.dB3 = Balloons(b,20)
        self.dB4 = Balloons(b,-20)
        self.dB5 = Balloons(b,-60)
        self.dB6 = Balloons(b,-100)
        self.dB7 = Balloons(b,-140)
        self.dB8 = Balloons(b,-180)
        self.dB9 = Balloons(b,-220)
        self.dB10 = Balloons(b,-260)
        self.dB11 = Balloons(b,-300)
        self.dB12 = Balloons(b,-340)
        self.dB13 = Balloons(b,-380)
        self.dB14 = Balloons(b,-420)
        self.dB15 = Balloons(b,-460)
            
        return [
        self.dB1,self.dB2,self.dB3,self.dB4,
        self.dB5,self.dB6,self.dB7,self.dB8,
        self.dB9,self.dB10,self.dB11,self.dB12,
        self.dB13,self.dB14,self.dB15]

    ## ROUND 1 Balloons
    ## Contains 20 balloons 
    def round2Balloons(self):

        self.dB1 = Balloons(b,100)
        self.dB2 = Balloons(b,60)
        self.dB3 = Balloons(b,20)
        self.dB4 = Balloons(b,-20)
        self.dB5 = Balloons(b,-60)
        self.dB6 = Balloons(b,-100)
        self.dB7 = Balloons(b,-140)
        self.dB8 = Balloons(b,-180)
        self.dB9 = Balloons(b,-220)
        self.dB10 = Balloons(b,-260)
        self.dB11 = Balloons(b,-300)
        self.dB12 = Balloons(b,-340)
        self.dB13 = Balloons(b,-380)
        self.dB14 = Balloons(b,-420)
        self.dB15 = Balloons(b,-460)
        self.dB16 = Balloons(b,-500)
        self.dB17 = Balloons(b,-540)
        self.dB18 = Balloons(b,-580)
        self.dB19 = Balloons(b,-620)
        self.dB20 = Balloons(b,-660)
        self.dB21 = Balloons(b,-700)
        self.dB22 = Balloons(b,-740)
        self.dB23 = Balloons(b,-780)
        self.dB24 = Balloons(b,-820)
        self.dB25 = Balloons(b,-860)
            
        return [
        self.dB1,self.dB2,self.dB3,self.dB4,
        self.dB5,self.dB6,self.dB7,self.dB8,
        self.dB9,self.dB10,self.dB11,self.dB12,
        self.dB13,self.dB14,self.dB15,self.dB16,
        self.dB17,self.dB18,self.dB19,self.dB20,
        self.dB21,self.dB22,self.dB23]

    def changeColor(self,balloon,color):

        pass

        

        
#contains a list of instances (and additional empty list for iteration)
#each instance is a list of instances for the incoming balloons each round
allRounds = [Balloons(b,0).round1Balloons(),Balloons(b,0).round2Balloons()]
                   
#Displays spikes on screen
#User can move spikes (only once) to the balloon path in the map
#Each bundle of spikes pops 6 balloons
class Spikes(pygame.sprite.Sprite):
    #initiallizes all variables, loads spikes images,
    #calls functions to display spikes on screen
    def __init__(self):

        #initiallizing sprite class
        super().__init__()
    
        self.count = 0
        self.spikesDamage = 0
        currentX = 0
        currentY = 0
        self.moving = False
        
        self.spikesImg1 = pygame.image.load('graphics/spikes1.png').convert_alpha()
        self.spikesImg1 = pygame.transform.scale(self.spikesImg1,(55,50))
        
        self.spikesImg2 = pygame.image.load('graphics/spikes2.png').convert_alpha()
        self.spikesImg2 = pygame.transform.scale(self.spikesImg2,(55,50))
        
        self.spikesImg3 = pygame.image.load('graphics/spikes3.png').convert_alpha()
        self.spikesImg3 = pygame.transform.scale(self.spikesImg3,(55,50))

        self.moving = False
        self.placed = False
        self.spikesCord = (80,470)

    #displays spikes images on screen
    def update(self):
        
        #updates image of spikes displayed on screen
        #spikes appear to be less for every two balloons popped
        if self.spikesDamage==0 or self.spikesDamage==1:
            self.image = self.spikesImg1
            self.rect = self.image.get_rect(center=self.spikesCord)
        if self.spikesDamage==2 or self.spikesDamage==3:
            self.image = self.spikesImg2
            self.rect = self.image.get_rect(center=self.spikesCord)
        if self.spikesDamage>=4:
            self.image = self.spikesImg3
            self.rect = self.image.get_rect(center=self.spikesCord)

        #displays spikes on screen if they are still active
        #spikes are active if they've popped less than 6 balloons
        if self.spikesDamage!=6:
            screen.blit(self.image,self.rect)

        if len(spikesGroup)!=3:
            screen.blit((pygame.font.Font(None,30)).render(
            str(4-len(spikesGroup)), False, 'light green'),(73,505))

    #returns true is balloon is colliding with spikes
    #otherwise returns false
    def popBalloon(self,balloon):
        
        if balloon.isColliding(self.rect) and (
            self.spikesDamage<6 and not self.moving):
            self.spikesDamage += 1
            return True

        return False

    # source: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def moveSpikes(self,event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.moving = True
                
        elif event.type == pygame.MOUSEBUTTONUP and self.moving:
            self.moving = False
            self.placed = True
            if len(spikesGroup) < 3:
                spikesGroup.add(Spikes())

        elif event.type == pygame.MOUSEMOTION:
            if self.moving==True and self.placed==False:
                self.spikesCord = event.pos

#Displays character, Bibbo, on screen
#User can drag Bibbo on screen
#Bibbo shoots feather darts to pop balloons
class Bibbo(pygame.sprite.Sprite):

    def __init__(self,cord):

        #initiallizing sprite class
        super().__init__()

        #loading Bibbo image, creating rect for image
        self.default_bird = pygame.image.load('graphics/bibbo.png').convert_alpha()
        self.default_bird = pygame.transform.rotate(self.default_bird, 180)
        self.rect = self.default_bird.get_rect(center=cord)

        #top left of bibbo's range
        self.rangeStr = (self.rect.left-100,self.rect.top-100)
        #bottom right of bibbo's range
        self.rangeFin = (self.rect.right+100,self.rect.bottom+100)
        #middle of bibbo's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)
        

        #bibbo's initial angle rotation is 0
        self.angle = 0

        #initiallizing variables for angle of player
        self.quad = None
        self.angleTaken = False

        #initiallizing variable for shooting status of bibbo
        self.canShoot = True

        #initiallizing variables for tracking time
        self.currentTime = 0
        self.dartTime = 0
        self.counting = True

        #initiallizing variables to move bibbo
        self.moving = False
        self.placed = False

    #if given balloon is colliding with bibbo's range,
    #gets angle bibbo needs to rotate at to face the balloon,
    #also calls function to shoot at balloon
    def getAngleCallShoot(self,balloon,bibbo):

        #saving current balloon's center position
        self.balloonPos = balloon.balloonPos()

        #checks if balloon is colliding with bibbo's range
        if self.balloonPos[0]>self.rangeStr[0] and self.balloonPos[0]<self.rangeFin[0]:
            if self.balloonPos[1]>self.rangeStr[1] and (
                self.balloonPos[1]<self.rangeFin[1]):
                #calculating angle using arc tangent 
                self.diffX = self.rangeMid[0]-self.balloonPos[0]
                self.diffY = self.rangeMid[1]-self.balloonPos[1]
                if self.diffY==0:
                    self.angleTemp = 0
                else: self.angleTemp = abs(math.degrees(math.atan(
                                                self.diffX/self.diffY)))
                #calls functions to change angle according to..
                #quadrant of the balloon collision
                self.checkQuad()
                #if shooting is valid,
                #calls function to shoot a dart at the balloon,
                #saves dart to a group
                if self.canShoot and self.placed:
                    self.dartAngle = self.angle
                    dartGroup.add(bibbo.createDart(balloon,
                            self.dartAngle,self.balloonPos[0],self.balloonPos[1]))

    #changes the angle depending on which quadrant...
    #..the balloon is colliding with bibbo's range
    def checkQuad(self):

        quad00 = self.rangeStr
        quad01 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeStr[1])
        quad02 = (self.rangeFin[0],self.rangeStr[1])

        quad10 = (self.rangeStr[0],(self.rangeStr[1]+self.rangeFin[1])//2)
        quad11 = ((self.rangeStr[0]+self.rangeFin[0])//2,
                  (self.rangeStr[1]+self.rangeFin[1])//2)
        quad12 = (self.rangeFin[0],(self.rangeStr[1]+self.rangeFin[1])//2)

        quad20 = (self.rangeStr[0],self.rangeFin[1])
        quad21 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeFin[1])
        quad22 = self.rangeFin

        #hold balloon's center position
        x = self.balloonPos[0]
        y = self.balloonPos[1]

        if y>quad00[1] and y<quad10[1]:
            #quad 1
            if x>quad01[0] and x<quad02[0]:
                self.quad = 1
                self.angle = -self.angleTemp

            #quad 2
            elif x>quad00[0] and x<quad01[0]:
                self.quad = 2
                self.angle = self.angleTemp

        elif y>quad10[1] and y<quad20[1]:

            #quad 3
            if x>quad00[0] and x<quad01[0]:
                self.quad = 3
                self.angle = 180 - self.angleTemp

            #quad 4
            elif x>quad01[0] and x<quad02[0]:
                self.quad = 4
                self.angle = 180 + self.angleTemp

    # source: https://www.youtube.com/watch?v=_TU6BEyBieE
    #diplays image of bibbo on screen
    #and rotates according to balloon collisions
    #and updates bibbo's range
    def blitRotateUpdateRange(self):

        #top left of bibbo's range
        self.rangeStr = (self.rect.left-100,self.rect.top-100)
        #bottom right of bibbo's range
        self.rangeFin = (self.rect.right+100,self.rect.bottom+100)
        #middle of bibbo's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)

        if not self.moving:
            self.img = pygame.transform.rotate(self.default_bird,self.angle)
                
        screen.blit(self.img,(self.rect.centerx-int(self.img.get_width()/2),
                              self.rect.centery-int(self.img.get_height()/2)))
        if currentMoney>=200:
            color = "light green"
        else: color = "red"
        screen.blit((pygame.font.Font(None,25)).render(
        '$200', False, color),(59,395))

    #creates a dart that shoots at given balloon at given angle
    def createDart(self,balloon,angle,balloonX,balloonY):

        self.canShoot = False

        return Darts(angle,self.quad,balloon,self.rangeMid[0],self.rangeMid[1],
                        balloonX,balloonY)

    #restricts bibbo to only shoot one dart per second
    def updateDartTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.canShoot == False and self.counting == True:
            self.counting = False
            self.dartTime = pygame.time.get_ticks()

        elif self.currentTime - self.dartTime > 1000:
            self.counting = True
            self.canShoot = True

    # source: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def moveBibbo(self,event):
        global currentMoney
        
        if event.type == pygame.MOUSEBUTTONDOWN and currentMoney>=200:
            if self.rect.collidepoint(event.pos):
                self.moving = True
                
        elif event.type == pygame.MOUSEBUTTONUP and self.moving:##and event.pos isnt colliding with bin
            if not self.placed:
                currentMoney -= 200
            self.placed = True
            self.moving = False
            bibboGroup.add(Bibbo((80,360)))

        elif event.type == pygame.MOUSEMOTION:
            if self.moving==True and self.placed==False:
                self.rect.center = event.pos

class Polly(pygame.sprite.Sprite):
    def __init__(self):
    
        #initiallizing sprite class
        super().__init__()

        self.image = pygame.image.load('polly.png').convert_alpha()
        self.rect = self.image.get_rect(center=(78,263))

        #top left of polly's range
        self.rangeStr = (self.rect.left-50,self.rect.top-50)
        #bottom right of polly's range
        self.rangeFin = (self.rect.right+50,self.rect.bottom+50)
        #middle of polly's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)

        #initiallizing variable for shooting status of polly
        self.canShoot = True

        #initiallizing variables for tracking time
        self.currentTime = 0
        self.dartTime = 0
        self.counting = True

        #initiallizing variables to move polly
        self.moving = False
        self.placed = False

    def blitUpdateRange(self):

        #top left of polly's range
        self.rangeStr = (self.rect.left-50,self.rect.top-50)
        #bottom right of polly's range
        self.rangeFin = (self.rect.right+50,self.rect.bottom+50)
        #middle of polly's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)

        screen.blit(self.image,(self.rect.centerx-int(self.image.get_width()/2),
                              self.rect.centery-int(self.image.get_height()/2)))
        if currentMoney>=100:
            color = "light green"
        else: color = "red"
        screen.blit((pygame.font.Font(None,25)).render(
        '$100', False, color),(59,297))

    def callShoot(self,balloon):

        #saving current balloon's center position
        self.balloonPos = balloon.balloonPos()

        #checks if balloon is colliding with bibbo's range
        if self.balloonPos[0]>self.rangeStr[0] and self.balloonPos[0]<self.rangeFin[0]:
            if self.balloonPos[1]>self.rangeStr[1] and (
                self.balloonPos[1]<self.rangeFin[1]):
                if self.canShoot and not self.moving:
                    self.canShoot = False
                    self.allSides = [(0,-1),(0,1),(1,0),(-1,0),
                                     (1,1),(-1,-1),(1,-1),(-1,1)]
                    for increase in self.allSides:
                        pollenGroup.add(Pollen(balloon,self.rect.center,increase))

    #restricts polly to only one pollen attack per second
    def updatePollenTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.canShoot == False and self.counting == True:
            self.counting = False
            self.dartTime = pygame.time.get_ticks()

        elif self.currentTime - self.dartTime > 1000:
            self.counting = True
            self.canShoot = True
        
    # source: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def movePolly(self,event):
        global currentMoney
        
        if event.type == pygame.MOUSEBUTTONDOWN and currentMoney>=100:
            if self.rect.collidepoint(event.pos):
                self.moving = True
                
        elif event.type == pygame.MOUSEBUTTONUP and self.moving:##and event.pos isnt colliding with bin
            if not self.placed:
                currentMoney -= 100
            self.placed = True
            self.moving = False
            pollyGroup.add(Polly())

        elif event.type == pygame.MOUSEMOTION:
            if self.moving==True and self.placed==False:
                self.rect.center = event.pos


class Pollen(pygame.sprite.Sprite):
    def __init__(self,balloon,cord,incXY):
    
        #initiallizing sprite class
        super().__init__()

        self.image = pygame.image.load('graphics/pollen.png').convert_alpha()
        self.rect = self.image.get_rect(center=cord)

        self.incX = incXY[0]
        self.incY = incXY[1]

        self.numPopped = 0
        self.distance = 0

    def update(self):

        self.distance += 1
        self.rect.centerx += self.incX
        self.rect.centery += self.incY

        if self.distance>50:
            self.kill()

    #kills pollen if it has popped 1 balloon
    #returns True if balloon collides with pollen
    #otherwise returns False
    def popBalloon(self,balloon):

        if balloon.isColliding(self.rect) and self.numPopped<1:
            self.numPopped += 1
            return True

        if self.numPopped >= 1:
            self.kill()

        return False
        
        

#Creates a dart that shoots at given balloon
#Dart pops balloons at collision
class Darts(pygame.sprite.Sprite):
    def __init__(self,angle,quad,balloon,x1,y1,x2,y2):
        
        #initiallizing sprite class
        super().__init__()

        #loading images and change angle according to direction of balloon
        self.feather_dart = pygame.image.load('graphics/feather.png').convert_alpha()
        self.feather_dart = pygame.transform.rotate(self.feather_dart, 180)

        #self.angle = math.degrees(math.atan((y2-y1)/(x2-x1)))
        self.image = pygame.transform.rotate(self.feather_dart, angle)

        #initiallizing variables that hold dart and balloon position
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        #initiallizing variables for dart angle and position
        self.quad = quad
        
        if x2-x1 != 0:
            self.m = abs((y2-y1)/(x2-x1))
            
        else: self.m = 0

        #initializing variable to track number of balloons dart pops
        self.numPopped = 0

        #making a rect of the dart
        self.rect = self.image.get_rect(center=(self.x1,self.y1))

    #updates position of dart
    def update(self):
        
        if self.quad == 1:
            if round(self.m)==0:
                self.rect.y -= 0
                self.rect.x += 5
            else:
                self.rect.y -= 5
                self.rect.x += 5*self.m
        if self.quad == 2:
            if round(self.m)==0:
                self.rect.y -= 0
                self.rect.x -= 5
            else:
                self.rect.y -= 5
                self.rect.x -= 5*self.m
        if self.quad == 3:
            if round(self.m)==0:
                self.rect.y += 0
                self.rect.x -= 5
            else:
                self.rect.y += 5
                self.rect.x -= 5*self.m
        if self.quad == 4:
            if round(self.m)==0:
                self.rect.y += 0
                self.rect.x += 5
            else:
                self.rect.y += 5
                self.rect.x += 5*self.m

        #kills dart if it passes the map borders
        if self.rect.x>1000 or self.rect.y>1000:
            self.kill()

    #kills dart if it has popped 2 balloons
    #returns True if balloon collides with dart
    #otherwise returns False
    def popBalloon(self,balloon):

        if balloon.isColliding(self.rect) and self.numPopped<2:
            self.numPopped += 1
            return True

        if self.numPopped >= 2:
            self.kill()

        return False

#displays balloons of each round
#returns current round number and instance in a tuple
def displayBalloonRounds(currentTime):

    currentRound = (0,None)

    #displays round 1 balloons
    if currentTime>2 and currentTime<38:
        currentRound = (1,allRounds[0])
        for balloon in currentRound[1]:
            balloon.round1()

    #displays round 2 balloons
    if currentTime>=30:
        currentRound = (2,allRounds[1])
        for balloon in currentRound[1]:
            balloon.round2()

    return currentRound


#creates spikes group for Spikes instance
spikesGroup = pygame.sprite.Group()
spikesGroup.add(Spikes())

#creates a player group for Bibbo instance
bibboGroup = pygame.sprite.Group()
bibboGroup.add(Bibbo((80,360)))

#creates dart group
dartGroup = pygame.sprite.Group()

#creates a player group for Polly instance
pollyGroup = pygame.sprite.Group()
pollyGroup.add(Polly())

#creates group for polly's pollen attacks
pollenGroup = pygame.sprite.Group()

updateMoneyTime = 0




# displays everything on game window
def drawPlayWindow():    
    global healthBar,currentMoney,updateMoneyTime
    
    screen.blit(test_surface,(0,0)) #displays map
    currentTime = pygame.time.get_ticks() #tracks time in seconds

    if currentTime - updateMoneyTime > 20000:
        updateMoneyTime = pygame.time.get_ticks()
        currentMoney += 50

    #gets current round number and
    #list of instances of balloons in current round
    roundIns = displayBalloonRounds(currentTime//1000)
    roundNum = roundIns[0]
    currentRound = roundIns[1]

    dartGroup.draw(screen) #displays darts
    dartGroup.update() #updates darts' positions
        
    screen.blit(game_bar,(0,0)) #displays game bar on left

    spikesGroup.update() #updates spikes bundle image

    for bibbo in bibboGroup:
        #updates frequency at which bibbo can shoot darts
        bibbo.updateDartTime() 
        bibbo.blitRotateUpdateRange() #rotates bibbo to face balloons

    for polly in pollyGroup:
        polly.blitUpdateRange()
        polly.updatePollenTime()

    pollenGroup.draw(screen)
    pollenGroup.update()

    #checks if rounds started
    #calls functions to pop balloons or not
    if currentRound != None:

        for balloon in currentRound:
            
            for bibbo in bibboGroup:
                bibbo.getAngleCallShoot(balloon,bibbo)

            for spikes in spikesGroup:
                if spikes.popBalloon(balloon):
                    if balloon in currentRound:
                        currentRound.remove(balloon)
                        screen.blit(pop,balloon)
                    
            for dart in dartGroup:
                if dart.popBalloon(balloon):
                    if balloon in currentRound:
                        currentRound.remove(balloon)
                        screen.blit(pop,balloon)

            for polly in pollyGroup:
                polly.callShoot(balloon)

            for pollen in pollenGroup:
                if pollen.popBalloon(balloon):
                    if balloon in currentRound:
                        currentRound.remove(balloon)
                        screen.blit(pop,balloon)

        for balloon in currentRound:
            #removes balloon from current round if it passes map border
            #also decreases health by one
            if balloon.checkPassing():
                if balloon in currentRound:
                    currentRound.remove(balloon)
                    healthBar -= 1 

    #displays current health of player
    screen.blit((pygame.font.Font(None,30)).render(
        'HEALTH: '+ str(healthBar), False, 'white'),(20,55))
    #displays current round number
    screen.blit((pygame.font.Font(None,30)).render(
        'ROUND: '+ str(roundNum), False, 'white'),(20,30))
    #displays current money
    screen.blit((pygame.font.Font(None,30)).render(
        'Bank: $'+ str(currentMoney), False, 'white'),(20,80))

#displays GAME OVER window
def gameOverWind():

    screen.blit(test_surface,(0,0)) #display map

    #displays words 'GAME OVER'
    screen.blit((pygame.font.Font(None,150)).render('GAME OVER',
                                                    False, 'red'),(200,300))

    #displays words 'click to start over'
    screen.blit((pygame.font.Font(None,50)).render('click to start over',
                                                    False, 'red'),(400,400))
    
#stores main loop of game
def main():
    global healthBar

    #infinite while loop 
    while True:
        #checking all events
        for event in pygame.event.get():

            #if players quits game, exit program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #if player clicks on screen in game over window,
            #health is restored
            if event.type == pygame.MOUSEBUTTONDOWN and healthBar == 0:
                healthBar = 20

            for bibbo in bibboGroup:
                bibbo.moveBibbo(event)

            for spikes in spikesGroup:
                spikes.moveSpikes(event)

            for polly in pollyGroup:
                polly.movePolly(event)

        #if player hasn't ran out of health, display game window
        if healthBar > 0:
            drawPlayWindow()

        #if player ran out of health, display game over window
        else:
            gameOverWind()

        #updates display every loop        
        pygame.display.update()
        clock.tick(60) #makes while loop run 60 times per second

#calling main loop
main()







    

