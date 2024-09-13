from aiogram.types import Message,FSInputFile,InputMediaPhoto,InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from loader import dp,db,bot
from aiogram import F
from aiogram.filters import CommandStart, Command
from handlers.users.insta import insta_save
from handlers.users.tiktok import tiktok_save

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="👋 *Salom!* Botimizga xush kelibsiz! 🎉\n\n"
            "📲 Bu bot orqali siz Instagram va TikTok'dan 📸 rasmlar, 🎥 videolar va 🎶 musiqalarni oson yuklab olishingiz mumkin.\n\n"
            "🔹 *Instagram videolarini yuklash:* Faqatgina Instagram video yoki rasm postining linkini yuboring va bot uni sizga yuklab beradi! 🚀\n"
            "🔹 *TikTok videolarini yuklash:* TikTok videolarini yuklash uchun TikTok'dagi video linkini yuboring va bot video, rasm va musiqalarni sizga jo'natadi! 🎧🎬\n\n"
            "💡 *Qanday ishlatish kerak?*\n"
            "1️⃣ Instagram yoki TikTok'dan linkni nusxalang.\n"
            "2️⃣ Linkni shu yerga yuboring.\n"
            "3️⃣ Bir necha soniya ichida yuklangan rasm, video yoki musiqani oling! 😍\n\n"
            "🛠 *Qo'shimcha imkoniyatlar:*\n"
            "👉 Instagram rasmlari va video postlarini yuklab olish\n"
            "👉 TikTok'dan rasmlar va musiqalarni ham yuklab olish\n"
            "👉 Tez va ishonchli yuklash jarayoni\n\n"
            "❓ Agar yordam kerak bo'lsa yoki muammo yuzaga kelsa, menga bemalol xabar yuboring! 😊\n\n"
            "Boshqa savollar uchun: /help\n"
            "Botimizdan zavqlaning! 🙌", parse_mode="Markdown")
    except:
        await message.answer(text="👋 *Salom!* Botimizga xush kelibsiz! 🎉\n\n"
            "📲 Bu bot orqali siz Instagram va TikTok'dan 📸 rasmlar, 🎥 videolar va 🎶 musiqalarni oson yuklab olishingiz mumkin.\n\n"
            "🔹 *Instagram videolarini yuklash:* Faqatgina Instagram video yoki rasm postining linkini yuboring va bot uni sizga yuklab beradi! 🚀\n"
            "🔹 *TikTok videolarini yuklash:* TikTok videolarini yuklash uchun TikTok'dagi video linkini yuboring va bot video, rasm va musiqalarni sizga jo'natadi! 🎧🎬\n\n"
            "💡 *Qanday ishlatish kerak?*\n"
            "1️⃣ Instagram yoki TikTok'dan linkni nusxalang.\n"
            "2️⃣ Linkni shu yerga yuboring.\n"
            "3️⃣ Bir necha soniya ichida yuklangan rasm, video yoki musiqani oling! 😍\n\n"
            "🛠 *Qo'shimcha imkoniyatlar:*\n"
            "👉 Instagram rasmlari va video postlarini yuklab olish\n"
            "👉 TikTok'dan rasmlar va musiqalarni ham yuklab olish\n"
            "👉 Tez va ishonchli yuklash jarayoni\n\n"
            "❓ Agar yordam kerak bo'lsa yoki muammo yuzaga kelsa, menga bemalol xabar yuboring! 😊\n\n"
            "Boshqa savollar uchun: /help\n"
            "Botimizdan zavqlaning! 🙌", parse_mode="Markdown")
        
#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("ℹ️ *Bot haqida ma'lumot* 🤖\n\n"
            "Bu bot sizga Instagram va TikTok'dan 📸 rasmlar, 🎥 videolar va 🎶 musiqalarni yuklab olishda yordam beradi! Bizning asosiy maqsadimiz – sizga oson va tezkor yuklash imkoniyatlarini taqdim etish. 🚀\n\n"
            "🔹 *Botning asosiy imkoniyatlari:*\n"
            "1️⃣ Instagram va TikTok'dan rasm va videolarni yuklab olish\n"
            "2️⃣ TikTok'dan musiqalarni yuklab olish\n"
            "3️⃣ Tezkor va ishonchli yuklash xizmati\n\n"
            "👨‍💻 *Loyihaning yaratuvchisi:* Nurbek Uktamov\n"
            "📆 *Botning yaratilgan vaqti:* 2024 yil\n\n"
            "💬 Agar bot haqida savollaringiz yoki takliflaringiz bo'lsa, biz bilan bog'lanishingiz mumkin: /support\n\n"
            "🎯 Maqsadimiz – sizga Instagram va TikTok mazmunini saqlab olishda eng yaxshi yordamchi bo'lish!", parse_mode="Markdown")
    

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("🆘 *Yordam bo'limi* 📚\n\n"
            "Botimizdan qanday foydalanish mumkinligi haqida batafsil ma'lumot: \n\n"
            "🔹 *Instagram va TikTok videolarini yuklash:*\n"
            "Instagram yoki TikTok'dagi video yoki rasm postining linkini nusxalang va shu yerga yuboring. Biz uni tezda yuklab beramiz! 🎥📸\n\n"
            "🔹 *Rasm va videolarni qanday yuklash:*\n"
            "Siz Instagram va TikTok'dan rasmlar va videolarni yuklab olishingiz mumkin. Faqat linkni yuboring va bot o'z ishini qiladi! 🚀\n\n"
            "🔹 *Bot qanday ishlaydi?*\n"
            "1️⃣ Instagram yoki TikTok'dan video yoki rasm postining linkini nusxalang.\n"
            "2️⃣ Bu linkni botga yuboring.\n"
            "3️⃣ Bot sizga yuklangan faylni yuboradi! 😎\n\n"
            "📨 Agar yordamga muhtoj bo'lsangiz yoki muammo yuzaga kelsa, bemalol menga xabar yuboring!\n"
            "📞 Qo'llab-quvvatlash: /support\n\n"
            "Boshqa imkoniyatlarni kashf qilish uchun davom eting! 🔍", parse_mode="Markdown")

@dp.message(F.text.contains("tiktok"))
async def tiktok_download(message: Message):
    link = message.text
    
    # Yuklanish jarayonini ko'rsatish uchun xabar
    loading_message = await message.answer("🔄 *Videoni yuklab olmoqdaman...* Iltimos, biroz kuting. 🕐")
    
    # TikTok ma'lumotlarini olish
    tiktok_data = tiktok_save(link)
    
    # Yuklanish tugadi, xabarni o'chirish
    await loading_message.delete()
    
    # TikTok'dan olingan ma'lumotlar
    video = tiktok_data.get("video")
    music = tiktok_data.get("music")
    rasmlar = tiktok_data.get("images")
    
    # Rasmlarni jo'natish
    if rasmlar:
        await message.answer("🖼️ *TikTok rasmlari tayyor!*\nQuyidagi rasmlarni ko'rib chiqing:")
        rasm_media = []
        for i, r in enumerate(rasmlar):
            if not r.startswith("http"):
                print(f"Rasm URL noto'g'ri: {r}")
                continue
            rasm_media.append(InputMediaPhoto(media=r))
            if (i + 1) % 10 == 0:
                await message.answer_media_group(rasm_media)
                rasm_media = []
        if rasm_media:
            await message.answer_media_group(rasm_media)
    
    # Videoni jo'natish
    if video:
        if not video.startswith("http"):
            print(f"Video URL noto'g'ri: {video}")
        else:
            await message.answer("🎥 *Mana sizning TikTok videongiz!*")
            await message.answer_video(video=video)
    
    # Musiqani jo'natish
    if music:
        if not music.startswith("http"):
            print(f"Audio URL noto'g'ri: {music}")
        else:
            await message.answer("🎵 *Mana sizning TikTok musiqangiz!* 🎧")
            await message.answer_audio(audio=music)

    # Tugatish xabari
    await message.answer("✅ *Yuklab olish tugadi!* Agar boshqa video yoki ma'lumot kerak bo'lsa, menga xabar bering. 😊👍")







@dp.message()
async def handle_message(message: Message):
    # Foydalanuvchi link yuborganini tekshirish
    if message.text.startswith('http'):
        link = message.text

        # Yuklanish jarayonini ko'rsatish uchun xabar
        loading_message = await message.reply("⏳ *Ma'lumot yuklanmoqda...* Iltimos, biroz sabr qiling. 🚀")

        # Instagram ma'lumotlarini yuklash
        media = insta_save(link)

        # Yuklanayotgan xabarni o'chirish
        await bot.delete_message(message.chat.id, loading_message.message_id)

        # Agar rasm mavjud bo'lsa
        if "images" in media:
            if media["images"]:
                await message.reply("📸 *Mana sizning Instagram rasmlaringiz!* Ko'rishdan zavqlaning. 😍")
                for image_url in media["images"]:
                    await message.answer_photo(image_url)
            else:
                await message.reply("❌ *Afsuski, hech qanday rasm topilmadi.* Iltimos, boshqa linkni sinab ko'ring. 🌐")
        
        # Agar video mavjud bo'lsa
        elif "video" in media:
            await message.reply("🎥 *Mana sizning Instagram videoyingiz!* Ko'rishdan zavqlaning. 🍿")
            await message.answer_video(media["video"])
        
        # Xatolik mavjud bo'lsa
        elif "error" in media:
            await message.reply(f"⚠️ *Xatolik yuz berdi:* {media['error']}")

    # Agar foydalanuvchi haqiqiy link yubormasa
    else:
        await message.reply("❌ *Iltimos, haqiqiy Instagram linkini yuboring va yana urinib ko'ring.* 🌐")


