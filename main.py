from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels
import time


Bot = Client(
    "Js_tata_rc_bot",
    bot_token = "7089649472:AAGfAAF64ZcfnyrcsTCTJjEjjXvL8mVkt2o",
    api_id = 9315174,
    api_hash = "6bdf32d081bcf4361f0654f092efe7d7"
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
        message.reply_text("<b>A Live Recording Telegram bot by  DORAEMON</b>\n\n<b>Made with Love by Doraemon From 22nd Century</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...




    





Bot.run()
