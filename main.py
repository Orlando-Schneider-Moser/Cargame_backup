import pygame, sys, math
from pygame.locals import QUIT


#lambda functions
#instead of making a function for one argument like this:   def plus1(a): a+=1, def plus2(b): b+=2 
#you do:   def base(n): return lambda a: a+=n,  p1 = base(1), p2 = base(2)   /now you can do/  a = p2(2) /and get/ >4
#yeah its complicated :/ but if you want more than 1 line separate them with \   and get more arguments with x, y, z

#==Variables=======================================
TitleScreen = False
InGame = True
InInventory = False
GameOver = False

#slow = 0.01

carimg = pygame.image.load('./Car.png')

pygame.init()
Surf = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Car go brrrrrrrrrrrrrrrrrrrrrr")
#==Other_stuff====================================



#==Classes=========================================

class player:
	
	def __init__(self, x, y, w, h, rotation):
		
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speed = 0
		self.rotation = rotation
		self.rect = pygame.Rect(x, y, w, h)

	def goLeft(self):		
		if self.speed > 0.4 or self.speed < -0.4: self.rotation += 3
	
	def goRight(self):		
		if self.speed > 0.4 or self.speed < -0.4: self.rotation -= 3
	
	def move(self):
		if self.speed < 5: self.speed += 0.25
	
	def backup(self):
		if self.speed > -2: self.speed -= 0.15
	
	def update(self):
		if self.rotation < 0: self.rotation = 360 + self.rotation
		if self.rotation > 360: self.rotation = self.rotation - 360

		self.x = self.x + (math.sin(math.radians(Player.rotation))*self.speed)*-1
		self.y = self.y + (math.cos(math.radians(Player.rotation))*self.speed)*-1

		if self.speed >= 0.1:
			self.speed -= Player.speed/20
		elif self.speed <= -0.1:
			self.speed -= Player.speed/20
		else:
			self.speed = 0
		
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
		
cararea = 640
Player = player(30, 240, 32, 32, 0)
#==================================================
def DoGameUpdate():
	Player.update()

def draw():
	Surf.fill((100, 100, 100))

	pygame.draw.rect(Surf, (0,0,0,0), Player.rect, 1)
	Surf.blit(pygame.transform.rotate(carimg, Player.rotation), Player.rect)
	pygame.transform.rotate(carimg, 0)

#==================================================
while True:

	pygame.time.Clock().tick(48)
	
	for event in pygame.event.get():	
		if event.type == QUIT:	
			pygame.quit()
			sys.exit()

	if pygame.key.get_pressed()[pygame.K_w]: Player.move()
	if pygame.key.get_pressed()[pygame.K_s]: Player.backup()
	if pygame.key.get_pressed()[pygame.K_a]: Player.goLeft()
	if pygame.key.get_pressed()[pygame.K_d]: Player.goRight()
	
	draw()
	
	if InGame:
		DoGameUpdate()
		
	pygame.display.update()