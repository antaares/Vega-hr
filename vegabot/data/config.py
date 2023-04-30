from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
admins_ = env.list("ADMINS")
ADMINS = [int(admin) for admin in admins_]  # Adminlar ro'yhati
IP = env.str("ip")  # Xosting ip manzili
channel_id = env.str('channel_id')

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
