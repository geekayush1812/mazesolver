from window import Window
from maze import Maze


def main():
    num_rows = 8
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x, screen_y, "Maze solver")

    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, window, 10)
    has_solved = maze.solve()

    print("Solved" if has_solved else "Not solved")
    window.wait_for_close()


main()
