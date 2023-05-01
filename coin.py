import pygame
import random

# initialize pygame
pygame.init()

# set up the window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# set up the font
font = pygame.font.SysFont(None, 30)

# set up the player
player_size = 50
player_pos = [window_width / 2, window_height - 2 * player_size]

# set up the obstacles
obstacle_size = 50
obstacle_pos = [random.randint(0, window_width - obstacle_size), 0]
obstacle_list = [obstacle_pos]

# set up the coins
coin_size = 20
coin_pos = [random.randint(0, window_width - coin_size), 0]
coin_list = [coin_pos]

# set up the game loop
game_over = False
score = 0
clock = pygame.time.Clock()
fps = 60

while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]

    # move the obstacles and coins
    for i, obstacle_pos in enumerate(obstacle_list):
        if obstacle_pos[1] >= 0 and obstacle_pos[1] < window_height:
            obstacle_pos[1] += 10
        else:
            obstacle_list.pop(i)

        # check for collision with the player
        if obstacle_pos[1] >= player_pos[1] and obstacle_pos[1] <= player_pos[1] + player_size:
            if obstacle_pos[0] >= player_pos[0] and obstacle_pos[0] <= player_pos[0] + player_size:
                game_over = True
                break

    for i, coin_pos in enumerate(coin_list):
        if coin_pos[1] >= 0 and coin_pos[1] < window_height:
            coin_pos[1] += 5
        else:
            coin_list.pop(i)

        # check for collision with the player
        if coin_pos[1] >= player_pos[1] and coin_pos[1] <= player_pos[1] + player_size:
            if coin_pos[0] >= player_pos[0] and coin_pos[0] <= player_pos[0] + player_size:
                coin_list.pop(i)
                score += 10

                # add new coin
                new_coin_pos = [random.randint(0, window_width - coin_size), 0]
                coin_list.append(new_coin_pos)

    # add new obstacle
    if len(obstacle_list) < 5:
        new_obstacle_pos = [random.randint(0, window_width - obstacle_size), 0]
        obstacle_list.append(new_obstacle_pos)

    # draw the background
    window.fill(white)

    # draw the player
    pygame.draw.rect(window, green, (player_pos[0], player_pos[1], player_size, player_size))

    # draw the obstacles
    for obstacle_pos in obstacle_list:
        pygame.draw.rect(window, black, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

    # draw the coins
    for coin_pos in coin_list:
        pygame.draw.circle(window, red, (coin_pos[0] + coin_size / 2, coin_pos[1] + coin_size / 2), coin_size / 2)

    # draw the score
    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, [0, 0])

    # update the display
    pygame.display.update()

    # set the clock tick
    clock.tick(fps)
pygame.quit()
