from queue import PriorityQueue
import math
import pygame

pygame.init()
WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Visualizer")

WHITE = (255, 255, 255)
RED = (209, 0, 0)
BLUE = (8, 44, 201)
GREEN = (31, 209, 0)
TURQUOISE = (0, 255, 195)
PINK = (209, 17, 110)
GREY = (79, 79, 79)

#Square object: Each square is a node
class Node:


    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows


    def is_closed(self):
        return self.color == BLUE

    def is_open(self):
        return self.color == WHITE

    def is_barrier(self):
        return self.color == RED

    def is_start(self):
        return self.color == PINK

    def is_target(self):
        return self.color == TURQUOISE

    def reset(self):
        return self.color == WHITE

    def make_closed(self):
        self.color = BLUE

    def make_open(self):
        self.color = WHITE

    def make_barrier(self):
        self.color = RED
    
    def make_start(self):
        self.color = PINK

    def make_target(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = GREEN

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def _lt_(self, other):
        return False

def heuristic_value(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j, gap, rows)
			grid[i].append(node)
	return grid

def draw_lines(WIN, rows, width):
    gap = width / WIN
    for i in range (rows):
        pygame.draw.line(WIN, GREY, (0, i * gap), (width, i * gap))
    for j in range (rows):
        pygame.draw.line(WIN, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in(grid):
        for node in(row):
            node.draw(win)
    draw_lines(win, rows, width)
    pygame.display.update()

def get_clicked_position(pos, rows, width):
    gap = width//rows
    y, x = pos

    row = y//gap
    col = x//gap

    return row, col
    
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
        
    #Start and end position
    start = None
    end = None

    run = True
    started = False


    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]: #LMB
                position = pygame.mouse.get_pos()
                row, col = get_clicked_position(position, ROWS, width)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()
                elif not end:
                    end = node
                    end.make_target
                elif node != start and node != end:
                    node.make_barrier
            elif pygame.mouse.get_pressed()[2]: #RMB
                position = pygame.mouse.get_pos()
                row, col = get_clicked_position(position, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
    pygame.quit()

main(WIN, WIDTH)