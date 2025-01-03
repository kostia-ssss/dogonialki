import pygame
pygame.init()

FPS = 60
clock = pygame.time.Clock()

wind_w, wind_h = 700, 500
window = pygame.display.set_mode((wind_w , wind_h))
pygame.display.set_caption("ДОГОНЯЛКИ")

background = pygame.image.load("images/bg.jfif")
background = pygame.transform.scale(background, (wind_w , wind_h))

pygame.mixer.music.load("sound.mp3")
pygame.mixer.music.play(-1)

class Player:
    def __init__(self , x , y , img , w , h):
        self.img = img
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(self.img , (w, h))
    
    def draw(self):
        window.blit(self.img , (self.rect.x, self.rect.y))
    
    def move_on_letters(self , speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= speed
            if self.rect.y < 0:
                self.rect.y += speed
        if keys[pygame.K_s]:
            self.rect.y += speed
            if self.rect.y > 400:
                self.rect.y -= speed
        if keys[pygame.K_a]:
            self.rect.x -= speed
            if self.rect.x < 0:
                self.rect.x += speed
        if keys[pygame.K_d]:
            self.rect.x += speed
            if self.rect.x > 600:
                self.rect.x -= speed
        
    def move_on_arrows(self , speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= speed
            if self.rect.y < 0:
                self.rect.y += speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed
            if self.rect.y > 400:
                self.rect.y -= speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
            if self.rect.x < 0:
                self.rect.x += speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
            if self.rect.x > 600:
                self.rect.x -= speed

player1_img = pygame.image.load("images/steve.png")
player1 = Player(20 , 250 , player1_img , 90 , 100)
player2_img = pygame.image.load("images/zombie.png")
player2 = Player(580 , 250 , player2_img , 90 , 100)

game = True
while game:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player1.draw()
    player1.move_on_letters(6)

    player2.draw()
    player2.move_on_arrows(5)
    
    pygame.display.update()
    clock.tick(FPS)
    