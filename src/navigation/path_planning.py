import numpy as np
from navigation_algorithm import NavigationAlgorithm

class PathPlanning:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def plan_path(self):
        """Plans a path from start to goal using A* algorithm."""
        nav_algo = NavigationAlgorithm(self.start, self.goal)
        path = nav_algo.a_star(self.grid)
        return path

    def optimize_path(self, path):
        """Optimizes the path by removing unnecessary waypoints."""
        optimized_path = [path[0]]
        for i in range(1, len(path) - 1):
            if not self.is_collinear(optimized_path[-1], path[i], path[i + 1]):
                optimized_path.append(path[i])
        optimized_path.append(path[-1])
        return optimized_path

    def is_collinear(self, p1, p2, p3):
        """Checks if three points are collinear."""
        return (p2[1] - p1[1]) * (p3[0] - p2[0]) == (p3[1] - p2[1]) * (p2[0] - p1[0])

# Example usage
if __name__ == "__main__":
    grid = np.array([[0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0],
                     [0, 0, 0 , 0, 0],
                     [0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0]])

    path_planner = PathPlanning(grid, start=(0, 0), goal=(4, 4))
    path = path_planner.plan_path()
    optimized_path = path_planner.optimize_path(path)
    print("Optimized path:", optimized_path)
