from game import Game

contador = open('games.log', 'r') #Abrindo o arquivo games.log
partidas = []
partida = None
total_kills = 0
while True:
    line = contador.readline() #lendo uma linha do arquivo.log
    if line == "": # se fim do arquivo, sair
        break
    #print(line+"\n")

    if line.find("InitGame") != -1: #se encontrar InitGame, cria uma partida
        partida = Game()
        continue

    if line.find("ClientUserinfoChanged") != -1: # Se encontrar informação de usuário, adicionar usuário a lista de jogadores
        partida.players[line.split("\\",2)[1]] = 1
        continue

    if line.find("Kill:") != -1: # Filtrando as mortes nesta linha
        total_kills += 1
        # partida.players.append(line.split("\\",2)[1])
        continue

    if line.find("ShutdownGame") != -1: # Se encontrar ShutdownGame adicionar partida na lista
        partida.total_kills = total_kills
        partidas.append(partida)
        partida = None
        total_kills = 0
        continue

print(partidas)
contador.close()

for partida in partidas:
    print(partida.kills)
    print(partida.total_kills)
    print(partida.players)
