# import pygame
# import time
# import random

# # Initialize pygame
# pygame.init()

# # Define colors
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)

# # Define display dimensions
# dis_width = 600
# dis_height = 400

# # Set up the display
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game')

# # Set the clock speed for the game
# clock = pygame.time.Clock()

# # Define the snake's speed
# snake_speed = 15
# snake_block = 10

# # Set up the font
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)

# # Function to display the player's score
# def display_score(score):
#     value = score_font.render("Score: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])

# # Function to draw the snake on the screen
# def draw_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# # Function to display a message on the screen
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])

# # The main game loop
# def game_loop():
#     game_over = False
#     game_close = False

#     # Initial position of the snake
#     x1 = dis_width / 2
#     y1 = dis_height / 2

#     # Change in position
#     x1_change = 0
#     y1_change = 0

#     # Snake's body list
#     snake_list = []
#     length_of_snake = 1

#     # Random position for the food
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

#     while not game_over:

#         while game_close:
#             dis.fill(blue)
#             message("You lost! Press Q-Quit or C-Play Again", red)
#             display_score(length_of_snake - 1)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         game_loop()

#         # Handling arrow key inputs
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0

#         # If the snake goes out of bounds, the game ends
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)

#         # Draw the food
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

#         # Add the new head position of the snake
#         snake_head = []
#         snake_head.append(x1)
#         snake_head.append(y1)
#         snake_list.append(snake_head)

#         if len(snake_list) > length_of_snake:
#             del snake_list[0]

#         # Check if the snake collides with itself
#         for x in snake_list[:-1]:
#             if x == snake_head:
#                 game_close = True

#         draw_snake(snake_block, snake_list)
#         display_score(length_of_snake - 1)

#         pygame.display.update()

#         # Check if the snake has eaten the food
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             length_of_snake += 1

#         # Set the speed of the snake
#         clock.tick(snake_speed)

#     pygame.quit()
#     quit()

# # Start the game
# game_loop()
