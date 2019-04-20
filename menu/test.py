import curses

def curses_fn(stdscr):
	stdscr.erase()
	stdscr.addch(0, 0, '*')
	stdscr.refresh()

	key = stdscr.getch()
	stdscr.addstr(0, 0, '{} {}'.format(key, chr(key)))
	if key == curses.KEY_ENTER:
		stdscr.addstr(1, 0, 'You pushed ENTER')

	stdscr.refresh()

	stdscr.getch()

if __name__ == '__main__':
	curses.wrapper(curses_fn)
