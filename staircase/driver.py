from staircase import staircaseBottomUp
from staircase import staircaseTopDown
from sys import argv

if __name__ == '__main__':
    print(staircaseBottomUp(int(argv[1])))
    print(staircaseTopDown(int(argv[1])))
