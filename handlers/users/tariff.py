class Tariff:
    def __init__(self, name, monthly_fee, minutes_limit, messages_limit, data_limit, international_roaming):
        self.name = name
        self.monthly_fee = monthly_fee
        self.minutes_limit = minutes_limit
        self.messages_limit = messages_limit
        self.data_limit = data_limit
        self.international_roaming = international_roaming

    def __str__(self):
        return self.name