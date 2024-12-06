#saba diasamidze

# to add:
#	track the exit path.
#	make maze inputable.
#	visualize maze path.
#	error handling.
#	support multiple maze exits.


### Logic:


#this block defines the maze
maze = [
	['#', '#', '#', '#', 'O', '#', '#'],
	['#', ' ', ' ', '#', ' ', ' ', '#'],
	['#', '#', ' ', '#', '#', ' ', '#'],
	['#', ' ', ' ', ' ', ' ', ' ', '#'],
	['#', ' ', '#', '#', '#', '#', '#'],
	['#', ' ', ' ', ' ', ' ', ' ', '#'],
	['#', '#', '#', 'X', '#', '#', '#']
	]


#this block defines the maze entrance	
for i in range(len(maze)):
	for j in range(len(maze)):
		if maze[i][j] == 'O':
			start_position = (i, j)
			break;
			
#threads is a list of tuples containing all starting positions in current iterration
threads = [start_position]


#we take all the starting positions and move them if there is no wall blocking them, after that we mark its previos position with '+'
for i in threads:
	if maze[i[0]][i[1] - 1] == ' ':
		threads.append((i[0], i[1] - 1))
		maze[i[0]][i[1] - 1] = '+'
	if maze[i[0]][i[1] + 1] == ' ':
		threads.append((i[0], i[1] + 1))
		maze[i[0]][i[1] + 1] = '+'
	if maze[i[0] + 1][i[1]] == ' ':
		threads.append((i[0] + 1, i[1]))
		maze[i[0] + 1][i[1]] = '+'
	if maze[i[0] - 1][i[1]] == ' ':
		threads.append((i[0] - 1, i[1]))
		maze[i[0] - 1][i[1]] = '+'
	
	
	#win condition
	if maze[i[0]][i[1] - 1] == 'X' or maze[i[0]][i[1] + 1] == 'X' or maze[i[0] + 1][i[1]] == 'X' or maze[i[0] - 1][i[1]] == 'X':
		print('maze solved after:', len(threads), 'moves')
		print('exit location:', threads[-1])
		break
		
	
