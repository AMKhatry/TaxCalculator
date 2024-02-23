# Income Tax Calculator

This simple Python script calculates weekly income after tax based on user input of pay frequency and income.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/income-tax-calculator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd income-tax-calculator
    ```

3. Run the script:
    ```bash
    python income_tax_calculator.py
    ```

4. Follow the prompts to input pay frequency and income.

## How It Works

1. The script prompts the user to select a pay frequency: Weekly, Fortnightly, Monthly, or Yearly.
2. Based on the selected pay frequency, the user is prompted to input their income.
3. The income is consolidated to a yearly amount.
4. The script calculates the tax based on the yearly income using Australian tax brackets.
5. The weekly income after tax is calculated.
6. The script prints the weekly income after tax rounded to two decimal places.

## Dependencies

- [inquirer](https://github.com/magmax/python-inquirer) - A Python package used for interactive command line user interfaces.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
