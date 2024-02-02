from telebot import TeleBot
from logic import TaskManager

bot = TeleBot('6776537855:AAG27b7SetOePXx9c4KjDfZPfDe8_7ZUVEE')

DATABASE = 'task_history.db'

task_manager = TaskManager(DATABASE)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот-менеджер задач 
Помогу тебе сохранить твои задачи!) 

/add_task - используй для добавления новой задачи
/delete_task - используй для удаления задачи                                      
                     """)
    
@bot.message_handler(commands=['add_task'])
def addtask_command(message):
    bot.send_message(message.chat.id, "Введите название задачи:")
    bot.register_next_step_handler(message, save_task)

def save_task(message):
    name = message.text
    user_id = message.chat.id  
    task_manager.add_task(user_id, name, '')
    bot.send_message(message.chat.id, "Задача добавлена")

@bot.message_handler(commands=['delete_task'])
def deletetask_command(message):
    bot.send_message(message.chat.id, "Введите имя задачи, которую хотите удалить:")
    bot.register_next_step_handler(message, delete_task_by_id)

def delete_task_by_id(message):
    task_name = message.text
    task_manager.delete_task(task_name)
    bot.send_message(message.chat.id, "Задача удалена")
    

bot.infinity_polling()
