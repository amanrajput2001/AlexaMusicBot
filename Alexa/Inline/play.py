# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


from pyrogram.types import (CallbackQuery, InlineKeyboardButton,

                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Alexa import db_mem

def url_markup(videoid, duration, user_id, query, query_type):

    buttons = [

        [

            InlineKeyboardButton(

                text="❮",

                callback_data=f"slider B|{query_type}|{query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🎵",

                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🎥",

                callback_data=f"Choose {videoid}|{duration}|{user_id}",

            ),

            InlineKeyboardButton(

                text="❯",

                callback_data=f"slider F|{query_type}|{query}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="🔎 𝐌𝐨𝐫𝐞 𝐫𝐞𝐬𝐮𝐥𝐭𝐬",

                callback_data=f"Search {query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🗑 𝐂𝐥𝐨𝐬𝐞 𝐬𝐞𝐚𝐫𝐜𝐡 ",

                callback_data=f"forceclose {query}|{user_id}",

            ),

        ],

    ]

    return buttons

def url_markup2(videoid, duration, user_id):

    buttons = [

        [

            InlineKeyboardButton(

                text="🎵 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜",

                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🎥 𝐏𝐥𝐚𝐲 𝐯𝐢𝐝𝐞𝐨",

                callback_data=f"Choose {videoid}|{duration}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="🗑 𝐂𝐥𝐨𝐬𝐞 𝐬𝐞𝐚𝐫𝐜𝐡",

                callback_data=f"forceclose {videoid}|{user_id}",

            )

        ],

    ]

    return buttons

def search_markup(

    ID1,

    ID2,

    ID3,

    ID4,

    ID5,

    duration1,

    duration2,

    duration3,

    duration4,

    duration5,

    user_id,

    query,

):

    buttons = [

        [

            InlineKeyboardButton(

                text="1️⃣", callback_data=f"𝐭𝐬𝐠 {ID1}|{duration1}|{user_id}"

            ),

            InlineKeyboardButton(

                text="2️⃣", callback_data=f"𝐭𝐬𝐠 {ID2}|{duration2}|{user_id}"

            ),

            InlineKeyboardButton(

                text="3️⃣", callback_data=f"𝐭𝐬𝐠 {ID3}|{duration3}|{user_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="4️⃣", callback_data=f"𝐭𝐬𝐠 {ID4}|{duration4}|{user_id}"

            ),

            InlineKeyboardButton(

                text="5️⃣", callback_data=f"𝐭𝐬𝐠 {ID5}|{duration5}|{user_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="<", callback_data=f"popat 1|{query}|{user_id}"

            ),

            InlineKeyboardButton(

                text="🗑 𝐜𝐥𝐨𝐬𝐞", callback_data=f"forceclose {query}|{user_id}"

            ),

            InlineKeyboardButton(

                text=">", callback_data=f"popat 1|{query}|{user_id}"

            ),

        ],

    ]

    return buttons

def search_markup2(

    ID6,

    ID7,

    ID8,

    ID9,

    ID10,

    duration6,

    duration7,

    duration8,

    duration9,

    duration10,

    user_id,

    query,

):

    buttons = [

        [

            InlineKeyboardButton(

                text="6️⃣",

                callback_data=f"𝐭𝐬𝐠 {ID6}|{duration6}|{user_id}",

            ),

            InlineKeyboardButton(

                text="7️⃣",

                callback_data=f"𝐓𝐬𝐠 {ID7}|{duration7}|{user_id}",

            ),

            InlineKeyboardButton(

                text="8️⃣",

                callback_data=f"𝐓𝐬𝐠 {ID8}|{duration8}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="9️⃣",

                callback_data=f"𝐓𝐬𝐠 {ID9}|{duration9}|{user_id}",

            ),

            InlineKeyboardButton(

                text="𝟷𝟶🔟",

                callback_data=f"𝐭𝐬𝐠 {ID10}|{duration10}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="<", callback_data=f"popat 2|{query}|{user_id}"

            ),

            InlineKeyboardButton(

                text="🗑 𝑪𝒍𝒐𝒔𝒆", callback_data=f"forceclose {query}|{user_id}"

            ),

            InlineKeyboardButton(

                text=">", callback_data=f"popat 2|{query}|{user_id}"

            ),

        ],

    ]

    return buttons

def secondary_markup(videoid, user_id):

    buttons = [

        [

            InlineKeyboardButton(text="💝 𝐍𝐞𝐭𝐰𝐨𝐫𝐤 💞", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [

            InlineKeyboardButton(

                text="🔗 𝐌𝐨𝐫𝐞 𝐌𝐞𝐧𝐮", callback_data=f"other {videoid}|{user_id}"

            ),

            InlineKeyboardButton(text="❤️ 𝐎𝐰𝐧𝐞𝐫 ❤️", url=f"https://t.me/itzamanrajput"),

        ],

    ]

    return buttons

def secondary_markup2(videoid, user_id):

    buttons = [

        [

            InlineKeyboardButton(text="❤️ 𝐓𝐒𝐆 𝐂𝐇𝐀𝐓 💞⁩", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [

            InlineKeyboardButton(text="❤️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ❤️", url=f"https://t.me/itsamanrajput"),

        ],

    ]

    return buttons

def primary_markup(videoid, user_id, current_time, total_time):

    if videoid not in db_mem:

        db_mem[videoid] = {}

    db_mem[videoid]["check"] = 2

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="💥 𝑻𝒔𝒈 𝒄𝒉𝒂𝒕 💞", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [

            InlineKeyboardButton(

                text="🔗 𝒎𝒐𝒓𝒆 𝑴𝒆𝒏𝒖", callback_data=f"other {videoid}|{user_id}"

            ),

            InlineKeyboardButton(text="❤️ 𝑶𝒘𝒏𝒆𝒓 ❤️", url=f"https://t.me/itzamanrajput"),

        ],

    ]

    return buttons

def timer_markup(videoid, user_id, current_time, total_time):

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="💥 𝑻𝑺𝑮 𝑪𝑯𝑨𝑻 💞", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [

            InlineKeyboardButton(

                text="🔗 𝑴𝑶𝑹𝑬 𝑴𝑬𝑵𝑼 ", callback_data=f"other {videoid}|{user_id}"

            ),

            InlineKeyboardButton(text="❤️ 𝑶𝒘𝒏𝒆𝒓 ❤️", url=f"https://t.me/itzamanrajput"),

        ],

    ]

    return buttons

def audio_markup(videoid, user_id, current_time, total_time):

    if videoid not in db_mem:

        db_mem[videoid] = {}

    db_mem[videoid]["check"] = 2

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="❤️ 𝐍𝐄𝐓𝐖𝐎𝐑𝐊 💞", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [InlineKeyboardButton(text="❤️ 𝐎𝐰𝐧𝐞𝐫 ❤️", url=f"https://t.me/itzamanarjput")],

    ]

    return buttons

def audio_timer_markup_start(videoid, user_id, current_time, total_time):

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="❤️ 𝑻𝒔𝒈 𝑪𝒉𝒂𝒕 💞⁩", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [InlineKeyboardButton(text="❤️ ᴏᴡɴᴇʀ ❤️", url=f"https://t.me/itzamanrajput")],

    ]

    return buttons

audio_markup2 = InlineKeyboardMarkup(

    [

        [

            InlineKeyboardButton(text="❤️ 𝑇𝑠𝑔 𝐶ℎ𝑎𝑡 💞", url=f"https://t.me/Friends_Chatting_Group3"),

        ],

        [InlineKeyboardButton(text="❤️ Owner ❤️", url=f"https://t.me/itzamanrajput")],

    ]

)
