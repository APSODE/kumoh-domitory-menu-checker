import discord
from discord.ext.commands import Context
from discord.ext import commands
from typing import Tuple, Any
from src.cogs.BaseCommand import BaseCommand
import asyncio


class UserDataCommand(BaseCommand):
    def __init__(self):
        self._file_name = "UserDataCommand"

    async def HandleCommandArgument(self, ctx: Context, arguments: Tuple[Any]):
        ica_task = asyncio.create_task(self.CommandArgumentDevider(arguments))
        await ica_task
        ica_result: dict = ica_task.result()
        ica_length = len(ica_result.keys())
        if ica_length == 0:
            user_command_help_message = discord.Embed(
                title = "!유저 명령어 도움말",
                description = "유저 명령어에 대한 도움말을 표현합니다."
            )
            await ctx.send(embed = user_command_help_message)


        # for key, value in input_command_arguments.items():

    @commands.command(name = "유저")
    async def UserCommand(self, ctx: Context, *args):
        hca_task = asyncio.create_task(self.HandleCommandArgument(ctx = ctx, arguments = args))
        await hca_task
        await ctx.send(f"{hca_task.result()}")
        #TODO 커멘드 벨류 입력과 파라미터 입력 체계 구상 필요

    async def cog_command_error(self, ctx: Context, error: Exception) -> None:
        pass

    @property
    def FileName(self) -> str:
        return self._file_name


async def setup(bot: commands.Bot):
    await bot.add_cog(UserDataCommand())
