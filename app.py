import discord
from discord.ext import commands
from discord import app_commands
import os  # 🔥 WE NEED THIS FOR ENV VARIABLES

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🔥 BOT ONLINE. {bot.user} is ready to dominate!")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash command(s). SIUUUUUU!")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.tree.command(name="role", description="Creates a new custom role with Chat & Read ONLY perms")
@app_commands.describe(name="The name you want to give the new role")
@app_commands.default_permissions(administrator=True) 
async def create_role(interaction: discord.Interaction, name: str):
    guild = interaction.guild
    
    chat_only_perms = discord.Permissions.none()
    chat_only_perms.view_channel = True
    chat_only_perms.send_messages = True
    chat_only_perms.read_message_history = True

    try:
        new_role = await guild.create_role(
            name=name,
            permissions=chat_only_perms,
            color=discord.Color.dark_theme(),
            reason=f"FORB1D🔥 Role generated via /role command"
        )
        await interaction.response.send_message(f"🔥 MASSIVE W! The **{new_role.name}** role was created.")
        print(f"✅ Created role '{new_role.name}'")
        
    except discord.Forbidden:
        await interaction.response.send_message("❌ My bot role isn't high enough! Move me up in settings.", ephemeral=True)

# 🛑 PULLS THE TOKEN FROM RENDER INSTEAD OF THE FILE 🛑
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
