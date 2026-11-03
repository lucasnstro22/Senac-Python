import platform
import subprocess
import getpass
import os
import socket

sistema=platform.system()
if sistema == "Windows":
	resultado =subprocess.run(
	["ping", "www.google.com"],
	capture_output=True,
	text=True,
	shell=False,
)
else:
	print("Sistema não suportado")
	exit()
print(resultado.stdout)
print(resultado.stderr)

def coletar_informacoes():
    print("=== INSPEÇÃO DE SERVIDOR ===")
    
    # Comandos utilizando a biblioteca platform
    print(f"Sistema operacional: {platform.system()}")
    print(f"Release:            {platform.release()}")
    print(f"Versão:             {platform.version()}")
    print(f"Arquitetura:        {platform.machine()}")
    print(f"Processador:        {platform.processor()}")
    print(f"Python:             {platform.python_version()}")
    
    # Comandos complementares para os outros dados da imagem
    hostname = socket.gethostname()
    print(f"Hostname:           {hostname}")
    
    try:
        ip_local = socket.gethostbyname(hostname)
    except Exception:
        ip_local = "Não foi possível obter o IP"
    print(f"IP:                 {ip_local}")
    
    print(f"Usuário:            {getpass.getuser()}")
    print(f"Diretório atual:    {os.getcwd()}")

if __name__ == "__main__":
    coletar_informacoes()



print("Funções,Dicionarios, return= Java Script Object Notation")

import platform

def coletar_sistema():
    # Criando um dicionário vazio
    dados = {}
    
    # Preenchendo o dicionário com as informações do sistema
    dados["sistema"] = platform.system()
    dados["release"] = platform.release()
    dados["versao"] = platform.version()
    dados["arquitetura"] = platform.machine()
    dados["processador"] = platform.processor()
    dados["python"] = platform.python_version()
    
    # Retornando o dicionário completo para quem chamou a função
    return dados

# Bloco de execução principal
if __name__ == "__main__":
    # Chamamos a função e guardamos o dicionário retornado na variável 'resultado'
    resultado = coletar_sistema()
    
    print("=== DADOS COLETADOS (DICIONÁRIO) ===")
    
    # Exibindo os dados do dicionário de forma organizada
    for chave, valor in resultado.items():
        print(f"{chave.capitalize()}: {valor}")



# exercicio apresentação

print("=" * 60)
print(" CYBERSERVER INSPECTOR")
print("=" * 60)
print(f"Hostname........: {rede['hostname']}")
print(f"IP..............: {rede['ip']}")
print("-" * 60)
print(f"Sistema.........: {sistema['sistema']}")
print(f"Release.........: {sistema['release']}")
print(f"Versão..........: {sistema['versao']}")
print(f"Arquitetura.....: {sistema['arquitetura']}")
print(f"Processador.....: {sistema['processador']}")
print(f"Python..........: {sistema['python']}")
print("-" * 60)
print(f"Usuário.........: {ambiente['usuario']}")
print(f"Diretório.......: {ambiente['diretorio']}")
print("=" * 60)


#Exercicios

# ==========================================
# 1. FUNÇÕES DE COLETA DE DADOS (Dicionários)
# ==========================================

def coletar_sistema():
    dados = {}
    dados["sistema"] = platform.system()
    dados["release"] = platform.release()
    dados["versao"] = platform.version()
    dados["arquitetura"] = platform.machine()
    dados["processador"] = platform.processor()
    dados["python"] = platform.python_version()
    return dados

def coletar_rede():
    dados = {}
    try:
        hostname = socket.gethostname()
        ip_local = socket.gethostbyname(hostname)
    except Exception:
        hostname = "Desconhecido"
        ip_local = "Não foi possível obter o IP"
        
    dados["hostname"] = hostname
    dados["ip"] = ip_local
    return dados

def coletar_ambiente():
    dados = {}
    dados["usuario"] = getpass.getuser()
    dados["diretorio"] = os.getcwd()
    return dados

# ==========================================
# 2. FUNÇÕES DE APRESENTAÇÃO E SALVAMENTO
# ==========================================

# FUNÇÃO 1: Serve APENAS para printar e mostrar na tela do terminal
def mostrar_relatorio(sistema, rede, ambiente):
    print("=" * 60)
    print("CYBERSERVER INSPECTOR")
    print("=" * 60)
    print(f"Hostname...........: {rede['hostname']}")
    print(f"IP.................: {rede['ip']}")
    print("-" * 60)
    print(f"Sistema............: {sistema['sistema']}")
    print(f"Release............: {sistema['release']}")
    print(f"Versão.............: {sistema['versao']}")
    print(f"Arquitetura........: {sistema['arquitetura']}")
    print(f"Processador........: {sistema['processador']}")
    print(f"Python.............: {sistema['python']}")
    print("-" * 60)
    print(f"Usuário............: {ambiente['usuario']}")
    print(f"Diretório..........: {ambiente['diretorio']}")
    print("=" * 60)

# FUNÇÃO 2: Serve APENAS para criar e salvar as informações no arquivo .txt
def salvar_relatorio(sistema, rede, ambiente):
    with open("server_report.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=" * 60 + "\n")
        arquivo.write("CYBERSERVER INSPECTOR\n")
        arquivo.write("=" * 60 + "\n")
        arquivo.write(f"Hostname: {rede['hostname']}\n")
        arquivo.write(f"IP: {rede['ip']}\n")
        arquivo.write(f"Sistema: {sistema['sistema']}\n")
        arquivo.write(f"Release: {sistema['release']}\n")
        arquivo.write(f"Arquitetura: {sistema['arquitetura']}\n")
        arquivo.write(f"Usuário: {ambiente['usuario']}\n")

# ==========================================
# 3. FUNÇÃO PRINCIPAL DE EXECUÇÃO
# ==========================================

def main():
    sistema = coletar_sistema()
    rede = coletar_rede()
    ambiente = coletar_ambiente()
    
    # Agora a main consegue chamar as duas funções sem erro!
    mostrar_relatorio(sistema, rede, ambiente)
    salvar_relatorio(sistema, rede, ambiente)

if __name__ == "__main__":
    main()

