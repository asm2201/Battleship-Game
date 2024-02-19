import pygame
import math
import random
from pygame import mixer #helps handle sound effects in gui

# intialise pygame 
pygame.init()
screen =  pygame.display.set_mode((800, 600)) #width, height

# adding title and icon to pygame window
pygame.display.set_caption("Battleship")
# icon download attribution 
# <a href="https://www.flaticon.com/free-icons/spaceship" title="spaceship icons">Spaceship icons created by Skyclick - Flaticon</a>
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# add background
backgroundImg = pygame.image.load("background.jpg")
backgroundImg = pygame.transform.scale(backgroundImg, (800,600))

mixer.music.load("background.wav")
mixer.music.play(-1) #plays the bgm on loop

# add player image 
playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (64,64))
playerX = 370 # little less than half of 800
playerY = 480 # little above the screen
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y)) #to draw the image in the window

# score value / Game over font
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 35
def shows_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = over_font.render("Game Over", True, (255,255,255))
    screen.blit(over_text, (220,250))


# add player image 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    ufo_img = pygame.image.load("ufo.png")
    ufo_img = pygame.transform.scale(ufo_img, (64,64))
    enemyImg.append(ufo_img)

    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150)) # little less than half of 800

    enemyX_change.append(1)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y)) #to draw the image in the window

# add bullet image 
bulletImg = pygame.image.load("bullet.png")
bulletImg = pygame.transform.scale(bulletImg, (32,32))
bulletX = 0 
bulletY = 480 # little above the screen
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready" #when ready bullet won't be visible
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10)) #to draw the image in the window at the center of the spaceship

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    else:
        return False



# 1. adding quit functionality
# 2. add anything that should appear on screen in isRunning loop

isRunning = True
while isRunning:

    screen.fill((0,0,0))
    screen.blit(backgroundImg, (0,0))

    # pygame.event.get() fetches all the events that took place in pygame window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN: #KEYDOWN IS PRESSING A KEY
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    
    playerX += playerX_change #checking for boundaries of spceship
    if (playerX < 0):
        playerX = 0
    elif playerX >= 736:  # 800-64 pixels
        playerX = 736

    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]  #checking for boundaries of ufo
        if (enemyX[i] < 0):
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:  # 800-64 pixels
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]
         # collision detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision :
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0, 735) # enemy gets respawned again at a new location
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    shows_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update() # to make sure that display gets updated after every action