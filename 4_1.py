file = open("4.txt", "r")
text = file.read()
file.close()

grid = []
count = 0

for line in text.split("\n"):
    if not line: break
    grid.append([])
    for char in line:
        grid[-1].append(char)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if ((i + a*3) < 0) or ((i + a*3) >= len(grid)): continue
                if ((j + b*3) < 0) or ((j + b*3) >= len(grid[0])): continue
                if grid[i][j] != 'X': continue
                if grid[i + a][j + b] != 'M': continue
                if grid[i + a*2][j + b*2] != 'A': continue
                if grid[i + a*3][j + b*3] != 'S': continue
                count += 1

print(count)
