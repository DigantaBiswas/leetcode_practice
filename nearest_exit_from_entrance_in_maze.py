class Solution:

    def __init__(self):
        self.m, self.n = 0, 0
        self.bottom_exit_x = 0
        self.right_exit_y = 0
        self.index_map = {}
        self.explored_for_mapping = []
        self.step_count_explored_cells = []


    def get_adjacent_indices(self, i, j, m, n):
        adjacent_indices = []
        if i > 0:
            adjacent_indices.append((i - 1, j))
        if i + 1 < m+1:
            adjacent_indices.append((i + 1, j))
        if j > 0:
            adjacent_indices.append((i, j - 1))
        if j + 1 < n+1:
            adjacent_indices.append((i, j + 1))
        return adjacent_indices


    def get_steps(self, adjacent_indices, maze):
        for adjacent_indice in adjacent_indices:
            if adjacent_indice and adjacent_indice not in self.explored_for_mapping:
                if maze[adjacent_indice[0]][adjacent_indice[1]] != "+":
                    next_adjacent_indices = self.get_adjacent_indices(self.m, self.n, adjacent_indice[0], adjacent_indice[1])
                    self.explored_for_mapping.append(adjacent_indice)
                    if next_adjacent_indices:
                        self.index_map.update({
                            tuple(adjacent_indice): next_adjacent_indices
                        })
                        for next_adjacent_indice in next_adjacent_indices:
                            self.get_steps(next_adjacent_indices, maze)

    def get_exits(self, maze):
        exits = []
        for index_row, value_row in enumerate(maze):
            for index_column, value_column in enumerate(value_row):
                if value_column == ".":
                    exits.append((index_row, index_column))
        return exits

    def get_cost_from_each_movement(self, current_position, exit, maze):
        costs = []

        for position in self.index_map.get(current_position):
            if position not in self.step_count_explored_cells and maze[position[0]][position[1]] != "+":
                steps += 1

                steps = 0
                while position != exit:
                    self.get_cost_from_each_movement(position, 0, exit)

                costs.append(steps)
        cost = min(costs)
        return cost



    def nearest_exit(self, maze, entrance):
        self.m = len(maze)-1
        self.n = len(maze[0])-1

        self.get_steps([entrance], maze)

        exits = self.get_exits(maze)


        costs = []
        for exits in exits:
            cost = self.get_cost_from_each_movement([entrance], exit, maze)

            costs.append(cost)

        print(min(costs))





Solution().nearest_exit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2])
