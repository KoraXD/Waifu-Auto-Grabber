# © Waifu Auto Grabber

"""
🔥 Developers:
     ⚡ Kora | @KoraXD
     ⚡ Dark | @IkariS0_0
     ⚡ Otazuki | @Otazuki
"""

import pyrogram, asyncio
from Waifu import waifu

async def main():
    await waifu.start()
    await pyrogram.idle()

if __name__ == "__main__":
    asyncio.run(main())
