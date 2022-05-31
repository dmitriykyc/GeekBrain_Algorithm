"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
    для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
    и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
import collections

Company = collections.namedtuple('Company', ['name', 'av_profit'])
result_companies = []

quantity_company = int(input('Введите количество компаний: '))
step = 0
all_profit = 0
while step != quantity_company:
    name_company = input('Введите название компании: ')
    av_profit_one_comp = 0
    for i in range(4):
        profit = int(input(f'Введите прибыль за {i + 1} квартал: '))
        av_profit_one_comp += profit

    all_profit += av_profit_one_comp
    result_companies.append(Company(name=name_company, av_profit=av_profit_one_comp / 4))
    step += 1

print(result_companies)
all_profit = (all_profit / quantity_company) / 4

print(f"Средняя прибыль по всем компаниям: {all_profit}")
min_profit = []
max_profit = []
for i in result_companies:
    if i.av_profit < all_profit:
        min_profit.append(i.name)
    else:
        max_profit.append(i.name)

print(f'Компании которые заработали меньше: {", ".join(min_profit)}\n'
      f'Компании которые заработали больше: {", ".join(max_profit)}')
