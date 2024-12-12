import pygame

pygame.init()
pygame.display.set_caption("rocket game by victor")
width = 800
height = 600
screen = pygame.display.set_mode((width,height))


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("game dev 2/rocketgame/rocket.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self,press_key):
        if press_key[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if press_key[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if press_key[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if press_key[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)

sprites = pygame.sprite.Group()
def start_game():
    player1 = Player(50,100)
    player2=Player(200,100)

    sprites.add(player1)
    sprites.add(player2)

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
        
        press_key = pygame.key.get_pressed()
        player1.update(press_key)
        player2.update(press_key)


        screen.blit(pygame.image.load("game dev 2/rocketgame/background.png"),(0,0))
        sprites.draw(screen)
    
        pygame.display.update()


start_game()
