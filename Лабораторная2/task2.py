salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital : float = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for _ in range(10):
    money_capital = money_capital + salary - spend
    spend *= (increase + 1)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", format(abs(money_capital),'.2f') )
