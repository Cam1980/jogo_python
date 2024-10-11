# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da Velha')
clock = pygame.time.Clock()
running = True
cor_fundo = 1 # 1:Azul, 2: Vermelho, 3: Amarelo, 4: rosa, 5: roxo


while running:
    # poll for events
       # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')   
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 4):
                cor_fundo = 1 
        
    if cor_fundo == 1:
        screen.fill('blue') 
    elif cor_fundo == 2:
        screen.fill('red') 
    elif cor_fundo == 3:
        screen.fill('yellow')
    elif cor_fundo == 4:
        screen.fill('pink')

    else:
        screen.fill('purple')
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 