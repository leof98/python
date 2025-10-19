# === TABELAS DE SOMA E MULTIPLICAÇÃO ENTRE DÍGITOS ===

tabela_soma = {
    "00": "0", "01": "1", "02": "2", "03": "3", "04": "4", "05": "5", "06": "6", "07": "7", "08": "8", "09": "9",
    "10": "1", "11": "2", "12": "3", "13": "4", "14": "5", "15": "6", "16": "7", "17": "8", "18": "9", "19": "10",
    "20": "2", "21": "3", "22": "4", "23": "5", "24": "6", "25": "7", "26": "8", "27": "9", "28": "10", "29": "11",
    "30": "3", "31": "4", "32": "5", "33": "6", "34": "7", "35": "8", "36": "9", "37": "10", "38": "11", "39": "12",
    "40": "4", "41": "5", "42": "6", "43": "7", "44": "8", "45": "9", "46": "10", "47": "11", "48": "12", "49": "13",
    "50": "5", "51": "6", "52": "7", "53": "8", "54": "9", "55": "10", "56": "11", "57": "12", "58": "13", "59": "14",
    "60": "6", "61": "7", "62": "8", "63": "9", "64": "10", "65": "11", "66": "12", "67": "13", "68": "14", "69": "15",
    "70": "7", "71": "8", "72": "9", "73": "10", "74": "11", "75": "12", "76": "13", "77": "14", "78": "15", "79": "16",
    "80": "8", "81": "9", "82": "10", "83": "11", "84": "12", "85": "13", "86": "14", "87": "15", "88": "16", "89": "17",
    "90": "9", "91": "10", "92": "11", "93": "12", "94": "13", "95": "14", "96": "15", "97": "16", "98": "17", "99": "18",
}

# Tabela de multiplicação de dois dígitos (como strings)
tabela_mult = {
    "00": "0", "01": "1", "02": "2", "03": "3", "04": "4", "05": "5", "06": "6", "07": "7", "08": "8", "09": "9",
    "10": "0", "11": "1", "12": "2", "13": "3", "14": "4", "15": "5", "16": "6", "17": "7", "18": "8", "19": "9",
    "20": "0", "21": "2", "22": "4", "23": "6", "24": "8", "25": "10", "26": "12", "27": "14", "28": "16", "29": "18",
    "30": "0", "31": "3", "32": "6", "33": "9", "34": "12", "35": "15", "36": "18", "37": "21", "38": "24", "39": "27",
    "40": "0", "41": "4", "42": "8", "43": "12", "44": "16", "45": "20", "46": "24", "47": "28", "48": "32", "49": "36",
    "50": "0", "51": "5", "52": "10", "53": "15", "54": "20", "55": "25", "56": "30", "57": "35", "58": "40", "59": "45",
    "60": "0", "61": "6", "62": "12", "63": "18", "64": "24", "65": "30", "66": "36", "67": "42", "68": "48", "69": "54",
    "70": "0", "71": "7", "72": "14", "73": "21", "74": "28", "75": "35", "76": "42", "77": "49", "78": "56", "79": "63",
    "80": "0", "81": "8", "82": "16", "83": "24", "84": "32", "85": "40", "86": "48", "87": "56", "88": "64", "89": "72",
    "90": "0", "91": "9", "92": "18", "93": "27", "94": "36", "95": "45", "96": "54", "97": "63", "98": "72", "99": "81",
}


# === FUNÇÃO DE SOMA DE STRINGS ===
def soma_strings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = "0"
    resultado = ""

    while i >= 0 or j >= 0 or carry != "0":
        dig1 = num1[i] if i >= 0 else "0"
        dig2 = num2[j] if j >= 0 else "0"

        soma_digitos = tabela_soma[dig1 + dig2]

        if len(soma_digitos) == 2:
            soma_final = tabela_soma[soma_digitos[-1] + carry]
        else:
            soma_final = tabela_soma[soma_digitos + carry]

        carry = "1" if len(soma_digitos) == 2 or len(soma_final) == 2 else "0"

        resultado = soma_final[-1] + resultado
        i -= 1
        j -= 1

    return resultado.lstrip("0") or "0"


# === FUNÇÃO DE MULTIPLICAÇÃO DE STRINGS ===
def multiplica_strings(num1, num2):
    # Se algum número for "0", o resultado é "0"
    if num1 == "0" or num2 == "0":
        return "0"

    resultado = "0"
    # contador para adicionar zeros ao final (posição do dígito)
    zeros_sufixo = ""

    # Multiplicação de cada dígito de num2 (de trás pra frente)
    for j in range(len(num2) - 1, -1, -1):
        dig2 = num2[j]
        carry = "0"
        parcial = ""

        # Multiplica cada dígito de num1 (de trás pra frente)
        for i in range(len(num1) - 1, -1, -1):
            dig1 = num1[i]
            produto = tabela_mult[dig1 + dig2]

            if len(produto) == 2:
                # Se o produto tiver dois dígitos (ex.: "12"), soma o carry com o último
                soma_final = tabela_soma[produto[-1] + carry]
                if len(soma_final) == 2:
                    carry = "1"
                else:
                    carry = produto[0]  # o "vai" vira o primeiro dígito do produto
                parcial = soma_final[-1] + parcial
            else:
                soma_final = tabela_soma[produto + carry]
                carry = "1" if len(soma_final) == 2 else "0"
                parcial = soma_final[-1] + parcial

        # se sobrar carry no final da linha de multiplicação
        if carry != "0":
            parcial = carry + parcial

        # adiciona zeros à direita conforme a posição do dígito multiplicador
        parcial += zeros_sufixo
        zeros_sufixo += "0"

        # soma o resultado parcial ao resultado total
        resultado = soma_strings(resultado, parcial)

    return resultado.lstrip("0") or "0"


# === TESTES ===
print(multiplica_strings("2", "3"))       # "6"
print(multiplica_strings("12", "3"))      # "36"
print(multiplica_strings("12", "12"))     # "144"
print(multiplica_strings("99", "99"))     # "9801"
print(multiplica_strings("25", "4"))      # "100"
