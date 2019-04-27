import curses
import time

DELAY = 0.5

def curses_fn(stdscr):
	stdscr.nodelay(True)
	curses.curs_set(False)
	stdscr.clear()
	stdscr.refresh()

	last_time = None
	while True:
		ch = stdscr.getch()

		if ch != -1:
			stdscr.addstr(0, 0, '{} {}\n'.format(ch, str(ch)))
			stdscr.refresh()
			last_time = time.time()

		if last_time and (time.time() - last_time >= DELAY):
			stdscr.move(0, 0)
			stdscr.clrtoeol()
			stdscr.addstr(0, 0, 'No key pressed\n')
			stdscr.refresh()

if __name__ == '__main__':
	curses.wrapper(curses_fn)
