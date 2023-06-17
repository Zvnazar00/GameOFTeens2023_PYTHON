from GAME_OF_TEENS.utils.database.connection import session, Database


class Tariff:
    def __init__(self, name, monthly_fee, minutes_limit, messages_limit, data_limit, social_pass,
                 social_platforms, photo, url):
        self.name = name
        self.monthly_fee = monthly_fee
        self.minutes_limit = minutes_limit
        self.messages_limit = messages_limit
        self.data_limit = data_limit
        self.social_pass = social_pass
        self.social_platforms = social_platforms
        self.photo = photo
        self.url = url

    def __str__(self):
        return self.name


tariff4 = Tariff('Platinum Лайф', 250, 3000, 50, 10000, True, True,
                 open(r'utils/misc/photos/Platinum.png', 'rb'), 'bit.ly/43M9h3x')
tariff1 = Tariff('Вільний Лайф', 180, 1600, 0, 10000, True, True,
                 open(r'utils/misc/photos/FreeLife.png', 'rb'), 'bit.ly/3qQWOgj')
tariff2 = Tariff('Смарт Лайф', 120, 800, 0, 25, True, True,
                 open(r'utils/misc/photos/SmartLife.png', 'rb'), 'bit.ly/43KLz7I')
tariff3 = Tariff('Просто Лайф', 90, 300, 0, 8, True, True,
                 open(r'utils/misc/photos/SimpleLife.png', 'rb'), 'bit.ly/46779Vw')
tariff5 = Tariff('Шкільний Лайф', 150, 10000, 0, 7, True, True,
                 open(r'utils/misc/photos/Schoollife.jpg', 'rb'), 'bit.ly/3NflOFl')

tariff7 = Tariff("Смарт Сім'я S", 375, 10000, 500, 20, True, True,
                 open(r"utils/misc/photos/SmartFamily1.jpg", 'rb'), 'bit.ly/3CAKLGy')
tariff8 = Tariff("Смарт Сім'я M", 425, 750, 1000, 30, True, True,
                 open(r"utils/misc/photos/SmartFamily2.png", 'rb'), 'bit.ly/443fdF4')
tariff9 = Tariff("Смарт Сім'я L", 500, 1500, 1500, 50, True, True,
                 open(r"utils/misc/photos/SmartFamily3.png", 'rb'), 'bit.ly/3CBJZZK')

tariff10 = Tariff('Ґаджет Безпека', 90, 15, 15, 0.15, False, False,
                  open(r'utils/misc/photos/Gadgets.png', 'rb'), 'https://bit.ly/3p257p7')
tariff11 = Tariff('Ґаджет Смарт', 150, 50, 50, 0.5, True, True,
                  open(r'utils/misc/photos/Gadgets.png', 'rb'), 'https://bit.ly/3NggBgA')
tariff12 = Tariff('Ґаджет Планшет', 275, 0, 0, 50, True, True,
                  open(r'utils/misc/photos/Gadgets.png', 'rb'), 'https://bit.ly/3CxP05x')
tariff13 = Tariff('Ґаджет Роутер', 375, 0, 0, 10000, True, True,
                  open(r'utils/misc/photos/Gadgets.png', 'rb'), 'https://bit.ly/3XahcFf')

self_tariffs = [tariff1, tariff2, tariff3, tariff4, tariff5]
family_tariffs = [tariff7, tariff8, tariff9]
gadgets_tariffs = [tariff10, tariff11, tariff12, tariff13]


def choose(id, func_name):
    user_tariff = []
    users = session.query(Database).filter_by(user_id=id).all()
    calls = ''
    internet = ''
    sms = ''
    social_pass = ''
    social_platforms = ''
    tariffs = ''
    if func_name == 'self':
        tariffs = self_tariffs
    elif func_name == 'family':
        tariffs = family_tariffs
    if func_name == 'gadgets':
        tariffs = gadgets_tariffs
    for user in users:
        calls = user.calls
        internet = user.internet
        sms = user.sms
        social_pass = user.social_pass
        social_platforms = user.social_platform
    for tariff in tariffs:
        if int(calls) <= int(tariff.minutes_limit):
            if int(internet) >= int(tariff.data_limit):
                if int(sms) <= int(tariff.messages_limit):
                    if social_pass == tariff.social_pass:
                        if social_platforms == tariff.social_platforms:
                            user_tariff.append(tariff)
    return user_tariff


def is_valid_tariff(tariff, calls, internet, sms, social_pass, social_platforms):
    return all([
        int(calls) <= int(tariff.minutes_limit),
        int(internet) >= int(tariff.data_limit),
        int(sms) <= int(tariff.messages_limit),
        social_pass == tariff.social_pass,
        social_platforms == tariff.social_platforms
    ])
