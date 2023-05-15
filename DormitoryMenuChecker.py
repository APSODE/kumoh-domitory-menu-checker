import discord
from src.cogs.CogHandler import CogHandler
from discord.ext import commands, tasks
from discord import Intents


class DormitoryMenuChecker(commands.Bot):
    def __init__(self):
        my_intents = Intents.default()
        my_intents.message_content = True
        super(DormitoryMenuChecker, self).__init__(
            command_prefix = "!",
            intents = my_intents,
            sync_command = True
        )
        self._cog_handler = CogHandler(
            bot = self
        )
        self._start()

    def _start(self):
        self.run("")

    async def on_ready(self):
        print("봇이 정상적으로 활성화되었습니다.")
        activity = discord.Game("상태 메세지")
        await self.change_presence(status = discord.Status.online, activity = activity)
        await self._cog_handler.setup_cogs()



if __name__ == '__main__':
    DMC = DormitoryMenuChecker()
