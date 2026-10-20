# Brian Medina
#
# Order Up: Sandwhiches (no pastrami)

sandwhich_orders = ['pastrami', 'meatball', 'pastrami', 'salami', 'pastrami', 'tuna']
finished_sandwhiches = []
print("Sorry, but we have run out of pastrami")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print(f'Finishing sandwhich: {current_sandwhich.title()}')
    finished_sandwhiches.append(current_sandwhich)

    print('\nThese orders are ready for pickup:')
    for finished_sandwhich in finished_sandwhiches:
        print(finished_sandwhich.title())