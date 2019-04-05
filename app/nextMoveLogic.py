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
		head = Status.getHeadPosition(gamedata)
		board_size  = Status.getBoardSize(gamedata)
		direction = Status.getMyDirection(gamedata)
		if head['x'] == 0 and direction == 'left':
			return 'right'
		elif head['y'] == 0 and direction == 'up':
			return 'right'
		elif head['x'] == board_size['width']-1 and direction =='right':
			return 'right'
		elif head['y'] == board_size['height']-1 and direction == 'down':
			return 'right'
		else: return 'false'
		


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
		 return Assess.wallProximity(gamedata)
		 





