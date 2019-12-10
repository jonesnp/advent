import curses
from curses import wrapper
from collections import namedtuple
import time

Dimensions = namedtuple('dimensions', 'height width')
Layer = namedtuple('layer', 'contents')
Layer.__lt__ = lambda self, other: len(list(filter(lambda x: x == 0, self.contents))) < len(
    list(filter(lambda x: x == 0, other.contents)))


with open('8.dat') as f:
    encoded = list(map(int, f.read()))

#encoded = [0,2,2,2,1,1,2,2,2,2,1,2,0,0,0,0]
#dimensions = Dimensions(2,2)

dimensions = Dimensions(6,25)
layer_size = dimensions.height * dimensions.width

layers = [Layer(encoded[i:i+layer_size])
          for i in range(0, len(encoded), layer_size)]

least_zero_layer = sorted(layers)[0]

ones = len(list(filter(lambda x: x == 1, least_zero_layer.contents)))
twos = len(list(filter(lambda x: x == 2, least_zero_layer.contents)))
print(ones * twos)

# Part 2

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.curs_set(False)
    
    for layer in reversed(layers):
        stdscr.addstr(dimensions.height,0, 'Layer: ' + str(n), curses.color_pair(1))
        for h in range(0,dimensions.height):
            for w in range(0,dimensions.width):
                idx = h * dimensions.width + w
                char = layer.contents[idx]
                if char != 2:
                    stdscr.addstr(h,w, str(char), curses.color_pair(char + 1))
        stdscr.refresh()
        #time.sleep(0.25)
    stdscr.getkey()

wrapper(main)