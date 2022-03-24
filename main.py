import discord
from discord.ext import commands
from discord.utils import get
import os
import requests
import json
import math
import urllib
import random
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time
from keep_alive import keep_alive

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='re ', intents=intents)

@bot.command(name='rarity', help='List of quotes and how rare')
async def rarity(ctx):
    if ctx.message.content.startswith('re rarity'):
      await ctx.message.channel.send("Total: 90\n Common: 29\n Uncommon: 19\n Rare: 15\n Epic: 11\n Legendary: 8\n God: 3\n Hidden: ???\n")


@bot.command(name='b', help='The quotes youve always wanted')
async def b(ctx):
    if ctx.message.content.startswith('re b'):

      dict = {"Im gonna blow up the plane. " : 3,"I quit. " : 1,"Im gonna shoot up work. " : 2,"FYI I got dibs on bed. " : 1,"Shoulda got her while she was vulnerable." : 3,"I loved Gina." : 4,"I love you " : 2,"Connor ima steal my girlfriend back " : 6,"Thats ass my guy. " : 1,"Ill even call you daddy." : 2,"I mean I will definitely watch a lot of porn tonight but crying in the shower is a gametime decision " : 6,"if you wanted to stop the stupidity you shoulda told my dad to pull out " : 4,"Lets go steal MILFs kayaks." : 2,"I dont need a 401k this is my retirement plan *gunshot* " : 4,"she can, i make sure to send it through the phone " : 1,"kelly wants me " : 3,"youre gonna roast me while im having a shit day then expect a roasting back " : 4,"Anyone tryn to play some catan? " : 1,"I am so tired. " : 1,"Evan you can have all the beer at my house " : 1,"Who the fuck ate my chicken nuggets " : 3,"Im gonna fuck a donkey " : 1,"nikhil i got you\n i offer payment plans for maintenance\n pay me in taco bell\n party packs " : 4,"idk why you expect me to behave normally " : 3,"go home pussy\n boys peep the text chat\n barps is LITERALLY ASKING FOR IT\n MIGHT HAVE KILLED HIM " : 2,"Im talking myself into getting angry." : 4, "I need to get alcohol poisioning " : 2, "he cornered me in highschool when the group was chillin in valley sqaure\n tried to suck me off for half hour " : 4,"no shot " : 1,"nah not a fan of gays\n unless theyre lesbians\n huge fan of those " : 3,"I read energy real well " : 1,"cuz they know i wanna fuck " : 1,"i love harry potter! " : 1,"smith ill put my pp in your mouth while youre sleeping " : 4,"are we allowed to talk to maya on this trip or is she off limits " : 5,"my gay side needs to know if im attractive looking to guys " : 4,"id say i love you katrina but weve been down that road " : 5,"i love you connor ": 1,"everyones awesome\n unless you point a gun at me " : 2,"definitely dont wanna work either\n yeah but now im dying " : 1,"i come here and get pissed off before 11am everyday now " : 1,"ill put your liver through the guantlet." : 2,"Im angry." : 5,"look at who you wanna be in the future and ask yourself if that guy jerks off on the daily " : 6,"oh bet so yeah all i was thinking about was mia khalifa and it was a STRUGGLE to get to bed " : 3,"Nick definitely should have gotten a DUI on the boat " : 2,"IM GONNA BE RAILING HOT CHOCO ALL DAY " : 2,"im 1 and half blasts in rn and its hard to contain myself in an office " : 4,"that seems very specific cuz i have no clue what sql is but you wouldnt catch me doing it " : 1,"Yeah he's getting his pp slapped again " : 2,"KEVIN DOESNT WANNA SEE ME LOSE MY SHIT " : 3,"I AM A HUGE PERV, YOU KNOW THIS " : 1,"matt take drugs " : 2,"i just wanna see her naked " : 1,"jess's sexy voice is right next to me " : 1,"im getting so high tonight that i wont be able to have a conversation " : 5, "Kevin raped my mom.... metaphorically. " : 1,"Tell kevin to go fuck himself " : 3,"Kevins wackin my dick rn. " : 5,"Its not a privilege to drive." : 2,"shes a stick with no assets " : 3,"coulda been a way better summer cuz if she was giving me daily head she wouldnt have thought i was fucking her mom\n big brain " : 3,"i fucked a milf in one pump\n i am proud " : 3,"im a freak\n you all should know this " : 1,"what have i done to her\n musta been the cheating " : 1,"ryann ratcliffe is apparently drinking more than me and woody combined\n and now shes fat " : 2,"shes definitely a screamer " : 1,"Not that Paris " : 3,"Im a jumper " : 1,"so she knows how to ride the right way " : 1,"I'll put it together retard " : 3,"i just found another sexy female\n not sure where she came from " : 2,"Im *investing* " : 5,"ill suck you off woody " : 5,"i need sex " : 2,"boys i wanna commit robbery " : 1,"I AM STIMULATED " : 1, "I do what I want, when I want. " : 3, "You can have the couch, $200 a month " : 4, "The things I would do to her. " : 1, "Im not trying to piss you off I just have big goals " : 2, "Tested positive this morning, yeah its lowkey amazing " : 2, "I ain't no side hoe " : 2, "80% chance I wonnt be up that late" : 1, "Yo your mom is still single rn?! I'll be your stepdad." : 5, "Special Airdrop!\n" : 7}		

    item = random.choice(list(dict.items()))
    x,y = item
    
    if (y == 7):
        await ctx.message.channel.send(x + " (Secret Rare)\n")
        q = random.randint(1, 5)
        if (q == 1):
            await ctx.message.channel.send(file=discord.File("brianmemeemail.jpeg"))
        elif (q == 2):
            await ctx.message.channel.send(file=discord.File("8ball meme.jpeg"))
        elif (q == 3):
            await ctx.message.channel.send(file=discord.File("fightme.jpeg"))
        elif (q == 4):
            await ctx.message.channel.send(file=discord.File("beach1.jpeg"))
        elif (q == 5):
            await ctx.message.channel.send(file=discord.File("patty1.jpeg"))
        else:
            return 0;
    elif(y == 1):
        await ctx.message.channel.send(x + " (Common)")
    elif(y == 2): 
        await ctx.message.channel.send(x + " (Uncommon)")
    elif(y == 3):
        await ctx.message.channel.send(x + " (Rare)")
    elif(y == 4):
        await ctx.message.channel.send(x + " (Epic)")
    elif(y == 5):   
        await ctx.message.channel.send(x + " (Legendary)")
    elif(y == 6):
        await ctx.message.channel.send(x + " (Godly)")
    else:
        return 0;


@bot.command()
async def pushP(ctx):
    print('We have logged in as {0.user}'.format(client))
    await bot.change_presence(activity=discord.Streaming(
        name='Catan', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


#inside joke with a server memeber
@bot.command(name='barps', help='Pulls a BARPS')
async def barps(ctx, members: commands.Greedy[discord.Member]):
    slapped = ", ".join(x.name for x in members)
    await ctx.message.channel.send('NO NIKHIL!')
    await ctx.send('Nikhil just got slapped by Barps!')


#fun little dice roll
@bot.command(name='rolld20', help='rolls a d20 to test your luck')
async def rolld20(ctx):
    if ctx.message.content.startswith('re rolld20'):
        await ctx.message.channel.send("Rolling D20")
        value = random.randint(1, 20)
        if (value > 19):
            await ctx.message.channel.send("AYE Nat 20 Baby!")
        elif (value > 15 and value < 20):
            await ctx.message.channel.send(
                "Hey thats pretty good you rolled a % d " % (value))
        elif (value > 10 and value < 15):
            await ctx.message.channel.send("Not bad you rolled a % d " %
                                           (value))
        elif (value > 1 and value < 10):
            await ctx.message.channel.send(
                "Oof could be better you rolled a % d " % (value))
        elif (value < 2):
            await ctx.message.channel.send("Eeeeelllllsssss Nat 1")
        else:
            await ctx.message.channel.send("Huh thats not supposed to happen")
        return


#silly work command
@bot.command(name='jillamy', help='The cult')
async def jillamy(ctx):
    if ctx.message.content.startswith('re jillamy'):
        await ctx.message.channel.send('<a:alert:814971914086121472>' +
                                       'Go Jillamy Go!!!' +
                                       '<a:alert:814971914086121472>')
        time.sleep(1)
        await ctx.message.channel.send('one of us')
        time.sleep(1)
        await ctx.message.channel.send('One Of Us')
        time.sleep(1)
        await ctx.message.channel.send('ONE OF US')
        return


#magic eight ball command. could be compacted with a switch probs
@bot.command(name='magic8', help='The decision make youve always wanted')
async def magic8(ctx):
    if ctx.message.content.startswith('re magic8'):
        value = random.randint(1, 20)
        if (value == 20):
            await ctx.message.channel.send("Certified BIG bet.")
        elif (value == 19):
            await ctx.message.channel.send("Naw but you'll get stinky feet.")
        elif (value == 18 or value == 3):
            await ctx.message.channel.send("Maybe...")
        elif (value == 17 or value == 4):
            await ctx.message.channel.send("No shot.")
        elif (value == 15 or value == 5 or value == 10):
            await ctx.message.channel.send("Try again.")
        elif (value == 16 or value == 6):
            await ctx.message.channel.send("Possible but not probable.")
        elif (value == 14 or value == 7):
            await ctx.message.channel.send(
                "Ill ask Bill Nye and get back to you.")
        elif (value == 13 or value == 8):
            await ctx.message.channel.send(
                "Don't worry about it just go play some Halo.")
        elif (value == 12 or value == 9):
            await ctx.message.channel.send("No.")
        elif (value == 11 or value == 2):
            await ctx.message.channel.send("Yes.")
        elif (value == 1):
            await ctx.message.channel.send("Never ask me a question again.")
        else:
            await ctx.message.channel.send("Wait how did you do that???")

#silly slap cmd
@bot.command(name="slap", help="re slap @person, reason for slapping ")
async def slap(ctx,
               members: commands.Greedy[discord.Member],
               *,
               reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    if (slapped == 'nikheat1#0391'):
        await ctx.send('No Nikhil')
        await ctx.send('{} just got slapped by Barps'.format(slapped))
    else:
        await ctx.send('{} just got slapped for {}'.format(slapped, reason))


#poll cmd
reactions = ["👍", "👎"]
@bot.command(name="poll", help="a cmd to create a poll.")
async def poll(ctx, *, question):
    m = await ctx.send(f"Poll: {question} -{ctx.author}")
    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await m.add_reaction(emoji or name)


#silly celebration command
@bot.command(name='c', help='A cmd build to celebrate')
async def c(ctx):
    if ctx.message.content.startswith('re c'):
        await ctx.message.channel.send('C o n g r a t s!')
        await ctx.message.channel.send('<a:ye:814971851485872140>' +
                                       '<a:catjam:824878456939610112>' +
                                       '<a:beat:814971891969294396>' +
                                       '<a:alert:814971914086121472>' +
                                       '<a:yee:814971872503529473>')
        return

#silly meme cmd
@bot.command(name='bagalert', help='Major Bag Alert')
async def bagalert(ctx):
    if ctx.message.content.startswith('re bagalert'):
        await ctx.message.channel.send('<a:alert:814971914086121472>' + 'Bag Alert'+'💰'+'Major Baaaag Alert' + '<a:alert:814971914086121472>')
        return


#A cmd to see whats new with the bot
@bot.command(name='news',
             help='Tells the bot to give you update on his changes')
async def news(ctx):
    if ctx.message.content.startswith('re news'):
        await ctx.message.channel.send(
            'I am Brian the III. Born on 3/10/2022, I can now roll dice, got a magic 8 ball, and got a new job at Jillamy. Type [re help] for the current command list. Oh I can also yell at Nikhil.'
        )
        return


#beginning of the weather command

api_key = os.getenv('WEATHER_TOKEN')
base_url = "http://api.openweathermap.org/data/2.5/weather?"


#weather cmd
@bot.command(help='gives the weather for a given city at current time')
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel

    if x["cod"] != "404":
        async with channel.typing():

            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_fahrenheit = str(
                round(1.8 * (current_temperature - 273.15) + 32))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            weather_description = z[0]["description"]
            embed = discord.Embed(
                title=f"Weather in {city_name}",
                color=ctx.guild.me.top_role.color,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(name="Descripition",
                            value=f"**{weather_description}**",
                            inline=False)
            embed.add_field(name="Temperature(F)",
                            value=f"**{current_temperature_fahrenheit}°F**",
                            inline=False)
            embed.add_field(name="Humidity(%)",
                            value=f"**{current_humidity}%**",
                            inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)",
                            value=f"**{current_pressure}hPa**",
                            inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")

        await channel.send(embed=embed)
    else:
        await channel.send("City not found.")



@bot.command(name='gm', help='Good Morning')
async def gm(ctx):
    if ctx.message.content.startswith('re gm'):
        await ctx.message.channel.send("Good morning fuckers")

@bot.command(name='re', help='re')
async def re(ctx):
    if ctx.message.content.startswith('re re'):
        await ctx.message.channel.send("re")


      
#========================================================================
#Dnd section
@bot.command(name='d100', help='dnd roll a d100')
async def d100(ctx):
    if ctx.message.content.startswith('re d100'):
        await ctx.message.channel.send("Rolling D100")
        value = random.randint(1, 100)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d20', help='dnd roll a d20')
async def d20(ctx):
    if ctx.message.content.startswith('re d20'):
        await ctx.message.channel.send("Rolling D20")
        value = random.randint(1, 20)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d12', help='dnd roll a d12')
async def d12(ctx):
    if ctx.message.content.startswith('re d12'):
        await ctx.message.channel.send("Rolling D12")
        value = random.randint(1, 12)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d10', help='dnd roll a d10')
async def d10(ctx):
    if ctx.message.content.startswith('re d10'):
        await ctx.message.channel.send("Rolling D10")
        value = random.randint(1, 10)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d8', help='dnd roll a d8')
async def d8(ctx):
    if ctx.message.content.startswith('re d8'):
        await ctx.message.channel.send("Rolling D8")
        value = random.randint(1, 8)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d6', help='dnd roll a d6')
async def d6(ctx):
    if ctx.message.content.startswith('re d6'):
        await ctx.message.channel.send("Rolling D6")
        value = random.randint(1, 6)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d4', help='dnd roll a d4')
async def d4(ctx):
    if ctx.message.content.startswith('re d4'):
        await ctx.message.channel.send("Rolling D4")
        value = random.randint(1, 4)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d2', help='dnd roll a d2')
async def d2(ctx):
    if ctx.message.content.startswith('re d2'):
        await ctx.message.channel.send("Rolling D2")
        value = random.randint(1, 2)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")

"""
dndBaseURL = "https://www.dnd5eapi.co/api/"


@bot.command(help='grants dnd info')
async def query(ctx, s1: str, s2: str, s3: str):
    completeDND_url = dndBaseURL + s1 + '/' + s2
    response = requests.get(completeDND_url)
    x = response.json()
    y = x.get(s3)
    await ctx.message.channel.send(y)

@bot.command(name='plshelp', help='grants dnd api info')
async def plshelp(ctx):
    await ctx.message.channel.send(
        "You can search the following things:\n"
        "ability-scores, skills, proficiencies, languages, alignment, background, classes, features, races, equipment-categories, spells, feats, monsters.\n"
        "Follow these with the subcriteria ex: 'ability-scores/dex'\n"
        "Subclass help will be added soon. For now just follow last entry with /yoursubsearch \n"
    )

"""

#=========================================================================

#imgflippy
username = os.getenv('MEME_USER')
password = os.getenv('MEME_PASS')

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

#Fetch the available memes
data = requests.get(
    'https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{
    'name': image['name'],
    'url': image['url'],
    'id': image['id']
} for image in data]


#List all the memes
@bot.command(name='memetypes',
             help='TBA: Tells the bot to list all the meme templetes')
async def memetypes(ctx):
    if ctx.message.content.startswith('re memetypes'):
        await ctx.message.channel.send(
            'Here is the list of available memes : \n')
        ctr = 1

        for img in images:
            a = ctr, img['name']
            await ctx.message.channel.send(a)
            ctr = ctr + 1
        return


@bot.command(name='memehelp',
             help='TBA: Tells the bot to explain how to make a meme')
async def memehelp(ctx):
    if ctx.message.content.startswith('re memehelp'):
        await ctx.message.channel.send(
            'I heard you needed help with making memes : \n')
        await ctx.message.channel.send(
            '1) first enter the serial number of the meme \n')
        await ctx.message.channel.send('2) Enter first text: \n')
        await ctx.message.channel.send('3) Enter second text: \n')
        await ctx.message.channel.send('Ex: [re makememe 10 text1 text2]')
        await ctx.message.channel.send(
            'Now just type [re makememe] to get started')


@bot.command(name='makememe', help='TBA: Tells the bot to make a meme')
async def makememe(ctx, id: int, text0: str, text1: str):
    #Fetch the generated meme
    if ctx.message.content.startswith('re makememe'):
        id = id
        text0 = text0
        text1 = text1
        URL = 'https://api.imgflip.com/caption_image'
        params = {
            'username': username,
            'password': password,
            'template_id': images[id - 1]['id'],
            'text0': text0,
            'text1': text1
        }
        response = requests.request('POST', URL, params=params).json()
        r = response.get('data')
        z = r.get('url')
        await ctx.message.channel.send(z)
        await ctx.message.channel.send('Memeo CompleteO ')




#####
amounts = {}

@bot.event
async def on_ready():
    global amounts
    try:
        with open('amounts.json') as f:             
            amounts = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}

@bot.command(pass_context=True)
async def balance(ctx):
    id = ctx.message.author.id
    if id in amounts:
       await ctx.message.channel.send("You have {} in the bank".format(amounts[id]))
    else:
        await ctx.message.channel.send("You dont have an account")

@bot.command(pass_context=True)
async def register(ctx):
    id = ctx.message.author.id
    if id not in amounts:
        amounts[id] = 100
        await ctx.message.channel.send("You are now registered")
        _save()
    else:
        await ctx.message.channel.send("You already have an account")

@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    primary_id = ctx.message.author.id
    other_id = other.id
    if primary_id not in amounts:
        await ctx.message.channel.send("You do not have an account")
    elif other_id not in amounts:
        await ctx.message.channel.send("The other party does not have an account")
    elif amounts[primary_id] < amount:
        await ctx.message.channel.send("You cannot afford this transaction")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.message.channel.send("Transaction complete")
    _save()

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

@bot.command()
async def save():
    _save()

#####

keep_alive()
bot.run(os.getenv('TOKEN'))