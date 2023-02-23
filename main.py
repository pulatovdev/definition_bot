import logging
from definitionLookup import getDefinitions
from googletrans import Translator

translator = Translator()
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6133248956:AAHVrcj0Ba3p51EYzXhmOkkOYMz2GzxB9IQ'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply('Assalomu alaykum!👋🏻 \n Men Advanced Learner`s Dictionary`man!🦾 \nIkkitadan ortiq so`z '
                        'yuborsangiz, uzb-eng yoki eng-uzb tarjima qilib beraman! \nAgar bitta yoki ikkita so`z '
                        'yuborsangiz, uning inglizcha ma`nosini (definition) beraman!💪\nMeni yaratgan odam : '
                        '@pulatov_developer \nMendan foydalanish uchun so`z yuboring!')


@dp.message_handler()
async def googlemi(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.answer(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"📋 Word: {word_id.upper()} \n  ✍️Definitions: \n 👉👉 {lookup['def']}")
            if lookup.get('audio'):
                await message.reply_audio(lookup['audio'])
        else:
            await message.reply('No such word was found. Check the spelling')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
