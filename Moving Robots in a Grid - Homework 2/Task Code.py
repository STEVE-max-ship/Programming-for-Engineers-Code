columns,rows,cycles = input().split()
X1,Y1,direction1 = input().split()
commands1 = input().split()
X2,Y2,direction2 = input().split()
commands2 = input().split()
commands = []
rows,columns,cycles,X1,Y1,direction1,X2,Y2,direction2 = int(rows),int(columns),int(cycles),int(X1),int(Y1),int(direction1),int(X2),int(Y2),int(direction2)
for i in range(len(commands1)):
    if commands1[i].isdigit():
        commands1[i] = int(commands1[i])
for i in range(len(commands2)):
    if commands2[i].isdigit():
        commands2[i] = int(commands2[i])
for i in range(cycles):
    index_one = i % len(commands1)
    index_two = i % len(commands2)
    commands.append(commands1[index_one])
    commands.append(commands2[index_two])
#print(commands)
heading1 = direction1
heading2 = direction2
visited1 = []
visited2 = []
robot1_pos = [X1,Y1]
robot2_pos = [X2,Y2]
def is_within_grid(next_pos, columns, rows):# Checks if a position is within the grid, returns true if it is
    x,y = next_pos
    if 1 <= x <= columns and 1 <= y <= rows:
        return True
    else:
        return False
def is_robotless(robot1_pos, robot2_pos, next_pos):# Checks if any robots have occupied the next cell, returns false if they have
    X1,Y1 = robot1_pos
    X2,Y2 = robot2_pos
    x,y = next_pos
    if (X1 == x and Y1 == y) or (X2 == x and Y2 == y):
        return False
    else:
        return True
def turn(current_heading, where_to_turn):# turns a robot?
    if where_to_turn == 'L':
        return (current_heading + 1) % 4
    elif where_to_turn == 'R':
        return (current_heading - 1) % 4
def straight1(next_cell):
    global visited1
    global robot1_pos
    visited1.append(next_cell)
    robot1_pos = next_cell
    return robot1_pos
def straight2(next_cell):
    global visited2
    global robot2_pos
    visited2.append(next_cell)
    robot2_pos = next_cell
    return robot2_pos
def next_pos(current_heading, current_position):
    x,y = current_position
    if current_heading == 0:
        return [x+1,y]
    if current_heading == 1:
        return [x,y+1]
    if current_heading == 2:
        return [x-1,y]
    if current_heading == 3:
        return [x,y-1]
def main_movement(commands, heading1, heading2,visited1,visited2,robot1_pos,robot2_pos):
    visited1.append(robot1_pos)
    visited2.append(robot2_pos)
    for index, instruction in enumerate(commands):
        if index % 2 == 0:
            if str(instruction).isdigit():
                for i in range(instruction):
                    next_cell = next_pos(heading1, robot1_pos)
                    if is_within_grid(next_cell, columns, rows) is True and is_robotless(robot1_pos, robot2_pos, next_cell) is True:
                        robot1_pos = straight1(next_cell)
                    else:
                        break
            else:
                heading1 = turn(heading1, instruction)

        else:
            if str(instruction).isdigit():
                for i in range(instruction):
                    next_cell = next_pos(heading2, robot2_pos)
                    if is_within_grid(next_cell, columns, rows) is True and is_robotless(robot2_pos, robot1_pos, next_cell) is True:
                        robot2_pos = straight2(next_cell)
                    else:
                        break
            else:
                heading2 = turn(heading2, instruction)
    #print(visited1)
    #print(visited2)
    combined_list = visited1 + visited2
    unique_sublists = []
    for sublist in combined_list:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    #print(len(unique_sublists))
    return len(unique_sublists)
print(main_movement(commands, heading1, heading2,visited1,visited2,robot1_pos,robot2_pos))
