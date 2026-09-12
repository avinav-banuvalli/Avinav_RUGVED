import math as math
import matplotlib.pyplot as plt

# pose is in (x, y, theta) 
# angle types in degrees
# start pose = (0, 0, 0)
def compute_pose (pose, name, value):
    x, y, theta = pose

    if name == "forward":
        x += value * math.cos(theta)
        y += value * math.sin(theta)
    elif name == "left":
        theta += math.radians(value)
    elif name == "right":
        theta = theta - math.radians(value)

    return (x, y, theta)

def run_commands(commands, start_pose):
    current_pose = start_pose
    history = [start_pose]
    for command in commands:
        parts = command.split()
        name = parts[0]
        value = float(parts[1])
        initial_pose = current_pose
        current_pose = compute_pose(current_pose, name, value)
        print(f"Initial Pos: {initial_pose} | Executing: {command} | Final Pos: {current_pose}")
        history.append(current_pose)
    # print(history)
    return history

def plot_trajectory(history):
    xs = [pose[0] for pose in history]
    ys = [pose[1] for pose in history]
    thetas = [pose[2] for pose in history]
    us = [math.cos(theta) for theta in thetas]
    vs = [math.sin(theta) for theta in thetas]

    fig, ax = plt.subplots(figsize = (10, 5))
    ax.plot(xs, ys, marker = '.', color = 'black', label = "Path")
    ax.plot(xs[0], ys[0], marker = 'o', color = 'green', label = "Start")
    ax.plot(xs[len(xs) - 1], ys[len(ys) - 1], marker = 'o', color = 'red', label = "End")
    ax.quiver(xs, ys, us, vs, angles = 'xy')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Robot Trajectory", pad = 20)
    ax.set_aspect('equal')
    ax.legend(loc = 'upper left', bbox_to_anchor = (1.02, 1))
    ax.grid(True)
    plt.tight_layout()
    plt.show()

def get_commands():
    n = int(input("Enter the number of commands:"))
    commands = []
    for i in range(n):
        command = input(f"Enter command {i + 1}:")
        commands.append(command)
    return commands 

def read_commands_file():
    filename = input("Enter the command file name:")
    with open(filename) as file:
        lines = file.readlines()
    commands = []
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            commands.append(cleaned)
    return commands

choice = input("Type 't' to enter the commands manually, or 'f' to read the commands from a file:")
if choice == choice.strip().lower() == "t":
    commands = get_commands()
elif choice == choice.strip().lower() == "f":
    commands = read_commands_file()
else:
    print("Error!!, Enter 't' or 'f'")

start_pose = (0, 0, 0)
history = run_commands(commands, start_pose)
plot_trajectory(history)