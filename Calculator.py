class Program:
    fuels = {
        #  возможные варианты для параметра fuel
        "none": 1,
        "coal": 1.05,
        "block_of_coal": 1.05,
        "e_bread": 1.05,
        "e_coal": 1.1,
        "e_charcoal": 1.2,
        "solar_panel": 1.25,
        "e_lava_bucket": 1.25,
        "magma_bucket": 1.30,
        "plasma_bucket": 1.35,
        "hamster_wheel": 1.5,
        "foul_flesh": 1.9,
        "catalyst": 3,
        "hyper_catalyst": 4
    }
    upgrades = [
        #  возможные апгрейды в слоты upgrade1 и upgrade2
        "diamond_spreading",
        "minion_expander",
        "flycatcher",
        "enchanted_egg"
    ]

    def __init__(self):
        self.closed = False

    def get_input(self) -> dict:
        values = {
            #  значения для теста
            "time_between_actions": 16,
            "items_per_action": 4.0,
            "unit_price": 480,
            "base_items_in_enchanted": 160,
            "fuel": self.fuels["none"],
            "upgrade1": self.upgrades[0],
            "upgrade2": None,
            "diamond_cost": 8.4,  # это дефолтное значение, не обязательно вводить каждый раз новое
            "egg_cost": 7.5,  # и это тоже
            "bonus_speed_multiplier": 1,
            "amount_of_minions": 16,
        }

        #  здесь твой код, возьми то что ввели в программу и
        #  задай значения по типу values["unit_price"] = 2.0
        #  или values["fuel"] = fuels["catalyst"]
        #
        #  это моя версия ввода через консоль
        for key in values:
            inp = input(key + ": ")
            try:
                values[key] = int(inp)
            except ValueError:
                values[key] = inp
        #
        #  program.closed = True если пользователь закрыл программу
        return values

    def show_output(self, profit_estimations: list) -> None:
        #  пример profit_estimations: [49832, 1285129, 8456712]
        #  (это доход за час, за сутки и за неделю)
        print(profit_estimations)
        #  сделай так, чтобы он показался на экране и сделай
        #  задержку чтобы новые данные вводились только после
        #  нажатия какой-нибудь кнопки
        pass


def calculate(values: dict) -> list:
    # coins per action
    cpa = values["items_per_action"] * values["unit_price"] / values["base_items_in_enchanted"]
    if "diamond_spreading" in values.values():
        cpa += 0.1 * values["diamond_cost"]
    if "enchanted_egg" in values.values():
        cpa += values["egg_cost"]
    if "minion_expander" in values.values():
        cpa *= 1.05
    if list(values.values()).count("flycatcher") == 1:
        cpa *= 1.2
    if list(values.values()).count("flycatcher") == 2:
        cpa *= 1.4

    multiplier = cpa * values["bonus_speed_multiplier"] * values["fuel"] * values["amount_of_minions"]
    divider = values["time_between_actions"] * 2

    cps = multiplier / divider  # coins per second

    profit_estimations = list(map(round, [3600 * cps, 86400 * cps, 604800 * cps]))
    return profit_estimations


def main():
    program = Program()
    while True:
        values = program.get_input()
        if not program.closed:
            profit_estimations = calculate(values)
            program.show_output(profit_estimations)

            print("\n")  # убрать в релизе
        else:
            break


if __name__ == "__main__":
    main()
