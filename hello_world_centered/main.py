import curses

def center(length, width):
	return (width - length) // 2

def curses_fn(stdscr):
	stdscr.clear()
	y_max, x_max = stdscr.getmaxyx()

	text = 'Hello World!'
	stdscr.addstr(center(1, y_max), center(len(text), x_max), text)
	stdscr.refresh()

	while True:
		ch = stdscr.getch()
		if chr(ch) == 'q':
			break

if __name__ == '__main__':
	curses.wrapper(curses_fn)
