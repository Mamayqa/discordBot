import os
import discord

from discord.ext import commands

intents = discord.Intents.all()

settings = {
    'token': os.getenv('BOT_TOKEN'),
    'bot': 'MaMaY_BOT',
    'id': os.getenv('BOT_ID'),
    'prefix': '$'
}

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.command('rand')  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(
        f'Hello, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.@bot.command('rand')  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.


@bot.command(commands=['пидор','леха пидор'])  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def test(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(
        f'сам ты пидор, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command(commands='*')
async def tes(ctx):
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(
        f'{author.mention}, сам ты {ctx.message}!')

bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
