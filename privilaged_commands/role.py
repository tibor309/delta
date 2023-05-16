import discord
from discord.ext import commands

class role_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Give role to user
    @discord.slash_command(name="usermod", description="Give a role to user", guild_only=True)
    @discord.commands.default_permissions(manage_roles=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    @discord.option("role", discord.Role, description="Select a role", required=True)
    async def give_role(self, ctx, user: discord.Member, role: discord.Role):

        try:
            await user.add_roles(role, reason=f"Gave role by {ctx.author.name}#{ctx.author.discriminator}")
        except:
            await ctx.respond(f"Failed to give role\nprobably a higher role than mine, or {user.mention} already has that role", ephemeral=True)

        await ctx.respond(f"Added the {role.mention} role to {user.mention}", ephemeral=True)


    # Revoke role from user
    @discord.slash_command(name="userdemod", description="Revoke a role from user", guild_only=True)
    @discord.commands.default_permissions(manage_roles=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    @discord.option("role", discord.Role, description="and select a role", required=True)
    async def revoke_role(self, ctx, user: discord.Member, role: discord.Role):

        try:
            await user.remove_roles(role, reason=f"Removed role by {ctx.author.name}#{ctx.author.discriminator}")
        except:
            await ctx.respond(f"Failed to remove role\nprobably a higher role than mine, or {user.mention} doesn't have that role.", ephemeral=True)

        await ctx.respond(f"Removed the {role.mention} role from {user.mention}", ephemeral=True)


def setup(bot):
    bot.add_cog(role_commands(bot))