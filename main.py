from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels
import time


Bot = Client(
    "Cartoon_India_TP_ripperbot",
    bot_token = "",
    api_id = ,
    api_hash = ""
)



@Bot.on_message(filters.private & filters.command(["multirec"]))
def multirec_handler(Bot, message):

    auth_user = check_user(message)
    if auth_user is None:
        return

    if len(message.text.split()) < 3:
        message.reply_text("<b>Syntax: </b>`/multirec [channelName] [duration] | [filename]`")
        return

    multi_rec(Bot, message)

@Bot.on_message(filters.private & filters.command(["channels"]))
def show_channels_handler(Bot, message):

    auth_user = check_user(message)
    if auth_user is None:
        return


    getChannels(Bot, message)


@Bot.on_message(filters.private & filters.command(["start"]))
def start_handler(Bot, message):

    if len(message.text.split()) < 3:
        message.reply_text("<b>A Mega Recording Telegram bot by  KIDS MOVIES AND EPISODES</b>\n\n<b>Made with Love by @kids_movies_and_Episodes_founder</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...




    





Bot.run()
