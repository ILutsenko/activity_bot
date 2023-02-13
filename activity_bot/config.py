from os import environ
import yaml

from pydantic import (
    BaseSettings,
    Field,
)

CONFIG_PATH = environ.get('CONFIG_PATH')


class TelegramSettings(BaseSettings):
    token: str = Field(description='Telegram bot token')


class DataBase(BaseSettings):
    username: str
    password: str
    host: str
    port: int
    database: str


class Config(BaseSettings):
    telegram_settings: TelegramSettings
    database: DataBase


def _read_config():
    with open(CONFIG_PATH, encoding='utf-8') as file:
        return Config(**yaml.load(file, Loader=yaml.Loader))


config: Config = _read_config()
