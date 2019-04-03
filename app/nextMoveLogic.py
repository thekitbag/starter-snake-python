class GameStatus(object):
	def getPosition(gameData):
		me = gameData['you']		
		my_position = me['body']
		return my_position

	def getHealth(gamedata):
		pass

	def getBoardSize(gamedata):
		pass

	def getFoodPositions(gamedata):
		pass

	def getSnakesPositions(gamedata):
		pass

class DecideNextMove(object):
	def avoidWalls(gamedata):
		board_size = GameStatus.getBoardSize(gamedata)


