#coding=utf-8
import pygame,sys
pygame.init()
speed=[0,0]
color=255,55,255
fps=300#每秒帧率参数
Vinfo=pygame.display.Info()
size=width,height=Vinfo.current_w,Vinfo.current_h
screen=pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("pygame游戏之旅")
ball=pygame.image.load("壁球.gif")
ballrect=ball.get_rect()
fclock=pygame.time.Clock()#创建一个Clock对象，用于操作时间

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				speed[0]=speed[0] if speed[0]==0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
			elif event.key==pygame.K_RIGHT:
				speed[0]=speed[0]+1 if speed[0]>0 else speed[0]-1
			elif event.key==pygame.K_UP:
				speed[1]=speed[1]+1 if speed[1]>0 else speed[1]-1
			elif event.key==pygame.K_DOWN:
				speed[1]=speed[1] if speed[1]==0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
			elif event.key==pygame.KEY_ESCAPE:
				sys.quit()
		elif event.type==pygame.VIDEORESIZE:
	ballrect=ballrect.move(speed[0],speed[1])
	if ballrect.left<0 or ballrect.right>width:
		speed[0]=-speed[0]
	if ballrect.top<0 or ballrect.bottom>height:
		speed[1]=-speed[1]
	screen.fill(color)
	#控制屏幕刷新与游戏背景色
	screen.blit(ball,ballrect)
	#将一个图像绘制在另一个图像上，即将src绘制到dest位置上，通过Rect对象引导对壁球的绘制
	fclock.tick(fps)
	#clock.tick(framerate)控制窗口刷新速度
	pygame.display.update()
