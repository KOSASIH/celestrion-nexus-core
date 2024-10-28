import numpy as np

class HazardDetection:
    def __init__(self, grid):
        self.grid = grid

    def detect_hazards(self, path):
        """Detects hazards along the path."""
        hazards = []
        for i in range(len(path) - 1):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                hazard_position = (path[i][0] + dx, path[i][1] + dy)
                if 0 <= hazard_position[0] < self.grid.shape[0] and 0 <= hazard_position[1] < self.grid.shape[1] and self.grid[hazard_position] == 1:
                    hazards.append(hazard_position)
        return hazards

# Example usage
if __name__ == "__main__":
    grid = np.array([[0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0]])

    hazard_detector = HazardDetection(grid)
    path = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    hazards = hazard_detector.detect_hazards(path)
    print("Hazards detected:", hazards)
