import numpy as np

class NavigationAlgorithm:
    def __init__(self, start, goal):
        self.start = np.array(start)
        self.goal = np.array(goal)

    def calculate_distance(self, point_a, point_b):
        """Calculates the Euclidean distance between two points."""
        return np.linalg.norm(point_a - point_b)

    def heuristic(self, current_position):
        """Heuristic function for A* algorithm (Euclidean distance)."""
        return self.calculate_distance(current_position, self.goal)

    def a_star(self, grid):
        """A* pathfinding algorithm."""
        open_set = {tuple(self.start)}
        came_from = {}
        g_score = {tuple(self.start): 0}
        f_score = {tuple(self.start): self.heuristic(self.start)}

        while open_set:
            current = min(open_set, key=lambda pos: f_score.get(pos, float('inf')))
            if np.array_equal(current, self.goal):
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)

            for neighbor in self.get_neighbors(current, grid):
                tentative_g_score = g_score[current] + self.calculate_distance(np.array(current), np.array(neighbor))
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(np.array(neighbor))
                    open_set.add(neighbor)

        return None  # No path found

    def get_neighbors(self, position, grid):
        """Returns valid neighboring positions in the grid."""
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (position[0] + dx, position[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1] and grid[neighbor] == 0:
                neighbors.append(neighbor)
        return neighbors

    def reconstruct_path(self, came_from, current):
        """Reconstructs the path from start to goal."""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Return reversed path

# Example usage
if __name__ == "__main__":
    grid = np.array([[0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0]])

    nav_algo = NavigationAlgorithm(start=(0, 0), goal=(4, 4))
    path = nav_algo.a_star(grid)
    print("Path found:", path)
