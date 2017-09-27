import pygame,random
from pygame.locals import *
import time
pygame.init()

blip=pygame.mixer.Sound("C:/Users/pvrao/Desktop/blip.wav")

random.seed()
screen=pygame.display.set_mode((1000,650))

sprite_paddle1=pygame.image.load("C:/Users/pvrao/Desktop/Paddle1.png")
sprite_paddle2=pygame.image.load("C:/Users/pvrao/Desktop/Paddle2.png")
ball=pygame.image.load("C:/Users/pvrao/Desktop/Ball.png")

rect_paddle1=sprite_paddle1.get_rect()
rect_paddle2=sprite_paddle2.get_rect()
rect_ball=ball.get_rect()

rect_paddle1.top=0
rect_paddle1.left=150

rect_paddle2.top=615	
rect_paddle2.left=150

rect_ball.top=350
rect_ball.left=350
#Width of Paddle is 35 pixels while length is 128 pixels

redscore=0
bluescore=0
font=pygame.font.SysFont(None,25)

def score_display(redscore,bluescore):
	screen_text1=font.render("Score",True,(0,0,0))
	screen_text3=font.render("Score",True,(0,0,0))
	screen_text4=font.render("Red: "+str(redscore),True,(255,0,0))
	
	screen_text2=font.render("Blue: "+str(bluescore),True,(0,0,255))
	screen.blit(screen_text1,(400,325))
	screen.blit(screen_text2,(460,325))
	screen.blit(screen_text3,(400,300))
	screen.blit(screen_text4,(460,300))



#----------DECLARING BALL SPEED HERE------------#
hspeed=0
vspeed=0
while hspeed==0:
	hspeed=random.randint(-1,1)
	hspeed=hspeed
while vspeed==0:
	vspeed=random.randint(-1,1)
	vspeed=vspeed
slower=2

run=True

while run:
	
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		if(rect_paddle1.left>0):
			rect_paddle1.left-=2

	if keys[pygame.K_RIGHT]:
		if(rect_paddle1.left<872):
			rect_paddle1.left+=2
    


	if (rect_ball.left<rect_paddle2.left) and (vspeed>0):
		if(rect_paddle2.left>0):
			rect_paddle2.left-=2

	if (rect_ball.left>(rect_paddle2.left+rect_paddle2.width)) and (vspeed>0):
		if(rect_paddle2.left<872):
			rect_paddle2.left+=2


			
#----Clever way to slow down the ball------------#
	slower-=1
	if(True):
		slower=2
	#-----------Horizontal Movement----------#
		if hspeed<0:
			if(rect_ball.left+hspeed>0):
				rect_ball.left+=hspeed
			else:
				hspeed=-hspeed

		else:
			if(rect_ball.left+hspeed<950):
				rect_ball.left+=hspeed
			else:
				hspeed=-hspeed

	#---------------Vertical Movement----------#

		if vspeed<0:
			if(rect_ball.top+vspeed>0):
				rect_ball.top+=vspeed
			else:

				bluescore+=1
				rect_ball.left=325
				rect_ball.top=325
				
		else:
			if(rect_ball.top+vspeed<950):
				rect_ball.top+=vspeed
			else:
				redscore+=1

				rect_ball.left=325
				rect_ball.top=325



    #-------------------COLLISION DETECTION-----------#

	#--------------ball collision with paddle 1-------#
	coll=False
	if((rect_ball.left>=rect_paddle1.left) and (rect_ball.left<=rect_paddle1.left+rect_paddle1.width) and (rect_ball.top<=rect_paddle1.top+rect_paddle1.height) and (rect_ball.top>=rect_paddle1.top)):
		coll=True
	


	if((rect_ball.left>=rect_paddle2.left) and (rect_ball.left<=rect_paddle2.left+rect_paddle2.width) and (rect_ball.top+rect_ball.height>=rect_paddle2.top) and (rect_ball.top+rect_ball.height<=rect_paddle2.top+rect_paddle2.height)):
		coll=True	
			



	flag=10
	if coll:
		blip.play()
		if((rect_ball.top<325) and (vspeed<0)):
			vspeed=-vspeed
			
			
		elif((rect_ball.top>325) and (vspeed>0)):
			vspeed=-vspeed
			
			
			
			
	screen.fill((255,255,255))
	score_display(redscore,bluescore)
	pygame.draw.line(screen,(0,0,0),(0,325),(1000,325))
	screen.blit(sprite_paddle1,rect_paddle1)
	screen.blit(sprite_paddle2,rect_paddle2)
	screen.blit(ball,rect_ball)
	pygame.display.set_caption("PONG")

	pygame.display.flip()
	pygame.display.update()
	for event in pygame.event.get():
		if event.type== QUIT:
			run=False


pygame.quit()


