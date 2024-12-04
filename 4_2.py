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

for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        for a in [[-1, -1, -1, 1], [-1, 1, 1, 1], [1, 1, 1, -1], [1, -1, -1, -1]]:
            if grid[i][j] != 'A': continue
            if grid[i+a[0]][j+a[1]] != 'M': continue
            if grid[i+a[2]][j+a[3]] != 'M': continue
            if grid[i-a[0]][j-a[1]] != 'S': continue
            if grid[i-a[2]][j-a[3]] != 'S': continue
            count += 1
print(count)
