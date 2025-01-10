from random import randint, choice
from time import sleep

def HuntAndKill(x, y):

    maze = [ [ [1, 1, 1, 1] for _ in range(x) ] for __ in range(y) ]
    mx = x
    my = y
    x_pos = randint(0, x - 1)
    y_pos = randint(0, y - 1)
    done = False
    counter = 0

    while not done:
        unvisited_neighbours = []
        for i, a in enumerate(maze[y_pos][x_pos]):
            if a == 1 and (
                (i == 0 and y_pos - 1 >= 0 and maze[y_pos - 1][x_pos] == [1, 1, 1, 1]) or
                (i == 1 and x_pos + 1 < mx and maze[y_pos][x_pos + 1] == [1, 1, 1, 1]) or
                (i == 2 and y_pos + 1 < my and maze[y_pos + 1][x_pos] == [1, 1, 1, 1]) or
                (i == 3 and x_pos - 1 >= 0 and maze[y_pos][x_pos - 1] == [1, 1, 1, 1])
            ):
                unvisited_neighbours.append(i)
        print(unvisited_neighbours)
        if len(unvisited_neighbours) > 0:
            the_rook = choice(unvisited_neighbours)
            if the_rook == 0:
                maze[y_pos][x_pos][0] = 0
                y_pos -= 1
                maze[y_pos][x_pos][2] = 0
            elif the_rook == 1:
                maze[y_pos][x_pos][1] = 0
                x_pos += 1
                maze[y_pos][x_pos][3] = 0
            elif the_rook == 2:
                maze[y_pos][x_pos][2] = 0
                y_pos += 1
                maze[y_pos][x_pos][0] = 0
            elif the_rook == 3:
                maze[y_pos][x_pos][3] = 0
                x_pos -= 1
                maze[y_pos][x_pos][1] = 0
        else:
            found = False
            for y in range(my):
                for x in range(mx):
                    if maze[y][x] == [1, 1, 1, 1]:
                        x_pos = x
                        y_pos = y
                        candidates = []
                        if y - 1 >= 0 and maze[y - 1][x] != [1, 1, 1, 1]: candidates.append(0)
                        if x + 1 < mx and maze[y][x + 1] != [1, 1, 1, 1]: candidates.append(1)
                        if y + 1 < my and maze[y + 1][x] != [1, 1, 1, 1]: candidates.append(2)
                        if x - 1 >= 0 and maze[y][x - 1] != [1, 1, 1, 1]: candidates.append(3)
                        if len(candidates) == 0: continue
                        chosen_candidate = choice(candidates)
                        if chosen_candidate == 0:
                            maze[y_pos][x_pos][0] = 0
                            maze[y_pos - 1][x_pos][2] = 0
                        elif chosen_candidate == 1:
                            maze[y_pos][x_pos][1] = 0
                            maze[y_pos][x_pos + 1][3] = 0
                        elif chosen_candidate == 2:
                            maze[y_pos][x_pos][2] = 0
                            maze[y_pos + 1][x_pos][0] = 0
                        elif chosen_candidate == 3:
                            maze[y_pos][x_pos][3] = 0
                            maze[y_pos][x_pos - 1][1] = 0
                        counter += 1
                        found = True
                        break
                if found: break
            else:
                print('все')
                print(counter)
                done = True

    symbs = {
        "[0, 0, 0, 0]": "┼",
        "[0, 0, 0, 1]": "├",
        "[0, 0, 1, 0]": "┴",
        "[0, 0, 1, 1]": "└",
        "[0, 1, 0, 0]": "┤",
        "[0, 1, 0, 1]": "│",
        "[0, 1, 1, 0]": "┘",
        "[0, 1, 1, 1]": "╵",
        "[1, 0, 0, 0]": "┬",
        "[1, 0, 0, 1]": "┌",
        "[1, 0, 1, 0]": "─",
        "[1, 0, 1, 1]": "╶",
        "[1, 1, 0, 0]": "┐",
        "[1, 1, 0, 1]": "╷",
        "[1, 1, 1, 0]": "╴",
        "[1, 1, 1, 1]": " ",
    }
    for row in maze:
        print("".join([symbs[str(block)] for block in row]))

    #for row in maze:
        #print(''.join([str(block) for block in row]))

    return maze
    
def walk():
    x = 10
    y = 10
    maze = HuntAndKill(x, y)
    player_char = '😀'
    p_x = 0
    p_y = 0 #player_x и player_y как координаты
    symbs = {
        "[0, 0, 0, 0]": "┼",
        "[0, 0, 0, 1]": "├",
        "[0, 0, 1, 0]": "┴",
        "[0, 0, 1, 1]": "└",
        "[0, 1, 0, 0]": "┤",
        "[0, 1, 0, 1]": "│",
        "[0, 1, 1, 0]": "┘",
        "[0, 1, 1, 1]": "╵",
        "[1, 0, 0, 0]": "┬",
        "[1, 0, 0, 1]": "┌",
        "[1, 0, 1, 0]": "─",
        "[1, 0, 1, 1]": "╶",
        "[1, 1, 0, 0]": "┐",
        "[1, 1, 0, 1]": "╷",
        "[1, 1, 1, 0]": "╴",
        "[1, 1, 1, 1]": " ",
        "[]": player_char,
    }
    for row in maze:
        print("".join([symbs[str(block)] for block in row]))
    while True:
        goto = int(input('Вверх - 0, вправо - 1, вниз - 2, влево - 3'))
        if not goto in [0, 1, 2, 3]: continue
        if maze[p_y][p_x][goto] == 0:
            if goto == 0: p_y -= 1
            elif goto == 1: p_x += 1
            elif goto == 2: p_y += 1
            elif goto == 3: p_x -= 1
            see = []
            for i, row in enumerate(maze):
                print(i, p_y)
                if i == p_y:
                    a = []
                    for j, block in enumerate(row):
                        if j == p_x:
                            a.append([])
                            print('оп')
                        else: a.append(block)
                    see.append(a)
                    print('ааа')
                else:
                    see.append(row)
            print(see)
            for row in see:
                print("".join([symbs[str(block)] for block in row]))
        if p_x == x and p_y == y: break
    print('ура. победа.')
    
walk()