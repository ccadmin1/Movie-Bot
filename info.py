import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(523341)
API_HASH = "802287dfc2482d86cc07fbf12f3c1750"
BOT_TOKEN = "2020023864:AAFIpFkL2X6cdzv3227_ePvQ0Z5-vHO2NtI"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = "https://telegra.ph/file/e92a3cfd34f26e84d7701.jpg https://telegra.ph/file/d053a8e9ef4ed93df38a0.jpg https://telegra.ph/file/d1c6ee6d32e142f3674ed.jpg https://telegra.ph/file/8fd7710ee17bd34a963a5.jpg https://telegra.ph/file/ecb7510e187f0e3b60852.jpg"

# Admins, Channels & Users
ADMINS = [897298824 1498911533]
CHANNELS = [-1001413599796 -1001681594064  -1001604040747]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(-1001628588311)
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://pdisk:pdisk@cluster0.veegd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "cluster0"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = "-1001751100720"
SUPPORT_CHAT = "https://t.me/+3FMHnwG5ED5jOWQ1"
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = "<b><code>{file_name}</code></b>
<b>▶️ Size : {file_size}</b>
╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
♻️ 𝙅𝙊𝙄𝙉 :- @Anjalina_bot
♻️ 𝙅𝙊𝙄𝙉 :- @cinemacollections
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝"
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>⍞ ᴛɪᴛʟᴇ:</b> <a href={url}>{title}</a>\n<b>〄 ᴛʏᴘᴇ:</b> {kind}\n<b>⟴ ʀᴇʟᴇᴀꜱᴇ ᴅᴀᴛᴇ:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>★ ʀᴀᴛɪɴɢ:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>⌥ ʀᴜɴᴛɪᴍᴇ:</b> <code>{runtime} minutes</code>\n<b>⌗ ɢᴇɴʀᴇ:</b> {genres}\n\n<b>⌬ ʟᴀɴɢᴜᴀɢᴇs:</b> {languages}\n<b>✠ ᴄᴏᴜɴᴛʀɪᴇs:</b> {countries}\n<a href='https://t.me/cinemacollections '>© cinemacollections</a></b>\n\n✍️ Note:</b> This message will be Auto-deleted after 10 minutes to avoid copyright issues")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
UPSTREAM_REPO = "https://github.com/ccadmin1/Movie-Bot"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
