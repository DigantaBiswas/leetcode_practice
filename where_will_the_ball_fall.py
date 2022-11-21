class Solution:
    ball_finish_index_list = []

    def calculate_ball_position(self, current_position_value, left_position_value, right_position_value,
                                current_position):
        if current_position_value == 1:
            if current_position_value == right_position_value:
                current_position = current_position + 1
            else:
                current_position = None
        if current_position_value == -1:
            if current_position_value == left_position_value:
                current_position = current_position - 1
            else:
                current_position = None
        return current_position

    def findBall(self, grid):

        number_of_balls = len(grid[0])
        left_wall_index = -1
        right_wall_index = number_of_balls
        end_line = len(grid)

        for balls in range(0, number_of_balls):
            step_count = 0
            current_position = balls
            while step_count != end_line:
                if current_position - 1 != left_wall_index and current_position + 1 != right_wall_index:
                    current_position_value = grid[step_count][current_position]
                    if not current_position - 1 == left_wall_index:
                        left_position_value = grid[step_count][current_position - 1]
                    else:
                        self.ball_finish_index_list.append(-1)
                        break
                    if not current_position + 1 == right_wall_index:
                        right_position_value = grid[step_count][current_position + 1]
                    else:
                        current_position = -1
                        break

                    current_position = self.calculate_ball_position(current_position_value, left_position_value,
                                                                    right_position_value, current_position)
                    if current_position == None:
                        current_position = -1
                        break


                elif current_position - 1 == left_wall_index and current_position + 1 != right_wall_index:
                    current_position_value = grid[step_count][current_position]
                    left_position_value = 1
                    right_position_value = grid[step_count][current_position + 1]
                    current_position = self.calculate_ball_position(current_position_value, left_position_value,
                                                                    right_position_value, current_position)
                    if current_position == None:
                        current_position = -1
                        break

                elif current_position + 1 == right_wall_index and current_position - 1 != left_wall_index:
                    current_position_value = grid[step_count][current_position]
                    left_position_value = grid[step_count][current_position - 1]
                    right_position_value = -1
                    current_position = self.calculate_ball_position(current_position_value, left_position_value,
                                                                    right_position_value, current_position)
                    if current_position == None:
                        current_position = -1
                        break
                else:
                    current_position_value = grid[step_count][current_position]
                    left_position_value = 1
                    right_position_value = -1
                    current_position = self.calculate_ball_position(current_position_value, left_position_value,
                                                                    right_position_value, current_position)
                    if current_position == None:
                        current_position = -1
                        break
                step_count += 1
            self.ball_finish_index_list.append(current_position)
        return self.ball_finish_index_list



Solution().findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])
