from random import randint

from time import time

def update ():
	pass

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0
game_over = False # prevents the gameover screen from showing at start
succeed_time = 0

time_start = time()

for dot in range(0,10):
	actor = Actor("dot")
	actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
	dots.append(actor)

def draw():
	screen.fill("black")
	number = 1 
	for dot in dots:
		screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
		dot.draw() 
		number = number + 1
	for line in lines:
		screen.draw.line(line[0], line[1], (100, 0, 0))
	if game_over:
		screen.fill("blue") # Change background to pink.
		screen.draw.text("game over! :( ", topleft=(10,60), fontsize=60)
	else:
		if not succeed_time:
			screen.draw.text("time: " + str(time() - time_start), (5, 5))
		else:
			screen.draw.text("You succeeded! time: " + str(succeed_time - time_start), (5, 5))

def on_mouse_down(pos):
	global next_dot
	global lines
	global game_over
	global succeed_time
	if dots[next_dot].collidepoint(pos):
		if next_dot:
			lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
		next_dot = next_dot + 1
		if next_dot == 10:
			succeed_time = time()
	else:
		game_over = True
		# lines = []
		# next_dot = 0