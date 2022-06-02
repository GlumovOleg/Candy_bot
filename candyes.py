import random

confety = 0
    
def start_game(message):
    global confety
    confety = random.randint(20,40)
    bot_start = random.choice([True,False])
    msg = f'Всего конфет разыгрывается: {confety}\n'
    msg += 'За ход можно взять от 1 до 4 конфет\n'
    msg += 'Первый ход '
    if bot_start:
        msg += 'Бота\n'
        bot = random.randint(1,4)
        get_candy = bot
        confety -= get_candy
        msg += f'Бот берёт: {get_candy} конфет\n'
        msg += f'На столе осталось {confety} конфет\n '
        msg += 'За ход можно взять от 1 до 4 конфет\n '
        msg += f'Ходит {message.from_user.first_name}'
    else:
        msg += str(message.from_user.first_name)
    return msg
    
def game(message):
    global confety
    if message.text in '1234' and int(message.text) <= confety:
        get_candy = int(message.text)
        confety -= get_candy
        msg = f'{message.from_user.first_name} взял {get_candy} конфет\n'
        if confety == 0:
            msg += f'{message.from_user.first_name}, Победил!\n'
            return msg
        else:
            bot = random.randint(1,4)
            get_candy = bot
            confety -= get_candy
            msg += f'Бот взял {get_candy} конфет\n'
            if confety == 0:
                msg += 'Бот победил :('
            else:
                msg += f'На столе осталось {confety} конфет\n'
                msg += 'Можно взять '
                if confety >= 4:
                    msg += 'от 1 до 4 конфет\n'
                else:
                    msg += f'от 1 до {confety} конфет\n'
            return msg
    else:
        print('Неверный ввод')