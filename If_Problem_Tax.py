try:
    gross_salary = input(f"What is your gross salary? ")
    gross_salary = int(gross_salary)
    if gross_salary < 0:
        print(f"Gross Salary cannot be negative. Please enter a valid value.")
        gross_salary = input(f"What is your gross salary? ")
        gross_salary = int(gross_salary)


    children = input(f"How many children do you have? ")
    children = int(children)
    if children < 0 or children > 20:
        print(f"Please do not lie to the tax calculator. Please enter the true value: ")
        children = input(f"How many children do you have? ")
        children = int(children)

    if gross_salary < 1000:
       tax_rate = 0.1
    elif gross_salary < 2000:
        tax_rate = 0.12
    elif gross_salary < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    if gross_salary < 2000:
        tax_cut = 0.01*children
    else:
        tax_cut = 0.005*children
    final_tax = max(0,tax_rate-tax_cut)
    net_salary = gross_salary*(1-final_tax)
    print(f"Your net salary is {net_salary}")

except ValueError:
    print("Please give valid values for salary and children")




