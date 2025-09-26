from datetime import datetime

def saudacao(nome):
    return f"Olá, {nome}!"

def saudacao_com_horario(nome):
    hora = datetime.now().hour
    if hora < 12:
        periodo = "Bom dia"
    elif hora < 18:
        periodo = "Boa tarde"
    else:
        periodo = "Boa noite"
    return f"{periodo}, {nome}!"

print("Versão 1: Olá mundo")
print("Versão 2: adicionando saudação personalizada")
print("Versão 3:", saudacao("PUCRS"))
print("Versão 4:", saudacao_com_horario("PUCRS"))
