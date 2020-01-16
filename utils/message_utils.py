# coding=utf-8

import pickledb
from utils.constants import *
import datetime

db = pickledb.load('user_data.db', auto_dump=True)


def get_history(user_id):
    return db.get(user_id)


def get_current_node(user_id):
    try:
        return db.lget(user_id, -1)[0]
    except KeyError:
        return None


def save_node(user_id, node, message):
    now = str(datetime.datetime.now())
    if db.exists(user_id):
        db.ladd(user_id, [node, [now, message]])
    else:
        db.set(user_id, [[node, [now, message]]])


def check_message(message):
    if message.lower() in YES:
        return 'yes'
    if message.lower() in NO:
        return 'no'
    return None


def process_message(user_id, message):
    '''
    :param user_id: user_id
    :param message: message
    :return: response + state
    '''
    if message == '/start':
        state = 'start'
        save_node(user_id, state, message)
        return question_tree['start']['message'], 0
    state = get_current_node(user_id)
    print('STATE', state)
    if not state:
        return WELCOME, 0

    question = question_tree.get(state)
    print('q', question)
    response = question.get(check_message(message))

    if not response:
        return WRONG_QUERY, 0
    if response in question_tree:
        question = question_tree.get(response)
        save_node(user_id, response, message)
        return question['message'], 0
    save_node(user_id, None, message)
    return response, 1
