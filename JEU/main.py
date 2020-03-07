import pygame
spygame.init()

#générer la fenetre du jeu
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))

running = True
# fond d'écran
backgroud = pygame.image.load('assets/bg.jpg')

#charger notre jeu
game = Game()
#boucle tant que "running" est vrai
while running:
    #appliquer l'arriere plan de notre jeu
    screen.blit(backgroud, (0, -200))
    #apliquer l'image de notre player
    screen.blit(game.player.image, game.player.rect)
    #verfier si le player souhaite allez à droite ou à gauche"
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game .pressed.get(pygame.K_LEFT) and game.player.rect.x > 0 :
        game.player.move_left()

    print(game.player.rect.x)
    #mettre a jour l'écran
    pygame.display.flip()
    # si le player ferme la fenetre
    for event in pygame.event.get():
        #si l'event est fermeture de la
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT
            print("Fermeture du jeu")
        #quand le player IRL lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] =  True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] =  False