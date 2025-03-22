   import os
   import random
   from pyrogram import Client, filters
   from pyrogram.types import InputPhoto

   # Replace these with your own values
   API_ID = "22012880"  # Get from https://my.telegram.org
   API_HASH = "5b0e07f5a96d48b704eb9850d274fe1d"  # Get from https://my.telegram.org
   BOT_TOKEN = "8113642693:AAG9yJpZjyhKIP_nhsIIoc8ZsiTJ-gsudLU"  # Get from @BotFather

   # Path to the folder containing wallpapers
   WALLPAPER_FOLDER = "minimalistic-wallpaper-collection/images"

   # Initialize the Pyrogram client
   app = Client("wallpaper_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

   # Command to start the bot
   @app.on_message(filters.command("start"))
   def start(client, message):
       message.reply_text("Welcome! Use /gen to get a random wallpaper.")

   # Command to send a random wallpaper
   @app.on_message(filters.command("gen"))
   def send_wallpaper(client, message):
       # Get a list of all wallpaper files
       wallpapers = [f for f in os.listdir(WALLPAPER_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg'))]

       if not wallpapers:
           message.reply_text("No wallpapers found!")
           return

       # Randomly select a wallpaper
       random_wallpaper = random.choice(wallpapers)
       wallpaper_path = os.path.join(WALLPAPER_FOLDER, random_wallpaper)

       # Send the wallpaper as a photo
       message.reply_photo(photo=wallpaper_path, caption="Here's your random wallpaper! 🎨")

   # Run the bot
   print("Bot is running...")
   app.run()
