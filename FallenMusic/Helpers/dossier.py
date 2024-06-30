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

from FallenMusic import BOT_NAME

PM_START_TEXT = """
<b>Merhaba</b> {0}, 🥀
๏ Saygılarımla 🥰  {1} !

<b>➻ Hızlı & Muhteşem Özelliklere Sahip En İyi Telegram Müzik Botu.</b>
"""

START_TEXT = """
<b>Merhaba</b> {0}, 🥀
  {1} Müzik Yayınını Başlatabilirsiniz 😎 {2}.

──────────────────
➻ Yardım Almak İstediğiniz Kategoriyi Seçin.\nDAHA FAZLA YARDIM İÇİN [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({3}).
"""

HELP_TEXT = f"""
<u>❄ **Kullanıcılar İçin Komutlar {BOT_NAME} :**</u>

๏ /play : İstenilen parçayı görüntülü sohbette yayınlamaya başlar.
๏ /pause : Mevcut oynatma akışını duraklatır.
๏ /resume : Duraklatılan akışı devam ettirir.
๏ /skip : Mevcut oynatma akışını atla ve sıradaki parçayı oynatmaya başlar.
๏ /end : Listeyi temizler ve mevcut oynatma akışını sonlandırır.

๏ /ping : Botun ping ve sistem istatistiklerini gösterir.
๏ /sudolist : Yetkili Kullanıcı listesi.

๏ /song :  Herhangi bir parçayı indirir.

๏ /search :  Youtube'dan herhangi bir parçayı mp3 veya mp4 formatında indirir.
"""

HELP_SUDO = f"""
<u>✨ **Yetkili Kullanıcılar {BOT_NAME} :**</u>

๏ /activevc : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /speedtest : ʀᴜɴs ᴀ sᴘᴇᴇᴅᴛᴇsᴛ ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /sysstats : sʜᴏᴡs ᴛʜᴇ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.

๏ /setname [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ɴᴀᴍᴇ.
๏ /setbio [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙɪᴏ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /setpfp [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /delpfp : ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
"""

HELP_DEV = f"""
<u>✨ **ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅs ɪɴ {BOT_NAME} :**</u>

๏ /config : ᴛᴏ ɢᴇᴛ ᴀʟʟ ᴄᴏɴꜰɪɢ ᴠᴀʀɪᴀʙʟᴇꜱ ᴏꜰ ʙᴏᴛ.
๏ /broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmdownloads : ᴄʟᴇᴀʀs ᴛʜᴇ ᴄᴀᴄʜᴇ ғɪʟᴇs ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /leaveall : ᴏʀᴅᴇʀs ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴀʟʟ ᴄʜᴀᴛs.

๏ /addsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ᴀᴅᴅ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
๏ /rmsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʀᴇᴍᴏᴠᴇ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
"""
