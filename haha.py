import pygame
import sys

screen=pygame.display.set_mode((1000,500))
clock=pygame.time.Clock()
pygame.display.set_caption("Flappy Witch")

pygame.init()
pygame.mixer.init()

class GameElements:

    def bgmusic():
        pygame.mixer.music.load('music/bgmusic.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def hit():
        collision= pygame.mixer.Sound('music/pop.mp3')
        collision.set_volume(0.2)
        collision.play()

    def mouse():
        mousepos=pygame.mouse.get_pos()
        mx,my=  mousepos
        pos=(mx,my)
        return pos
    
    def seconds():
        secs= int(pygame.time.get_ticks()/1000)
        secs1=font3.render(f"Seconds: {secs}", False, 'goldenrod4')
        return secs1
    
    def cursor():
        cursor1=pygame.image.load('char/cursor.png').convert_alpha()
        cursor2=pygame.transform.scale(cursor1, (20,30))
        cursor=cursor2.get_rect(topleft=(GameElements.mouse()))
        return cursor2, cursor
    
    def exitbutton():

        color_not='goldenrod3'
        color_umm='goldenrod4'
       

        button=pygame.Rect(900,450,70,30)
        color=color_umm if button.collidepoint(GameElements.mouse()) else color_not

        pygame.draw.rect(screen, color, button, border_radius=8)
        text_surf = font.render("exit", False, 'WHITE')
        text_rect = text_surf.get_rect(center=button.center)
        return button, text_surf, text_rect
    


background1=pygame.image.load('char/final.png')
background2=pygame.transform.scale(background1,(3000,500))
background=background2.get_rect(topleft=(0,0))

playbut1=pygame.image.load('char/play1.png').convert_alpha()
playbut2=pygame.transform.scale(playbut1, (160,80))
playbut3=playbut2.get_rect(topleft=(425,220))

playp2=pygame.image.load('char/play2.png').convert_alpha()
playp1=pygame.transform.scale(playp2, (160,80))
playp=playp1.get_rect(topleft=(425,220))

over2=pygame.image.load('char/gameover1.png').convert_alpha()
over1=pygame.transform.scale(over2, (445,100))
over=over1.get_rect(topleft=(280,200))

heart12=pygame.image.load('char/heart1.png').convert_alpha()
heart11=pygame.transform.scale(heart12, (200,50))
heart1=heart11.get_rect(topleft=(50,5))

heart22=pygame.image.load('char/heart2.png').convert_alpha()
heart21=pygame.transform.scale(heart22, (200,50))
heart2=heart21.get_rect(topleft=(50,5))

heart32=pygame.image.load('char/heart3.png').convert_alpha()
heart31=pygame.transform.scale(heart32, (200,50))
heart3=heart31.get_rect(topleft=(50,5))

heart42=pygame.image.load('char/heart4.png').convert_alpha()
heart41=pygame.transform.scale(heart42, (200,50))
heart4=heart41.get_rect(topleft=(50,5))

heart52=pygame.image.load('char/heart5.png').convert_alpha()
heart51=pygame.transform.scale(heart52, (200,50))
heart5=heart51.get_rect(topleft=(50,5))

one11=pygame.image.load('char/1.png').convert_alpha()
one12=pygame.transform.scale(one11, (31,72))
one=one12.get_rect(topleft=(485, 240))

two21=pygame.image.load('char/2.png').convert_alpha()
two22=pygame.transform.scale(two21, (57,72))
two=two22.get_rect(topleft=(470, 240))

three31=pygame.image.load('char/3.png').convert_alpha()
three32=pygame.transform.scale(three31, (57,73))
three=three32.get_rect(topleft=(470, 240))

zero1=pygame.image.load('char/0.png').convert_alpha()
zero2=pygame.transform.scale(zero1, (57,73))
zero=zero2.get_rect(topleft=(470, 240))


GameElements.bgmusic()

# mousepos=pygame.mouse.get_pos()
# mx,my=mousepos

collided_last_frame=False


witch1=pygame.image.load('char/witch.png').convert_alpha()
witch2=pygame.transform.scale(witch1, (55,55))
witch=witch2.get_rect(topleft=(-55,350))

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

y=2
lose=40
start=0
run=True
vel=2
velo=5

mes=font1.render("Game Ended", False, 'white')


while run:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                # pygame.display.update()
                pygame.quit()
                sys.exit()


    background.right-=1
    if background.right<=1000:
        background.left=0
    screen.blit(background2, background)


    pygame.mouse.set_visible(False)
    

    pillars = [pillarupp, pillarupp2, pillarupp3, pillarupp4,
            pillardownn, pillardownn2, pillardownn3, pillardownn4]
    current_collision=False

    for p in pillars[0:4]:
        p.left-=1.4
        if p.right<=0:
            p.left=1000
        screen.blit(pillarup1, p)

    for p in pillars[4:8]:
        p.left-=1.4
        if p.right<=0:
            p.left=1000
        screen.blit(pillardown1, p)
    
    
    mes=font1.render("Save the Witch!", False, 'goldenrod2') 
    
    if start==0:
        
        mess=font1.render("Click Play to start", False, 'goldenrod2')
        by=font.render("Game By Chaitali Ingle", False, 'goldenrod2')
        screen.blit(by, (370, 450))
        screen.blit(mess, (250,50))
        screen.blit(playbut2,playbut3)
        screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )

        pygame.display.update()
        for events in pygame.event.get():
            
            if playbut3.collidepoint(GameElements.mouse()[0], GameElements.mouse()[1]):
                # pygame.display.update()
                screen.blit(playp1,playp)
                screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )
                pygame.display.update()
                if events.type==pygame.MOUSEBUTTONDOWN:
                
                    
                    pygame.display.update()
                    start+=1

    elif start==1:

        screen.blit(mes, (300, 150))

        for i in range (1, 5):
            screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )
            
            if i==4:
                start+=1
                
            if i==1:
                screen.blit(one12,one)
            
                
            if i==2:
                screen.blit(two22,two)
               
                
            if i==3:
                screen.blit(three32,three)

            pygame.time.wait(1000)
                

            pygame.display.update()
                

      
            
    else:
        
        sec=pygame.time.get_ticks()
        screen.blit(GameElements.seconds(), (800,15))

        screen.blit(GameElements.exitbutton()[1], GameElements.exitbutton()[2])
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if GameElements.exitbutton()[0].collidepoint(GameElements.mouse()[0], GameElements.mouse()[1]):
                 
                    screen.blit(over1, over)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    # pygame.qu
                    sys.exit()

        
        key=pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            witch.centery-=2
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            witch.centery+=velo
        

        
        if any(witch.colliderect(p) for p in pillars):
            current_collision=True
            witch.left-=0.5
        
        if current_collision and not collided_last_frame:
            witch.left-=1
            lose-=1
            GameElements.hit()
            
        collided_last_frame=current_collision

        #witch
        witch.left+=vel
        witch.top-=y
        if witch.left>=1000:
            witch.left=-witch.width
            
        screen.blit(witch2, witch)

        
        if witch.top<=0 or witch.bottom>=500:
            y*=-1
        
        name=font.render(f"Save the Witch!", False, 'goldenrod4')
        screen.blit(name, (420, 15))


        # message2=font.render(f"Health: {int(lose)}", False, 'goldenrod4')
        # screen.blit(message2, (100, 20))
        screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )


        if lose>0 and lose<=10:
            vel=3.8
            y=5
            velo=8.2
            screen.blit(heart21, heart2)
            pygame.display.update()

        elif lose>10 and lose<=20:
            vel=3.2
            y=4
            velo=7.2
            screen.blit(heart31, heart3)
            pygame.display.update()

        elif lose>20 and lose<=30:
            vel=2.6
            y=3
            velo=5.5
            screen.blit(heart41, heart4)
            pygame.display.update()

        elif lose>30 and lose<=40:
            screen.blit(heart51, heart5)


        if lose<=0:
                screen.blit(heart11, heart1)
                # message1=font1.render("Amazing!", False, 'white')
                screen.blit(over1, over)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False


        pygame.display.update()
        clock.tick(60)


pygame.quit()
