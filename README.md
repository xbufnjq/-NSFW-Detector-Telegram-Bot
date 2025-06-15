# 🚫 NSFW Detector Telegram Bot

A Telegram bot that automatically bans users with NSFW (18+) profile pictures when they join a group. The bot uses a pre-trained Keras/TensorFlow model to detect explicit content.

## 🔍 Features

- Detects NSFW content using a CNN model.
- Automatically bans users with inappropriate profile photos.
- Runs with `aiogram` for efficient async handling.

## 📦 Requirements

- Python 3.7+
- Telegram Bot API token
- Pre-trained Keras model (`nsfw_model.h5`)
- OpenCV for image processing

## 🛠 Installation

```bash
git clone https://github.com/YOUR_USERNAME/nsfw-telegram-bot.git
cd nsfw-telegram-bot
pip install -r requirements.txt
