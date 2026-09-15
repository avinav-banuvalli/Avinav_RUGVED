# Discrete Motion Model & Trajectory Tracking of a Robot

import math as math
import matplotlib.pyplot as plt

# pose is in (x, y, theta) 
# angle types in degrees
# start pose = (0, 0, 0)
DT = 0.1 # seconds, Euler integration step size

# Function to calculate pose 
def compute_pose (pose, name, value):
    x, y, theta = pose

    if name == "forward":
        x += value * math.cos(theta)
        y += value * math.sin(theta)
    elif name == "left":
        theta += math.radians(value)
    elif name == "right":
        theta -= math.radians(value)

    return (x, y, theta)

# Function to calculate pose using  linear velocity, angular velocity and time duration
def compute_pose_velocity(pose, v, omega, duration):
    x, y, theta = pose
    n_steps = duration/DT
    n = round(n_steps)
    intermediate_pose = []
    for i in range(n):
        x += v * math.cos(theta) * DT
        y += v * math.sin(theta) * DT
        theta += math.radians(omega) * DT
        intermediate_pose.append((x, y, theta))
    return intermediate_pose

# Function to run the commands
def run_commands(commands, start_pose):
    current_pose = start_pose
    # Creating empty list with start_pose at 0th index
    history = [start_pose]
    for command in commands:
        parts = command.split()
        name = parts[0]
        if parts[0] == "move":
            v = float(parts[1])
            omega = float(parts[2])
            duration = float(parts[3])
        else:
            value = float(parts[1])
        initial_pose = current_pose
        if name == "move":
            poses = compute_pose_velocity(current_pose, v, omega, duration)
            current_pose = poses[-1]
            history.extend(poses)
        else:
            current_pose = compute_pose(current_pose, name, value)
            history.append(current_pose)
        print(f"Initial Pos: {initial_pose} | Executing: {command} | Final Pos: {current_pose}")
    return history

# Function to plot the points on the graph
def plot_trajectory(history):
    xs = [pose[0] for pose in history]
    ys = [pose[1] for pose in history]
    thetas = [pose[2] for pose in history]
    us = [math.cos(theta) for theta in thetas]
    vs = [math.sin(theta) for theta in thetas]

    # Creates a figure and axes in a single call
    fig, ax = plt.subplots(figsize = (10, 5))
    ax.plot(xs, ys, marker = '.', color = 'black', label = "Path")
    ax.plot(xs[0], ys[0], marker = 'o', color = 'green', label = "Start")
    ax.plot(xs[len(xs) - 1], ys[len(ys) - 1], marker = 'o', color = 'red', label = "End")
    # Makes small arrows at each (x,y) and at each change in angle
    ax.quiver(xs, ys, us, vs, angles = 'xy', scale = 30, width = 0.01, headwidth = 1, headlength = 3)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    # Pad is used to leave some space between heading and graph
    ax.set_title("Robot Trajectory", pad = 20)
    # To mske the x-axis and y axis equal in dimension
    ax.set_aspect('equal')
    ax.legend(loc = 'upper left')
    #To put grids in the graph
    ax.grid(True)
    plt.tight_layout()
    plt.show()

# Function to read the file
def read_commands_file():
    filename = input("Enter the command file name:")
    with open(filename) as file:
        lines = file.readlines()
    # Creating empty list to input values after reading 
    commands = []
    for line in lines:
        # Strip removes whitespaces, tabs, and \n
        cleaned = line.strip()
        if cleaned:
            commands.append(cleaned)
    return commands

# Initializing start position as origin
start_pose = (0, 0, 0)
commands = read_commands_file()
history = run_commands(commands, start_pose)
plot_trajectory(history)