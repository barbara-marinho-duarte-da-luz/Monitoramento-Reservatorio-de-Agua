import colorama
from colorama import Fore, Style

#Inicializa o colorama para garantir compatibilidade no terminal
colorama.init(autoreset=True)

print("Monitoramento Reservatório de Água!\n")

#Lista armazenando os níveis do reservatório
nivel_agua = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5"]


#Função responsável por definir a cor e a mensagem conforme o nível informado
def verifica_nivel (volume):
    if volume == "Nivel 1":
        print(Fore.RED + "Muito baixo (crítico)!")
    elif volume == "Nivel 2":
        print(Fore.YELLOW + "Baixo")
    elif volume == "Nivel 3":
        print(Fore.GREEN + "Médio")
    elif volume == "Nivel 4":
        print(Fore.CYAN + "Alto")
    elif volume == "Nivel 5":
        print(Fore.BLUE + "Muito alto (alerta)!")

#Simulação do monitoramento exibindo todos os níveis cadastrados na lista
for atual in nivel_agua:
    verifica_nivel (atual)

print(Style.RESET_ALL) 
