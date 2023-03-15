"""Generate Pyrogram Session String and send it to
Saved Messages of your Telegram account

requirements:
- Pyrogram
- TgCrypto

Get your Telegram API Key from:
https://my.telegram.org/apps
"""
import asyncio
from pyrogram import Client


async def main():
    print("""
        Go to my.telegram.org
        Login using your Telegram account
        Click on API Development Tools
        Create a new application, by entering the required details
        Check your Telegram saved messages section to get your SESSION_NAME
        """
        )
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**Pyrogram Session String**:\n\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "Done, your Pyrogram session string has been sent to "
            "Saved Messages of your Telegram account!"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())