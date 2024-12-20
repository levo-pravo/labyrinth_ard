from create_maze import HuntAndKill
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
            for row in maze:
                print(maze.index(row), p_y - 1)
                if maze.index(row) == p_y - 1:
                    a = []
                    for block in row:
                        if row.index(block) == p_x - 1:
                            a.append([])
                            print('оп')
                        else: a.append(block)
                    see.append(a)
                    print('ааа')
                else:
                    for block in row:
                        see.append(block)
            print(see)
            for row in see:
                print("".join([symbs[str(block)] for block in row]))
        if p_x == x and p_y == y: break
    print('ура. победа.')
    
walk()