import requests


def convert(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_currency]
    converted_amount = amount * rate
    return converted_amount


def check_float(msg):
    while True:
        try:
            value = float(input(msg).replace(',', '.'))
        except ValueError:
            print('O valor fornecido não é um numero.')
            continue
        return value


def main():
    try:
        msg = "Digite o valor a ser convertido: "
        amount = check_float(msg)
        from_currency = input("Digite a moeda de origem: ")
        to_currency = input("Digite a moeda de destino: ")
        converted_amount = convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
