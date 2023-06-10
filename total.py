total_number_of_orders = int(input())
the_number_of_orders = int(input())

calculation = total_number_of_orders // the_number_of_orders
resolt = total_number_of_orders % the_number_of_orders

print(f"Количество полных недель: {calculation} Оставшиеся заказы: {resolt}")
