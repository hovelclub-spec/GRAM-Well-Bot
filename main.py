import asyncio
import httpx

TOKEN = "8643414210:AAG-6Flr1vfE-tBAa7FJvRl1XdTpQtQ7Y7w"
CHANNEL_ID = "@gram_well"


async def main():
    print("Bot has been successfully started!")
    while True:
        async with httpx.AsyncClient() as client:
            try:
                # Используем стабильный и открытый API CoinCap для Toncoin (GRAM)
                url = "https://coincap.io"
                response = await client.get(url, timeout=10.0)

                if response.status_code == 200:
                    data = response.json()
                    price_str = data.get("data", {}).get("priceUsd", None)

                    if price_str:
                        price = round(float(price_str), 2)

                        # Отправка сообщения в Telegram-канал
                        telegram_url = f"https://telegram.org{TOKEN}/sendMessage"
                        payload = {
                            "chat_id": CHANNEL_ID,
                            "text": f"💎 **GRAM Live Price:** ${price}",
                            "parse_mode": "Markdown",
                        }
                        await client.post(
                            telegram_url, json=payload, timeout=10.0
                        )
                        print(f"Price updated successfully: ${price}")
                else:
                    print(f"CoinCap API error status: {response.status_code}")
            except Exception as error:
                print(f"Error occurred: {error}")

        # Ожидание 5 минут (300 секунд)
        await asyncio.sleep(300)


if __name__ == "__main__":
    asyncio.run(main())
