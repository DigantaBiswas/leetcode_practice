class Solution:

    def __init__(self):
        self.m, self.n = 0, 0
        self.index_map = {}
        self.explored_for_mapping = []

    def get_adjacent_indices(self, i, j, m, n):
        adjacent_indices = []
        if i > 0:
            adjacent_indices.append((i - 1, j))
        if i + 1 < m + 1:
            adjacent_indices.append((i + 1, j))
        if j > 0:
            adjacent_indices.append((i, j - 1))
        if j != n and j + 1 < n + 1:
            adjacent_indices.append((i, j + 1))
        return adjacent_indices

    def populate_adjecent_node_dict(self, positions):
        for position in positions:
            if position not in self.explored_for_mapping:
                self.explored_for_mapping.append(tuple(position))
                next_points = self.get_adjacent_indices(position[0], position[1], self.m, self.n )
                self.index_map.update({
                    tuple(position): next_points
                })
                if next_points:
                    self.populate_adjecent_node_dict(next_points)

    def get_exit_indexes(self, maze, entrance):
        border_indexes = []
        for row_index, row_value in enumerate(maze):
            for column_index, column_value in enumerate(row_value):
                if  (row_index, column_index) != entrance:
                    if column_value == ".":
                        if row_index == 0 or row_index == self.m:
                            border_indexes.append((row_index, column_index))
                        elif column_index == self.n or column_index == 0:
                            border_indexes.append((row_index, column_index))
        return border_indexes

    def nearest_exit(self, maze, entrance):
        self.m = len(maze) - 1
        self.n = len(maze[0]) - 1

        border_list = self.get_exit_indexes(maze, tuple(entrance))
        self.populate_adjecent_node_dict([entrance])

        path_list_to_borders = {}


        # for border in border_list:
        path_remaining = [(entrance)]
        step_count = 0
        visited_list = []

        while path_remaining:
            current_position = path_remaining.pop(0)

            if not current_position in visited_list:
                visited_list.append(current_position)
                adjecent_cells = self.index_map.get(tuple(current_position))

                if tuple(current_position) in border_list:
                    path_list_to_borders.update({tuple(current_position):step_count})
                    continue
                step_count += 1
                for adjecent_cell in adjecent_cells:
                    if maze[adjecent_cell[0]][adjecent_cell[1]] != "+":
                        path_remaining.append(adjecent_cell)
        final_step_counts = [value for key, value in path_list_to_borders.items()]
        if final_step_counts:
           print(min(final_step_counts))
        else:
            print("-1")



Solution().nearest_exit([["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
,[0,1])
