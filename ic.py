# Dicionário que representa a soma entre dois dígitos (de "0" a "9"), como strings.
# Exemplo: "07" → "7", "19" → "10", "99" → "18"
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


def soma_strings(num1, num2):
    # Índices para começar do último dígito de cada número
    i, j = len(num1) - 1, len(num2) - 1
    # "carry" guarda o vai-um; começa como "0"
    carry = "0"
    # "resultado" acumula o número final, construído da direita para a esquerda
    resultado = ""

    # O loop continua enquanto houver dígitos ou ainda existir carry
    while i >= 0 or j >= 0 or carry != "0":
        # Pega os dígitos atuais; se já acabou a string, usa "0"
        dig1 = num1[i] if i >= 0 else "0"
        dig2 = num2[j] if j >= 0 else "0"

        # Soma os dois dígitos (sem considerar o carry ainda)
        soma_digitos = tabela_soma[dig1 + dig2]

        # Se a soma dos dois dígitos for de 2 caracteres (ex.: "10"), soma o último com o carry
        # Caso contrário, soma o próprio resultado com o carry
        if len(soma_digitos) == 2:
            soma_final = tabela_soma[soma_digitos[-1] + carry]  # Exemplo: "10" + carry="1" → soma "0" + "1"
        else:
            soma_final = tabela_soma[soma_digitos + carry]       # Exemplo: "7" + carry="1" → "71"

        # Define o novo carry:
        # Se alguma das somas produziu 2 dígitos (ex.: "10"), significa que há vai-um.
        if len(soma_digitos) == 2 or len(soma_final) == 2:
            carry = "1"
        else:
            carry = "0"

        # Pega o último dígito do resultado da soma atual e adiciona à esquerda do resultado final
        resultado = soma_final[-1] + resultado

        # Move os ponteiros uma posição para a esquerda
        i -= 1
        j -= 1

    # Remove zeros à esquerda, garantindo que "000" vire "0"
    return resultado.lstrip("0") or "0"


# Exemplos de teste:
print(soma_strings("99", "1"))       # Saída esperada: "100"
print(soma_strings("123", "877"))    # Saída esperada: "1000"
print(soma_strings("5", "5"))        # Saída esperada: "10"
print(soma_strings("0", "0"))        # Saída esperada: "0"
