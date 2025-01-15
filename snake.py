import pygame
import time
import random

pygame.init()

# define colours
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# define window size
display_width = 500
display_height = 500

# create game window and name it
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('what the fuck even')

# define pygame clock for game speed
clock = pygame.time.Clock()

# define size and speed of snake
snake_block = 10
snake_speed = 15

# define score and font(???) because chatgpt told me to
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# score display
def score(score):
    value = score_font.render("score " + str(score), True, black)
    dis.blit(value, [0, 0])

# function to draw snake on the screen
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# function for gameover message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

# main game loop
def gameloop():
    game_over = False
    game_closed = False

    # initial position of snake
    x1 = display_width / 2
    y1 = display_height / 2

    # initial movement direction of the snake
    x1_change = 0
    y1_change = 0

    # create empty list for snake and set initial length
    snake_list = []
    length_of_snake = 1

    # generate the initial position of the apple
    applex = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    appley = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # game loop for handling events
    while not game_over:

        # check if game over (snake hit wall or itself)
        while game_closed:
            dis.fill(blue)
            message("you are bad . q for quit c for restart", red)
            score(length_of_snake - 1)
            pygame.display.update()

            # check for input to quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_closed = False
                    if event.key == pygame.K_c:
                        # Reset the game state
                        gameloop()

        # user input (movement | wasd)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        # check if snake hit wall
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_closed = True

        # update snake position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # draw apple
        pygame.draw.rect(dis, yellow, [applex, appley, snake_block, snake_block])

        # update snake list and check if it has eaten apple
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # check if snake has collided with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_closed = True

        # draw snake
        snake(snake_block, snake_list)

        # display score
        score(length_of_snake - 1)

        pygame.display.update()

        # check if snake has eaten food
        if x1 == applex and y1 == appley:
            applex = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            appley = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake = length_of_snake + 1

        # set speed of the game (snake movement speed)
        clock.tick(snake_speed)

    # quit pygame when game is over
    pygame.quit()
    quit()

# run game
gameloop()
