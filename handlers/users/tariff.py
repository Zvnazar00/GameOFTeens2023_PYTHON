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


tarif1 = Tariff('Вільний Лайф', 180, 1600, 0, 'Безліміт', False, True, True)
tarif2 = Tariff('Смайрт Лайф', 120, 800, 0, 25, False, True, True)
tarif3 = Tariff('Просто Лайф', 90, 300, 0, 8, False, True, True)
tarif4 = Tariff('Platinum Лайф', 250, 3000, 50, "Безліміт", True, True, True)
tarif5 = Tariff('Шкільний Лайф', 150, 'Безліміт', 0, 7, False, True, True)
tarif6 = Tariff('Ґаджет')
tafif7 = Tariff("Смарт Сім'я")