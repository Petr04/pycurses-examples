import curses
import time

def center(length, width):
	return (width - length) // 2

menu_entries = ['hello', 'world', '1qaz2wsx', 'qwertyuiop[]asdfghjkl;zxcvbnm,./']
menu_title = 'Menu'
delay = 0.7

def curses_fn(stdscr):
	stdscr.nodelay(True)
	stdscr.clear()
	curses.curs_set(False)
	y_max, x_max = stdscr.getmaxyx()

	# Adding a menu window
	height = len(menu_entries) + 2
	width = 0
	for i in menu_entries:
		new_width = len(i)
		if new_width > width:
			width = new_width

	if len(menu_title) + 2 > width:
		width = len(menu_title) + 4
	else:
		width += 3

	menu = curses.newwin(height, width, center(height, y_max), center(width, x_max))
	menu.erase()
	menu.border()
	menu.addstr(0, 1, ' {} '.format(menu_title))

	for i, text in enumerate(menu_entries, 1):
		menu.addstr(i, 2, text)
	menu.addch(1, 1, '*')
	stdscr.refresh()
	menu.refresh()

	cur_entry = 0
	keybinds = {curses.KEY_UP: -1, curses.KEY_DOWN: +1}
	time_printed = None
	while True:
		if time_printed:
			if time.time() - time_printed >= delay:
				stdscr.move(0, 0)
				stdscr.clrtoeol()
				stdscr.refresh()

				time_printed = None

		key = stdscr.getch()

		if key == -1:
			continue

		if key in keybinds:
			last_entry = cur_entry
			cur_entry_new = cur_entry + keybinds[key]
			if cur_entry_new in range(len(menu_entries)):
				cur_entry = cur_entry_new

				menu.addch(cur_entry+1, 1, '*')
				menu.addch(last_entry+1, 1, ' ')
				menu.refresh()

		elif key == 10: # Enter
			stdscr.addstr(0, 0, menu_entries[cur_entry])
			time_printed = time.time()
			stdscr.refresh()

		elif chr(key) == 'q':
			break

if __name__ == '__main__':
	curses.wrapper(curses_fn)
