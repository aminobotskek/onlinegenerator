import requests
class Client():
	def __init__(self):
		self.api="https://onlinegenerator.org/ajax"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def random_name(self,amount:int=2,gender:str=None):
		if gender:return requests.get(f"{self.api}/name?amount={amount}&gender={gender}",headers=self.headers).json()
		else:return requests.get(f"{self.api}/name?amount={amount}&gender=",headers=self.headers).json()
	def random_password(self,amount,length):
		return requests.get(f"{self.api}/password?amount={amount}&length={length}",headers=self.headers).json()
	def random_uid(self,amount):
		return requests.get(f"{self.api}/uuid?amount={amount}",headers=self.headers).json()
	def random_person(self,amount):
		return requests.get(f"{self.api}/person?amount={amount}",headers=self.headers).json()
	def random_mac_address(self,amount):
		return requests.get(f"{self.api}/mac-address?amount={amount}",headers=self.headers).json()
	def random_user_agent(self,amount):
		return requests.get(f"{self.api}/user-agent?amount={amount}",headers=self.headers).json()
	def random_username(self,amount):
		return requests.get(f"{self.api}/username?amount={amount}",headers=self.headers).json()