
import random
import lightbulb

from bot import Bot

plugin = lightbulb.Plugin("Functions")

# Prep functions
def mock_case(message):

    new_message = ""

    for letter in message:
        choice = bool(random.getrandbits(1))
        if choice:
            new_message += letter.upper()
        else:
            new_message += letter.lower()

    return(new_message)


# Discord Bot commands
@plugin.command
@lightbulb.option(
    name="message",
    description="message to be repeated back",
    type = str, default = "",
    modifier=lightbulb.commands.OptionModifier.CONSUME_REST
)
@lightbulb.command(name="mock", description="Mock the message received")
@lightbulb.implements(lightbulb.PrefixCommand)
async def command_echo(ctx: lightbulb.Context) -> None:

    message = ctx.options.message.strip()[:125]
    new_message = mock_case(message)

    await ctx.respond(new_message)



##
def load(bot: Bot):
    bot.add_plugin(plugin)

def unload(bot: Bot):
    bot.remove_plugin(plugin)