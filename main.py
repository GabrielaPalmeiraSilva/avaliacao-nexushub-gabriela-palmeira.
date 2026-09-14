startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}
solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]
print("CADASTRO DE STARTUP")
print(f"Startup: {startup['nome']}")
print(f"Segmento: {startup['segmento']}")
print(f"Primeiro produto: {solucoes_ativas[0]}")
print("-" * 30 + "\n")

bancadas = [
    [1,0],
    [0,1]
]
print("Mapeamento das Bancadas")
print("Legenda: 1 = Ocupado e 0 = Livre\n")
print(f"Bancada N1 [0][0]: {bancadas[0][0]}")
print(f"Bancada N2 [0][1]: {bancadas[0][1]}")
print(f"Bancada S1 [1][0]: {bancadas[1][0]}")
print(f"Bancada S2 [1][1]: {bancadas[1][1]}")
print("-" * 30)

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_1 = arquivo.readline()
    linha_2 = arquivo.readline()
    linha_3 = arquivo.readline()
    linha_4 = arquivo.readline()

print(cabecalho, end="")
print(linha_1, end="")
print(linha_2, end="")
print(linha_3, end="")
print(linha_4, end="")

custos = [
    float(linha_1.split(",")[1].strip()),
    float(linha_2.split(",")[1].strip()),
    float(linha_3.split(",")[1].strip()),
    float(linha_4.split(",")[1].strip())
]
total_custos = sum(custos)

print("\nPAINEL FINAL")
print(f"Startup: {startup['nome']}")
print("Bancada alocada: Bancada N1")
print(f"Total da infraestrutura em nuvem: R$ {total_custos:.2f}")