import telegram
import telegram.ext
from constants import TOKEN, START, MY_PROJECTS, BACK
from base_module import BaseModule
from project_module import ProjectModule

#/start


def main ():
    project_module = ProjectModule ()
    base_module = BaseModule (project_module)
    bot = telegram.ext.ApplicationBuilder().token(TOKEN).build()

    bot.add_handler (telegram.ext.MessageHandler(telegram.ext.filters.Regex (START), base_module.start))
    bot.add_handler (telegram.ext.MessageHandler(telegram.ext.filters.Regex (MY_PROJECTS), project_module.my_projects))
    bot.add_handler (telegram.ext.MessageHandler(telegram.ext.filters.Regex (BACK), base_module.back))

    bot.run_polling ()



main ()