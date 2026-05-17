import pygame
import sys

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
        secs1=font3.render(f"Seconds: {secs}", False, 'darkslategray')
        return secs1
    
    def cursor():
        cursor1=pygame.image.load('char/cursor.png').convert_alpha()
        cursor2=pygame.transform.scale(cursor1, (20,30))
        cursor=cursor2.get_rect(topleft=(GameElements.mouse()))
        return cursor2, cursor
    
    def exitbutton():

        color_not='aquamarine4'
        color_umm='olivedrab4'
        color_yes='chartreuse4'

        button=pygame.Rect(900,450,70,30)
        color=color_umm if button.collidepoint(GameElements.mouse()) else color_not

        pygame.draw.rect(screen, color, button, border_radius=8)
        text_surf = font.render("exit", False, 'WHITE')
        text_rect = text_surf.get_rect(center=button.center)
        return button, text_surf, text_rect
    
    def background():

        background1=pygame.image.load('char/final.png')
        background2=pygame.transform.scale(background1,(3000,500))
        background=background2.get_rect(topleft=(0,0))
        background.right-=1
        if background.right<=1000:
            background.left=0

        return background2, background


GameElements.bgmusic()

screen=pygame.display.set_mode((1000,500))
clock=pygame.time.Clock()
pygame.display.set_caption("Flappy Witch")

mousepos=pygame.mouse.get_pos()
mx,my=mousepos

collided_last_frame=False


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

y=5
lose=100
start=False
run=True


mes=font1.render("Game Ended", False, 'white')


while run:

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
            if (event.type==pygame.MOUSEBUTTONDOWN):
                if GameElements.exitbutton()[0].collidepoint(mousepos):
                    pygame.time.wait(1000)
                    pygame.quit()
                    sys.exit() 


    screen.blit(GameElements.background()[0], GameElements.background()[1])


    pygame.mouse.set_visible(False)
    

    
    mes=font1.render("Welcome! Let's save the Witch!", False, 'white') 
    sec=pygame.time.get_ticks()


    if not start:

        screen.blit(mes, (100, 150))
  
        for i in range (3, 0, -1):
            
            seconds=font1.render(f'{i}', False, 'white')
            screen.blit(seconds, (450,250))
            pygame.time.wait(500)
            pygame.display.update()
            if seconds==1:
                break
           
            
    else:

        screen.blit(GameElements.seconds()[0], (800,15))

        screen.blit(GameElements.exitbutton()[1], GameElements.exitbutton()[2])

        pillars = [pillarupp, pillarupp2, pillarupp3, pillarupp4,
                pillardownn, pillardownn2, pillardownn3, pillardownn4]
        current_collision=False

        for p in pillars[0:4]:
            p.left-=4
            if p.right<=0:
                p.left=1000
            screen.blit(pillarup1, p)

        for p in pillars[4:8]:
            p.left-=4
            if p.right<=0:
                p.left=1000
            screen.blit(pillardown1, p)

    
        screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )

        
        key=pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            witch.centery-=2
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            witch.centery+=14
        

        
        if any(witch.colliderect(p) for p in pillars):
            current_collision=True

        
        if current_collision and not collided_last_frame:
            witch.left-=1
            lose-=1
            GameElements.hit()
            
        collided_last_frame=current_collision

        #witch
        witch.left+=5
        witch.top-=y
        if witch.left>=1000:
            witch.left=-witch.width
            
        screen.blit(witch2, witch)

        
        if witch.top<=0 or witch.bottom>=500:
            y*=-1
        
        name=font.render(f"Save the Witch!", False, 'darkslategray')
        screen.blit(name, (430, 15))


        message2=font.render(f"Health: {int(lose)}", False, 'darkslategray')
        screen.blit(message2, (100, 20))


        if lose<=0:
                message1=font1.render("Game Over!", False, 'white')
                screen.blit(message1, (370, 240))
                pygame.display.update()
                pygame.time.wait(2000)
                run = False


        pygame.display.update()
        clock.tick(1000)


pygame.quit()
