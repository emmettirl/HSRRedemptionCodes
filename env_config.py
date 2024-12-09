# env_config.py
import os
from dotenv import load_dotenv

class EnvConfig:
    def __init__(self):
        load_dotenv()
        self.mi18n_lang = os.getenv("MI18N_LANG")
        self.devicefp = os.getenv("DEVICEFP")
        self.hyvuuid = os.getenv("HYVUUID")
        self.mhyuuid = os.getenv("MHYUUID")
        self.devicefp_seed_id = os.getenv("DEVICEFP_SEED_ID")
        self.devicefp_seed_time = os.getenv("DEVICEFP_SEED_TIME")
        self.cookie_token_v2 = os.getenv("COOKIE_TOKEN_V2")
        self.account_mid_v2 = os.getenv("ACCOUNT_MID_V2")
        self.account_id_v2 = os.getenv("ACCOUNT_ID_V2")
        self.ltoken_v2 = os.getenv("LTOKEN_V2")
        self.ltmid_v2 = os.getenv("LTMID_V2")
        self.ltuid_v2 = os.getenv("LTUID_V2")
        self.e_bh3_token = os.getenv("E_BH3_TOKEN")
        self.doorman_event_hkrpg_pro_bot_discord_token = os.getenv("DOORMAN_EVENT_HKRPG_PRO_BOT_DISCORD_TOKEN")
        self.doorman_event_hkrpg_pro_bot_discord_openid = os.getenv("DOORMAN_EVENT_HKRPG_PRO_BOT_DISCORD_OPENID")

        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json;",
            "Origin": "https://hsr.hoyoverse.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://hsr.hoyoverse.com/"
        }

        self.COOKIES = {
            "mi18nLang": self.mi18n_lang,
            "DEVICEFP": self.devicefp,
            "_HYVUUID": self.hyvuuid,
            "_MHYUUID": self.mhyuuid,
            "DEVICEFP_SEED_ID": self.devicefp_seed_id,
            "DEVICEFP_SEED_TIME": self.devicefp_seed_time,
            "cookie_token_v2": self.cookie_token_v2,
            "account_mid_v2": self.account_mid_v2,
            "account_id_v2": self.account_id_v2,
            "ltoken_v2": self.ltoken_v2,
            "ltmid_v2": self.ltmid_v2,
            "ltuid_v2": self.ltuid_v2,
            "e_bh3_token": self.e_bh3_token,
            "doorman_event_hkrpg_pro_bot_discord_token": self.doorman_event_hkrpg_pro_bot_discord_token,
            "doorman_event_hkrpg_pro_bot_discord_openid": self.doorman_event_hkrpg_pro_bot_discord_openid
        }