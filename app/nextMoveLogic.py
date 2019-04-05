import random

class Status(object):

	def getHeadPosition(gamedata):
		me = gamedata['you']		
		my_position = me['body']
		head = my_position[0]
		return head

	def getMyLength(gamedata):
		me = gamedata['you']		
		my_position = me['body']
		if my_position[0] == my_position[1] == my_position[2]:
			return 1
		elif my_position[1] == my_position[2]:
			return 2
		else: return len(my_position)

	def getMyDirection(gamedata):
		me = gamedata['you']		
		my_position = me['body']
		if Status.getMyLength(gamedata) == 1:
			return 'none'
		elif my_position[0]['x'] > my_position[1]['x']:
			return 'right'
		elif my_position[0]['x'] < my_position[1]['x']:
			return 'left'
		elif my_position[0]['x'] == my_position[1]['x'] and my_position[0]['y'] < my_position[1]['y']:
			return 'up'
		else: return 'down'


	def getHealth(gamedata):
		pass

	def getBoardSize(gamedata):
		board_height = gamedata['board']['height']
		board_width = gamedata['board']['width']
		dimensions = {'height': board_height, 'width': board_width}
		return dimensions

	def getFoodPositions(gamedata):
		pass

	def getSnakesPositions(gamedata):
		pass


class Assess(object):

	def wallProximity(gamedata):
		"""returns proximity to a wall
		either parallel to, head-on or corner"""
		head = Status.getHeadPosition(gamedata)
		board_size  = Status.getBoardSize(gamedata)
		direction = Status.getMyDirection(gamedata)
		height = board_size['height'] - 1
		width = board_size['width'] - 1
		#corners				
		if head['x'] == 0 and head['y'] == 0:
			return {'type': 'corner', 'identifier': 'top left', 'direction': direction}
		elif head['x'] == 0  and head['y'] == height:
			return {'type': 'corner', 'identifier': 'bottom left', 'direction': direction}
		elif head['x'] == width  and head['y'] == 0:
			return {'type': 'corner', 'identifier': 'top right', 'direction': direction}
		elif head['x'] == width  and head['y'] == height:
			return {'type': 'corner', 'identifier': 'bottom right', 'direction': direction}
		#headons
		elif head['x'] == 0 and direction == 'left':
			return {'type': 'head-on', 'identifier': 'left', 'direction': direction}
		elif head['y'] == 0 and direction == 'up':
			return {'type': 'head-on', 'identifier': 'top', 'direction': direction}
		elif head['x'] == width and direction == 'right':
			return {'type': 'head-on', 'identifier': 'right', 'direction': direction}
		elif head['y'] == height and direction == 'down':
			return {'type': 'head-on', 'identifier': 'bottom', 'direction': direction}
		#parrallels
		elif head['x'] == 0 and direction == 'up' or head['x'] == 0 and direction == 'down':
			return {'type': 'parallel', 'identifier': 'left', 'direction': direction}
		elif head['y'] == 0 and direction == 'right' or head['y'] == 0 and direction =='left':
			return {'type': 'parallel', 'identifier': 'top', 'direction': direction}
		elif head['x'] == width and direction =='down' or head['x'] == width and direction == 'up':
			return {'type': 'parallel', 'identifier': 'right', 'direction': direction}
		elif head['y'] == height and direction == 'left' or head['y'] == height and direction == 'right':
			return {'type': 'parallel', 'identifier': 'bottom', 'direction': direction}
		else: return False

	def ownBodyProximity(gamedata):
		pass
		


	def killPossible(gamedata):
		pass

	def smallerSnakeNearby(gamedata):
		pass

	def biggerSnakeNearby(gamedata):
		pass

	def foodNearby(gamedata):
		pass


class Action(object):

	def avoidDeath():
		pass

	def chaseFood():
		pass

	def fleeSnake():
		pass

	def chaseSnake():
		pass

class Decision(object):

	def chooseBestOption(gamedata):
		options = ['up', 'down', 'right', 'left']
		current_direction = Status.getMyDirection(gamedata)
		#first go
		if current_direction == 'none':
			choice = random.choice(options)
		#remove opposite direction
		if current_direction == 'up':
			options.remove('down')
		if current_direction == 'down':
			options.remove('up')
		if current_direction == 'right':
			options.remove('left')
		if current_direction == 'left':
			options.remove('right')
		#no danger keep going
		if Assess.wallProximity(gamedata) == False:
			choice = current_direction
		#in a corner
		elif Assess.wallProximity(gamedata)['type'] == 'corner':
			options.remove(current_direction)
			if Assess.wallProximity(gamedata)['identifier'][0] == 't' and Assess.wallProximity(gamedata)['identifier'][4] == 'l':
				if 'up' in options:
					choice = 'down'
				else: choice = 'right'
			elif Assess.wallProximity(gamedata)['identifier'][0] == 't' and Assess.wallProximity(gamedata)['identifier'][4] == 'r':
				if 'up' in options:
					choice = 'down'
				else: choice = 'left'
				
		#headon
		elif Assess.wallProximity(gamedata)['type'] == 'head-on':
			options.remove(current_direction)
			choice = random.choice(options)
		#parallel
		elif Assess.wallProximity(gamedata)['type'] == 'parallel':			
			choice = current_direction	
		else: print("shit")
		print(options)
		return choice

		 





