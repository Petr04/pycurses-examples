import curses
from time import sleep

def curses_fn(stdscr):
	stdscr.clear()
	stdscr.curs_set(0)

	h, w = stdscr.getmaxyx()

	while True:
		for i in range(0, h):
			for j in range(0, w):
				if (i, j) == (h-1, w-1):
					continue

				stdscr.addstr(i, j, '\u2588')
		stdscr.refresh()
		# sleep(0.01)
		# stdscr.clear()
		# stdscr.refresh()
		# sleep(0.01)

if __name__ == '__main__':
	curses.wrapper(curses_fn)
