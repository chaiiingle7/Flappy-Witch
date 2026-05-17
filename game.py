import pygame
import os


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('music/bgmusic.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


screen=pygame.display .set_mode((1000,500))
clock=pygame.time.Clock()
pygame.display.set_caption("Flappy Witch")

background1=pygame.image.load('char/graveyard.jpeg').convert()
background=pygame.transform.scale(background1,(1000,500))

witch1=pygame.image.load('char/witch.png').convert_alpha()
witch2=pygame.transform.scale(witch1, (80,80))
witch=witch2.get_rect(topleft=(100,250))

pillarup=pygame.image.load('char/uppipe.png').convert_alpha()
pillarup1=pygame.transform.scale(pillarup, (40,300))


pillarupp=pillarup1.get_rect(topleft=(500,310))
pillarupp2=pillarup1.get_rect(topleft=(250,350))
pillarupp3=pillarup1.get_rect(topleft=(730,300))
pillarupp4=pillarup1.get_rect(topleft=(970,400))

pillardown=pygame.image.load('char/downpipe.png').convert_alpha()
pillardown1=pygame.transform.scale(pillardown, (40,300))

pillardownn=pillardown1.get_rect(topleft=(100,0))
pillardownn2=pillardown1.get_rect(topleft=(350,-50))
pillardownn3=pillardown1.get_rect(topleft=(900,0))
pillardownn4=pillardown1.get_rect(topleft=(600,-110))

font=pygame.font.Font('font/yoster.ttf', 20)
score=0





run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.blit(background, (0,0))

    #witch
    witch.left+=1.1
    if witch.left==1000:
        witch.right=0
    screen.blit(witch2, witch)


    pillarupp.left-=1
    if pillarupp.right==0:
        pillarupp.left=1000
    screen.blit(pillarup1, pillarupp)

    pillarupp2.left-=1
    if pillarupp2.right==0:
        pillarupp2.left=1000
    screen.blit(pillarup1, pillarupp2)

    pillarupp3.left-=1
    if pillarupp3.right==0:
        pillarupp3.left=1000
    screen.blit(pillarup1, pillarupp3)

    pillarupp4.left-=1
    if pillarupp4.right==0:
        pillarupp4.left=1000
    screen.blit(pillarup1, pillarupp4)


    pillardownn.left-=1
    if pillardownn.right==0:
        pillardownn.left=1000
    screen.blit(pillardown1, pillardownn)

    pillardownn2.left-=1
    if pillardownn2.right==0:
        pillardownn2.left=1000
    screen.blit(pillardown1, pillardownn2)


    pillardownn3.left-=1
    if pillardownn3.right==0:
        pillardownn3.left=1000
    screen.blit(pillardown1, pillardownn3)


    pillardownn4.left-=1
    if pillardownn4.right==0:
        pillardownn4.left=1000
    screen.blit(pillardown1, pillardownn4)

    mousepos=pygame.mouse.get_pos()

    if witch.collidepoint(mousepos):
        mx,my=mousepos
        witch.centery=my
   
    pillars = [pillarupp, pillarupp2, pillarupp3, pillarupp4,
               pillardownn, pillardownn2, pillardownn3, pillardownn4]
    
    if any(witch.colliderect(p) for p in pillars):

        score-=0


    if any (witch.centery-p.centery<=30 and witch.centery-p.centery>=0 and not witch.colliderect(p) for p in pillars): 
        score+=1



           
    name=font.render(f"Score: {score}", False, 'black')
    screen.blit(name, (450, 15))



    pygame.display.update()
    clock.tick(60)


pygame.quit()
