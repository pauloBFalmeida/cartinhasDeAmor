# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from client.interfaceUsuario import InterfaceUsuario

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *

import threading


from time import sleep

class InterfaceVisual(InterfaceUsuario):

    def __init__(self):
        self.size = (800,500)
        self.centro = (self.size[0]//2, self.size[1]//2)
        self.root = tk.Tk()
        self.root.title("Cartinha de Amor")
        self.root.resizable(False, False)
        self.root.geometry(str(self.size[0])+'x'+str(self.size[1]))

        self.__telaInicial()


    def __telaInicial(self):
        self.__entrarOnline = False
        self.__criarServer = False
        self.__esperarPartida = BooleanVar(False)

        def entrarOnlineToggle():
            self.__entrarOnline = not self.__entrarOnline
        def criarServerToggle():
            self.__criarServer = not self.__criarServer

        # botoes e checks
        check_entrarOnline = Checkbutton(self.root, text = "Entrar Online", command=entrarOnlineToggle)
        check_criarServer = Checkbutton(self.root, text  = "Criar Server", command=criarServerToggle)
        self.btn_esperarPartida = Button(self.root, text = "Entrar Partida", command=lambda: self.__esperarPartida.set(True))
        check_entrarOnline.place(x = self.centro[0], y= 50)
        check_criarServer.place (x = self.centro[0], y= 75)
        self.btn_esperarPartida.place(x = self.centro[0], y= 150)
        # nome jogador
        self.nome_contents = tk.StringVar()
        self.nome_contents.set("Insira o nome")
        entrada_nome = Entry()
        entrada_nome["textvariable"] = self.nome_contents
        entrada_nome.place(x = self.centro[0], y= 10)
        
    def __telaJogo(self):
        self.btn_carta1.place(x = self.centro[0]-50, y= self.centro[1])
        self.btn_carta2.place(x = self.centro[0]+50, y= self.centro[1])
        self.btn_carta1.place(x = self.centro[0]-50, y= self.centro[1])
        self.btn_carta2.place(x = self.centro[0]+50, y= self.centro[1])


    def __reset(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.root.update()

    def numeroJogadores(self) -> int:
        numero = simpledialog.askinteger("numero", "Entre o número de jogadores:",
                                            parent=self.root, minvalue=2, maxvalue=4)
        return numero

    def nomeJogador(self) -> str:
        nome = self.nome_contents.get()
        if nome == "Insira o nome" or len(nome) < 1:
            nome = 'jogador_'
        if len(nome) > 10:
            nome = nome[:10]
        return nome

    def esperarPartida(self) -> list:
        self.btn_esperarPartida.wait_variable(self.__esperarPartida)
        self.__reset()
        return [self.__entrarOnline, self.__criarServer]
        
    def entrarIpHost(self) -> str:
        IP = simpledialog.askstring("IP do Host", "Insira o IP do host")
        return IP

    def addChat(self, texto: str):
        print("chat: "+ texto)

    def iniciarRound(self):
        self.__telaJogo()
        #print("--- INICIANDO ROUND ---")

    def apresentarGanhadorDoJogo(self, jg_nome: str, jg_pontos: int):
        messagebox.showinfo(message=jg_nome+" ganhou o jogo com "+str(jg_pontos)+" pontos")

    def apresentarGanhadorDoRound(self, jg_nome: str, jg_pontos: int):
        if jg_nome:
            messagebox.showinfo(message=jg_nome+" ganhou o round, agora possui "+str(jg_pontos)+" pontos")
        else:
            messagebox.showinfo(message="nao houve ganhadores nesse round")

    def anunciarCompararCartas(self):
        messagebox.showinfo(message='sem cartas no deck, comparando valor na mao dos jogadores restantes')

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
        messagebox.showinfo(message=j_nome+' jogou a carta '+c_nome)

    # seleciona um dos jogadores podendo ser siMesmo
    def selecionaJogador(self, jogadores_texto: list, possiveis: list, textoInicio: str) -> int:
        print("escolha outro jogador para "+textoInicio)
        # 
        if len(possiveis) == 0:
            messagebox.showinfo(message='nenhum jogador possivel de ser escolhido')
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
                messagebox.showinfo(message='escolha nao e valida')
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
        messagebox.showinfo(message='Voce deve jogar a condessa, pois tem um rei ou principe na mão!')

    def anunciarMorto(self, j_nome: str):
        messagebox.showinfo(message=j_nome+' foi morto')

    def resultadoGuarda(self, resultadoAcusacao: bool):
        if resultadoAcusacao:
            messagebox.showinfo(message='acertou a acusacao')
        else:
            messagebox.showinfo(message='errou a acusacao')
        
    def resultadoPadre(self, c_nome: str):
        messagebox.showinfo(message='carta na mao '+c_nome)
        
    def resultadoBarao(self, j_nome: str):
        if j_nome:
            messagebox.showinfo(message=j_nome+' possuia a carta de menor valor')
        else:
            messagebox.showinfo(message='empate')
        
    def resultadoAia(self, j_nome: str):
        messagebox.showinfo(message=j_nome+' esta protegido pelo proximo round')
        
    def resultadoPrincipe(self, j_nome: str):
        messagebox.showinfo(message=j_nome+' pegou uma nova mao')
        
    def resultadoRei(self, j1_nome: str, j2_nome: str):
        messagebox.showinfo(message='trocadas as maos de '+j1_nome+' e '+j2_nome)
        
    def resultadoPrincesa(self, j_nome: str):
        messagebox.showinfo(message=j_nome+" tentou descartar a Princesa")