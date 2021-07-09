from aiogram import types
from bot import dp, bot
from bot.api import MobileTikTokAPI, TikTokAPI


platforms = [MobileTikTokAPI(), TikTokAPI()]


@dp.message_handler()
async def get_message(message: types.Message):
    lol = await message.reply("Mengunduh video...")
    for api in platforms:
        if videos := [v for v in await api.handle_message(message) if v and v.content]:
            for video in videos:
                lol = await message.reply("Mengunggah video...")
                await bot.send_video(
                    message.chat.id, video.content, reply_to_message_id=message.message_id
                )
                await lol.delete()
            break

@dp.message_handler(commands=['start', 'help'], commands_prefix='!/')
async def start(message: types.Message):
    await message.reply("Untuk mengunduh video, cukup kirimkan tautan video tiktok anda")

