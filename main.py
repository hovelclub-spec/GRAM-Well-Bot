import asyncio
import httpx

TOKEN = "8643414210:AAG-6Flr1vfE-tBAa7FJvRl1XdTpQtQ7Y7w"
CHANNEL_ID = "@gram_well"
INTERVAL = 300


async def get_gram_price():
    url = (
        "https://coingecko.com"
    )
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            data = response.json()
            return data.get("gram", {}).get("usd", None)
        except Exception as e:
            print(f"API Error: {e}")
            return None


async def main():
    print(f"Bot started! Broadcasting to {CHANNEL_ID} every 5 minutes...")
    while True:
        price = await get_gram_price()

        if price is not None:
            text = f"💎 **GRAM Live Price:** ${price}"

            async with httpx.AsyncClient() as client:
                api_url = f"https://telegram.org{TOKEN}/sendMessage"
                payload = {
                    "chat_id": CHANNEL_ID,
                    "text": text,
                    "parse_mode": "Markdown",
                }
                response = await client.post(api_url, json=payload)

                if response.status_code == 200:
                    print(f"Success: Sent ${price} to {CHANNEL_ID}")
                else:
                    print(f"Telegram API Error: {response.text}")
        else:
            print("Failed to fetch price, skipping this interval.")

        await asyncio.sleep(INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())
  
