import converter

optimistic_rate = 22
catastrophic_rate = 28

available_currencies = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']

print("\n\tDUTIES AND TAXES CALCULATOR\n")

if (input("Do you need me to convert currencies?: ")).lower() in ["yes", "y", "yup"]:
    converting_from = ""
    while converting_from.upper() not in available_currencies:
        converting_from = input("\nPlease input the currency I'll be converting from in a three letter format (EUR, default: USD, JPY etc.): ")
        converting_from = converting_from.upper()
        if len(converting_from) == 0:
            converting_from="USD"

    to_currency = ""
    while to_currency.upper() not in available_currencies:
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

print("\nHere are the results:\n\nConverted Price: " + str(converted_amount) + " " + to_currency + "\nOptimistic final price estimate (22% Taxes&Duties): " + str(optimistic_amount) + " " + to_currency +  "\nCatastrophic final price estimate (28% Taxes&Duties): " + str(catastrophic_amount) + " " + to_currency + "\n\n")