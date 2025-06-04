from random import randint


grid = [["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","#","~",],
        ["~","#","~","#","#","#","#","#","~","~",],
        ["~","#","~","~","~","~","~","~","~","~",],
        ["~","#","~","#","#","#","#","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","#","#","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],]
schiff_getroffen = "X"
wasser_getroffen = "O"
wasser = "~"
schiff = "#"


def render_grid(l_grid):
    for row in l_grid:
        for field in row:
            print(field,end="")
        print()

from random import choice
alle_felder = {(x, y) for x in range(10) for y in range(10)}
def shoot_on_board(l_grid):
    feld = choice(list(alle_felder))
    alle_felder.remove(feld)
    return feld
    

def check_end_game(l_grid : list[list[str]]):
    for row in l_grid:
        for field in row:
            if field == schiff:
             return False
    return True



render_grid(grid)

Versuche = 0

while not check_end_game(grid):
    x,y = shoot_on_board(grid)
    Versuche +=1
    if grid[y][x] == schiff:
        grid[y][x] = schiff_getroffen
    if grid[y][x] == wasser:
        grid[y][x] = wasser_getroffen
    # Clear cmd
    print("\033[H\033[J", end="")
    render_grid(grid)

print (f"Alle Schiffe versenkt in {Versuche} Versuchen")

