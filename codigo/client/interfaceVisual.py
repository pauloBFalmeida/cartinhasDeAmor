# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from client.interfaceUsuario import InterfaceUsuario

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk

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
        
        # carrega as imagens 
            # cartas
        self.imagens = [PhotoImage(file=r"recursos/cartas/carta"+str(i)+".png") for i in range(9)]
        self.imagens_size = (150, 210)
            # background
        self.background_vit = PhotoImage(file=r"recursos/tigrao.png")
        
        self.placar = StringVar()
        self.__telaInicial()


    def __telaInicial(self):
        self.__entrarOnline = False
        self.__criarServer  = False
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
        self.btn_esperarPartida.place(x = self.centro[0], y= 200)
        # nome jogador
        self.nome_contents = tk.StringVar()
        self.nome_contents.set("Insira o nome")
        entrada_nome = Entry()
        entrada_nome["textvariable"] = self.nome_contents
        entrada_nome.place(x = self.centro[0], y= 10)


    def __telaJogo(self):
        # cartas
        self.carta_escolhida = IntVar(0)
        self.btns_cartas = [
                            Button(self.root, image=self.imagens[0], command=lambda: self.carta_escolhida.set(0)),
                            Button(self.root, image=self.imagens[0], command=lambda: self.carta_escolhida.set(1))
                            ]        
        # texto
        self.texto_esq = StringVar()
        self.texto_esq.set("Novo turno")
        label = Label(self.root, textvariable=self.texto_esq, font=("Courier", 11))
        label.place(x=20, y=self.centro[1])

        # placar
        self.placar.set(self.placar.get())
        label = Label(self.root, textvariable=self.placar)
        label.place(x=self.centro[0], y=10)

        self.root.update()


    def __telaVitoria(self, texto):
        self.__reset()
        
        background_label = Label(self.root, image=self.background_vit)
        background_label.place(x=0, y=0)
        
        textoVar = StringVar()
        textoVar.set(texto)
        label_texto = Label(self.root, textvariable=textoVar, font=("Courier", 13))
        label_texto.place(x=self.size[0]-270, y=130)

        self.root.mainloop()



    def __addTexto(self, texto):
        chars_linha= 50
        linhas_text= 10
        if len(texto) > 0:
            linhas = self.texto_esq.get().split('\n')
            texto_chunks = [texto[i:i+chars_linha] for i in range(0, len(texto), chars_linha)]
            texto_chunks.reverse()
            for t in texto_chunks:
                linhas.insert(0, t)
            linhas = linhas[:linhas_text]
            #
            t = ""
            for l in linhas:
                t += l + '\n'
            self.texto_esq.set(t)
            self.root.update()

    def __dropMenu(self, opcoes):
        # drop menu
        var_opcao = StringVar()
        var_opcao.set(opcoes[0]) # default value
        opt_menu = OptionMenu(self.root, var_opcao, *opcoes)
        opt_menu.place(x=self.size[0]-200, y=self.centro[1]+50)
        # btn
        var_wait = BooleanVar(False)
        btn_confirma = Button(self.root, text = "Confirmar", command=lambda: var_wait.set(True))
        btn_confirma.place(x=self.size[0]-200, y=self.centro[1])
        # espera apertar o btn
        btn_confirma.wait_variable(var_wait)
        #
        id = opcoes.index(var_opcao.get())
        # limpar
        opt_menu.destroy()
        btn_confirma.destroy()
        self.root.update()
        return id

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
            nome = ""
        if len(nome) > 10:
            nome = nome[:10]
        return nome

    def esperarPartida(self) -> list:
        self.btn_esperarPartida.wait_variable(self.__esperarPartida)
        return [self.__entrarOnline, self.__criarServer]

    def esperarandoJogadores(self):
        self.__reset()
        var = StringVar()
        var.set("Esperando jogadores")
        label = Label(self.root, textvariable=var)
        label.place(x=self.centro[0], y=self.centro[1])
        self.root.update()

    def entrarIpHost(self) -> str:
        IP = simpledialog.askstring("IP do Host", "Insira o IP do host")
        return IP

    def addChat(self, texto: str):
        print("chat: "+ texto)

    def iniciarRound(self):
        self.__reset()
        self.__telaJogo()

    def apresentarGanhadorDoJogo(self, jg_nome: str, jg_pontos: int):
        texto = jg_nome+" ganhou o jogo"+"\n"+"Com "+str(jg_pontos)+" pontos"
        self.__telaVitoria(texto)

    def apresentarGanhadorDoRound(self, jg_nome: str, jg_pontos: int):
        if jg_nome:
            messagebox.showinfo(message=jg_nome+" ganhou o round, agora possui "+str(jg_pontos)+" pontos")
        else:
            messagebox.showinfo(message="nao houve ganhadores nesse round")

    def anunciarCompararCartas(self):
        self.__addTexto('sem cartas no deck, comparando valor na mao dos jogadores restantes')

    def compararCartas(self, set_m: tuple,  set_j: tuple, ganhador_j: bool):
        n_m, c_n_m, v_m = set_m     # antigo maior
        n_j, c_n_j, v_j = set_j     # novo maior
        #
        self.__addTexto('comparando cartas de '+n_maior+' e '+n_j)
        self.__addTexto(v_j+' tinha carta '+c_n_j+' com o valor '+str(v_j) //
                        +'enquanto '+ v_m+' tinha carta '+c_n_m+' com o valor '+str(v_m))
        #
        if ganhador_j:
            self.__addTexto(n_j+' teve a maior carta')
        else:
            self.__addTexto('empate no valor das cartas ambos jogadores morrem')
            
            
    def anunciarCarta(self, j_nome: str, c_nome: str):
        self.__addTexto(j_nome+' jogou a carta '+c_nome)

    # seleciona um dos jogadores podendo ser siMesmo
    def selecionaJogador(self, jogadores_texto: list, possiveis: list, textoInicio: str) -> int:
        self.__addTexto("escolha outro jogador para "+textoInicio)
        # 
        if len(possiveis) == 0:
            self.__addTexto('nenhum jogador possivel de ser escolhido')
            return None
        # dentro dos possiveis
        alvo_i = None
        aceito = False
        while not aceito:
            alvo_i = self.__dropMenu(jogadores_texto)
            if alvo_i in possiveis:
                aceito = True
            else:
                messagebox.showinfo(message='escolha nao e valida')
        # retorna o indice do jogador escolhido
        return alvo_i

    def selecionaValorGuarda(self):
        self.__addTexto('escolha o tipo da carta')
        options = ['Padre', 'Barao', 'Aia', 'Principe', 'Rei', 'Condessa', 'Princesa']
        i = self.__dropMenu(options)
        self.__addTexto('Foi escolhido ' + str(i))
        # self.__addTexto('Foi escolhida ' + options[i])
        return i + 2

    def jogadorEscolherCarta(self, cartasMao_tipos: list) -> int:
        # mostrar cartas
        self.mostrarMao(cartasMao_tipos)
        # espera clicar em uma das cartas
        self.btns_cartas[0].wait_variable(self.carta_escolhida)
        carta_i = int(self.carta_escolhida.get())
        # esconder a carta clicada
        self.btns_cartas[carta_i].place_forget()
        # retornar index do botao
        return carta_i

    def alertarSobreCondessa(self):
        messagebox.showinfo(message='Voce deve jogar a condessa, pois tem um rei ou principe na mão!')

    def anunciarMorto(self, j_nome: str):
        self.__addTexto(j_nome+' foi morto')

    def resultadoGuarda(self, resultadoAcusacao: bool):
        if resultadoAcusacao:
            self.__addTexto('acertou a acusacao')
        else:
            self.__addTexto('errou a acusacao')
        
    def resultadoPadre(self, c_nome: str):
        self.__addTexto('carta na mao '+c_nome)
        
    def resultadoBarao(self, j_nome: str):
        if j_nome:
            self.__addTexto(j_nome+' possuia a carta de menor valor')
        else:
            self.__addTexto('empate')
        
    def resultadoAia(self, j_nome: str):
        self.__addTexto(j_nome+' esta protegido pelo proximo round')
        
    def resultadoPrincipe(self, j_nome: str):
        self.__addTexto(j_nome+' pegou uma nova mao')
        
    def resultadoRei(self, j1_nome: str, j2_nome: str):
        self.__addTexto('trocadas as maos de ' + j1_nome + ' e ' + j2_nome)
        
    def resultadoPrincesa(self, j_nome: str):
        self.__addTexto(j_nome+' tentou descartar a Princesa')

    def mostrarMao(self, cartasMao_tipo):
        xs = [-self.imagens_size[0]//2, 5+self.imagens_size[0]//2]
        for i in range(len(cartasMao_tipo)):
            self.btns_cartas[i].configure(image=self.imagens[cartasMao_tipo[i]])
            self.btns_cartas[i].place(x = self.centro[0]+xs[i],   y= self.size[1]-self.imagens_size[1]-20)
        self.root.update()

    def atualizarPlacar(self, placar):
        self.placar.set(placar)
