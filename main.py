from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels
import time


Bot = Client(
    "Doraemon4u_bot",
    bot_token = "7050143499:AAHGo49qqqFgsjKnjPOlwRvX8gU3YD-CPRg",
    api_id = 27201791,
    api_hash = "f9fb64257a2125fdc06ba2de02b8a418"
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
