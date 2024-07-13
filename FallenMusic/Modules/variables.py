# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from FallenMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} Yapılandırma Değişkenleri:**</u>

**ᴀᴘɪ_ɪᴅ :** `{config.API_ID}`
**ᴀᴘɪ_ʜᴀsʜ :** `{config.API_HASH}`

**ʙᴏᴛ_ᴛᴏᴋᴇɴ :** `{config.BOT_TOKEN}`
**ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ :** `{config.DURATION_LIMIT}`

**ᴏᴡɴᴇʀ_ɪᴅ :** `{config.OWNER_ID}`
**sᴜᴅᴏ_ᴜsᴇʀs :** `{config.SUDO_USERS}`

**ᴘɪɴɢ_ɪᴍɢ :** `{config.PING_IMG}`
**sᴛᴀʀᴛ_ɪᴍɢ :** `{config.START_IMG}`
**sᴜᴘᴘᴏʀᴛ_ᴄʜᴀᴛ :** `{config.SUPPORT_CHAT}`

**sᴇssɪᴏɴ :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("» Yapılandırma Değişkenleri Gönderiminde Hata Oluştu.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "» Lütfen PM Kontrol Et Bebeğim 🙃, İsteğiniz Gerçekleşti."
        )
