import jwt
import datetime


class EncoderJWT():

	def __init__(self, private_key, expiration, device, algorithm):
		self.FILE_PATH_PRIVATE_KEY = private_key 
		self.DEVICE = device
		self.ALGORITHM = algorithm
		self.EXP = datetime.timestamp(datetime.datetime.now() - datetime.timedelta(expiration))

 
	def getJWToken():
		jwt.encode({"exp":self.EXP}, self.PRIVATE_KEY, self.ALGORITHM)

