from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import BadRequest
# ====================================================================
app = Client("MrTak",config_file="config.ini")
# ====================================================================
@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""😃Hello <b>{message.from_user.mention}</b>, dear
To use the robot, first enter the robot idea and write your text in front of the idea and select one of the options :)
Example:
<code>@MrTextBot Hello</code>""",parse_mode="html")
# ====================================================================
THUMB1 = "https://i.imgur.com/6WBimhB.png"
THUMB2 = "https://i.imgur.com/HVKyqUQ.png"
THUMB3 = "https://i.imgur.com/XsSPeze.png"
THUMB4 = "https://i.imgur.com/boZOPsZ.png"
THUMB5 = "https://i.imgur.com/IN2LeFX.png"
THUMB6 = "https://i.imgur.com/kes6heT.png"
# ====================================================================
@app.on_inline_query()
def answer(client, inline_query):
    try:
        inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title="Bold",
                    input_message_content=InputTextMessageContent(f"**{inline_query.query}**"),
                    description=f"{inline_query.query}",
                    thumb_url= THUMB1,
                ),
                InlineQueryResultArticle(
                    title="Italic",
                    input_message_content=InputTextMessageContent(f"__{inline_query.query}__"),
                    description=f"{inline_query.query}",
                    thumb_url= THUMB2,
                ),
                InlineQueryResultArticle(
                    title="Underline",
                    input_message_content=InputTextMessageContent(f"--{inline_query.query}--"),
                    description=f"{inline_query.query}",
                    thumb_url= THUMB3,
                ),
                InlineQueryResultArticle(
                    title="Strikethrough",
                    input_message_content=InputTextMessageContent(f"~~{inline_query.query}~~"),
                    description=f"{inline_query.query}",
                    thumb_url= THUMB4,
                ),
                InlineQueryResultArticle(
                    title="MonoSpace",
                    input_message_content=InputTextMessageContent(f"`{inline_query.query}`"),
                    description=f"{inline_query.query}",
                    thumb_url= THUMB5,
                ),
                InlineQueryResultArticle(
                    title="Spoiler",
                    input_message_content=InputTextMessageContent(f"||{inline_query.query}||"),
                    description=f"{inline_query.query}",
                    thumb_url= THUMB6,
                ),
            ],
            cache_time=1
        )
    except BadRequest as e:
        pass
# ====================================================================
app.run()