import curses
import time

DELAY = 0.5

f = open('log.txt', 'w')

def curses_fn(stdscr):
	stdscr.timeout(1000)
	curses.curs_set(False)
	stdscr.clear()
	stdscr.refresh()

	while True:
		ch = stdscr.getch()
		f.write(str(ch) + '\n')

		if ch == ord('q'):
			break

if __name__ == '__main__':
	curses.wrapper(curses_fn)
	f.close()
