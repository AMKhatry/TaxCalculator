import inquirer

# Define the question for user input
pay_frequency_question = [
    inquirer.List('pay_frequency', 
                  message='Pay Frequency:', 
                  choices=['Weekly', 'Fortnightly', 'Monthly', 'Yearly']
    ),
]

# Prompt the user to select pay frequency
selected_frequency_answer = inquirer.prompt(pay_frequency_question)
selected_frequency = selected_frequency_answer['pay_frequency']

# Prompt the user to input income based on selected frequency
income = int(input(f"Enter your {selected_frequency.lower()} income: "))

# Function to consolidate income based on selected frequency to yearly income
def frequency_consolidation(selected_frequency, income):
    if selected_frequency == 'Weekly':
        yearly_income = income * 52
        return yearly_income
        
    elif selected_frequency == 'Fortnightly':
        yearly_income = income * 26
        return yearly_income

    elif selected_frequency == 'Monthly':
        yearly_income = income * 12
        return yearly_income

    elif selected_frequency == 'Yearly':
        yearly_income = income * 1
        return yearly_income

# Function to calculate tax based on yearly income
def calculate_tax(yearly_income):
    if yearly_income <= 18200:
        tax = 0

    elif 18201 <= yearly_income <= 45000:
        tax = 0.19 * (yearly_income - 18200)

    elif 45001 <= yearly_income <= 120000:
        tax = 5092 + 0.325 * (yearly_income - 45000)

    elif 120001 <= yearly_income <= 180000:
        tax = 29467 + 0.37 * (yearly_income - 120000)

    else:
        tax = 51667 + 0.45 * (yearly_income - 180000)

    return tax

# Function to calculate weekly income after tax
def calculate_weekly_income_after_tax(yearly_income, tax_amount):
    yearly_net_income = yearly_income - tax_amount
    weekly_income_after_tax = yearly_net_income/52
    return weekly_income_after_tax

# Consolidate income to yearly
yearly_income = frequency_consolidation(selected_frequency, income)

# Calculate tax
tax_amount = calculate_tax(yearly_income)

# Calculate weekly income after tax
weekly_income = calculate_weekly_income_after_tax(yearly_income, tax_amount)

# Round weekly income to two decimal places
rounded_weekly_income = round(weekly_income, 2)

# Print the weekly income after tax
print("Weekly Income:", rounded_weekly_income)
