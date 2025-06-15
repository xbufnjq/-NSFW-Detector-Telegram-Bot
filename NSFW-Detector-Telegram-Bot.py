from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberUpdated
from aiogram.utils import executor
from tensorflow.keras.models import load_model
import cv2
import numpy as np

API_TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Загрузка модели
model = load_model('nsfw_model.h5')

# Функция предсказания 18+ контента
def is_nsfw(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    return prediction[0][0] > 0.5  # Если вероятность больше 50%, считаем 18+

# Обработка новых участников в группе
@dp.chat_member_handler()
async def handle_new_member(update: ChatMemberUpdated):
    if update.new_chat_member.status == "member":
        user = update.new_chat_member.user
        if user.photo:
            photo = await bot.get_user_profile_photos(user.id, limit=1)
            file_id = photo.photos[0][-1].file_id
            file = await bot.get_file(file_id)
            file_path = file.file_path
            await bot.download_file(file_path, "user_photo.jpg")
            
            if is_nsfw("user_photo.jpg"):
                await bot.kick_chat_member(update.chat.id, user.id)
                await update.chat.send_message(
                    f"Пользователь {user.full_name} был забанен за 18+ фото профиля."
                )

if __name__ == '__main__':
    executor.start_polling(dp)
