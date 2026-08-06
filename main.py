import asyncio
import httpx

TOKEN = "8643414210:AAG-6Flr1vfE-tBAa7FJvRl1XdTpQtQ7Y7w"
CHANNEL_ID = "@gram_well"


async def main():
    print("Bot has been successfully started!")
    while True:
        async with httpx.AsyncClient() as client:
            try:
                url = (
                    "https://binance.com"
                )
                response = await client.get(url, timeout=10.0)

                if response.status_code == 200:
                    data = response.json()
                    price = round(float(data["price"]), 2)

                    telegram_url = (
                        f"https://telegram.org{TOKEN}/sendMessage"
                    )
                    payload = {
                        "chat_id": CHANNEL_ID,
                        "text": f"💎 **GRAM Live Price:** ${price}",
                        "parse_mode": "Markdown",
                    }
                    await client.post(telegram_url, json=payload, timeout=10.0)
                    print(f"Price updated successfully: ${price}")
                else:
                    print(f"Binance API error status: {response.status_code}")
            except Exception as error:
                print(f"Error occurred: {error}")

        await asyncio.sleep(300)


if __name__ == "__main__":
    asyncio.run(main())
