import requests

# Returns the converted amount int the desired currency, or just returns the rate
def currency_converter_api(amount_to_convert=1, convert_from="USD", convert_to="EUR"):

    # Completes the url with whatever currency you need the exchange rates from
    url = "https://api.exchangerate-api.com/v4/latest/" + convert_from

    # stores the api response as a dict
    data = requests.get(url).json()

    # Selects the correct dictionary entry, storing it inside a variable
    rate = data["rates"][convert_to]

    return round((amount_to_convert * rate),2)


def vat_calculator(amount, percentage=100):
    return round((((amount / 100) * percentage)+ amount), 2)