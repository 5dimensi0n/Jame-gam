def game():
    import pygame
    from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT, K_LSHIFT
    import random


    pygame.init()

    counter, text = 5, '5'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    viruses = ['Mycoplasma.png', 'secco.png', 'Mimivirus.png']
    all_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enemyIndex = 0

    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y, mass):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load('macrophage.png'), (mass, mass))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
            self.accel = 2
            self.maxspeed = 20
            self.friction = 0.9
            self.speedX = 0
            self.speedY = 0
            self.mass = mass
            self.index = 0

        def update(self, keys_pressed, mass, ):
            if keys_pressed[K_LEFT] and self.rect.left > 0:
                self.speedX -= self.accel
        
            if keys_pressed[K_RIGHT] and self.rect.right < 500:
                self.speedX += self.accel
            
            if keys_pressed[K_UP] and self.rect.top > 0:
                self.speedY-= self.accel
            if keys_pressed[K_DOWN] and self.rect.bottom < 500:
                self.speedY += self.accel

            self.speedX *= self.friction
            self.speedY *= self.friction

            if self.speedX > self.maxspeed:
                self.speedX = self.maxspeed
            elif self.speedX < -self.maxspeed:
                self.speedX = -self.maxspeed

            self.rect.x += self.speedX
            self.rect.y += self.speedY

            self.rect.width = mass
            self.rect.height = mass

            self.image = pygame.transform.scale(pygame.image.load('macrophage.png'), (mass, mass))

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y, mass, sprites, index):
            super().__init__()
            self.mass = mass
            self.image = pygame.transform.scale(pygame.image.load(sprites[0]), (mass, mass))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.index = index

        def reset_pos(self):
            enemy = Enemy(-10 ,random.randint(0, 600),random.randint(playermass-50, playermass+50),viruses,enemyIndex )
                            
            all_group.add(enemy)
            enemies.add(enemy)
            self.kill()

        def Update(self, sprites):
            self.rect.x += 2
            if self.rect.x > 610:
                self.reset_pos()
            self.image = pygame.transform.scale(pygame.image.load(sprites[self.index]), (self.mass, self.mass))
            
    playermass = 50
    player = Player(10, 10, playermass)

    playerAlive = True

    for i in range(15):
        enemy = Enemy(random.randint(0, 600),random.randint(0, 600),random.randint(playermass-50, playermass+5),viruses,enemyIndex)
        
        all_group.add(enemy)
        enemies.add(enemy)

    all_group.add(player)

    def colCheck(player, enemies):
        nonlocal playermass
        collision_sprites = pygame.sprite.spritecollide(player, enemies, False)
        for sprite in collision_sprites:
            if playermass > sprite.mass:
                
                sprite.reset_pos()
                playermass += 10
                player.image = pygame.transform.scale(player.image, (playermass, playermass))
            else:
                pass

    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('thing')

    run = True
    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'boom!'
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        
        player.update(keys_pressed, playermass)
        for enemy in enemies:
            enemy.Update(viruses)
        if counter < 1:
            colCheck(player, enemies)
        if not enemies:
            for i in range(15):
                enemy = Enemy(random.randint(0, 600),random.randint(0, 600),random.randint(playermass-50, playermass+5),viruses,enemyIndex)
                
                all_group.add(enemy)
                enemies.add(enemy)
            

        match playermass:
            case n if n < 200:
                pass
            case n if n > 200:
                counter = 5
                playermass = 50
                for enemy in enemies:
                    enemies.remove(enemy)
                    all_group.remove(enemy)
                enemyIndex += 1

        window.fill((45,39,50))
        all_group.draw(window) 
        window.blit(font.render(text, True, (0, 0, 0)), (32, 48))

        pygame.display.update()
    pygame.quit()
