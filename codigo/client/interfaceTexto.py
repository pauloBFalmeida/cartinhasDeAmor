# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from client.interfaceUsuario import InterfaceUsuario

class InterfaceTexto(InterfaceUsuario):
        
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

    def nomeJogador(self) -> str:
        print('nome do jogador')
        nome = input()
        if len(nome) < 1:
            nome = 'jogador_'
        return nome

    def esperarPartida(self) -> list:
        print('deseja jogar online? (sim/nao)')
        r = input()
        jogarOnline = ("S" in r or "s" in r)
        #
        print('deseja se criar o server? (sim/nao)')
        r = input()
        criarServer = ("S" in r or "s" in r)
        return [jogarOnline, criarServer]

    def entrarIpHost(self) -> str:
        print('entre com ip do host')
        return input()

    def addChat(self, texto: str):
        print("chat: "+ texto)

    def iniciarRound(self):
        print("--- INICIANDO ROUND ---")

    def apresentarGanhadorDoJogo(self, jg_nome: str, jg_pontos: int):
        print(jg_nome+" ganhou o jogo com "+str(jg_pontos)+" pontos")

    def apresentarGanhadorDoRound(self, jg_nome: str, jg_pontos: int):
        if jg_nome:
            print(jg_nome+" ganhou o round, agora possui "+str(jg_pontos)+" pontos")
        else:
            print("nao houve ganhadores nesse round")

    def anunciarCompararCartas(self):
        print('sem cartas no deck, comparando valor na mao dos jogadores restantes')

    def compararCartas(self, set_m: tuple,  set_j: tuple, ganhador_j: bool):
        n_m, c_n_m, v_m = set_m     # antigo maior
        n_j, c_n_j, v_j = set_j     # novo maior
        #
        print('comparando cartas de '+n_maior+' e '+n_j)
        print(v_j+' tinha carta '+c_n_j+' com o valor '+str(v_j) //
            +'enquanto '+ v_m+' tinha carta '+c_n_m+' com o valor '+str(v_m))
        #
        if ganhador_j:
            print(n_j+' teve a maior carta')
        else:
            print('empate no valor das cartas ambos jogadores morrem')
            
            
    def anunciarCarta(self, j_nome: str, c_nome: str):
        print(j_nome+' jogou a carta '+c_nome)

    # seleciona um dos jogadores podendo ser siMesmo
    def selecionaJogador(self, jogadores_texto: list, possiveis: list, textoInicio: str) -> int:
        print("escolha outro jogador para "+textoInicio)
        # 
        if len(possiveis) == 0:
            print('nenhum jogador possivel de ser escolhido')
            return None
        #
        for t in jogadores_texto:
            print(t)
        # dentro dos possiveis
        alvo_i = None
        aceito = False
        while not aceito:
            alvo_i = int(input())
            if alvo_i in possiveis:
                aceito = True
            else:
                print('escolha nao e valida')
        # retorna o indice do jogador escolhido
        return alvo_i

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
    
    def jogadorEscolherCarta(self, cartasMao_nomes: list) -> int:
        i = -1
        possivel = False
        qtdCartas = len(cartasMao_nomes)
        if qtdCartas < 1:
            return None
        while not possivel:
            print('escolha uma carta')
            for i in range(qtdCartas):
                print(str(i)+' '+cartasMao_nomes[i])
            i = int(input())
            possivel = (i >= 0 and i < qtdCartas)
        return i

    def alertarSobreCondessa(self):
        print('voce deve jogar a condessa, pois tem um rei ou principe na mao')

    def anunciarMorto(self, j_nome: str):
        print(j_nome+' foi morto')

    def resultadoGuarda(self, resultadoAcusacao: bool):
        if resultadoAcusacao:
            print('acertou a acusacao')
        else:
            print('errou a acusacao')
        
    def resultadoPadre(self, c_nome: str):
        print('carta na mao '+c_nome)
        
    def resultadoBarao(self, j_nome: str):
        if j_nome:
            print(j_nome+' possuia a carta de menor valor')
        else:
            print('empate')
        
    def resultadoAia(self, j_nome: str):
        print(j_nome+' esta protegido pelo proximo round')
        
    def resultadoPrincipe(self, j_nome: str):
        print(j_nome+' pegou uma nova mao')
        
    def resultadoRei(self, j1_nome: str, j2_nome: str):
        print('trocadas as maos de '+j1_nome+' e '+j2_nome)
        
    def resultadoPrincesa(self, j_nome: str):
        print(j_nome+" tentou descartar a Princesa")
