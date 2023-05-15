import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the game window
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the game window
pygame.display.set_caption("Snake Game")

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the block size and the clock speed
BLOCK_SIZE = 10
clock = pygame.time.Clock()

# Define a function to draw the snake
def draw_snake(snake_head, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
    pygame.draw.rect(screen, RED, [snake_head[0], snake_head[1], BLOCK_SIZE, BLOCK_SIZE])

# Define a function to move the snake
def move_snake(snake_head, snake_body, snake_direction):
    if snake_direction == 'up':
        snake_head[1] -= BLOCK_SIZE
    elif snake_direction == 'down':
        snake_head[1] += BLOCK_SIZE
    elif snake_direction == 'left':
        snake_head[0] -= BLOCK_SIZE
    elif snake_direction == 'right':
        snake_head[0] += BLOCK_SIZE

    # Move the snake by adding the new head position to the beginning of the body list and removing the last block of the body
    snake_body.insert(0, list(snake_head))
    snake_body.pop()

    return snake_body

# Define a function to generate food randomly
def generate_food():
    food_x = round(random.randrange(0, WINDOW_SIZE[0]-BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, WINDOW_SIZE[1]-BLOCK_SIZE) / 10.0) * 10.0
    return [food_x, food_y]

# Define a function to check for collisions
def check_collision(snake_head, snake_body, food_position):
    # Check for collisions with the walls
    if snake_head[0] < 0 or snake_head[0] >= WINDOW_SIZE[0]:
        return True
    elif snake_head[1] < 0 or snake_head[1] >= WINDOW_SIZE[1]:
        return True

    # Check for collisions with the body
    for block in snake_body[1:]:
        if snake_head == block:
            return True

    # Check for collisions with the food
    if snake_head == food_position:
        food_position = generate_food()
        snake_body.append(list(snake_body[-1]))
    return False

# Initialize the snake and the food position
snake_head = [200, 200]
snake_body = [[200, 210], [200, 220], [200, 230]]
food_position = generate_food()

# Initialize the score
score = 0

# Initialize the snake direction
snake_direction = 'up'

# Set the font for the score text
font = pygame.font.Font('freesansbold.ttf', 18)

# Start the game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
            elif event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'

    # Move the snake
    snake_body = move_snake(snake_head, snake_body, snake_direction)

    # Check for collisions
    if check_collision(snake_head, snake_body, food_position):
        game_over = True

    # Check if the snake has eaten the food
    if snake_head == food_position:
        food_position = generate_food()
        snake_body.append(list(snake_body[-1]))
        score += 10

    # Fill the background with white
    screen.fill(WHITE)

    # Draw the snake and the food
    draw_snake(snake_head, snake_body)
    pygame.draw.rect(screen, BLACK, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])

    # Draw the score text
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, [10, 10])

    # Update the display
    pygame.display.update()

    # Set the game clock
    clock.tick(10)

# Quit Pygame
pygame.quit()
