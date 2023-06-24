import telegram
import telegram.ext
from constants import BACK, CREATE_PROJECT

class ProjectModule:
    def __init__(self):
        self.projects = {}


    async def my_projects (self, update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
        projects = self.projects[update.effective_chat.id] 
        reply_message = 'Список проектов:\n\n'
        for key, project in enumerate(projects):
            reply_message += f'{(key + 1)}. {project}\n'

        reply_markup = telegram.ReplyKeyboardMarkup ([
            [
                telegram.InlineKeyboardButton (BACK),
                telegram.InlineKeyboardButton (CREATE_PROJECT)
            ]
        ])

        await update.message.reply_text (text = reply_message, reply_markup = reply_markup)