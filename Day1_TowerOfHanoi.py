# It consists of three rods and a number of disks of different sizes, which can slide onto any rod.
# The disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
#
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
# 3) No disk may be placed on top of a smaller disk.
#
# New line
# Test2
#The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n − 1, where n is the number of disks.

A = [3, 2, 1]
B = []
C = []


def printtest():
    print('Hello')

def move(n, source, target, auxiliary):
    if n:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C, '##############', sep='\n')

        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)


# initiate call from source A to target C with auxiliary B
move(3, A, C, B)
