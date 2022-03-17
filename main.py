import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='re ', intents=intents)

@bot.command(name='rarity', help='List of quotes and how rare')
async def rarity(ctx):
    if ctx.message.content.startswith('re rarity'):
      await ctx.message.channel.send("Total: 85\n Common: 29\n Uncommon: 20\n Rare: 15\n Epic: 11\n Legendary: 7\n God: 3\n")


@bot.command(name='b', help='The quotes youve always wanted')
async def b(ctx):
    if ctx.message.content.startswith('re b'):

      dict = {"Im gonna blow up the plane. " : 3,"I quit. " : 1,"Im gonna shoot up work. " : 2,"FYI I got dibs on bed. " : 1,"Shoulda got her while she was vulnerable." : 3,"I loved Gina." : 4,"I love you " : 2,"Connor ima steal my girlfriend back " : 6,"Thats ass my guy. " : 1,"Ill even call you daddy." : 2,"I mean I will definitely watch a lot of porn tonight but crying in the shower is a gametime decision " : 6,"if you wanted to stop the stupidity you shoulda told my dad to pull out " : 4,"Lets go steal MILFs kayaks." : 2,"I dont need a 401k this is my retirement plan *gunshot* " : 4,"she can, i make sure to send it through the phone " : 1,"kelly wants me " : 3,"youre gonna roast me while im having a shit day then expect a roasting back " : 4,"Anyone tryn to play some catan? " : 1,"I am so tired. " : 1,"Evan you can have all the beer at my house " : 1,"Who the fuck ate my chicken nuggets " : 3,"Im gonna fuck a donkey " : 1,"nikhil i got you\n i offer payment plans for maintenance\n pay me in taco bell\n party packs " : 4,"idk why you expect me to behave normally " : 3,"go home pussy\n boys peep the text chat\n barps is LITERALLY ASKING FOR IT\n MIGHT HAVE KILLED HIM " : 2,"Im talking myself into getting angry." : 4, "I need to get alcohol poisioning " : 2, "he cornered me in highschool when the group was chillin in valley sqaure\n tried to suck me off for half hour " : 4,"no shot " : 1,"nah not a fan of gays\n unless theyre lesbians\n huge fan of those " : 3,"I read energy real well " : 1,"cuz they know i wanna fuck " : 1,"i love harry potter! " : 1,"smith ill put my pp in your mouth while youre sleeping " : 4,"are we allowed to talk to maya on this trip or is she off limits " : 5,"my gay side needs to know if im attractive looking to guys " : 4,"id say i love you katrina but weve been down that road " : 5,"i love you connor ": 1,"everyones awesome\n unless you point a gun at me " : 2,"definitely dont wanna work either\n yeah but now im dying " : 1,"i come here and get pissed off before 11am everyday now " : 1,"ill put your liver through the guantlet." : 2,"Im angry." : 5,"look at who you wanna be in the future and ask yourself if that guy jerks off on the daily " : 6,"oh bet so yeah all i was thinking about was mia khalifa and it was a STRUGGLE to get to bed " : 3,"Nick definitely should have gotten a DUI on the boat " : 2,"IM GONNA BE RAILING HOT CHOCO ALL DAY " : 2,"im 1 and half blasts in rn and its hard to contain myself in an office " : 4,"that seems very specific cuz i have no clue what sql is but you wouldnt catch me doing it " : 1,"Yeah he's getting his pp slapped again " : 2,"KEVIN DOESNT WANNA SEE ME LOSE MY SHIT " : 3,"I AM A HUGE PERV, YOU KNOW THIS " : 1,"matt take drugs " : 2,"i just wanna see her naked " : 1,"jess's sexy voice is right next to me " : 1,"im getting so high tonight that i wont be able to have a conversation " : 5,"Definitely air pods. " : 2,"Kevin raped my mom.... metaphorically. " : 1,"Tell kevin to go fuck himself " : 3,"Kevins wackin my dick rn. " : 5,"Its not a privilege to drive." : 2,"shes a stick with no assets " : 3,"coulda been a way better summer cuz if she was giving me daily head she wouldnt have thought i was fucking her mom\n big brain " : 3,"i fucked a milf in one pump\n i am proud " : 3,"im a freak\n you all should know this " : 1,"what have i done to her\n musta been the cheating " : 1,"ryann ratcliffe is apparently drinking more than me and woody combined\n and now shes fat " : 2,"shes definitely a screamer " : 1,"Not that Paris " : 3,"Im a jumper " : 1,"so she knows how to ride the right way " : 1,"I'll put it together retard " : 3,"i just found another sexy female\n not sure where she came from " : 2,"Im *investing* " : 5,"ill suck you off woody " : 5,"i need sex " : 2,"boys i wanna commit robbery " : 1,"I AM STIMULATED " : 1, "I do what I want, when I want. " : 3, "You can have the couch, $200 a month " : 4, "The things I would do to her. " : 1, "Im not trying to piss you off I just have big goals " : 2, "Tested positive this morning, yeah its lowkey amazing " : 2, "I ain't no side hoe " : 2, "80% chance I wonnt be up that late" : 1}		

    item = random.choice(list(dict.items()))
    x,y = item
    if (y == 1):
      {
        await ctx.message.channel.send(x)
      }
    elif(y == 2):
      {
        await ctx.message.channel.send("Nice Uncommon\n\n" + x)
      }
    elif(y == 3):
      {
        await ctx.message.channel.send("Oooooo rare\n\n" + x)
      }
    elif(y == 4):
      {
        await ctx.message.channel.send("EPIC!\n" + x)
      }
    elif(y == 5):
      {
        await ctx.message.channel.send("LEGENDARY QUOTE!\n\n" + x)
      }
    elif(y == 6):
      {
        await ctx.message.channel.send("May the heavens shine upon you with this GODLY quote:\n\n" + x)
      }
    else:
        return 0;


keep_alive()
bot.run(os.getenv('TOKEN'))