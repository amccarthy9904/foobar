import numpy as np




class Rover:

    def getPos(self, grid_size: int, commands: [str]):

        def get_grid(size):
            return [[x for x in range(row*size, size + row*size)] for row in range(size)]
        def print_grid(grid):
            for row in grid: print(row)

        def get_transform(cmd):
            cmd = cmd.lower()
            if cmd == 'right': return (0,1)
            elif cmd == 'left': return (0,-1)
            elif cmd == 'down': return (1,0)
            elif cmd == 'up': return (-1,0)

        def is_inside(next, pos):
            new_pos = (pos[0] + next[0], pos[1] + next[1])
            if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
                return True
            else: return False

        grid = get_grid(grid_size)
        print_grid(grid)
        pos = (0,0)
        while commands:
            next = get_transform(commands.pop(0))
            if is_inside(next, pos):
                pos = (pos[0] + next[0], pos[1] + next[1])

        return grid[pos[0]][pos[1]]


    def test(self):
        cmds = ['RIGHT', 'DOWN', 'LEFT', 'LEFT', 'DOWN']
        size = 4
        print("Result: " + str(self.getPos(size, cmds)) + "\nExpected: 8")


        cmds = ['RIGHT', 'UP', 'DOWN', 'LEFT', 'DOWN', 'DOWN']
        size = 4
        print("Result: " + str(self.getPos(size, cmds)) + "\nExpected: 12")


rov = Rover()
rov.test()