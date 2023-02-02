import requests


def convert(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_currency]
    converted_amount = amount * rate
    return converted_amount


def main():
    amount = float(input("Digite o valor a ser convertido: "))
    from_currency = input("Digite a moeda de origem: ")
    to_currency = input("Digite a moeda de destino: ")
    converted_amount = convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")


if __name__ == "__main__":
    main()
