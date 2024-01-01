from gpt4all import GPT4All
from pathlib import Path

model_path = Path("D:\Tool\GPT\Model")
class GPT:
	def __init__(self, model="mistral-7b-instruct-v0.1.Q4_0.gguf"):
		self.model = GPT4All(model, model_path)

	def __str__(self):
		return self.model

	def Message(self, text):
		return self.model.generate(text)
		
"""
	def Command(self, text, cxt):
		S = ""
		for token in self.model.generate(text, streaming=True):

def Debug():
	#from Fnc.gptA import *
	AI = GPT("mpt-7b-chat-merges-q4_0.gguf")
	print(AI.Message("人在做天在看芹奈又在跟蹤為師了啦"))
"""