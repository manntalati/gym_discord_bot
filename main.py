import discord
import os
from online import online
from discord.ext import commands, tasks
from discord import Embed, Color


#bicep_exercises = ["Seated Hammer Curl", "Bicep Curls", "EZ Bar Curl", "Preacher Curls", "Hammer Curl", "Chin Ups", "Dumbell Incline Bicep Curls"]
#  tricep_exercises = ["Dips", "Rope Pushdowns", "Skullcrushers", "Overhead Dumbell Extensions"]
#  shoulder_exercises = ["Seated Shoulder Press", "Arnold Press", "Front Press", "Lateral Raises", "Shoulder Shrugs", "Overhead Shoulder Press"]

intents = discord.Intents.all()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix="-", intents=intents)

@client.event
async def on_ready():
    print("KACHOW")


def buttons(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == "⏪":
            return True
        if r and reaction.emoji == "⏩":
            return True
        return False

    return check

@client.command()
async def gym(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    embed = discord.Embed(
        title = 'Gym',
        description = 'Arms - 🏋️\t\n Push - 💪\t\n Pull - 🎉\t\n Chest&Back - ⚙️\t\n Legs - 🦵',
        color = 0xb042f5
    )
    embed.set_footer(text=f"Gym")
    msg = await ctx.send(embed=embed)
  
    await msg.add_reaction("🏋️")
    await msg.add_reaction("💪")
    await msg.add_reaction("🎉")
    await msg.add_reaction("⚙️")
    await msg.add_reaction("🦵")

    @client.event
    async def on_reaction_add(reaction, user):
      if user == "Gym_Bot#6486":
        pass
      else:
        if reaction.emoji == "🏋️" and user != "Gym_Bot#6486":
          pages = []
          await msg.delete()
          embedVar = discord.Embed(title=f"Gym",
                                   colour=0xb042f5)
          embedVar.add_field(
              name="Biceps",
              value=
              "1. Seated Hammer Curls\n2. Bicep Curls\n3. EZ Bar Curls\n 4. Preacher Curls\n 5. Hammer Curl \n 6. Chin Ups \n 7. Dumbell Incline Bicep Curls"
          )
          embedVar2 = discord.Embed(title=f"Gym",
                                   colour=0xb042f5)
          embedVar2.add_field(
              name="Triceps",
              value=
              "1. Dips\n2. Rope Pushdowns\n3. Skullcrushers\n4. Overhead Dumbell Extensions"
          )
          embedVar3 = discord.Embed(title=f"Gym",
                                   colour=0xb042f5)
          embedVar3.add_field(
              name="Shoulders",
              value=
              "1. Seated Shoulder Press\n2. Arnold Press\n3. Front Press\n4. Lateral Raises\n5. Shoulder Shrugs\n6. Overhead Shoulder Press"
          )
          pages.append(embedVar)
          pages.append(embedVar2)
          pages.append(embedVar3)
          page = 0
          left = "⏪"
          right = "⏩"
          while True:
              msg2 = await ctx.send(embed=pages[(page)])
              l_reaction = page != 0
              r_reaction = page <= len(pages) - 1
              if l_reaction:
                  await msg2.add_reaction(left)
              if r_reaction:
                  if page == (len(pages) - 1):
                      react = await client.wait_for('reaction_add',
                                                    check=buttons(
                                                        msg2, l_reaction, r_reaction))
                  else:
                      await msg2.add_reaction(right)
                      react = await client.wait_for('reaction_add',
                                                    check=buttons(
                                                        msg2, l_reaction, r_reaction))
      
              if str(react[0]) == left:
                  page -= 1
              elif str(react[0]) == right:
                  page += 1
      
              await msg2.delete()
      



online()
token = os.environ.get("TOKEN")
client.run(token)