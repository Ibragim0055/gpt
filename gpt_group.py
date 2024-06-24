import openai
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import PhotoSize, Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import time

import urllib3

import aiohttp
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector

proxy_list = [
    {'host': '123.45.67.89', 'port': 8000},
    {'host': '210.120.36.45', 'port': 9000},
    {'host': '45.67.89.12', 'port': 7000}
]

async def fetch_data_with_proxy(url, connector):
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

async def main1():
    url = 'https://api.example.com/data'
    for proxy in proxy_list:
        proxy_url = f'http://{proxy["host"]}:{proxy["port"]}'
        connector = ProxyConnector.from_url(proxy_url, proxy_headers=True)
        print(f"Using proxy: {proxy['host']}:{proxy['port']}")
        data = await fetch_data_with_proxy(url, connector)
        print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main1())




openai.api_key = "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"

conversation = []

# Инициализация бота
bot = Bot(token='6890822241:AAFK1bX5imtZAdVrrvTaGPBk47MfDoFa8DQ')
dp = Dispatcher(storage=MemoryStorage())

class rass(StatesGroup):
    a = State()

# Функция для получения приветствия от модели
def get_model_greeting():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ] + conversation,
)

    
    return response.choices[0].message['content']



speech_context = {}

class viv:
    def __init__(self):
        self.context = ""
        self.msg = ""


gpttt_0 = InlineKeyboardButton(text='Как пользоваться', callback_data='kak')
gpttt_1 = InlineKeyboardButton(text='Помощь', callback_data='pom')
gpttt = InlineKeyboardMarkup(inline_keyboard=[[gpttt_0], [gpttt_1]])


kanal_1 = InlineKeyboardButton(text='✅ Подписаться', url='https://t.me/stalker_channeI')
kanal1 = InlineKeyboardButton(text='👀 Проверить', callback_data='b')
ab = InlineKeyboardMarkup(inline_keyboard=[[kanal_1], [kanal1]])

@dp.message(Command('start'))
async def start_message(message: Message):
    speech_context[message.from_user.id] = viv()
    channel_username = '@stalker_channeI'
    user_id = message.from_user.id
    username = message.from_user.username
    user_chat_member = await bot.get_chat_member(channel_username, user_id)
    if user_chat_member.status == 'member':
        await bot.send_message(user_id, text='''Привет! Я, GPT 3.5 TURBO бот из проекта STALKER. Чем могу помочь?''', reply_markup=gpttt)
    else:
        await bot.send_message(user_id, text='Для использования бота просто подпишитесь на наш канал!', reply_markup=ab)
    
    

@dp.message(Command('id'))
async def show_ids(message: Message):
    if message.from_user.id == 1994579994 or message.from_user.id == 1351718225:

        with open('мои проекты/gpt/ids_group.txt', 'r') as f:
            ids = f.read().splitlines()
        ids_str = '\n'.join(ids)
        await message.answer(f"Список айди из файла:\n{ids_str}")

@dp.message(Command('info'))
async def get_info(message: types.Message):
    with open('мои проекты/gpt/gpt.txt', 'r') as file:
        i = 0
        for line in file:
            chat_id = int(line.strip())
            username = await get_chat_info(chat_id)
            i += 1
            await message.answer(f"Chat ID: <code>{chat_id}</code>, Username: @{username}", parse_mode='HTML')
        await message.answer(i, "групп")



rasss = False

@dp.message(Command('rass'))
async def handle_rass_command(message: Message, state: FSMContext):
    global rasss
    if message.from_user.id == 1994579994 or message.from_user.id == 1351718225:
       rasss = True
       await message.answer('Введите текст')
       await state.set_state(rass.a)

file_path = 'мои проекты/gpt/gpt.txt'

@dp.message(StateFilter(rass.a))
async def rassss(message: Message, state: FSMContext):
    global rasss
    if rasss == True:
        print('рассылаем')
        rasss = False
        # Читаем айди групп из файла
        with open(file_path, 'r') as file:
            group_ids = file.read().splitlines()
        # Отправляем приветственное сообщение в каждую группу
            i = 0
            j = 0
        for group_id in group_ids:
            try:
                await bot.send_message(chat_id=int(group_id), text=f'{message.text}', parse_mode='HTML')
                i += 1
                print('Отправлен', i)
            except:
                j += 1
                print('error', j)
        await message.answer(f'отправлен {i}\nне отправлен {j}')
    else:
        print('false')
    


aaa = ""
aaa1 = False

@dp.message()
async def handle_message(message: Message):
    global aaa, aaa1

    if message and message.text and message.text.startswith('gpt: '):
        speech_context[message.from_user.id] = viv()
        speech_context[message.from_user.id].msg = message.text[5:]
        await handle_message(message)
    else:
        if message.text.startswith('/context'):
            speech_context[message.from_user.id] = viv()
            speech_context[message.from_user.id].context = ""
            await message.reply('Контекст речи сброшен')
            speech_context[message.from_user.id].msg = ""
    if message.text.startswith('/chat') and (message.from_user.id == 1994579994 or message.from_user.id == 1351718225):
        print('kkkkkkkkkkkkkkkkkkkkk')
        aaa = message.text[5:]
        aaa1 = True
    if message.text == '/chat' and (message.from_user.id == 1994579994 or message.from_user.id == 1351718225):
        aaa1 = False


    


@dp.callback_query()
async def po(callback: CallbackQuery):
    if callback.data == 'kak':
        await bot.send_message(callback.from_user.id, text='1. Добавьте бота в любую группу\n2. Сделайте бота администратором в группе\n3. Для того, чтобы пользоваться этим ботом в группе, напишите: "gpt: мой вопрос", где написано "мой вопрос", вместо это напишите ваш вопрос, который вы хотите задать.')
    if callback.data == 'pom':
        await bot.send_message(callback.from_user.id, text='Если у вас возникли вопросы или проблемы, то напишите пожалуйста нам - @ibrashua.')
    if callback.data == 'b':
        await start_message(callback)


# Обработка входящих сообщений
@dp.message()
async def proverka(message: Message):
    if message and message.text and message.text.startswith('gpt: '):
        speech_context[message.from_user.id] = viv()
        speech_context[message.from_user.id].msg = message.text[5:]
        await handle_message(message)
    else:
        if message.text.startswith('/context'):
            speech_context[message.from_user.id] = viv()
            speech_context[message.from_user.id].context = ""
            await message.reply('Контекст речи сброшен')
            speech_context[message.from_user.id].msg = ""
    


async def get_chat_info(chat_id):
    chat = await bot.get_chat(chat_id)
    return chat.username




async def handle_message(message: Message):
    try:
        user_input = speech_context[message.from_user.id].msg
        speech_context[message.from_user.id] = viv()
        speech_context[message.from_user.id].context += user_input + '\n'

        
        
        # Добавление пользовательских сообщений в разговор
        conversation.append({"role": "user", "content": user_input})
        await bot.send_chat_action(message.chat.id, "typing")
        # Генерация ответа модели
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        )
        # Вывод ответа модели
        model_response = response.choices[0].message['content']
        conversation.append({"role": "assistant", "content": model_response})
        await message.reply(model_response + "\n\nДля сброса диалога, используйте команду /context", parse_mode='Markdown')
        speech_context[message.from_user.id].msg = ""
            

    except:
        speech_context[message.from_user.id] = viv()
        user_input = message.text
    
        speech_context[message.from_user.id].context += user_input + '\n'

        
        # Добавление пользовательских сообщений в разговор
        conversation.append({"role": "user", "content": user_input})
        await bot.send_chat_action(message.chat.id, "typing")
        # Генерация ответа модели
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        )
        # Вывод ответа модели
        model_response = response.choices[0].message['content']
        conversation.append({"role": "assistant", "content": model_response})
        await message.reply(model_response + "\n\nДля сброса диалога, используйте команду /context", parse_mode='Markdown')
        speech_context[message.from_user.id].msg = ""



@dp.message()
async def send_to_groups(message: Message):
    if message.text.startswith('rass'):
        msg = message.text[4:]
        print("начинаем")
        # Получаем список всех чатов, в которых находится бот
        chats = await bot.get_chat_members_count(message.chat.id)
        # Отправляем сообщение во все группы
        i = 0
        for chat in chats:
            if chat.is_chat:
                i+=1
                print(i)
                await bot.send_message(chat.chat.id, msg)



async def main():
    while True:
        try:
            await dp.start_polling(bot)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            await asyncio.sleep(3)
            continue

if __name__ == '__main__':
    asyncio.run(main())
