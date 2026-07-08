import discord
from discord.ext import commands
from discord import app_commands

# Critical intents to see members and manage roles
intents = discord.Intents.default()
intents.guilds = True
intents.manage_roles = True
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
    
    # Baseline: Zero power
    chat_only_perms = discord.Permissions.none()
    
    # Add survival essentials ONLY
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
        await interaction.response.send_message(f"🔥 MASSIVE W! The **{new_role.name}** role was created with locked-down chat perms.")
        print(f"✅ Created role '{new_role.name}'")
        
    except discord.Forbidden:
        await interaction.response.send_message("❌ My bot role isn't high enough! Move me up in server settings.", ephemeral=True)

# PASTE YOUR SECRET TOKEN HERE
bot.run('MTUyNDM0MTgwODI3MDkzNDAyNg.GjDWhs.uTaq6JTWqhTMwsfdqPDZALN8LhULCCSorSRpas')