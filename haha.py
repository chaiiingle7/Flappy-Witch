import pygame
import sys
import os 


screen=pygame.display.set_mode((1000,500))
clock=pygame.time.Clock()
pygame.display.set_caption("Flappy Witch")

pygame.init()
pygame.mixer.init()
start_time = 0 
survival_time = 0

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
    
    def seconds(start_time):
        current_time = pygame.time.get_ticks()
        
        if start_time == 0:
            start_time = current_time
        
        
        survival_time = (current_time - start_time) / 1000
   
        score_text = font.render(f"Time: {int(survival_time)}s", False, 'goldenrod4')
        # screen.blit(score_text, (800, 15))
        return score_text
    
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
    
    def load_highscore():
        if os.path.exists("highscore.txt"):
            try:
                with open("highscore.txt", "r") as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0

    def save_highscore(score):
        current_best = GameElements.load_highscore()
        if score > current_best:
            with open("highscore.txt", "w") as f:
                f.write(str(score))
            return True # Saved new record
        return False 
    

font=pygame.font.Font('font/yoster.ttf', 20)
font1=pygame.font.Font('font/yoster.ttf', 50)
font3=pygame.font.Font('font/yoster.ttf', 15)
    

text1="Fly through the pipes coming in all through your way.\nThe Witch flies in right and drifts upwards.\nPress 'S' or 'Key Down' button for flying downwards,\nto avoid colliding the pipes.\nYou have 4 lives, with each collision you lose one \nwhile the speed of the witch increases.\nAll the best!".split('\n')


text=font3.render(text1[0], False, 'yellow')
text2=font3.render(text1[1], False, 'goldenrod2')
text3=font3.render(text1[2], False, 'gold')
text4=font3.render(text1[3], False, 'yellow')
text5=font3.render(text1[4], False, 'gold')
text6=font3.render(text1[5], False, 'goldenrod2')
text7=font3.render(text1[6], False, 'yellow')


        


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


collided_last_frame=False


witch1=pygame.image.load('char/witch.png').convert_alpha()
witch2=pygame.transform.scale(witch1, (55,55))
witch=witch2.get_rect(topleft=(-55,350))

pillarup=pygame.image.load('char/uppipe.png').convert_alpha()
pillarup1=pygame.transform.scale(pillarup, (30,300))

pillarupp=pillarup1.get_rect(topleft=(333,380))
pillarupp2=pillarup1.get_rect(topleft=(1000,350))
pillarupp3=pillarup1.get_rect(topleft=(667,350))
# pillarupp4=pillarup1.get_rect(topleft=(857,400))


pillardown=pygame.image.load('char/downpipe.png').convert_alpha()
pillardown1=pygame.transform.scale(pillardown, (30,300))

pillardownn=pillardown1.get_rect(topleft=(167,-20))
# pillardownn2=pillardown1.get_rect(topleft=(1000,-50))
pillardownn3=pillardown1.get_rect(topleft=(500,-30))
pillardownn4=pillardown1.get_rect(topleft=(834,-110))


back_vel=2
y=2
lose=4
start=0
run=True

vel=2
velo=5
i=3


best_score = GameElements.load_highscore()

countdown_images = [three32, two22, one12] 
countdown_rects = [three, two, one]

while run:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                # pygame.display.update()
                pygame.quit()
                sys.exit()


    background.right-=back_vel
    if background.right<=1000:
        background.left=0
    screen.blit(background2, background)


    pygame.mouse.set_visible(False)
    

    pillars = [pillarupp, pillarupp3, pillarupp2,
            pillardownn, pillardownn3, pillardownn4]
    current_collision=False

    for p in pillars[0:3]:
        p.left-=1.4
        if p.right<=0:
            p.left=1000
        screen.blit(pillarup1, p)

    for p in pillars[3:6]:
        p.left-=1.4
        if p.right<=0:
            p.left=1000
        screen.blit(pillardown1, p)
    
    
    mes=font1.render("Save the Witch!", False, 'goldenrod2') 
    
    if start==0:
        screen.blit(text, (250+40,230+100))
        screen.blit(text2, (250+70,230+120))
        screen.blit(text3, (250+40,230+140))
        screen.blit(text4, (250+130,230+160))
        screen.blit(text5, (250+50,230+180))
        screen.blit(text6, (250+80,230+200))
        screen.blit(text7, (250+180,230+220))

        best_text = font.render(f"Best Score: {best_score}s", False, 'goldenrod2')
        screen.blit(best_text, (400, 140))
        
        mess=font1.render("Click Play to start", False, 'goldenrod2')
        by=font.render("Game By Chaitali Ingle", False, 'goldenrod2')
        screen.blit(by, (370, 20))
        screen.blit(mess, (250,70))
        screen.blit(playbut2,playbut3)
        screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )

        pygame.display.update()
        for events in pygame.event.get():
            
            if playbut3.collidepoint(GameElements.mouse()[0], GameElements.mouse()[1]):
              
                screen.blit(playp1,playp)
                screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )
                pygame.display.update()
                if events.type==pygame.MOUSEBUTTONDOWN:
                
                    
                    pygame.display.update()
                    start+=1

    elif start==1:
        # screen.blit(witch2, witch)
        

        screen.blit(mes, (300, 150))

        
        screen.blit(GameElements.cursor()[0], GameElements.cursor()[1] )

        for i in range(1, 4, 1): 
        
            index = 3 - i 
            screen.blit(countdown_images[index], countdown_rects[index])
            
            pygame.display.update()
            
        
            pygame.time.wait(1000)

        else:
            start+=1
            
                

      
            
    else:
        
        current_time = pygame.time.get_ticks()
        
        if start_time == 0:
            start_time = current_time
        
        
        survival_time = (current_time - start_time) / 1000
   
        score_text = font.render(f"Time: {int(survival_time)}s", False, 'goldenrod4')
        screen.blit(score_text, (800,15))

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
            # if witch.top<=0 or witch.bottom>=500:
            #     y*=-1
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            witch.centery+=velo
            # if witch.top<=0 or witch.bottom>=500:
            #     y*=-1
        


        
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


        if lose>0 and lose<=1:
            vel=3.5
            y=3.6
            velo=7.2
            back_vel=3.5
            screen.blit(heart21, heart2)
            pygame.display.update()

        elif lose>1 and lose<=2:
            vel=3
            y=3
            velo=6.4
            back_vel=3
            screen.blit(heart31, heart3)
            pygame.display.update()

        elif lose>2 and lose<=3:
            vel=2.6
            y=2.5
            velo=5.5
            back_vel=2.5
            screen.blit(heart41, heart4)
            pygame.display.update()

        elif lose>3 and lose<=4:
            screen.blit(heart51, heart5)


        elif lose<=0:
            if survival_time > best_score:
                GameElements.save_highscore(int(survival_time))
                best_score = int(survival_time)
            screen.blit(heart11, heart1)
            # message1=font1.render("Amazing!", False, 'white')
            screen.blit(over1, over)
            pygame.display.update()
            pygame.time.wait(2000)
            run = False


        pygame.display.update()
        clock.tick(60)


pygame.quit()
