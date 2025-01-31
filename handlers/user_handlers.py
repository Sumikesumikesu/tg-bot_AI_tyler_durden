from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from servises.get_gpt_response import get_gpt_response
# from servises.narration import text_to_audio
# from aiogram.types import FSInputFile
# # import os

router: Router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands=['help']))
async def process_comand_help(messsage: Message):
    await messsage.answer(
        text=LEXICON_RU['/help'])


# @router.message(Command(commands=['voice']),
#                 lambda message: message.text.endswith('?'))
# async def process_question_audio(message: Message):
#     await message.reply(text="Погоди голосовое запишу")
#     gpt_response = get_gpt_response(message.text)
#     text_to_audio(gpt_response)
#     voice = FSInputFile("output.wav")
#     await message.reply_voice(voice=voice)
#     os.remove("output.wav")

@router.message(lambda message: message.text.startswith('@tyler'),
                lambda message: message.text.endswith('?'))
async def process_tyler_message(message: Message):
    gpt_response = get_gpt_response(
        message.text.replace('@tyler ', ''),
        'tyler')
    await message.reply(text=gpt_response)


@router.message(lambda message: message.text.startswith('@samanta'),
                lambda message: message.text.endswith('?'))
async def process_samanta_message(message: Message):
    gpt_response = get_gpt_response(
        message.text.replace('@samanta ', ''),
        'samanta')
    await message.reply(text=gpt_response)


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
