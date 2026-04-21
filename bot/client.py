from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    # ✅ THIS is the correct way
    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

    return client