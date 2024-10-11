# Example file showing a basic pygame "game loop"
import pygame # importa a biblioteca pygame para script

# pygame setup configuração
pygame.init() # inicio do jogo
pygame.font.init() # Inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((500, 500)) # modo de configuração do jogo
pygame.display.set_caption('Jogo da Velha') # definir legenda do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100) # Importa fonte
running = True # A variável booleana que pode acompanhar uma chamada
personagem_X = fonte_quadrinhos.render('X', True, 'Black')
personagem_Y = fonte_quadrinhos.render('O', True, 'Black')
cor_fundo = 1
while running:
    # poll for events
       # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')   
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1 
        
    if cor_fundo == 1:
       screen.fill('blue') 
       screen.blit(personagem_X,(250,250))
    elif cor_fundo == 2:
        screen.fill('Blue') 
        screen.blit(personagem_Y,(225,225))
   
    else:
        screen.fill('purple')
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 