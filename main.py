import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Логтарды қосу
logging.basicConfig(level=logging.INFO)

# Токенді жүктеу
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Назар аударыңыз! Тапсырыстар сізге келуі үшін өз Telegram ID-іңізді жазыңыз.
# Егер ID білмесеңіз, осы күйінде қалдырыңыз, Render Env-ке ADMIN_ID деп қосуға да болады.
ADMIN_ID = os.getenv("ADMIN_ID", "ӨЗ_ТЕЛЕГРАМ_ID_ЖАЗЫҢЫЗ") 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Тапсырыс қабылдау кезеңдері (FSM)
class OrderState(StatesGroup):
    name = State()
    phone = State()
    details = State()

# Негізгі мәзір кнопкалары
def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📄 Заңдық құжаттар мен хаттар"), KeyboardButton(text="🎤 Баяндама және сөздер")],
            [KeyboardButton(text="💰 Қызметтер мен Бағалар"), KeyboardButton(text="✍️ Тапсырыс беру")]
        ],
        resize_keyboard=True
    )

# /start командасы
@dp.message(Command("start"))
async def start_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    welcome_text = (
        "Сәлеметсіз бе! 👋\n\n"
        "Мен — «Qalamger» кәсіби қазақша мәтін жазу қызметінің көмекшісімін.\n\n"
        "🖊 Қызметтерімізге кіреді:\n"
        "• Заңдық құжаттар мен ресми хаттар\n"
        "• Баяндама және сөз сөйлеу мәтіндері\n\n"
        "Төменгі батырмалардан қажетті бөлімді таңдаңыз:"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

# 2. Заңдық құжаттар бөлімі
@dp.message(F.text == "📄 Заңдық құжаттар мен хаттар")
async def legal_docs(message: types.Message):
    text = (
        "📄 **Заңдық құжаттар мен хаттар**\n"
        "Біздің қызметтер:\n\n"
        "🔹 **Шарттар мен келісімшарттар**\n"
        "Азаматтық-құқықтық, еңбек, серіктестік шарттарын таза қазақ тілінде жасаймыз.\n\n"
        "🔹 **Ресми хаттар**\n"
        "Мемлекеттік органдарға, ұйымдарға арналған іскерлік хаттар.\n\n"
        "🔹 **Арыздар мен өтініштер**\n"
        "Сот, прокуратура, мемлекеттік мекемелерге арналған арыз мәтіндері.\n\n"
        "🔹 **Нотариалдық құжаттар**\n"
        "Сенімхаттар, мұрагерлік өтініштер және т.б.\n\n"
        "🔹 **Корпоративтік құжаттар**\n"
        "Жарғы, хаттама, шешімдер, бұйрықтар.\n\n"
        "Барлық мәтін — заңдық талаптарға сай, таза қазақ тілінде."
    )
    await message.answer(text, parse_mode="Markdown")

# 3. Баяндамалар бөлімі
@dp.message(F.text == "🎤 Баяндама және sөздер")
@dp.message(F.text == "🎤 Баяндама және сөздер")
async def speeches(message: types.Message):
    text = (
        "🎤 **Баяндама және Сөз сөйлеу мәтіндері**\n"
        "Біздің қызметтер:\n\n"
        "🔹 **Ресми баяндамалар**\n"
        "Конференция, симпозиум, ғылыми жиналыстарға арналған баяндама мәтіндері.\n\n"
        "🔹 **Салтанатты сөздер**\n"
        "Мерейтой, ашылу рәсімі, марапаттау шарасына арналған тост пен сөздер.\n\n"
        "🔹 **Ұйымдастырушы сөздері**\n"
        "Іс-шара жүргізушісіне арналған мәтін дайындаймыз.\n\n"
        "🔹 **Қоғамдық сөздер**\n"
        "Саяси, қоғамдық, мәдени тақырыптардағы ашық сөздер.\n\n"
        "🔹 **Оқу-ағарту баяндамалары**\n"
        "Мектеп, университет, семинарға арналған баяндамалар.\n\n"
        "Тіл мәнері — шешендік, бай, ресми немесе жылы — сіздің қалауыңызша."
    )
    await message.answer(text, parse_mode="Markdown")

# 4. Бағалар бөлімі
@dp.message(F.text == "💰 Қызметтер мен Бағалар")
async def prices(message: types.Message):
    text = (
        "💰 **Қызметтер мен Бағалар**\n\n"
        "📄 **Заңдық құжаттар**\n"
        "┌─────────────────────────────────\n"
        "│ Қарапайым хат / өтініш — 3 000 ₸\n"
        "│ Стандартты шарт — 8 000 ₸\n"
        "│ Күрделі шарт / келісімшарт — 15 000 ₸\n"
        "│ Жарғы / корпоративтік құжат — 20 000 ₸\n"
        "│ Нотариалдық дайындық — 5 000 ₸\n"
        "└─────────────────────────────────\n\n"
        "🎤 **Баяндама мен Сөздер**\n"
        "┌─────────────────────────────────\n"
        "│ Қысқа сөз (1-2 бет) — 4 000 ₸\n"
        "│ Орташа баяндама (3-5 бет) — 9 000 ₸\n"
        "│ Ұзақ баяндама (5+ бет) — 15 000 ₸\n"
        "│ Салтанатты сөз — 5 000 ₸\n"
        "└─────────────────────────────────\n\n"
        "⏱ **Дедлайн үстемесі**\n"
        "• 24 сағат — +50%\n"
        "• 12 сағат — +100%\n\n"
        "✅ **Бонустар**\n"
        "• Тегін бір реттік түзету\n"
        "• Конфиденциалдылық кепілдігі\n"
        "• Сапа кепілдемесі\n\n"
        "Нақты бағаны білу үшін ✍️ **Тапсырыс беру** арқылы хабарласыңыз."
    )
    await message.answer(text, parse_mode="Markdown")

# 5. Тапсырыс беру басылуы
@dp.message(F.text == "✍️ Тапсырыс беру")
async def order_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Сізбен байланысу үшін бірнеше сұрақ қояйын. \n\n1️⃣ **Атыңызды жазыңыз:**", 
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
    await state.set_state(OrderState.name)

# Атын қабылдау
@dp.message(OrderState.name)
async def order_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("2️⃣ **Байланыс телефоныңызды жазыңыз:**\n(Мысалы: +7 707 123 4567)")
    await state.set_state(OrderState.phone)

# Телефонын қабылдау
@dp.message(OrderState.phone)
async def order_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("3️⃣ **Тапсырыс туралы толық сипаттап жазыңыз:**\n(Қандай құжат немесе мәтін керек, бет саны, дедлайн уақыты)")
    await state.set_state(OrderState.details)

# Толық сипаттаманы қабылдау және админге жіберу
@dp.message(OrderState.details)
async def order_finish(message: types.Message, state: FSMContext):
    await state.update_data(details=message.text)
    data = await state.get_data()
    await state.clear()
    
    # Клиентке жауап
    await message.answer(
        "Рақмет! Тапсырыс қабылданды. ✨\nЖақын арада сізбен байланысамын.", 
        reply_markup=get_main_keyboard()
    )
    
    # Админге (сізге) хабарлама жіберу
    admin_text = (
        "🔔 **ЖАҢА ТАПСЫРЫС ТҮСТІ!**\n\n"
        f"👤 **Клиент:** {data['name']}\n"
        f"📞 **Телефон:** {data['phone']}\n"
        f"💬 **Тапсырыс сипаттамасы:** {data['details']}\n"
        f"🆔 **Юзернейм:** @{message.from_user.username if message.from_user.username else 'Жоқ'}"
    )
    
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Админге хат кетпеді: {e}")

# Ботты іске қосу
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
