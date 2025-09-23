import pygame
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    """Renders text to the screen."""
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    """Draws the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome_screen():
    """Displays the welcome screen and waits for user input."""
    gameWindow.fill(white)
    text_screen("Welcome to Snakes!", black, 260, 250)
    text_screen("Press Enter to Play", black, 240, 300)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

def gameloop():
    """The main game loop, managing the game's state and logic."""
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 450
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1

    # High score file handling without 'os' module
    try:
        with open("highscore.txt", "r") as f:
            highscore = int(f.read())
    except FileNotFoundError:
        # If the file does not exist, set high score to 0
        highscore = 0
    
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60

    while not exit_game:
        # State: Game Over
        if game_over:
            # Save the high score before displaying
            if score > highscore:
                highscore = score
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            
            gameWindow.fill(white)
            text_screen("Game Over!", red, screen_width / 4, screen_height / 3)
            text_screen(f"Score: {score}", black, screen_width / 4, screen_height / 2)
            text_screen(f"High Score: {highscore}", black, screen_width / 4, screen_height / 2 + 50)
            text_screen("Press Enter to Play Again", black, screen_width / 4 - 25, screen_height / 2 + 100)
            pygame.display.update()

            # Wait for user input to restart or quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop() # Restart the game

        # State: Playing
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    # Prevent the snake from reversing its direction
                    if event.key == pygame.K_RIGHT and velocity_x == 0:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT and velocity_x == 0:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP and velocity_y == 0:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN and velocity_y == 0:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10 
                           
            snake_x += velocity_x
            snake_y += velocity_y

            # Check for collision with food
            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                snake_length += 5
                    
            gameWindow.fill(white)
            text_screen(f"Score: {score}  Highscore: {highscore}", red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            
            # Check for self-collision
            if head in snake_list[:-1]:
                game_over = True

            # Check for boundary collision
            if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.display.update()
            clock.tick(fps)
            
    pygame.quit()
    quit()

# Start the game with the welcome screen
welcome_screen()