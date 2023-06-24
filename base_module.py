import telegram
import telegram.ext
from constants import CREATE_TASK, MY_PROJECTS, MY_TASK, OPTIONS, ARCHIVE
from project_module import ProjectModule


class BaseModule:
    def __init__(self, project_module: ProjectModule):
        self.project_module = project_module


    async def start (self, update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
        hello_message = f'Здравствуй, {update.effective_user.first_name}!\nЭто бот для управления задачами.\nВыберите действие ↓'

        reply_markup = self.__build_keyboard_markup ()
        await update.message.reply_text (reply_markup = reply_markup, text = hello_message)
        self.project_module.projects [update.effective_chat.id] = ['Тест', 'Test']

    def __build_keyboard_markup (self):
        return telegram.ReplyKeyboardMarkup ([
            [telegram.KeyboardButton (CREATE_TASK)],
            [
                telegram.InlineKeyboardButton (MY_PROJECTS),
                telegram.InlineKeyboardButton (MY_TASK)
            ],
            [
                telegram.InlineKeyboardButton (OPTIONS),
                telegram.InlineKeyboardButton (ARCHIVE)
            ]
        ])

    async def back (self, update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
        back_message = 'Выберите действие ↓'
        reply_markup = self.__build_keyboard_markup ()
        await update.message.reply_text (reply_markup = reply_markup, text = back_message)