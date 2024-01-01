import discord

from discord.ext import commands
from discord.ext import tasks
from datetime import *
from Fnc.gptA import *

intents		= discord.Intents.default()
intents.message_content = True
intents.members = True

bot_ID = ""
Token = ""

class MyBot(commands.Bot):
	
	def __init__(self, command_prefix, intent):
		commands.Bot.__init__(self, command_prefix=command_prefix, intents=intent)
		self.AI = GPT()

	async def on_ready(self):
		self.message1 = f"正在使用身分: {self.user}({self.user.id})"
		self.message2 = f"正在使用身分: {self.user}({self.user.id})"
		print(self.message1)
		await self.change_presence(activity=discord.Activity(name="學習", type=0))

	async def on_message(self, message):
		#排除自己的訊息，避免陷入無限循環
		if str(message.author).find(str(self.user)) != -1:
			return
		#列印接收到的訊息
		print(f"[{Get_Time()}] Get Message from {str(message.guild)}.{str(message.channel)}.{str(message.author.display_name)}: {str(message.content)}")
	
		#指令程序
		if (message.content.find(bot_ID) != -1):
	
			await self.cmd(message)
			send = False

	#指令讀取
	async def cmd(self, message):
		async with message.channel.typing():
			f = open("data/CharacterSet.md", "r", encoding="utf-8")
			file = f.read()
			f.close()
			file = file.replace("# Discord API setting", "")
			file = file.replace("\n", "")
			Chara = file.split("# Character info")
			Chara = Chara[1].split("- ")
			Str = ""
			for S in Chara:
				Str = Str + S
			Str = await self.ChangeText(message, Str)
			await message.reply(self.AI.Message(Str))
			print(f"[{Get_Time()}] Reply message to {str(message.guild)}.{str(message.channel)}.{str(message.author.display_name)}: {Str}")
			del file, Chara, Str

	async def ChangeText(self, ctx, text):
		contant = f"{ctx.guild}.{ctx.channel}.{ctx.author.display_name}：「{ctx.content}」"
		text = text.replace("&guild;", str(ctx.guild))
		text = text.replace("&channel;", str(ctx.channel))
		text = text.replace("&mauthor;", str(ctx.author.display_name))
		text = text.replace("&bot_ID;", str(bot_ID))
		text = text.replace("&Time;", str(Get_Time()))
		return text + contant

	utc = timezone.utc
	times = [
		time(hour=0, tzinfo=utc),
		time(hour=8, tzinfo=utc),
		time(hour=16, tzinfo=utc)
	]
	#Reflash CharacterAI
	@tasks.loop(time=times)
	async def Reflash_CharacterAI(self):
		await self.Reflash_Character()
		await self.CloseSelf()

	async def CloseSelf(self):
		try:
			await self.close()
		except:
			pass
		finally:
			exit()
	

def getSetting():
	global bot_ID
	global Token
	f = open("data/CharacterSet.md", "r", encoding="utf-8")
	file = f.read()
	file = file.replace("# Discord API setting", "")
	file = file.replace("\n", "")
	Setting= file.split("# Character info")
	Setting = Setting[0].split("- ")
	bot_ID = Setting[4]
	Token = Setting[2]
	f.close()
	del file, Setting

def bot1():
	getSetting()
	bot = MyBot(command_prefix="/", intent=intents)
	bot.run(Token)

	

#獲取時間
def Get_Time():
  
	dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
	dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區

	#timezone_TW = pytz.timezone('ROC')
	#now = datetime.now(timezone_TW)
	return dt2.strftime("%Y-%m-%d %H:%M:%S")

bot1()