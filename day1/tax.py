name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic monthly salary: "))
special_allowances = float(input("Enter special allowances (monthly): "))
bonus_percentage = float(input("Enter annual bonus percentage: "))
gross_mon_salary=basic_salary+special_allowances
annual_gross_salary=gross_mon_salary*12+bonus_percentage*gross_mon_salary/100
stand_deduction=50000
taxable=annual_gross_salary-stand_deduction
print('Employee details are:')
print('-' * 50)
print(f'%-20s = {name}'%('Name'))
print(f'%-20s = {emp_id}'%('Id'))
print(f'%-20s = {basic_salary}'%('Basic Salary'))
print(f'%-20s = {special_allowances}'%('Allowances'))
print(f'%-20s = {bonus_percentage}'%('Bonus percentage'))
print(f'%-20s = {gross_mon_salary}'%('Monthly Gross Salary'))
print(f'%-20s = {annual_gross_salary}'%('Annual Gross Salary'))
print(f'%-20s = -{stand_deduction}'%('Standard Deduction'))
print(f'%-20s = {taxable}'%('Taxable Income'))