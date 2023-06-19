from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀☆𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬☆🥀",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀☆𝐒𝐫𝐭𝐭𝐢𝐧𝐠𝐬☆🥀", callback_data="settings_helper"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀☆𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬☆🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀☆𝐇𝐞𝐥𝐩☆🥀", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀☆𝐂𝐡𝐚𝐧𝐧𝐞𝐥☆🥀", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="🥀☆𝐆𝐫𝐨𝐮𝐩☆🥀", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀☆𝐑𝐞𝐩𝐨☆🥀", url="https://github.com/XdityaHalder/SankiMusic"
            )
        ]
     ]
    return buttons
