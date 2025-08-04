'''SUBG'''
'''It is an simple runner game based on the character shinchan'''

import pygame
import webbrowser
from random import randint
from random import randrange
from sys import exit
import pyttsx3
import speech_recognition as sr

current_time=0
def display_score():
   global current_time
   current_time+=10#pygame.time.get_ticks()
   score_surf = text_font.render('SCORE :'+str(current_time//500),False,'#1CC809',)
   score_rect = score_surf.get_rect(center = (75,25))
   screen.blit(score_surf,score_rect)

def speak(text):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return ""

pygame.init()
current_time=pygame.time.get_ticks()
screen=pygame.display.set_mode((1000,500))
pygame.display.set_caption('SUBG')
clock= pygame.time.Clock()
text_font=pygame.font.Font(None, 45)
text_font1=pygame.font.Font(None, 60)
game_active = 'loll'

test_surface1=pygame.image.load('OP/PYTHON11.png')
detail_surf1= text_font1.render('MARS',False,'#630002')
test_surface2=pygame.image.load('OP/back.png')
detail_surf2= text_font1.render('HORROR NIGHT',False,'#010C44')
test_surface3=pygame.image.load('OP/Capture.JPG')
detail_surf3= text_font1.render('HIMALAYA',False,'#DD05FA')
test_surface= test_surface1
detail_surf=detail_surf1
detail_brect=detail_surf.get_rect(center=(500,250))

restart = pygame.image.load('OP/restart.JPG')
quit = pygame.image.load('OP/quit.JPG')
restart_rect= restart.get_rect(center =(300,400))
quit_rect= quit.get_rect(center =(650,400))

lobby1= pygame.image.load('OP/lobby1.jpg')
lobby2= pygame.image.load('OP/LOBBY.jpg')
lobby=lobby1
lobby_rect=lobby.get_rect(topleft=(0,0))

back1=pygame.image.load('OP/back/1.jpeg')
back2=pygame.image.load('OP/back/2.jpeg')
back3=pygame.image.load('OP/back/4.jpg')
ronit=pygame.image.load('OP/ronit.png')
EA= pygame.image.load('OP/ea1.jpg')


coin_x=300
coin_y=300

player_health=200

background=pygame.image.load('OP/backb.png')
background=pygame.transform.scale(background,(150,100))
background_rect=background.get_rect(center=(925,450))
player_=pygame.image.load('OP/player.png')
player_=pygame.transform.scale(player_,(150,100))
player__rect=player_.get_rect(center=(75,450))

pause_menu=pygame.image.load('OP/shinchan pause1.png')
pause_rect=pause_menu.get_rect(topleft=(0,0))

GREY= (68,67,68)
BLACK= (0,0,0)
RED= (255,0,0)
GREEN = (64,219,21)



#thank= pygame.image.load('OP/THANK.JPG')
#thank_rect = thank.get_rect(center=(500,400))

warning= text_font1.render('WARNING',False,'#D00707',)
warning_rect= warning.get_rect(center = (500,50))

snail_surface = pygame.image.load('OP/snail1.png')
snail_rect = snail_surface.get_rect(bottomright =(1100,400))
snail_x_pos=800

rock_surface = pygame.image.load('OP/caps.png')
rock_x=500
rock_rect= rock_surface.get_rect(center = (rock_x,-5000))

gift_x=200
gift = pygame.image.load('OP/GIFT.png')
gift_rect= gift.get_rect(center=(gift_x,-3000))

player1_surf1=pygame.image.load('OP/shinchan.png').convert_alpha()
player1_jump=pygame.image.load('OP/jump.png').convert_alpha()
player1_surf2=pygame.image.load('OP/shinchan1.png').convert_alpha()
player_surf=player1_surf1
player_jump=player1_jump
player_surf2=player1_surf2
player=player_surf

player2_surf1=pygame.image.load('OP/player2.png').convert_alpha()
player2_surf1= pygame.transform.scale(player2_surf1,(113,137))
player2_jump= pygame.image.load('OP/player1.png').convert_alpha()
player2_jump= pygame.transform.scale(player2_jump,(145,138))
player2_surf2 = pygame.image.load('OP/player3.png').convert_alpha()
player2_surf2= pygame.transform.scale(player2_surf2,(113,137))

detail_player1=text_font1.render('SHINCHAN    AGE:5',False,'#0ACEFF')
detail_player2=text_font1.render('ASTRONAUT RONIT    AGE:16',False,'#2002A4')
detail_player=detail_player1
detail_prect=detail_player.get_rect(center= (500,100))

player_rect= player.get_rect(midbottom = (80,400))

player_gravity = 0
player_stand = pygame.image.load('OP/player2.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (80,400))
score=0
pygame.display.set_icon(player1_surf1)

loading=0

#potion=pygame.image.load('OP/potion.png')

settings= pygame.image.load('OP/settings.png')
settings_rect=settings.get_rect(bottomright = (975,100))

game = pygame.image.load('OP/GAME.JPG')
coin=0
coin_count= text_font.render(':'+str(coin),False,'#140779')
coin_count_rect = coin_count.get_rect(center=(100,75))
speed=0

blit=False
blit1=True

resume= pygame.image.load('OP/pause/resume.png')
resume_rect= resume.get_rect(center=(500,150))
restart1= pygame.image.load('OP/pause/restart.png')
restart_rect1= restart1.get_rect(center=(500,250))
end= pygame.image.load('OP/pause/end.png')
end_rect= end.get_rect(center=(500,350))

vol3= pygame.image.load('OP/pause/vol3.png')
vol2= pygame.image.load('OP/pause/vol2.png')
vol1= pygame.image.load('OP/pause/vol1.png')
vol0= pygame.image.load('OP/pause/vol0.png')
vol=vol3
vol_rect=vol.get_rect(center= (550,70))

sound3= pygame.image.load('OP/pause/sound3.png')
sound2= pygame.image.load('OP/pause/sound2.png')
sound1= pygame.image.load('OP/pause/sound1.png')
sound0= pygame.image.load('OP/pause/sound0.png')
sound_=sound3
sound_rect=sound_.get_rect(center= (450,70))

heart= pygame.image.load('OP/heart.png')
heart_rect= heart.get_rect(center=(800,15))
heart_x=200
heart1=pygame.image.load('OP/heart1.png') 

choco= pygame.image.load('OP/choco.png')

sad=0
sad1=True
sad_sound=pygame.mixer.Sound('AUDIO/Sad Funny Meme - Sound Effect.wav')
sound=pygame.mixer.Sound('AUDIO/Title Screen.wav')

pygame.mixer.Sound.set_volume(sound,0.05)
coin_sound=pygame.mixer.Sound('AUDIO/coin.wav')
jump_sound=pygame.mixer.Sound('AUDIO/jump.wav')
yeah_boy=pygame.mixer.Sound('AUDIO/yeah-boy-114748.wav')
intro= pygame.mixer.Sound('AUDIO/intro.wav')
ea_s= pygame.mixer.Sound('AUDIO/ea_sports.wav')
game1=True
while game1:
   for event1 in pygame.event.get():
      if event1.type == pygame.QUIT:
         pygame.quit()
         exit()
      elif event1.type == pygame.KEYDOWN:
         if event1.key == pygame.K_SPACE:
            game1 = False
                  
   if loading==100:
      speak('Welcome to Ronit Production')
   if 50<= loading<= 150:
      screen.blit(ronit,(0,0))
   elif 150<= loading <= 250:
      screen.blit(EA,(0,0))
   elif 250<=loading<=316:
      screen.blit(back1,(0,0))
   elif 316<= loading <=382:
      screen.blit(back2,(0,0))
   elif 382<= loading <=450:
      screen.blit(back3,(0,0))
   if loading>=250:
      pygame.draw.rect(screen,GREY,(400,400,200,20))
      pygame.draw.rect(screen, GREEN, (400, 400, loading-250, 20))
   if loading==10:
      intro.play()
   elif loading==150:
      ea_s.play()
   loading+=0.5

   pygame.display.update()
   clock.tick(60)
   if loading >= 450:
      game1=False
sound.play(loops=-1)
main = True
while True:
   screen.blit(lobby,lobby_rect)
   screen.blit(background,background_rect)
   screen.blit(player_,player__rect)
   for event2 in pygame.event.get():
      if event2.type == pygame.QUIT:
         pygame.quit()
         exit()
      elif event2.type== pygame.MOUSEBUTTONDOWN:
         if background_rect.collidepoint(event2.pos):
            back=True
            while back:
               screen.blit(test_surface,(0,0))
               screen.blit(detail_surf,detail_brect)
               for event3 in pygame.event.get():
                  if event3.type == pygame.KEYDOWN:
                     if event3.key == pygame.K_RIGHT:
                        if test_surface==test_surface1:
                           test_surface = test_surface2
                           detail_surf=detail_surf2
                        elif test_surface==test_surface2:
                           test_surface = test_surface3
                           detail_surf = detail_surf3
                        elif test_surface==test_surface3:
                           test_surface = test_surface1
                           detail_surf = detail_surf1
                     elif event3.key == pygame.K_LEFT:
                        if test_surface==test_surface1:
                           test_surface = test_surface3
                           detail_surf=detail_surf3
                        elif test_surface==test_surface2:
                           test_surface = test_surface1
                           detail_surf = detail_surf1
                        elif test_surface==test_surface3:
                           test_surface = test_surface2
                           detail_surf = detail_surf2
                     elif event3.key == pygame.K_ESCAPE:
                        back=False
               pygame.display.update()
               clock.tick(60)
         elif player__rect.collidepoint(event2.pos):
            play=True

            while play:
               screen.blit(test_surface,(0,0))
               screen.blit(player_surf,(450,270))
               screen.blit(detail_player,detail_prect)
               for event4 in pygame.event.get():
                  if event4.type== pygame.KEYDOWN:
                     if event4.key == pygame.K_RIGHT:
                        if player_surf == player1_surf1:
                           player_surf= player2_surf1
                           player_jump= player2_jump
                           player_surf2= player2_surf2
                           detail_player=detail_player2
                           lobby=lobby2
                        elif player_surf == player2_surf1:
                           player_surf= player1_surf1
                           player_jump= player1_jump
                           player_surf2= player1_surf2
                           detail_player = detail_player1
                           lobby = lobby1
                     elif event4.key == pygame.K_LEFT:
                        if player_surf == player1_surf1:
                           player_surf= player2_surf1
                           player_jump= player2_jump
                           player_surf2= player2_surf2
                           detail_player=detail_player2
                           lobby=lobby2
                        elif player_surf == player2_surf1:
                           player_surf= player1_surf1
                           player_jump= player1_jump
                           player_surf2= player1_surf2
                           detail_player = detail_player1
                           lobby = lobby1

                     elif  event4.key == pygame.K_ESCAPE:
                        play = False

               pygame.display.update()
               clock.tick(60)

      elif event2.type == pygame.KEYDOWN:
         #if op.key == pygame.K_ESCAPE:

         if event2.key == pygame.K_SPACE:
            main = True
            game_active='loll'
            while main:
               for event5 in pygame.event.get():
                  if event5.type== pygame.QUIT:
                     pygame.quit()
                     exit()
                  elif event5.type== pygame.MOUSEBUTTONDOWN:
                     if settings_rect.collidepoint(event5.pos):
                        pause=True
                        while pause:
                           screen.blit(pause_menu,pause_rect)
                           screen.blit(resume,resume_rect)
                           screen.blit(restart1,restart_rect1)
                           screen.blit(end,end_rect)
                           screen.blit(vol,vol_rect)
                           screen.blit(sound_,sound_rect)
                           for event6 in pygame.event.get():
                              if event6.type == pygame.MOUSEBUTTONDOWN:
                                 if resume_rect.collidepoint(event6.pos):
                                    pause = False
                                    #webbrowser.open('www.youtube.com')
                                    break
                                 elif restart_rect1.collidepoint(event6.pos):
                                    game_active = 'lol'
                                    sad1=False
                                    pause = False
                                    break
                                 elif end_rect.collidepoint(event6.pos):
                                    main = False
                                    pause = False
                                    player_rect.left = 80
                                    snail_rect.right = 1100
                                    current_time = 0
                                    coin = 0
                                    player_health = 200
                                    gift_rect.bottom = -8000
                                    rock_rect.bottom = -5000
                                    break
                                 elif vol_rect.collidepoint(event6.pos):
                                    if vol==vol3:
                                       vol=vol2
                                       pygame.mixer.Sound.set_volume(sound, 0.03)
                                    elif vol==vol2:
                                       vol=vol1
                                       pygame.mixer.Sound.set_volume(sound, 0.01)
                                    elif vol==vol1:
                                       vol=vol0
                                       pygame.mixer.Sound.set_volume(sound, 0)
                                    elif vol==vol0:
                                       vol=vol3
                                       pygame.mixer.Sound.set_volume(sound, 0.05)

                                 elif sound_rect.collidepoint(event6.pos):
                                    if sound_==sound3:
                                       sound_=sound2
                                       pygame.mixer.Sound.set_volume(coin_sound, 0.03)
                                       pygame.mixer.Sound.set_volume(jump_sound, 0.03)
                                       pygame.mixer.Sound.set_volume(sad_sound, 0.03)
                                       pygame.mixer.Sound.set_volume(yeah_boy, 0.03)
                                    elif sound_==sound2:
                                       sound_=sound1
                                       pygame.mixer.Sound.set_volume(coin_sound, 0.01)
                                       pygame.mixer.Sound.set_volume(jump_sound, 0.01)
                                       pygame.mixer.Sound.set_volume(sad_sound, 0.01)
                                       pygame.mixer.Sound.set_volume(yeah_boy, 0.01)
                                    elif sound_==sound1:
                                       sound_=sound0
                                       pygame.mixer.Sound.set_volume(coin_sound, 0)
                                       pygame.mixer.Sound.set_volume(jump_sound, 0)
                                       pygame.mixer.Sound.set_volume(sad_sound, 0)
                                       pygame.mixer.Sound.set_volume(yeah_boy, 0)
                                    elif sound_==sound0:
                                       sound_=sound3
                                       pygame.mixer.Sound.set_volume(coin_sound, 0.05)
                                       pygame.mixer.Sound.set_volume(jump_sound, 0.05)
                                       pygame.mixer.Sound.set_volume(sad_sound, 0.05)
                                       pygame.mixer.Sound.set_volume(yeah_boy, 0.05)


                                                
                           pygame.display.update()
                           clock.tick(60)


                  elif event5.type == pygame.KEYDOWN:
                     if event5.key == pygame.K_LEFT:
                        if player_rect.bottom == 410:
                           player = player_surf2
                        elif event5.key == pygame.K_LEFT:
                           if player_rect.bottom == 410:
                              player = player_surf
                        
                      #if event5.key == pygame.K_SPACE:
                         #if player_rect.bottom==410:
                           #player=player_jump
                           #jump_sound.play()
                           #player_gravity = -20
                      #elif event5.key==pygame.K_LEFT:
                         #player_rect.x -= 25
                         #if player_rect.bottom == 410:
                            #player = player_surf2
                      #elif event5.key == pygame.K_RIGHT:
                         #player_rect.x += 25
                         #if player_rect.bottom == 410:
                            #player = player_surf
                      #elif event5.key == pygame.K_ESCAPE:
                       #  player_health = 0
               

               keys = pygame.key.get_pressed()
               if keys[pygame.K_LEFT]:
                  player_rect.x -= 5
                  #if player_rect.bottom == 410:
                     #player = player_surf2
               elif keys[pygame.K_RIGHT]:
                  player_rect.x +=5
                  #if player_rect.bottom == 410:
                     #player = player_surf
               if keys[pygame.K_SPACE] and player_rect.bottom==410 :
                  player=player_jump
                  jump_sound.play()
                  player_gravity = -20
                  
                  
                  
                  

               coin_surface = pygame.image.load('OP/coin.png')
               coin_rect = coin_surface.get_rect(center=(coin_x,coin_y))
               coin_rect2= coin_surface.get_rect(center=(50,75))
               coin_count = text_font.render(':' + str(coin), False, '#140779')
               coin_count_rect = coin_count.get_rect(center=(100, 75))

               choco_rect1 = choco.get_rect(center=(heart_x, 390))

               if game_active=='loll':
                  screen.blit(test_surface,(0,0))
                  #pygame.draw.rect(screen, '#F20519', score_rect)
                  #pygame.draw.rect(screen, '#F20519', score_rect,10)
                  #screen.blit(score_surf,score_rect)
                  display_score()


                  pygame.draw.rect(screen,RED,(800,10,200,20))
                  pygame.draw.rect(screen, GREEN, (800, 10, player_health, 20))

                  speed+=0.001
                  snail_rect.x -= 5+speed
                  if snail_rect.right <= 0:
                     snail_rect.left = 1000
                  screen.blit(snail_surface,snail_rect)

                  screen.blit(coin_surface, coin_rect)
                  screen.blit(coin_surface, coin_rect2)
                  screen.blit(coin_count,coin_count_rect)

                  screen.blit(heart, heart_rect)

                  #Player
                  player_gravity+=1
                  player_rect.y +=player_gravity
                  if player_rect.bottom>=410:
                     player=player_surf
                     player_rect.bottom = 410
                  screen.blit(player, player_rect)

                  screen.blit(settings,settings_rect)

                  if player_rect.right>1000:
                     player_rect.right=1000
                  elif player_rect.left<0:
                     player_rect.left=0


                  if coin_rect.colliderect(player_rect):
                     coin_sound.play()
                     coin_x=randint(0,1000)
                     coin_y=randint(300,400)
                     coin+=1
                     #py=pygame.transform.rotozoom(player_stand,135,2)
                  screen.blit(rock_surface, rock_rect)
                  rock_rect.y += 4
                  if rock_rect.bottom>=480:
                     lim=randint(0,1000)
                     rock_rect.bottom=-5000
                     rock_rect.x=lim

                  if rock_rect.bottom>=-500:
                     screen.blit(warning, warning_rect)
                  if rock_rect.colliderect(player_rect):
                     player_health-=1

                  screen.blit(gift,gift_rect)
                  gift_rect.y+=3
                  if gift_rect.bottom>=430:
                     #gift_rect.bottom=-20000
                     blit=True
                     heart_x=gift_x
                     gift_x = randint(50, 950)
                     gift_rect.left = gift_x
                  if blit:
                     heart_y = 390
                     screen.blit(choco,choco_rect1)
                     gift_rect.bottom = -8000
                     if choco_rect1.colliderect(player_rect):
                        player_health+=25
                        screen.blit(heart1,(2000,0))
                        yeah_boy.play()
                        blit=False

                  if snail_rect.colliderect(player_rect):
                     py=pygame.transform.rotozoom(player_stand,135,2)
                     player_health -= 2

                  if player_health==0:
                     game_active=False

               elif game_active==False:
                  sound.stop()
                  sad+=1
                  if sad1==False:
                     if sad==1:
                        sad_sound.play()
                  screen.blit(game,(0,0))
                  screen.blit(restart,restart_rect)
                  screen.blit(quit, quit_rect)
                  if event5.type == pygame.MOUSEBUTTONDOWN:
                     if restart_rect.collidepoint(event5.pos):
                        game_active='lol'
                        player_rect.left=80
                        snail_rect.right=1100
                        current_time=0
                        coin=0
                        player_health=200
                        gift_rect.bottom = -8000
                        rock_rect.bottom=-5000

                     if quit_rect.collidepoint(event5.pos):
                        game_active='loll'
                        player_rect.left = 80
                        snail_rect.right = 1100
                        current_time = current_time - current_time
                        coin = 0
                        player_health = 200
                        gift_rect.bottom = -8000
                        rock_rect.bottom = -5000

                        break
               elif game_active=='lol':
                  game_active = 'loll'
                  
                  player_rect.left = 80
                  snail_rect.right = 1100
                  current_time = 0
                  coin = 0
                  player_health = 200
                  gift_rect.bottom = -8000
                  rock_rect.bottom = -5000
                  
                  #break

               pygame.display.update()
               clock.tick(60)

   pygame.display.update()
   clock.tick(500)
input('...') 

