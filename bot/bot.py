import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import hikari
import lightbulb

PREFIX = ["ketchup."]

VERSION = "LinKetchup Test 6-29"

HOME_GUILD_ID = "833477250841837598"
STDOUT_CHANNEL_ID = "1256819760759570464"

class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone="utc")

        intents = (
            hikari.Intents.GUILD_MESSAGES | 
            hikari.Intents.MESSAGE_CONTENT
        )

        super().__init__(
            prefix = lightbulb.when_mentioned_or(PREFIX),
            #token = DISCORD_TOKEN,
            intents = intents,
        )

    def run(self) -> None:

        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)
        
        super().run(
            activity = hikari.Activity(
                name = f"{PREFIX[0]}help | /meme",
                type = hikari.ActivityType.WATCHING)
        )

    async def on_starting(self, event: hikari.StartedEvent) -> None:
        self.load_extensions_from("./bot/extensions/")

    async def on_started(self, event: hikari.StartedEvent) -> None:
        self.scheduler.start()
        self.stdout_channel = await self.rest.fetch_channel(STDOUT_CHANNEL_ID)
        await self.stdout_channel.send(f"{VERSION} bot now online")
        logging.info("BOT READY")

    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        await self.stdout_channel.send(f"{VERSION} bot shutting down")
        self.scheduler.shutdown()

