import pygame
import random


pygame.init()
pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
color = (177, 156, 217)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

welcome_image = pygame.image.load("welcome image.jpg")
welcome_image = pygame.transform.scale(welcome_image, (screen_width, screen_height))

main = pygame.image.load("main game.jpg")
main = pygame.transform.scale(main, (screen_width, screen_height))

end = pygame.image.load("end.jpg")
end = pygame.transform.scale(end, (screen_width, screen_height))

# Game Title
pygame.display.set_caption("Saap Ka Khel")
pygame.display.update()
clock = pygame.time.Clock()




def text_screen(text, color, x, y, z):
    font = pygame.font.SysFont(None, z)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Game specific variables
def welcome():
    exit_game = False
    gameWindow.fill(white)
    gameWindow.blit(welcome_image, (0,0))
    pygame.display.update()
    while not exit_game:
        text_screen("Namaskaar", black, 300,200, 70)
        text_screen("Saap Ka Khel Khelne Ke Liye Enter Dabaae", black, 10,300, 60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play_game()

    clock.tick(60)
    pygame.quit()
    quit()



def play_game():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 4
    velocity_y = 0

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 60


    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x, y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


    snk_list = []
    snk_length = 1
    while not exit_game:
        if game_over:
            gameWindow.blit(end, (0, 0))
            text_screen('Game Over.Firse Khelne Ho To Enter Dabaae!',black, 1, 15,49)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        play_game()

        else:
            gameWindow.fill(color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if velocity_y!=0:
                            velocity_x = 4
                            velocity_y = 0


                    if event.key == pygame.K_LEFT:
                        if velocity_y!=0:
                            velocity_x = - 4
                            velocity_y = 0

                    if event.key == pygame.K_UP:
                        if velocity_x!=0:
                            velocity_y = - 4
                            velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        if velocity_x!=0:
                            velocity_y = 4
                            velocity_x = 0


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:
                score += 1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5


            text_screen("Score: " + str(score * 10), red, 5, 5, 55)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []

            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_width:
                game_over = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load('hey_hey_hey.mp3')
                pygame.mixer.music.play()

            for a in snk_list:
                if snk_list.count(a)==2:
                    game_over = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('hey_hey_hey.mp3')
                    pygame.mixer.music.play()


            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)


        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()



