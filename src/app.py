# -*- coding:utf-8 -*-
import json
import sys
from list_cmd import COMMAND

NOTES = 'notes.json'
NEXT_ID = 1
DATA = {}


def read(mode=0):
    global NEXT_ID
    try:
        with open(NOTES, 'r', encoding='utf-8') as f:
            DATA = json.load(f)
    except FileNotFoundError:
        with open(NOTES, 'w', encoding='utf-8') as f:
            json.dump({}, f)


    for i in DATA:
        if mode == 1:
            print('%s: %s' % (i, DATA[i]))

    NEXT_ID = len(DATA) + 1


def write(index=None):
    global NEXT_ID
    if DATA == {}:
        read()
    text = input('Введите текст заметки\n')
    if index is not None:
        DATA.update({str(index): text})
    else:
        DATA.update({str(NEXT_ID): text})
        NEXT_ID += 1

    with open(NOTES, 'w', encoding='utf-8') as f:
        json.dump(DATA, f)


def clear():
    global NEXT_ID, DATA
    try:
        with open(NOTES, 'w', encoding='utf-8') as f:
            json.dump({}, f)
            print("Все заметки удалены")
    except FileNotFoundError as e:
        print('ERROR: %s' % e)

    NEXT_ID = 1
    DATA = {}


def help():
    cmd = ''
    for i in COMMAND:
        print('\t%s - %s' % (i, COMMAND[i]))


def check_cmd(cmd):
    if cmd.strip() == 'e':
        sys.exit()
    elif cmd.strip() == 'ls':
        read(1)
    elif 'w' in cmd.strip():
        arg = cmd.split(' ')
        write(arg[1] if len(arg) > 1 else None)
    elif cmd.strip() == 'c':
        clear()
    else:
        print('Указанная команда не поддерживается')


def start():
    while True:
        cmd = input()
        check_cmd(cmd)


print('Добро пожаловать в программу "Мои заметки"!\n')
help()
start()

