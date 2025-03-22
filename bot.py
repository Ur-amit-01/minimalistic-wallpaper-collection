import os
import random
import requests
from pyrogram import Client, filters

# Replace these with your own values
API_ID = "22012880"  # Get from https://my.telegram.org
API_HASH = "5b0e07f5a96d48b704eb9850d274fe1d"  # Get from https://my.telegram.org
BOT_TOKEN = "8113642693:AAG9yJpZjyhKIP_nhsIIoc8ZsiTJ-gsudLU"  # Get from @BotFather

# GitHub repository details
GITHUB_REPO = "Ur-amit-01/minimalistic-wallpaper-collection"
GITHUB_FOLDER = "images"  # Folder containing wallpapers

# Initialize the Pyrogram client
app = Client("wallpaper_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to fetch wallpapers from GitHub
def fetch_wallpapers():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FOLDER}"
    response = requests.get(url)
    if response.status_code == 200:
        files = response.json()
        wallpapers = [file["download_url"] for file in files if file["name"].endswith(('.png', '.jpg', '.jpeg'))]
        return wallpapers
    return []

# Command to start the bot
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Welcome! Use /gen to get a random wallpaper.")

# Command to send a random wallpaper
@app.on_message(filters.command("gen"))
def send_wallpaper(client, message):
    wallpapers = fetch_wallpapers()
    if not wallpapers:
        message.reply_text("No wallpapers found!")
        return

    # Randomly select a wallpaper
    random_wallpaper = random.choice(wallpapers)

    # Send the wallpaper as a photo
    message.reply_photo(photo=random_wallpaper, caption="Here's your random wallpaper! 🎨")

# Run the bot
print("Bot is running...")
app.run()

