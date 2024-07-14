import telebot
import random

# Replace YOUR_TOKEN_HERE with your actual Telegram bot token
bot = telebot.TeleBot("YOUR_TOKEN_HERE")

# Define a list of greetings
greetings = ["Yoi ki haal", "Kaisa h dost", "Faltu group join krne ke alawa aur koi kaam nhi h??", "Firse aa gye bro!"]

# Define a list of compliments
compliments = ["You are amazing!", "You are the best!", "You are a genius!", "You are a superhero!"]

# Define a list of kisses
kisses = ["💋", "😘", "😚", "😗", "😙"]

# Define a list of hugs
hugs = ["🤗", "🤗🤗", "🤗🤗🤗", "🫂"]

# Define a command handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hey there! Type /help to see the available commands.")

# Define a command handler for the /help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Here are the available commands:\n/start - start the bot\n/help - display the available commands\n/about - display information about the bot\n/praise - praise a user\n/kiss - send a kiss\n/hug - send a hug")

# Define a command handler for the /about command
@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "This bot was created by some idiot dont ask for anything please.")

# Define a command handler for the /praise command
@bot.message_handler(commands=['praise'])
def praise(message):
    user = message.reply_to_message.from_user.first_name if message.reply_to_message else "you"
    compliment = random.choice(compliments)
    bot.reply_to(message, f"{compliment} {user}!")

# Define a command handler for the /kiss command
@bot.message_handler(commands=['kiss'])
def kiss(message):
    user = message.reply_to_message.from_user.first_name if message.reply_to_message else "you"
    kiss = random.choice(kisses)
    bot.reply_to(message, f"{kiss} {user}!")

# Define a command handler for the /hug command
@bot.message_handler(commands=['hug'])
def hug(message):
    user = message.reply_to_message.from_user.first_name if message.reply_to_message else "you"
    hug = random.choice(hugs)
    bot.reply_to(message, f"{hug} {user}!")

# Define a message handler for regular text messages
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Sorry, I didn't understand that. Type /help to see the available commands.")

# Define a handler for new members joining the group
@bot.message_handler(content_types=['new_chat_members'])
def greet_new_member(message):
    for user in message.new_chat_members:
        greeting = random.choice(greetings)
        bot.send_message(message.chat.id, f"{greeting} {user.first_name}!")

# Start the bot
bot.polling()
