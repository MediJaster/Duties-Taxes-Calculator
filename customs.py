import converter

optimistic_rate = 22
catastrophic_rate = 28

print("\n\tITALIAN CUSTOMS CALCULATOR\n")

if (input("Do you need me to convert currencies?: ")).lower() in ["yes", "y", "yup"]:
    converting_from = ".."
    while len(converting_from) != 0 and len(converting_from) != 3:
        converting_from = input("\nPlease input the currency I'll be converting from in a three letter format (EUR, default: USD, JPY etc.): ")
        converting_from = converting_from.upper()
        if len(converting_from) == 0:
            converting_from="USD"

    to_currency = ".."
    while len(to_currency) != 0 and len(to_currency) != 3:
        to_currency = input("\nPlease input the currency I'll be converting to in a three letter format (default: EUR, USD, JPY etc.): ")
        if len(to_currency) == 0:
            to_currency="EUR"

    initial_amount = 0

    while initial_amount == 0:
        initial_amount = input("Please write the desired amount to convert: ")
        try:
            initial_amount = int(initial_amount)
        except ValueError:
            initial_amount = 0
            print("Please enter only numbers in this field")

    converted_amount = converter.currency_converter_api(initial_amount, converting_from, to_currency)
    
else:
    converted_amount = input("Please write the desired amount, possibly including shipping, in EUR: ")
    converted_amount = int(converted_amount)


optimistic_amount = converter.vat_calculator(int(converted_amount), optimistic_rate)
catastrophic_amount = converter.vat_calculator(int(converted_amount), catastrophic_rate)

print("\nHere are the results:\n\nConverted Price: " + str(converted_amount) + to_currency + "\nOptimistic final price estimate (22% Taxes&Duties): " + str(optimistic_amount) + to_currency +  "\nCatastrophic final price estimate (28% Taxes&Duties): " + str(catastrophic_amount) + to_currency + "\n\n")