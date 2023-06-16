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

    def compare(self, other_tariff):
        print("Comparing tariffs:")
        print(f"Tariff 1: {self.name}")
        print(f"Tariff 2: {other_tariff.name}")

        if self.monthly_fee < other_tariff.monthly_fee:
            print(f"{self.name} has a lower monthly fee.")
        elif self.monthly_fee > other_tariff.monthly_fee:
            print(f"{other_tariff.name} has a lower monthly fee.")
        else:
            print("Both tariffs have the same monthly fee.")

        if self.minutes_limit < other_tariff.minutes_limit:
            print(f"{self.name} has a lower minutes limit.")
        elif self.minutes_limit > other_tariff.minutes_limit:
            print(f"{other_tariff.name} has a lower minutes limit.")
        else:
            print("Both tariffs have the same minutes limit.")

        # Аналогично сравнивайте остальные характеристики тарифов

        print()  # Пустая строка для разделения вывода


# Создание объектов тарифов
tariff1 = Tariff("Тариф 1", 10, 500, 1000, 5, True)
tariff2 = Tariff("Тариф 2", 15, 800, 1500, 10, False)

# Сравнение тарифов
tariff1.compare(tariff2)
