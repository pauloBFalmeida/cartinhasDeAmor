# coding: utf-8
from codigo.interfaceUsuario import InterfaceUsuario
from codigo.jogador import Jogador
from codigo.carta import Carta

class InterfaceTexto(InterfaceUsuario):
        
    def entrarOnline(self) -> bool:
        print('deseja jogar online? (sim/nao)')
        r = input()
        return ("S" in r or "s" in r)

    def numeroJogadores(self) -> int:
        print('numero de jogadores')
        valido = False
        while not valido:
            numero = int(input())
            if numero < 2 or numero > 4:
                print('este numero de jogadores não é válido, tente de novo')
            else:
                valido = True
        return numero

    def nomeJogador(self, id: int) -> str:
        print('nome do jogador '+str(id))
        nome = input()
        if len(nome) < 1:
            nome = 'jogador_'+str(id)
        return nome

    def iniciarRound(self):
        print("--- INICIANDO ROUND ---")

    def apresentarGanhadorDoJogo(self, j_ganhador: Jogador):
        nome = j_ganhador.getNome()
        pontos = str(j_ganhador.getPontos())
        print(nome+" ganhou o jogo com "+pontos+" pontos")

    def apresentarGanhadorDoRound(self, j_ganhador: Jogador):
        if j_ganhador != None:
            nome = j_ganhador.getNome()
            pontos = str(j_ganhador.getPontos())
            print(nome+" ganhou o round, agora possui "+pontos+" pontos")
        else:
            print("nao houve ganhadores nesse round")

    def compararCartas(self, j_ganhador: Jogador, jogadores: list):
        print('sem cartas no deck, comparando valor na mao dos jogadores restantes')
        for j in [x for x in jogadores if x.get_vivo()]:
            c = j.getCartasMao()[0]
            print( j.getNome()+' tinha carta '+c.get_nome()+' com o valor '+str(c.get_valor()) )
        if j_ganhador != None:
            c = j_ganhador.getCartasMao()[0] 
            print(j_ganhador.getNome()+' teve a maior carta '+c.get_nome()+'  com o valor '+str(c.get_valor()))
        else:
            print('empate no valor das cartas')
            
    def jogarCarta(self, j: Jogador, c: Carta):
        print(j.getNome()+' jogou a carta '+c.get_nome())

    def jogadorEscolherCarta(self, j_origem: Jogador):
        i = -1
        possivel = False
        while not possivel:
            print(j_origem.getNome()+' escolha uma carta')
            for i in range(len(j_origem.getCartasMao())):
                print(str(i)+' '+j_origem.getCartasMao()[i].get_nome())
            i = int(input())
            possivel = (i >= 0 and i < len(j_origem.getCartasMao()))
        return i

    # seleciona um dos jogadores podendo ser siMesmo
    def selecionaJogador(self, j_origem: Jogador, jogadores: list, siMesmo: bool, textoInicio: str) -> Jogador:
        print("escolha outro jogador para "+textoInicio)
        possiveis = []
        for i in range(len(jogadores)):
            j = jogadores[i]
            # vejo se e si mesmo
            if siMesmo or j != j_origem:
                texto = str(i)+' '+j.getNome()
                if not j.get_vivo():
                    texto += " (morto)"
                elif j.getProtecao():
                    texto += " (protegido)"
                else:
                    possiveis.append(i)
                print(texto)
        if len(possiveis) == 0:
            print('nenhum jogador possivel de ser escolhido')
            return None
        # dentro dos possiveis
        aceito = False
        while not aceito:
            alvo_i = int(input())
            if alvo_i in possiveis:
                aceito = True
            else:
                print('escolha nao e valida')
        # retorna o jogador escolhido
        return jogadores[alvo_i]

    def selecionaValorGuarda(self):
        print('escolha o tipo da carta')
        i = 2
        for tipo in ['Padre', 'Barao', 'Aia', 'Principe', 'Rei', 'Condessa', 'Princesa']:
            print(str(i)+' '+tipo)
            i += 1
        aceito = False
        while not aceito:
            card_id = int(input())
            aceito = card_id > 1 and card_id <= 8
            if not aceito:
                print('escolha nao e valida')
        return card_id

    def jogadorEscolherCarta(self, j_origem: Jogador) -> int:
        possivel = False
        qtdCartas = len(j_origem.getCartasMao())
        if qtdCartas < 1:
            return None
        while not possivel:
            print(j_origem.getNome()+' escolha uma carta')
            for i in range(qtdCartas):
                print(str(i)+' '+j_origem.getCartasMao()[i].get_nome())
            i = int(input())
            if i >= 0 and i < qtdCartas:
                return i

    def alertarSobreCondessa(self):
        print('voce deve jogar a condessa, pois tem um rei ou principe na mao')

    def anunciarMorto(self, j_origem: Jogador):
        print(j_origem.getNome()+' foi morto')

    def resultadoGuarda(self, resultadoAcusacao: bool):
        if resultadoAcusacao:
            print('acertou a acusacao')
        else:
            print('errou a acusacao')
        
    def resultadoPadre(self, cartaMao: Carta):
        print('carta na mao '+cartaMao.get_nome())
        
    def resultadoBarao(self, jogadorMorto: Jogador):
        if jogadorMorto == None:
            print('empate')
        else:
            print(jogadorMorto.getNome()+' possuia a carta de menor valor')
        
    def resultadoAia(self, j: Jogador):
        print(j.getNome()+' esta protegido pelo proximo round')
        
    def resultadoPrincipe(self, j: Jogador):
        print(j.getNome()+' pegou uma nova mao')
        
    def resultadoRei(self, j1: Jogador, j2: Jogador):
        print('trocadas as maos de '+j1.getNome()+' e '+j2.getNome())
        
    def resultadoPrincesa(self, j: Jogador):
        print(j.getNome()+" tentou descartar a Princesa")

    def entrarPartida(self) -> bool:
        print('deseja se conectar a uma partida online? (sim/nao)')
        r = input()
        return ("S" in r or "s" in r)

    def entrarIpHost(self) -> str:
        print('entre com ip do host')
        return input()

    def addChat(self, texto: str):
        print("chat: "+ texto)