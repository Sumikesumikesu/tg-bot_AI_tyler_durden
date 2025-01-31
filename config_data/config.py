from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class APIKey:
    key: str


@dataclass
class Config:
    tg_bot: TgBot
    api_key: APIKey


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    bot_token = env("BOT_TOKEN")
    api_key = env("API_KEY")

    return Config(
        TgBot(token=bot_token),
        APIKey(key=api_key)
        )
