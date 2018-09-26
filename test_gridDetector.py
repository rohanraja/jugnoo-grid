import unittest
from grid_cell_detection import detect_cell
import json

class TestDetectGrid(unittest.TestCase):

    def test_grid_Detection(self):
        with open('grid.json', 'r') as fp:
            grid = json.load(fp)

        target = [360,350]
        outP = detect_cell(grid["x"], grid["y"], grid["origin"], target)
        print("Grid Cell Location -", outP)
        self.assertEqual(outP[0], 1)
        self.assertEqual(outP[1], 1)



if __name__ == '__main__':
    unittest.main()
