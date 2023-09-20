import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game board
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 'X'
game_over = False

# Function to draw the grid lines
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(window, WHITE, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)
        pygame.draw.line(window, WHITE, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), 2)

# Function to draw X and O
def draw_symbols():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            symbol = board[row][col]
            if symbol == 'X':
                pygame.draw.line(window, RED, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), 5)
                pygame.draw.line(window, RED, (col * CELL_SIZE, (row + 1) * CELL_SIZE), ((col + 1) * CELL_SIZE, row * CELL_SIZE), 5)
            elif symbol == 'O':
                pygame.draw.circle(window, BLUE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5, 5)

# Function to check for a win
def check_win():
    # Check rows, columns, and diagonals
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Function to check for a tie
def check_tie():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == '':
                return False
    return True

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if board[row][col] == '':
                    board[row][col] = current_player
                    if current_player == 'X':
                        current_player = 'O'
                    else:
                        current_player = 'X'

            if check_win():
                game_over = True
            elif check_tie():
                game_over = True

    window.fill(BLACK)
    draw_grid()
    draw_symbols()
    
    if game_over:
        font = pygame.font.Font(None, 36)
        if check_win():
            text = font.render(f'Player {current_player} wins!', True, WHITE)
        else:
            text = font.render('It\'s a tie!', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text, text_rect)
    
    pygame.display.update()
