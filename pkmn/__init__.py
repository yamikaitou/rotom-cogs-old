from .pkmn import Pkmn


def setup(bot):
    bot.add_cog(Pkmn(bot))
