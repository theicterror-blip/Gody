import requests
import random
import json
import time
from datetime import datetime, timedelta
import pytz
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

PAIRS = ["EURUSD-OTC", "USDJPY-OTC", "GBPUSD-OTC", "EURJPY-OTC", "AUDUSD-OTC"]
DIRECTIONS = ["CALL", "PUT"]
total_win = 0
total_loss = 0

def generate_signal():
    pair = random.choice(PAIRS)
    direction = random.choice(DIRECTIONS)
    now = datetime.now(pytz.timezone("Asia/Karachi"))
    signal_time = now.strftime("%I:%M %p")
    return {
