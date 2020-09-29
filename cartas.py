import jogador

class Carta():

    def __init__(self, valor, nome, im_verso, im_frente):
        self.__valor = valor
        # desnecessario ;-;
        self.__nome = nome
        self.__im_verso = im_verso
        self.__im_frente = im_frente
        self.__jogador = None

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def set_jogador(self, jogador):
        self.__jogador = jogador

    def get_jogador(self):
        return self.__jogador

    def executar_acao(self): pass

    def getJogadorAlvo(self, siMesmo):
        jogadores = self.get_jogador().get_mesa().getJogadores()
        possiveis = []
        for i in range(len(jogadores)):
            j = jogadores[i]
            # vejo se e si mesmo
            if j != self.get_jogador() or siMesmo:
                texto = str(i)+' '+j.getNome()
                if not j.get_vivo():
                    texto += " (morto)"
                elif j.getProtecao():
                    texto += " (protegido)"
                else:
                    possiveis.append(i)
                print(texto)
        if len(possiveis) == 0:
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

class Guarda(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(1, 'Guarda', im_verso, im_frente)

    def acuse(self, j_alvo, card_valor):
        if j_alvo.getCartasMao()[0].get_valor() == card_valor:
            return True
        return False

    def executar_acao(self):
        print("escolha outro jogador para acusar")
        alvo = self.getJogadorAlvo(False)
        if alvo == None: return None
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
        # acusar
        if self.acuse(alvo, card_id):
            print('escolha correta')
            alvo.morre()
        else:
            print('escolha errada')


class Padre(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(2, 'Padre', im_verso, im_frente)

    def see_hand(self, jogador):
        return jogador.getCartasMao()[0]

    def executar_acao(self):
        print("escolha outro jogador para ver a mao")
        alvo = self.getJogadorAlvo(False)
        if alvo == None: return None
        alvo_mao = self.see_hand(alvo)
        print(alvo_mao.get_nome())


class Barao(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(3, 'Barão', im_verso, im_frente)

    def compare_hands(self, j_origem, j_alvo):
        valor_origem = j_origem.getCartasMao()[0].get_valor()
        valor_alvo = j_alvo.getCartasMao()[0].get_valor()
        if valor_origem < valor_alvo:
            return j_origem
        elif valor_origem > valor_alvo:
            return j_alvo
        else:
            return None

    def executar_acao(self):
        print("escolha outro jogador para comparar maos")
        alvo = self.getJogadorAlvo(False)
        if alvo == None: return None
        origem = self.get_jogador()
        morto = self.compare_hands(origem, alvo)
        if morto != None:
            morto.morre()
        else:
            print('empate')

class Aia(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(4, 'Aia', im_verso, im_frente)

    def protect(self, jogador):
        jogador.darProtecao()

    def executar_acao(self):
        self.protect(self.get_jogador())
        print(self.get_jogador().getNome()+" esta protegido")

class Principe(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(5, 'Príncipe', im_verso, im_frente)

    def change_card(self, j_alvo):
        j_alvo.discard()
        j_alvo.get_mesa().pegarCarta(j_alvo)

    def executar_acao(self):
        print("escolha jogador para pegar nova mao")
        alvo = self.getJogadorAlvo(True)
        if alvo == None: return None
        self.change_card(alvo)
        print(alvo.getNome()+" pegou outra mao")

class Rei(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(6, 'Rei', im_verso, im_frente)

    def trade_cards(self, j_origem, j_alvo):
        temp = j_origem.getCartasMao()
        j_origem.setCartasMao(j_alvo.getCartasMao())
        j_alvo.setCartasMao(temp)

    def executar_acao(self):
        print("escolha outro jogador para trocarem maos")
        alvo = self.getJogadorAlvo(False)
        if alvo == None: return None
        origem = self.get_jogador()
        self.trade_cards(origem, alvo)
        print('trocadas as maos de '+origem.getNome()+' e '+alvo.getNome())

class Condessa(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(8, 'Condessa', im_verso, im_frente)

class Princesa(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(9, 'Princesa', im_verso, im_frente)

    def executar_acao(self):
        self.get_jogador().morre()
