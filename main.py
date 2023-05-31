from base.module import BaseModule, command
from pyrogram.types import Message

# Modules
import httpx

class ModuleTemplate(BaseModule):
    # Register handler
    @command("tt")
    async def tt_cmd(self, _, message: Message):
        """Download videos from TikTok for free without sms and registration"""

        # [/tt, tt_url]
        params = message.text.split()
        if len(params) == 1:
            return await message.reply(f"❌ <b>{self.S['error']['no_link']}</b>")

        await message.delete()

        async with httpx.AsyncClient() as client:
            tik_get = (await client.get(f"https://api.douyin.wtf/api?url={params[1]}&minimal=true")).json()
            if tik_get["type"] not in ["video"]:
                return await message.reply(f"❌ <b>{self.S['error']['not_supported_type']}</b>")
                
            await message.reply_video(tik_get["nwm_video_url"], caption=tik_get["desc"])
