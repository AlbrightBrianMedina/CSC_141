#
#
#


sandwhich_orders = ['meatball', 'salami', 'tuna']
finished_sandwhiches = []

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print(f'Finishing sandwhich: {current_sandwhich.title()}')
    finished_sandwhiches.append(current_sandwhich)

    print('\nThese orders are ready for pickup:')
    for finished_sandwhich in finished_sandwhiches:
        print(finished_sandwhich.title())