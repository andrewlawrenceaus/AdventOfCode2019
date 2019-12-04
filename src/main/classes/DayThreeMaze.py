class DayThreeMaze:
    grid = []
    position = [0, 0]
    crossover_points = []

    def __init__(self, size, starting_position):
        self.grid = [[int(0) for x in range(size)] for y in range(size)]
        self.position = starting_position

    def move_right(self, no_moves):
        for k in range(0, no_moves):
            self.position[1] += 1
            self.move()

    def move_down(self, no_moves):
        for k in range(0, no_moves):
            self.position[0] += 1
            self.move()

    def move(self):
        self.grid[self.position[0]][self.position[1]] += 1
        if self.grid[self.position[0]][self.position[1]] > 1:
            self.crossover_points.append(self.position)