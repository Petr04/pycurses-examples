import curses

def center(length, width):
	return (width - length) // 2

menu_entries = ['lol', 'keck', '4ebureck']

def main(stdscr):
	stdscr.clear()
	curses.curs_set(0)
	y_max, x_max = stdscr.getmaxyx()

	# Adding a menu window
	height = len(menu_entries)
	width = max([len(i) for i in menu_entries])

	l_begin = []
	for i in zip((height, width), (y_max, x_max)):
		l.append(center(i[0], i[1]))

	l_end = []
	# for i in l_begin:
	# To be continued... :)


	menu = curses.newwin(center(height, y_max), center(width, x_max), )
	menu.clear()
	stdscr.addstr(0, 0, str(menu.getmaxyx()))

	# Drawing menu
	for i, text in enumerate(menu_entries):
		stdscr.addstr(i, 0, text)
		menu.addstr(i, 0, text)
	stdscr.refresh()
	menu.refresh()

	while True:
		ch = stdscr.getch()
		if chr(ch) == 'q':
			break

if __name__ == '__main__':
	curses.wrapper(main)
