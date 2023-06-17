from GAME_OF_TEENS.utils.database.connection import session, Database
class Tariff:
    def __init__(self, name, monthly_fee, minutes_limit, messages_limit, data_limit, international_roaming, social_pass,
                 social_platforms):
        self.name = name
        self.monthly_fee = monthly_fee
        self.minutes_limit = minutes_limit
        self.messages_limit = messages_limit
        self.data_limit = data_limit
        self.international_roaming = international_roaming
        self.social_pass = social_pass
        self.social_platforms = social_platforms

    def __str__(self):
        return self.name

    def compare(self, other_tariff):
        print("tarif1=", self.name)
        print("tarif2=", other_tariff.name)


tariff1 = Tariff('Вільний Лайф', 180, 1600, 0, 'Безліміт', False, True, True)
tariff2 = Tariff('Смайрт Лайф', 120, 800, 0, 25, False, True, True)
tariff3 = Tariff('Просто Лайф', 90, 300, 0, 8, False, True, True)
tariff4 = Tariff('Platinum Лайф', 250, 3000, 50, "Безліміт", True, True, True)
tariff5 = Tariff('Шкільний Лайф', 150, 'Безліміт', 0, 7, False, True, True)
# tariff6 = Tariff('Ґаджет')
# tafiff7 = Tariff("Смарт Сім'я")

tariffs = [tariff1, tariff2, tariff3, tariff4, tariff5]


def choose(id):
    user_tariff = []
    users = session.query(Database).filter_by(id=id).all()
    calls = ''
    internet = ''
    sms = ''
    social_pass = ''
    social_platforms = ''
    for user in users:
        calls = user.calls
        internet = user.internet
        sms = user.sms
        social_pass = user.social_pass
        social_platforms = user.social_platform
    for tariff in tariffs:
        if calls > tariff.minutes_limit:
            if internet > tariff.data_limit:
                if sms > tariff.messages_limit:
                    if social_pass == tariff.social_pass:
                        if social_platforms == tariff.social_platforms:
                            user_tariff.append(tariff.name)
    return user_tariff

# choose(716226509)
