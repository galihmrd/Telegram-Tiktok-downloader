from aiogram.types import Message
from bot import dp, bot
from bot.api import MobileTikTokAPI, TikTokAPI


platforms = [MobileTikTokAPI(), TikTokAPI()]


@dp.message_handler()
async def get_message(message: Message):
    for api in platforms:
        if videos := [v for v in await api.handle_message(message) if v and v.content]:
            for video in videos:
                lol = await message.reply("Mengunduh...")
                await bot.send_video(
                    message.chat.id, video.content, reply_to_message_id=message.message_id
                )
                await lol.delete()
            break

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.reply("Untuk mengunduh video, cukup kirimkan tautan video tiktok anda")

