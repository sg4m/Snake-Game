import pygame
import time
import random
while True:
	snake_speed = 15

	#Window size
	window_x = 800
	window_y = 600

#defining colors
	black = pygame.Color(0, 0, 0)
	white = pygame.Color(255, 255, 255)
	red = pygame.Color(255, 0, 0)
	green = pygame.Color(0, 255, 0)
	blue = pygame.Color(0, 0, 255)

#Initialise game and window
	pygame.init()

	pygame.display.set_caption("Gamborino's Snake game")
	game_window = pygame.display.set_mode((window_x, window_y))

#FPS
	fps = pygame.time.Clock()

#snake position
	snake_position = [100, 50]

#body
	snake_body = [ [100, 50],
				[90, 50],
				[80, 50],
				[70, 50]
			]
#fruit posiiton
	fruit_position = [random.randrange(1, (window_x//10)) * 10,
					random.randrange(1, (window_y//10)) * 10]
	fruit_spawn = True

	#snake direction

	direction = 'RIGHT'
	change_to = direction

	#initial score
	score = 0

	#Score function
	def show_score(choice, color, font, size):

		
		score_font = pygame.font.SysFont(font, size)
		
		score_surface = score_font.render('Score : ' + str(score), True, color)
		
		score_rect = score_surface.get_rect()
		
		game_window.blit(score_surface, score_rect)


	#game over
	def game_over():

		
		font = pygame.font.SysFont('Arial', 50)
		
		game_over_surface = font.render('Your Score is : ' + str(score), True, red)
		
		game_over_rect = game_over_surface.get_rect()
		
		game_over_rect.midtop = (window_x/2, window_y/4)
		
		game_window.blit(game_over_surface, game_over_rect)
		pygame.display.flip()
		
		time.sleep(2)
		pygame.quit()
		
		quit()

	#Main
	while True:

		#Keys
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					change_to = 'UP'
				if event.key == pygame.K_DOWN:
					change_to = 'DOWN'
				if event.key == pygame.K_LEFT:
					change_to = 'LEFT'
				if event.key == pygame.K_RIGHT:
					change_to = 'RIGHT'
		#Simultaneus keys 
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'

		if direction == 'UP':
			snake_position[1] -= 10
		if direction == 'DOWN':
			snake_position[1] += 10
		if direction == 'LEFT':
			snake_position[0] -= 10
		if direction == 'RIGHT':
			snake_position[0] += 10

		#Snake grow
		snake_body.insert(0, list(snake_position))
		if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
			score += 20
			fruit_spawn = False
		else:
			snake_body.pop()
			
		if not fruit_spawn:
			fruit_position = [random.randrange(1, (window_x//10)) * 10,
							random.randrange(1, (window_y//10)) * 10]
			
		fruit_spawn = True
		game_window.fill(black)
		
		for pos in snake_body:
			pygame.draw.rect(game_window, green, pygame.Rect(
			pos[0], pos[1], 10, 10))
			
		pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

		#Conditions for game over
		if snake_position[0] < 0 or snake_position[0] > window_x-10:
			game_over()
		if snake_position[1] < 0 or snake_position[1] > window_y-10:
			game_over()
		
		#Snake touching
		for block in snake_body[1:]:
			if snake_position[0] == block[0] and snake_position[1] == block[1]:
				game_over()
		
		#Showing the score in game
		show_score(1, white, 'Arial', 20)
		
		pygame.display.update()
		fps.tick(snake_speed)
		font = pygame.font.SysFont('Arial', 30)