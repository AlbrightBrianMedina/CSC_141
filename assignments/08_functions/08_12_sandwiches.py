# Brian Medina
#
# making and adding lists of toppings
 
def sandwhiches(*toppings):

    print("\nSandwhiches with toppings")
    for topping in toppings:
        print(f"- {topping}")

sandwhiches('salami')
sandwhiches('cheese', 'lettuce', 'bacon')
sandwhiches('onion slices',"tomato")