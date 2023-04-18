import pygame
import math
from queue import PriorityQueue

WIDTH = 800
# setting the dimensions of display
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algo")

# setting up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == RED

    def is_notVisited(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == BLUE

    def reset(self):
        self.color = WHITE

    def makeVisited(self):
        self.color = RED

    def makenotVisited(self):
        self.color = GREEN

    def makeObstacle(self):
        self.color = BLACK

    def make_end(self):
        self.color = BLUE

    def make_start(self):
        self.color = ORANGE

    def make_path(self):
        self.color = YELLOW

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        # checking up down left and right and mark the unvisited neighbours
        self.neighbours = []
        # moving down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle():
            self.neighbours.append(grid[self.row + 1][self.col])
        # up
        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():
            self.neighbours.append(grid[self.row - 1][self.col])
        # right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_obstacle():
            self.neighbours.append(grid[self.row][self.col+1])
        # left
        if self.col > 0 and not grid[self.row][self.col-1].is_obstacle():
            self.neighbours.append(grid[self.row][self.col-1])

    # less than

    def __lt__(self, other):
        return False

# making hyrestic function h() L is the quickest distance cause we can't move diagonally in pixel


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

# i need a data structure to hold this


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    # putting 0 as initial fscore
    open_set.put((0, count, start))
    came_from = {}
    # initializing all these with infinity as iniital
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    # hyrestic should be default L path
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            # make path
            return True
        for neighbour in current.neighbours:
            temp_g_score = g_score[current]+1
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + \
                    h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.makenotVisited()
        draw()
        if current != start:
            current.makeVisited()
    return False


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            # creating a instance
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, GRAY, (j*gap, 0), (j*gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

# knows mouse position


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col


def main(win, width):
    ROWS = 50
    # make grid returns 2d array of spot
    grid = make_grid(ROWS, width)

    start = None
    end = None
    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        # events are what happened during the runtime i.e if a mouse is clicked or a keyboard button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            # if mouse is pressed on left
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.makeObstacle()
            # if mouse is pressed on right
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                if spot == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    # passing draw function as a actual argument
                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start, end)

    pygame.quit()


main(WIN, WIDTH)
