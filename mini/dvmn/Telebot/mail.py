import ptbot
import os
from pytimeparse import parse

api_token= os.getenv("TOKEN")
user_id=os.getenv("ID")
bot = ptbot.Bot(api_token)
bot.send_message(user_id, "Бот запущен")


def timeout():
   bot.send_message(user_id, "Время вышло")


def notify_progress(secs_left, message_id, total):
    bot.update_message(user_id, message_id, "Осталось {} секунд\n".format(secs_left) + render_progressbar(total, total-secs_left))
  
  
def render_progressbar(total, iteration, prefix='', suffix='', length=18, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(text):
   timer = parse(text)
   message = "Таймер запущен на {} секунд".format(timer)
   bot.send_message(user_id, message)
   current_id = bot.send_message(user_id, "Осталось {} секунд\n".format(timer) + render_progressbar(timer, 0))
   bot.create_timer(timer, timeout)
   bot.create_countdown(timer, notify_progress, message_id= current_id, total=timer)
  

bot.wait_for_msg(reply)
