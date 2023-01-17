""" A program to search for phone numbers and email addresses in the clipboard."""

import re
import pyperclip

# Regular expression for phone number
phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?               # Код региона
                        (\s|--|\.)?                      # Разделитель
                        (\d{3})                          # Первые три цифры
                        (\s|--|\.)                       # Разделитель
                        (\d{4})                          # Последние 4 цифры
                        (\s*(ext|x|ext.)\s*(\d{2, 5}))?  # Добавочный номер
                        )''', re.VERBOSE)

# Regular expression for email search.
email_regex = re.compile(r'''
                        #some.+thing@(\d{2,5}))?.com
                        [a-zA-Z0-9_.+]+ # Имя пользователя
                        @               # Символ @
                        [a-zA-Z0-9_.+]+ # Домен
                        ''', re.VERBOSE)


# Assigning the text variable text from the clipboard
text = str(pyperclip.paste())

# search for matches in the text from the clipboard and add in list matches.
matches = list()
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups)

# Examination. If numbers and emails were found, display them on the screen. If not, display a message about it.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса эл.почты не обнаружены.')

input('Press ENTER to exit')
