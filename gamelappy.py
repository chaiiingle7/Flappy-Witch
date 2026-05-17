import pygame
import sys



pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('music/bgmusic.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


screen=pygame.display .set_mode((1000,500))
clock=pygame.time.Clock()
pygame.display.set_caption("Flappy Witch")

mousepos=pygame.mouse.get_pos()
mx,my=mousepos

cursor1=pygame.image.load('char/cursor.png').convert_alpha()
cursor2=pygame.transform.scale(cursor1, (20,30))
cursor=cursor2.get_rect(topleft=(mx,my))

background1=pygame.image.load('char/final.png')
background2=pygame.transform.scale(background1,(3000,500))
background=background2.get_rect(topleft=(0,0))

witch1=pygame.image.load('char/witch.png').convert_alpha()
witch2=pygame.transform.scale(witch1, (55,55))
witch=witch2.get_rect(topleft=(100,350))

pillarup=pygame.image.load('char/uppipe.png').convert_alpha()
pillarup1=pygame.transform.scale(pillarup, (30,300))


pillarupp=pillarup1.get_rect(topleft=(500,310))
pillarupp2=pillarup1.get_rect(topleft=(250,350))
pillarupp3=pillarup1.get_rect(topleft=(730,300))
pillarupp4=pillarup1.get_rect(topleft=(970,400))

pillardown=pygame.image.load('char/downpipe.png').convert_alpha()
pillardown1=pygame.transform.scale(pillardown, (30,300))

pillardownn=pillardown1.get_rect(topleft=(100,0))
pillardownn2=pillardown1.get_rect(topleft=(350,-50))
pillardownn3=pillardown1.get_rect(topleft=(900,0))
pillardownn4=pillardown1.get_rect(topleft=(600,-110))

font=pygame.font.Font('font/yoster.ttf', 20)
font1=pygame.font.Font('font/yoster.ttf', 50)
font3=pygame.font.Font('font/yoster.ttf', 20)


color_not='aquamarine4'
color_umm='olivedrab4'
color_yes='chartreuse4'
hii=pygame.Rect(900,450,70,30)
mousepos=pygame.mouse.get_pos()
color=color_umm if hii.collidepoint(mousepos) else color_not


lose=100
start=False
run=True

color_not='darkgreen'
color_umm='darkolivegreen'
color_yes='chartreuse4'

mes=font1.render("Game Ended", False, 'white')


while run:

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
            if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
                if hii.collidepoint(mousepos):
                    color=color_yes
                    pygame.draw.rect(screen, color, hii, border_radius=8)
                    text_surf = font.render("exited", False, 'WHITE')
                    text_rect = text_surf.get_rect(center=hii.center)
                    screen.blit(text_surf, text_rect)
                    screen.blit(mes, (470, 240))
                    pygame.time.wait(1000)
                    pygame.quit()
                    sys.exit() 

    background.right-=1
    if background.right<=1000:
        background.left=0
    screen.blit(background2, background)
    mousepos=pygame.mouse.get_pos()
    mx,my=mousepos

    pygame.mouse.set_visible(False)
    cursor=cursor2.get_rect(topleft=(mx,my))

    
    mes=font1.render("Welcome! Let's save the Witch!", False, 'white') 
    sec=pygame.time.get_ticks()


    if not start:

        screen.blit(mes, (100, 150))
  
        sec1=3- (int(sec/1000))/2
        seconds=font1.render(f'{int(sec1)}', False, 'white')
        screen.blit(seconds, (450,250))
        pygame.display.update()
        
        pygame.time.wait(2000)
        
        if sec1<=1:
         
            start=True
            pygame.display.update()

    else:

        mousepos=pygame.mouse.get_pos()
        color=color_umm if hii.collidepoint(mousepos) else color_not
        pygame.draw.rect(screen, color, hii, border_radius=8)
        text_surf = font.render("exit", False, 'WHITE')
        text_rect = text_surf.get_rect(center=hii.center)
        screen.blit(text_surf, text_rect)

         

        #witch
        witch.left+=2
        if witch.left>=1000:
            witch.left=-witch.width
            # witch.top=350
        screen.blit(witch2, witch)

        pillars = [pillarupp, pillarupp2, pillarupp3, pillarupp4,
                pillardownn, pillardownn2, pillardownn3, pillardownn4]


        for p in pillars[0:4]:
            p.left-=1.4
            if p.right==0:
                p.left=1000
            screen.blit(pillarup1, p)

        for p in pillars[4:8]:
            p.left-=1.4
            if p.right==0:
                p.left=1000
            screen.blit(pillardown1, p)

    
        screen.blit(cursor2, cursor)

        key=pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            witch.centery-=2
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            witch.centery+=1.5
        

        
        if any(witch.colliderect(p) for p in pillars):
            # for p in pillars:
            #     p.centerx+=1
            witch.centerx-=0.4
        #     score-=0
            lose-=0.1


        
        name=font.render(f"Save the Witch!", False, 'darkslategray')
        screen.blit(name, (430, 15))


        message2=font.render(f"Score Countdown: {int(lose)}", False, 'darkslategray')
        screen.blit(message2, (100, 20))
            

        secs= int(pygame.time.get_ticks()/1000)
    

        secs1=font3.render(f"Seconds: {secs}", False, 'darkslategray')
        screen.blit(secs1, (800,15))


        if lose<=0:
                message1=font1.render("Game Over!", False, 'white')
                screen.blit(message1, (370, 240))
                pygame.display.update()
                pygame.time.wait(2000)
                run = False


        pygame.display.update()
        clock.tick(60)


pygame.quit()
