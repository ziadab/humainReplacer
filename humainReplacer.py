try:
	import apiai
except:
	import sys
	sys.exit('Sorry but you need to install the apiai model to use this script')

import json

class HumainReplacer(object):
	"""docstring for HumainReplacer"""
	def __init__(self):
		self.client_access_token = "a19e56e58cd74938b112cf6ee248a12b"
		self.ai = apiai.ApiAI(self.client_access_token)

	def replay(self,msg):
		# Hir each time you start a new request 
		self.request = self.ai.text_request()
		self.request.lang = "en"
		self.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
		self.request.query = msg
		server_responce = self.request.getresponse()
		json_responce = json.load(server_responce)
		print('Humain Replacer:',json_responce['result']["fulfillment"]["speech"])


humainReplacer = HumainReplacer()
while True:
	try:
		msg = str(input("You: "))
		humainReplacer.replay(msg)
	except KeyboardInterrupt:
		print("\nSee you soon !!")
		break	
	