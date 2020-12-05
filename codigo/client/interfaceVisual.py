# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from client.interfaceUsuario import InterfaceUsuario

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

import threading


class InterfaceVisual(InterfaceUsuario):

    def __init__(self):
        self.__entrarOnline = False
        self.__criarServer = False
        self.__sem_esperarPartida = threading.Semaphore(0)
        
        self.root = tk.Tk()
        self.root.title("Cartinha de Amor")
        self.root.geometry("800x500")
        
        self.telaInicial()


    def telaInicial(self):
        def entrarOnlineCallBack():
            self.__entrarOnline = not self.__entrarOnline
            btn_entrarOnline.config(bg= "yellow" if self.__entrarOnline else "white")
        btn_entrarOnline = Button(self.root, text = "Entrar Online", command = entrarOnlineCallBack)
        #btn_entrarOnline.place(x = 50,y = 50)
            
        def criarServerCallBack():
            self.__criarServer = not self.__criarServer
            btn_criarServer.config(bg= "yellow" if self.__criarServer else "white")

        btn_criarServer = Button(self.root, text = "Criar Server", command = criarServerCallBack)
        btn_criarServer.place(x = 50,y = 100)
        
        def esperarPartidaCallBack():
            self.root.quit()
            self.__sem_esperarPartida.release()
        btn_esperarPartida = Button(self.root, text = "Entrar Partida", command = esperarPartidaCallBack)
        btn_esperarPartida.place(x = 50,y = 150)
        
        # nome jogador
        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.nome_contents = StringVar()
        self.nome_contents.set("Insira o nome")
        self.entrythingy["textvariable"] = self.nome_contents

        self.root.mainloop()



    def entrarOnline(self) -> bool:
        print('deseja jogar online? (sim/nao)')
        r = input()
        return ("S" in r or "s" in r)

    def numeroJogadores(self) -> int:
        numero = simpledialog.askinteger("2", "Entre o número de jogadores:", parent=self.root, minvalue=2, maxvalue=4)
        return numero

    def nomeJogador(self) -> str:
        nome = self.nome_contents.get()
        if len(nome) > 10:
            nome = nome[:10]
        if nome == "Insira o nome" or len(nome) < 1:
            nome = jogador+'_'
        return nome

    def esperarPartida(self) -> bool:
        # self.__sem_esperarPartida.acquire()
        wait_variable()
        return [self.__entrarOnline, self.__criarServer]
        
    def criarServer(self) -> bool:
        print('deseja se criar o server? (sim/nao)')
        r = input()
        return ("S" in r or "s" in r)

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