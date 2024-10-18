# Example file showing a basic pygame "game loop"
import pygame # importa a biblioteca pygame para script

# pygame setup configuração
pygame.init() # inicio do jogo
pygame.font.init() # Inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) # modo de configuração do jogo
pygame.display.set_caption('Jogo da Velha') # definir legenda do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100) # Importa fonte
running = True # A variável booleana que pode acompanhar uma chamada
personagem_X = fonte_quadrinhos.render('X', True, 'Red') # Criar personagem X
personagem_Y = fonte_quadrinhos.render('O', True, 'Red') # Criar personagem Y
cor_fundo = 1 # Cor do fundo do cenário
while running:
    # poll for events (começo do evento)
       # pygame.QUIT event means the user clicked X to close your window
       # Evento pygame.QUIT significa que o usuário clicou no X para fechar sua janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')   
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1 
        
    
        
        screen.blit(personagem_Y,(225,225))
    # Desenhar Tabuleiro    
    # Linhas Verticais
    #                                  origem        destino
    #                                    (x   y)    (y     x)
        pygame.draw.line(screen, 'white',(200, 0), (200, 600), 5) 
        pygame.draw.line(screen, 'white',(400, 0), (400, 600), 5)
    # Linhas Horizontais
        pygame.draw.line(screen, 'white',(0, 200), (600, 200), 5)
        pygame.draw.line(screen, 'white',(0, 400), (600, 400), 5)

   #
    screen.blit(personagem_X,(60,30))
    screen.blit(personagem_Y,(260,30))
    screen.blit(personagem_Y,(460,30))
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 