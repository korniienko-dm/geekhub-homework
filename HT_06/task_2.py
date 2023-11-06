"""
Task_2:
Написати функцію <bank> , яка працює за наступною логікою: користувач робить
вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків
(кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до
суми вкладу і в наступному році на них також нараховуються відсотки).

Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%).
Функція повинна принтануть суму, яка буде на рахунку, а також її повернути
(але округлену до копійок).
"""


def procent_calculate(percents: int or float, money_amount: int or float) -> float:
    """
    Calculate the increased amount of money after applying a percentage increase.

    Parameters:
        percents (int or float): The percentage increase to apply.
        money_amount (int or float): The initial amount of money.

    Returns:
    float: The final amount of money after applying the percentage increase.
    """
    coefficient = 1 + (percents / 100)
    increased_money_amount = (money_amount * coefficient) - money_amount
    return float(increased_money_amount)


def bank(years: int, a: int or float, percents=10):
    """
    Calculate the amount of money in a bank account after a specified number of years.

    Parameters:
        years (int): The number of years to calculate.
        a (int or float): The initial amount of money in the bank account.
        percents (int, optional): The annual percentage increase (default is 10%).

    Returns:
    float: The amount of money in the bank account after the specified number of years.
    """
    argument_tuple = (years, a, percents)
    for i in argument_tuple:
        if not isinstance(i, int):
            return "Error! All parameters must be positive int."

    if years < 0 or a < 0 or percents < 0:
        return "Error! All parameters must be non-negative."

    amount = a
    for i in range(years):
        amount += procent_calculate(percents, amount)

    # Show results
    amount_int = int(amount)
    round_amount = round(amount, 2)
    print(f"Sum for your wallet: {amount_int}")
    return round_amount


print(bank(4, 1500))
