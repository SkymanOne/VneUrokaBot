import logging
from telebot import types
from datetime import datetime
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                    filename=u'logs/mylog' + str(datetime.now().time()) + '.log')


def my_log_info(user: types.User, message):
    logging.info('Пользователь -- ' + user.first_name + '(' + str(user.id)
                 + '): ' + message)
