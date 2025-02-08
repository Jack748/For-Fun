import curses
import random 

curses.initscr()
win = curses.newwin(30,30,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

score = 0

snake = [[4,10],[4,9]]
food = (random.randint(1,28), random.randint(1,28))

win.addch(food[0], food[1], '#')

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
	win.addstr(0, 2, 'score' + str(score) + ' ')
	win.timeout(150 - (len(snake)) // 5  + len(snake) // 10 % 120)

	prev_key = key
	event = win.getch()
	key = event if event != -1 else prev_key

	if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP, ESC]:
		key = prev_key


	y = snake[0][0]
	x = snake[0][1]
	if key == curses.KEY_DOWN:
		y += 1
	if key == curses.KEY_UP:
		y -= 1

	if key == curses.KEY_RIGHT:
		x += 1

	if key == curses.KEY_LEFT:
		x -= 1

	

	if y == 0:
	    y = 28
	if y == 29:	 
	    y = 1
	if x == 0:
	    x = 28
	if x == 29:
		x = 1

	snake.insert(0, (y,x))


	if snake[0] in snake[1:]:  break

	if snake[0] == food:
		score +=1
		food = ()
		while food == ():
		  food = (random.randint(1,28), random.randint(1,28))
		  if food in snake:
		  	food = ()
		win.addch(food[0],food[1], '#')

	else:
		last = snake.pop()
		win.addch(last[0], last[1], ' ')

	win.addch(snake[0][0], snake[0][1], '0')



	for c in snake[1:]:
		win.addch(c[0],c[1], '*')

	win.addch(food[0],food[1], '#')


curses.endwin()
print("Final score = ",score)