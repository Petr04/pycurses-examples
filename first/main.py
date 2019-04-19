import curses
from time import sleep

def main(stdscr):
	stdscr.clear()

	for i in range(0, 10):
		v = i-10
		stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v), curses.A_BLINK)

	i += 1

	stdscr.refresh()
	while True:
		ch = stdscr.getch()
		stdscr.addstr(i, 0, 'ord({}) == {}'.format(chr(ch), str(ch)))

		if chr(ch) == 'q':
			break

if __name__ == '__main__':
	curses.wrapper(main)
