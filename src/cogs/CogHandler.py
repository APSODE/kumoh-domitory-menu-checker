import os

from discord.ext import commands
from typing import List

from src.cogs.BaseCommand import BaseCommand


class CogHandler:
    def __init__(self, bot: commands.Bot):
        self._bot = bot

    async def setup_cogs(self):
        for cog_file in os.listdir(".\\src\\cogs\\"):
            print(cog_file)
            if cog_file in ["CogHandler.py", "BaseCommand.py"]:
                pass

            else:
                try:
                    await self._bot.load_extension(f"src.cogs.{cog_file[:-3]}")

                except Exception as MSG:
                    print("cog등록에 실패하였습니다.")
