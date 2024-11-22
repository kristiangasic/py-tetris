import pygame
import random

# Initialisiere Pygame
pygame.init()

# Bildschirmkonfiguration
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0),    # Red
]

# Spielfeld
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Figuren (Tetrominoes)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],        # O
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 0], [1, 1, 1]],  # T
]

# Klasse für das Spielfeld
class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_shape = None
        self.current_color = None
        self.current_position = [0, GRID_WIDTH // 2 - 1]
        self.score = 0
        self.level = 1
        self.spawn_new_shape()
        self.game_over = False

    def spawn_new_shape(self):
        self.current_shape = random.choice(SHAPES)
        self.current_color = random.choice(COLORS)
        self.current_position = [0, GRID_WIDTH // 2 - len(self.current_shape[0]) // 2]
        if not self.valid_move(self.current_shape, self.current_position):
            self.game_over = True

    def valid_move(self, shape, position):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    px, py = position[1] + x, position[0] + y
                    if px < 0 or px >= GRID_WIDTH or py >= GRID_HEIGHT or self.grid[py][px]:
                        return False
        return True

    def lock_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    px, py = self.current_position[1] + x, self.current_position[0] + y
                    self.grid[py][px] = self.current_color
        self.clear_lines()
        self.spawn_new_shape()

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = len(self.grid) - len(new_grid)
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(lines_cleared)] + new_grid
        self.score += lines_cleared * 100
        if lines_cleared > 0:
            self.level = self.score // 500 + 1

    def move(self, dx, dy):
        new_position = [self.current_position[0] + dy, self.current_position[1] + dx]
        if self.valid_move(self.current_shape, new_position):
            self.current_position = new_position

    def rotate(self):
        rotated_shape = [[self.current_shape[y][x] for y in range(len(self.current_shape))]
                         for x in range(len(self.current_shape[0]) - 1, -1, -1)]
        if self.valid_move(rotated_shape, self.current_position):
            self.current_shape = rotated_shape

# Zeichnet das Spielfeld
def draw_grid(tetris):
    for y, row in enumerate(tetris.grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    for y, row in enumerate(tetris.current_shape):
        for x, cell in enumerate(row):
            if cell:
                px, py = tetris.current_position[1] + x, tetris.current_position[0] + y
                pygame.draw.rect(screen, tetris.current_color, (px * BLOCK_SIZE, py * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Hauptspiel
def main():
    clock = pygame.time.Clock()
    tetris = Tetris()
    fall_time = 0

    while True:
        screen.fill(BLACK)
        draw_grid(tetris)

        if tetris.game_over:
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        fall_speed = 500 - (tetris.level * 50)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > fall_speed:
            tetris.move(0, 1)
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    tetris.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    tetris.move(0, 1)
                elif event.key == pygame.K_UP:
                    tetris.rotate()

        if not tetris.valid_move(tetris.current_shape, [tetris.current_position[0] + 1, tetris.current_position[1]]):
            tetris.lock_shape()

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
