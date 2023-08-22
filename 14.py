import os
import re
import tkinter as tk
import time
import ast


# TK Applet to display the sand states nicely
class SandFallApp:
    def __init__(self, root, sand_state_data):
        self.root = root
        self.root.title("SAND")

        self.sand_state_data = sand_state_data

        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="top", fill="both", expand=True)

        self.x_scrollbar = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.x_scrollbar.pack(side="bottom", fill="x")
        self.canvas.config(xscrollcommand=self.x_scrollbar.set)

        self.y_scrollbar = tk.Scrollbar(root, command=self.canvas.yview)
        self.y_scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=self.y_scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.current_frame = 0
        self.paused = False

        self.create_grid()
        self.create_buttons()
        self.display_frames()

    def create_grid(self):
        grid_data = self.sand_state_data[self.current_frame]

        rows = len(grid_data)
        cols = len(grid_data[0])
        cell_size = 3

        for i in range(rows):
            for j in range(cols):
                char = grid_data[i][j]
                x = j * cell_size
                y = i * cell_size
                self.canvas.create_text(x, y, text=char, anchor="nw", font=("Arial", 5))

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side="top")

        play_button = tk.Button(button_frame, text="Play", command=self.play)
        play_button.pack(side="left")

        pause_button = tk.Button(button_frame, text="Pause", command=self.pause)
        pause_button.pack(side="left")

        restart_button = tk.Button(button_frame, text="Restart", command=self.restart)
        restart_button.pack(side="left")

    def play(self):
        self.paused = False
        self.display_frames()

    def pause(self):
        self.paused = True

    def restart(self):
        self.current_frame = 0
        self.display_frames()

    def display_frames(self):
        if self.current_frame < len(self.sand_state_data) and not self.paused:
            self.canvas.delete("all")
            self.create_grid()
            self.root.after(1000, self.display_frames)
            self.current_frame += 1


# file reading function for puzz input
def read_file_as_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

# read the txt file and convert it to a list of tuples
def parse_puzz_input(file_path):
    puzz_input = read_file_as_list('14_input.txt')

    puzz_input = [x.split(' -> ') for x in puzz_input]

    for i in range(len(puzz_input)):
        puzz_input[i] = [ast.literal_eval(f'({x})') for x in puzz_input[i]]

    return puzz_input


def get_max_values(puzz_input):
    # get the max value of each 'wall'
    max_values = [tuple(max(item) for item in zip(*tuples_list)) for tuples_list in puzz_input]
    #print(max_values)
    # do the same for this to get the overall max values to define our grid
    all_max = tuple(max(item) for item in zip(*max_values))

    return all_max



puzz_input = parse_puzz_input('14_input.txt')


get_max_values(puzz_input)


def initialise_grid(puzz_input):
    grid_limits = get_max_values(puzz_input)

    # add padding so sand can fall around the walls
    grid_lim_x = grid_limits[0] + 5

    # create first line of grid by unpacking str of len = max x_limit
    init_grid = [*'.'*grid_lim_x]

    #do the same for the y limit
    grid_lim_y = grid_limits[1] + 5
    init_grid = [init_grid]*grid_lim_y

    for i in range(len(puzz_input)):
        for j in range(len(puzz_input[i])-1):
            wall_coord_1 = puzz_input[i][j]
            wall_coord_2 = puzz_input[i][j+1]
            print(wall_coord_1,  wall_coord_2)

            #determine is it vert or horiz wall
            # horizontal (x coords diff)
            if wall_coord_1[0] != wall_coord_2[0]:

                # need to get min and max in right order to index properly
                big_coord = max(wall_coord_1[0], wall_coord_2[0])
                small_coord = min(wall_coord_1[0], wall_coord_2[0])

                init_grid[wall_coord_1[1]][small_coord:big_coord] = \
                    [*'#' * abs(wall_coord_1[0] - wall_coord_2[0])]

                print(init_grid[wall_coord_1[1]])

            else: # vertical (y coords diff)
                for k in range(abs(wall_coord_1[1] - wall_coord_2[1])):
                    init_grid[k][wall_coord_1[0]] = '#'

            print(f'x length: {len(init_grid[0])}')
            assert len(init_grid[0]) <= grid_lim_x, 'x limit exceeded'

    return init_grid

init_grid = initialise_grid(puzz_input)

video_input = [

 #       [x[0:100] for x in init_grid[0:100]]
    init_grid
    ,
    # Add more frames as needed
]

root = tk.Tk()
app = SandFallApp(root, video_input)
root.mainloop()














video_input_1 = [*'.'*10]

video_input_1 = [video_input_1]*10

video_input_a = [

        video_input_1
    ,
    #
    #     video_input_1
    # ,
    #
    #     video_input_1
    # ,
    # Add more frames as needed
]



a =[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']]

video_input_2 = [
    [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ],
    [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ],
    # Add more frames as needed
]

root = tk.Tk()
app = SandFallApp(root, video_input)
root.mainloop()








