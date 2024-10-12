import random

def get_motivation(language: str):
    motivational_expressions_dict = {
    'fa': [
        "🔥 دمت گرم!",
        "🌟 عالی بود!",
        "👏 ایول، تو حرف نداری!",
        "💪 تو حرف نداری!",
        "🙌 دستت طلا!",
        "✅ کارت درسته!",
        "💥 ادامه بده!",
        "🌸 گل کاشتی!",
        "👌 به این میگن کار درست!",
        "🚀 حسابی داری پیشرفت می‌کنی!",
        "🧠 همیشه می‌دونی چی کار کنی!",
        "🏆 هیچی جلودارت نیست!",
        "❤️ بهت افتخار می‌کنم!",
        "✨ همیشه بهت ایمان داشتم!",
        "🤩 مثل همیشه فوق‌العاده‌ای!",
        "⚡️ با قدرت برو جلو!",
        "🌞 مثل خورشید می‌درخشی!",
        "👍 کارت حرف نداره، عالیه!",
        "🙌 یعنی واقعا دمت گرم!",
        "💯 بیشتر از این انتظار نداشتم!",
        "💥 واقعاً محشری!",
        "🌈 تو بهترینی!",
        "🔥 فوق‌العاده‌ای، ادامه بده!",
        "💫 همه جا می‌درخشی!",
        "🤔 چی می‌تونه جلوی تو رو بگیره؟",
        "🤝 استاد کارهای درست!",
        "🎯 هر روز داری بهتر می‌شی!",
        "😎 بهت حسادت می‌کنم با این انرژی!",
        "🥳 خیلی باحال و با انگیزه‌ای!",
        "🏅 می‌دونم موفق می‌شی!"
    ],
    'en': [
        "🔥 You're on fire!",
        "🌟 That was awesome!",
        "👏 Wow, you're unstoppable!",
        "💪 You're a rockstar!",
        "🙌 You crushed it!",
        "✅ You're nailing it!",
        "💥 Keep it going!",
        "🌸 You knocked it out of the park!",
        "👌 Now that's what I call perfect!",
        "🚀 You're making huge progress!",
        "🧠 You always know what to do!",
        "🏆 Nothing can stop you!",
        "❤️ I'm so proud of you!",
        "✨ I've always believed in you!",
        "🤩 You're amazing as always!",
        "⚡️ Keep pushing forward!",
        "🌞 You're shining like the sun!",
        "👍 You're killing it, great job!",
        "🙌 Seriously, you're awesome!",
        "💯 Couldn't expect anything less!",
        "💥 You're absolutely incredible!",
        "🌈 You're the best!",
        "🔥 You're amazing, keep it up!",
        "💫 You're shining everywhere!",
        "🤔 What's gonna stop you?",
        "🤝 Master of getting it right!",
        "🎯 You're improving every day!",
        "😎 I'm jealous of your energy!",
        "🥳 You're super cool and motivated!",
        "🏅 I know you're going to succeed!"
    ],
    'ru': [
        "🔥 Ты просто огонь!",
        "🌟 Это было круто!",
        "👏 Вау, ты непобедим(а)!",
        "💪 Ты настоящий молодец!",
        "🙌 Ты отлично справился(ась)!",
        "✅ Всё у тебя отлично получается!",
        "💥 Продолжай в том же духе!",
        "🌸 Ты отлично справился(ась)!",
        "👌 Вот это настоящий успех!",
        "🚀 Ты делаешь огромные шаги!",
        "🧠 Ты всегда знаешь, что делать!",
        "🏆 Ничто тебя не остановит!",
        "❤️ Я горжусь тобой!",
        "✨ Я всегда в тебя верил(а)!",
        "🤩 Как всегда, ты великолепен(на)!",
        "⚡️ Вперёд, с полной силой!",
        "🌞 Ты сияешь, как солнце!",
        "👍 Отличная работа, ты на высоте!",
        "🙌 Серьёзно, ты просто супер!",
        "💯 Я и не ожидал(а) другого!",
        "💥 Ты просто невероятен(на)!",
        "🌈 Ты лучший(ая)!",
        "🔥 Ты великолепен(на), так держать!",
        "💫 Ты сияешь везде!",
        "🤔 Что может тебя остановить?",
        "🤝 Ты мастер своего дела!",
        "🎯 С каждым днём ты становишься лучше!",
        "😎 Я завидую твоей энергии!",
        "🥳 Ты такой крутой и мотивированный!",
        "🏅 Я уверен(а), что у тебя всё получится!"
    ]
    }

    if language == 'fa':
        word = random.choice(motivational_expressions_dict['fa'])
    if language == 'en':
        word = random.choice(motivational_expressions_dict['en'])
    if language == 'ru':
        word = random.choice(motivational_expressions_dict['ru'])
    return word

def communication_expression(language: str, first_name: str, word_counter: int):
    expressions_dict = {
    'fa': [
        f"خوش برگشتی {first_name} جون 😍\nاز منوی زیر میتونی انتخاب کنی.",
        f"سلام {first_name} جون. تو قبلا رجیستر شدی.\n از منوی زیر میتونی انتخاب کنی.",
        "شما رجیستر نشدی. میخوای رجیستر کنی؟",
        "به چه اسمی صدات کنم؟",
        "میخوای فنلاندی رو به چه زبونی یاد بگیری؟",
        f"رجیسر شدی {first_name} 🤩🎉\nاز منوی زیر میتونی وارد برنامه بشی.",
        "گرفتم! بعدی",
        "شما وارد منو شدید.",
        "شما در صفحه اصلی هستید.",
        f"هووورااا🎉\nامروز {word_counter} کلمه مرور کردی. واسه امروز بسه، فردا میبینمت.",
        "بزن بریم 💥"
    ],
    'ru': [
        f"С возвращением, {first_name}! 😍\nВыберите пункт из меню ниже.",
        f"Привет, {first_name}! Вы уже зарегистрированы.\nВыберите пункт из меню ниже.",
        "Вы не зарегистрированы. Хотите зарегистрироваться?",
        "Как мне вас называть?",
        "На каком языке хотите учить финский?",
        f"Вы зарегистрированы, {first_name}! 🤩🎉\nТеперь вы можете воспользоваться меню ниже.",
        "Понял! Далее",
        "Вы вошли в меню.",
        "Вы находитесь на главной странице.",
        f"Ура! 🎉\nСегодня вы повторили {word_counter} слов. На сегодня достаточно, до завтра!",
        "Поехали! 💥"
    ],
    'en': [
        f"Welcome back, {first_name}! 😍\nChoose an option from the menu below.",
        f"Hi, {first_name}! You are already registered.\nChoose an option from the menu below.",
        "You are not registered. Would you like to register?",
        "What name should I call you?",
        "Which language would you like to learn Finnish in?",
        f"You are registered, {first_name}! 🤩🎉\nYou can now enter the program through the menu below.",
        "Got it! Next",
        "You entered the menu.",
        "You are on the main page.",
        f"Hooray! 🎉\nToday you reviewed {word_counter} words. That's enough for today; see you tomorrow!",
        "Let's go! 💥"
    ]
    }

    if language == 'fa':
        expressions_list = expressions_dict['fa']
    if language == 'en':
        expressions_list = expressions_dict['en']
    if language == 'ru':
        expressions_list = expressions_dict['ru']

    return expressions_list

def generate_user_record_text(remember, not_remember, language):
    
    if (remember + not_remember > 0):
        if language == 'fa':
            return f"""توی هفته گذشته:\nتعداد {remember + not_remember} کلمه رو مرور کردی که از این تعداد، {remember} تا رو بلد بودی و {not_remember} تا رو بلد نبودی."""
        elif language == 'en':
            return f"""In the past week:\nYou reviewed a total of {remember + not_remember} words, out of which you knew {remember} and didn't know {not_remember}."""
        elif language == 'ru':
            return f"""За последнюю неделю:\nВы повторили {remember + not_remember} слов, из которых {remember} вы знали, а {not_remember} не знали."""
    else:
        if language == 'fa':
            return "توی هفته گذشته هیچ کلمه‌ای رو مرور نکردی. از منوی زیر میتونی تمرین کلمات رو شروع کنی."
        elif language == 'en':
            return "You didn't review any words last week. You can start practicing words from the menu below."
        elif language == 'ru':
            return "На прошлой неделе вы не повторяли ни одного слова. Вы можете начать практиковать слова из меню ниже."

def generate_word_review_text(words, language):
    messages = {
    'fa': [
        f"""اینها کلماتی هستند که توی هفته گذشته بلد بودی و جلوشون تعداد دفعاتیه که مرور کردی تا یادشون بگیری:\n\n{words}""", 
        "توی هفته گذشته هیچ کلمه‌ای رو یاد نگرفتی."
    ],
    'en': [
        f"""These are the words you knew last week, along with the number of times you reviewed them to learn them:\n\n{words}""", 
        "You didn't learn any words last week."
    ],
    'ru': [
        f"""Это слова, которые вы знали на прошлой неделе, вместе с количеством раз, когда вы их повторяли, чтобы их выучить:\n\n{words}""", 
        "На прошлой неделе вы не выучили ни одного слова."
    ]
    }
    message = messages[language]
    return message

if __name__ == '__main__':
    language = 'en'
    print(get_motivation(language= language))








