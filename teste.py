from game import Game

contador = open('games.log', 'r')
partidas = []
partida = None
while True:
    line = contador.readline()
    if line == "":
        break
    #print(line+"\n")

    if line.find("InitGame") != -1:
        partida = Game()
        continue

    if line.find("ClientUserinfoChanged") != -1:
        #20:34 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\xian/default\hmodel\xian/default\g_redteam\\g_blueteam\\c1\4\c2\5\hc\100\w\0\l\0\tt\0\tl\0
        partida.players.append(line.split("\\",2)[1])
        continue

    if line.find("ShutdownGame") != -1:
        partidas.append(partida)
        continue

print(partidas)
contador.close()
