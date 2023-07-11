import jwt

class KeyEngine():

	def __init__(self, device, days):
		self.PASS = "cf612795c141baae734bb281d7013955016e6f1f19166792de7a03bd34ca952f"
		self.DEVICE = device
		self.ALGORITHM = "HS256"
		self.EXP =  days


	def create(self):
		return jwt.encode({"exp": self.EXP,"device":self.DEVICE},self.PASS, algorithm = self.ALGORITHM, headers={"typ":"JWT"})


	def decoder(self, jwtString):
		print(jwtString)
		print(self.PASS)
		return jwt.decode(jwtString, self.PASS, algorithms = [self.ALGORITHM])
