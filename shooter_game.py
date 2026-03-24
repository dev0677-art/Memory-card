from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 70)


window = display.set_mode((700, 500))
display.set_caption('pygame window')
background = transform.scale(image.load('galaxy.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,saiz_x,saiz_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (saiz_x, saiz_y))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 700 - 80)
            self.rect.y = 0
            lost = lost + 1
    

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 700 - 80)
            self.rect.y = 0


            

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        
        
        

            
    


        
    

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < (700 - 80):
            self.rect.x += self.speed
    def fire(self):
        bullets = Bullet('bullet.png',ship.rect.x, ship.rect.y, 2, 45, 20)
        bullet.add(bullets)
        






    


answer = 0
ticks = 0
ship = Player('rocket.png',300, 350, 7, 55, 65)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mone = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60
max_bullets = 5
num_fire = 0
finish = False
reload = False

monsters = sprite.Group()
for i in range(1,5):
    monster = Enemy('ufo.png', randint(80, 700), -40, randint(1,3), 105, 65)
    monsters.add(monster)
bullet = sprite.Group()

asteroids = sprite.Group()
for i in range(1,3):
    asteroid = Asteroid('asteroid.png', randint(80,700), -40, randint(1,3), 105, 65)
    asteroids.add(asteroid)
    
win = font2.render('You Win!', True, (255,255,0))
lose = font2.render('You Lose!', False,(180,0,0))

game = True
while game:
    clock.tick(FPS)
    if reload == True:
        ticks += 1
    if ticks%(FPS*3)==0 and reload == True:
        reload=False
        num_fire = 0
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullets = Bullet('bullet.png',ship.rect.x, ship.rect.y, 2, 45, 20)
                bullet.add(bullets)
                if num_fire < max_bullets and reload == False:
                    mone.play()
                    ship.fire()
                    num_fire += 1
                if num_fire >= max_bullets and reload == False:
                    reload == True
                    mone.play()

        
    if finish != True:
        if sprite.groupcollide(monsters, bullet, True, True):
            answer += 1
            monster = Enemy('ufo.png', randint(80, 700), -40, randint(1,3), 65, 65)
            monsters.add(monster)
        window.blit(background,(0,0))
        if answer == 10:
            finish = True
            window.blit(win,(200, 200))
        if sprite.spritecollide(ship, monsters, True):
            finish = True
            window.blit(lose,(200,200))
        if lost == 3:
            finish = True
            window.blit(lose,(200,200))
            
            
        

        
    
        

        text = font1.render('Счет:' + str(answer), 1, (255,255,255))
        mender = font1.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        
   
    
        
        window.blit(text,(10, 20))
        window.blit(mender, (10, 50))
        ship.reset()
        monsters.update()
        asteroids.update()
    
        ship.update()

        monsters.draw(window)
        asteroids.draw(window)
    
    





    
            

        bullet.update()
        bullet.draw(window)
    
                
        clock.tick(FPS)
        display.update()
