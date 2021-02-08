def check_afk(update, context, user_id, fst_name, userc_id):
    if is_user_afk(user_id):
        reason = afk_reason(user_id)
        since_afk = get_readable_time((time.time() - float(REDIS.get(f'afk_time_{user_id}'))))
        if reason == "none":
            if int(userc_id) == int(user_id):
                return
            res = "<b>{}</b> is currently AFK!\nLast Seen: <code>{}</code>".format(fst_name, since_afk)
            update.effective_message.reply_text(res, parse_mode="html")
        else:
            if int(userc_id) == int(user_id):
                return
            res = "<b>{}</b> is currently Away!\n<b>Reason</b>:{}\nLast Seen : <code>{}</code>".format(fst_name, reason, since_afk)
            update.effective_message.reply_text(res, parse_mode="html")



def gdpr(user_id):
    end_afk(user_id)



mod_name = "AFK"


help = """
  ✪ /afk <reason>*:* Mark yourself as AFK.
  ✪ brb <reason>*:* Same as the afk command, but not a command.\n
  When marked as AFK, any mentions will be replied to with a message stating that you're not available!
"""


AFK_HANDLER = DisableAbleCommandHandler("afk", afk)
AFK_REGEX_HANDLER = MessageHandler(Filters.regex("(?i)brb"), afk)
NO_AFK_HANDLER = MessageHandler(Filters.all & Filters.group, no_longer_afk)
AFK_REPLY_HANDLER = MessageHandler(Filters.all & Filters.group, reply_afk)

dispatcher.add_handler(AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REGEX_HANDLER, AFK_GROUP)
dispatcher.add_handler(NO_AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REPLY_HANDLER, AFK_REPLY_GROUP)
