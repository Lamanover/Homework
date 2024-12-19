import re
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    else:
        if recipient.count('.com') or recipient.count('.ru') or recipient.count('.net'):
            if recipient.count('@'):
                if sender.count('.com') or sender.count('.ru') or sender.count('.net'):
                     if sender.count('@'):
                        if sender == 'university.help@gmail.com':
                            print('Письмо успешно отправлено с адреса', sender, 'на адрес ', recipient)
                        else:
                             print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
                     else:
                        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
                else:
                    print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
            else:
                print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
        else:
            print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')