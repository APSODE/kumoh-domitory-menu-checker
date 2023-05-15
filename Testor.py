import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents = intents.all()
        )

    async def on_ready(self):
        print("ready!")

        activity = discord.Game("상태 메세지")
        await self.change_presence(status=discord.Status.online, activity=activity)
        self.add_command(self.ping)

    @commands.command(name = "테스트")
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong!")


bot = MyBot()

bot.run("MTA4NTc2MDkyNjIxNDUyOTExNw.GLY96E.JFI0OieIJkPHie5SPBZPE8O7izf48Z2RuNBf6k")