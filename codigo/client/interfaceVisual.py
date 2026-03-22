# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from client.interfaceUsuario import InterfaceUsuario

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

import gettext
import locale
from datetime import datetime

class InterfaceVisual(InterfaceUsuario):

    def __init__(self):
        self.size = (800,500)
        self.centro = (self.size[0]//2-50, self.size[1]//2)
        self.root = Tk()

        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        # gettext
        pt_br = gettext.translation('base', localedir=path[1]+'/locales', languages=['en'])
        pt_br.install()
        _ = pt_br.gettext # Portugues Brasil

        self.root.title(_("App Title"))
        self.root.resizable(False, False)
        self.root.geometry(str(self.size[0])+'x'+str(self.size[1]))

        # carrega as imagens
            # cartas
        self.imagens = [PhotoImage(file=r"recursos/cartas/carta"+str(i)+".png") for i in range(9)]
        self.imagens_size = (150, 210)
            # background
        self.background_vit = PhotoImage(file=r"recursos/tigrao.png")

        self.placar = StringVar()
        self.scoreVar = StringVar()
        self.__telaInicial()


    def __telaInicial(self):
        self.__entrarOnline = False
        self.__criarServer  = False
        self.__esperarPartida = BooleanVar(False)

        def entrarOnlineToggle():
            self.__entrarOnline = not self.__entrarOnline
        def criarServerToggle():
            self.__criarServer = not self.__criarServer


        # datas
        formato_data = locale.nl_langinfo(locale.D_FMT)
        hoje = datetime.today()
        hoje = hoje.strftime(formato_data)

        texto = _('Date: %s') % (hoje)
        l_data = Label(self.root, text = texto)
        l_data.place(x = self.centro[0], y= 150)

        # botoes e checks
        check_entrarOnline = Checkbutton(self.root, text = _("Join Online"), command=entrarOnlineToggle)
        check_criarServer = Checkbutton(self.root, text  = _("Create Server"), command=criarServerToggle)
        self.btn_esperarPartida = Button(self.root, text = _("Join Match"), command=lambda: self.__esperarPartida.set(True))

        check_entrarOnline.place(x = self.centro[0], y= 50)
        check_criarServer.place (x = self.centro[0], y= 75)
        self.btn_esperarPartida.place(x = self.centro[0], y= 200)
        # nome jogador
        self.nome_contents = StringVar()
        self.nome_contents.set(_("Name"))
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
        self.texto_esq.set(_("New Round"))
        label = Label(self.root, textvariable=self.texto_esq)
        label.place(x=5, y=5)

        # placar
        self.placar.set(self.placar.get())
        label = Label(self.root, textvariable=self.placar)
        label.place(x=self.centro[0]+100, y=10)

        self.root.update()


    def __telaVitoria(self, texto):
        self.__reset()

        background_label = Label(self.root, image=self.background_vit)
        background_label.place(x=0, y=0)

        textoVar = StringVar()
        textoVar.set(texto)
        label_texto = Label(self.root, textvariable=textoVar, font=("Courier", 11))
        label_texto.place(x=self.size[0]-250, y=80)

        label_score = Label(self.root, textvariable=self.scoreVar, font=("Courier", 10))
        label_score.place(x=self.size[0]-255, y=120)

        self.root.mainloop()


    def __addTexto(self, texto):
        chars_linha= 50
        linhas_text= 13
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
        xoff = -200
        # drop menu
        var_opcao = StringVar()
        var_opcao.set(opcoes[0]) # default value
        opt_menu = OptionMenu(self.root, var_opcao, *opcoes)
        opt_menu.place(x=self.size[0]+xoff, y=self.centro[1]+50)
        # btn
        var_wait = BooleanVar(False)
        btn_confirma = Button(self.root, text = _("Confirm"), command=lambda: var_wait.set(True))
        btn_confirma.place(x=self.size[0]+xoff, y=self.centro[1])
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

    def numeroJogadores(self) -> int: #Entre o número de jogadores
        numero = simpledialog.askinteger("", _("Enter the number of players:"),
                                            parent=self.root, minvalue=2, maxvalue=4)
        return numero

    def nomeJogador(self) -> str:
        nome = self.nome_contents.get()
        if len(nome) < 1:
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
        var.set(_("Waiting players"))
        label = Label(self.root, textvariable=var)
        label.place(x=self.centro[0], y=self.centro[1])
        self.root.update()

    def entrarIpHost(self, *args) -> str:
        meuIp = ""
        if len(args) > 0:
            if args[0]:
                meuIp = _("Your IP: %s") % (args[0])
        IP = simpledialog.askstring(_("Host's IP"), _("Enter Host's IP, your IP: %s") % (meuIp) )
        return IP

    def addChat(self, texto: str):
        print(_("chat: %s") % texto)

    def iniciarRound(self):
        self.__reset()
        self.__telaJogo()

    def apresentarGanhadorDoJogo(self, jg_nome: str, jg_pontos: int):
        texto = _("{name} won the game with {points} points").format(
                                                                    name= jg_nome,
                                                                    points= locale.currency(jg_pontos)
                                                                    )
        # texto  = jg_nome + ' '
        # texto += _("ganhou jogo")
        # texto += "\n"
        # texto += _("ganhou Com")
        # texto += ' ' + str(jg_pontos) + ' '
        # texto += _("ganhou pontos")
        self.__telaVitoria(texto)

    def apresentarGanhadorDoRound(self, jg_nome: str, jg_pontos: int):
        if jg_nome:#ganhou o round, pontos:
            # messagebox.showinfo(message=jg_nome+' '+ _("ganhou round") + ' ' +str(jg_pontos)+)
            messagebox.showinfo(message= _("{name} won the round with {points} points").format(
                                                                                            name= jg_nome,
                                                                                            points= locale.currency(jg_pontos)
                                                                                            ) )
        else:#nao houve ganhadores nesse round
            messagebox.showinfo(message=_("no winners round"))

    def anunciarCompararCartas(self):
        #sem cartas no deck, comparando valor na mao dos jogadores restantes
        self.__addTexto(_('empty deck'))

    def compararCartas(self, set_m: tuple,  set_j: tuple, ganhador_j: bool):
        # nome, carta_nome, valor
        n_m, c_n_m, v_m = set_m     # antigo maior
        n_j, c_n_j, v_j = set_j     # novo maior

        self.__addTexto(_('comparing cards from {name1} and {name2}').format(
                                                                        nome1= n_m,
                                                                        nome2= n_j
                                                                    ) )

        # self.__addTexto(_("%name2 tinha carta %card2 com o valor %points2 enquanto %name1 tinha carta %card1 com o valor %points1")
        self.__addTexto(_("{name2} had a card {card2} worth {points2} while {name1} had a card {card1} worth {points1}").format(
                                name1= n_m,
                                name2= n_j,
                                card1= c_n_m,
                                card2= c_n_j,
                                points1= locale.currency(float(v_m)),
                                points2= locale.currency(float(v_j))
                            ) )
        # n_j+' tinha carta '+c_n_j+' com o valor '+str(v_j) //
        #                 +'enquanto '+ n_m+' tinha carta '+c_n_m+' com o valor '+str(v_m))
        #
        if ganhador_j:
            self.__addTexto(_("{name} had a higher value card").format(name= n_j) )
            # self.__addTexto('%n_j+' teve a carta de maior valor')
        else:
            self.__addTexto(_('tie in card value both players die'))
            #empate no valor das cartas ambos jogadores morrem


    def anunciarCarta(self, j_nome: str, c_nome: str):
        self.__addTexto(_("{name} played the {card}").format(name=j_nome, card=c_nome) )

    # seleciona um dos jogadores podendo ser siMesmo
    def selecionaJogador(self, jogadores_texto: list, possiveis: list, textoInicio: str) -> int:
        # self.__addTexto("escolha outro jogador para "+ textoInicio)
        self.__addTexto(_("choose another player to %s") % (textoInicio) )
        #
        if len(possiveis) == 0:
            # nenhum jogador possível de ser escolhido
            self.__addTexto(_('no player possible to be chosen'))
            return None
        # dentro dos possiveis
        alvo_i = None
        aceito = False
        while not aceito:
            alvo_i = self.__dropMenu(jogadores_texto)
            if alvo_i in possiveis:
                aceito = True
            else:
                #escolha nao e valida
                messagebox.showinfo(message=_('not valid choice'))
        # retorna o indice do jogador escolhido
        return alvo_i

    def selecionaValorGuarda(self):
        # self.__addTexto('escolha o tipo da carta')
        self.__addTexto(_('Choose the card type'))
        # options = ['Padre', 'Barao', 'Aia', 'Principe', 'Rei', 'Condessa', 'Princesa']
        options = [ _('Priest'),
                    _('Baron'),
                    _('Handmaid'),
                    _('Prince'),
                    _('King'),
                    _('Countess'),
                    _('Princess')]
        i = self.__dropMenu(options)
        self.__addTexto(_('{card} was choosen').format(card = str(i)) )
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
        # 'Voce deve jogar a condessa, pois tem um rei ou principe na mão!'
        messagebox.showinfo(message=_('You must choose countess, since you have a king or prince in your hand!'))

    def anunciarMorto(self, j_nome: str):
        self.__addTexto(_('{name} was killed').format(name = j_nome) )

    def exibirMorto(self):
        texto = StringVar()
        texto.set(_('Dead'))
        label = Label(self.root, textvariable=texto, font=("Courier", 12))
        label.place(x=self.centro[0], y=self.centro[1]-50)

    def resultadoGuarda(self, resultadoAcusacao: bool):
        if resultadoAcusacao:
            # 'acertou a acusação'
            self.__addTexto(_('got the accusation right'))
        else:
            # 'errou a acusação'
            self.__addTexto(_('got the accusation wrong'))

    def resultadoPadre(self, c_nome: str):
        self.__addTexto(_('card in hand: %s') % (c_nome))

    def resultadoBarao(self, j_nome: str):
        if j_nome:
            # possuía a carta de menor valor
            self.__addTexto(_('{name} had the lowest value card').format(name = j_nome))
        else:
            self.__addTexto(_('Tie'))

    def resultadoAia(self, j_nome: str):
        self.__addTexto(_('{name} is protected by the next round').format(name = j_nome))
        # está protegido pelo próxima rodada

    def resultadoPrincipe(self, j_nome: str):
        self.__addTexto(_('{name} took a new hand').format(name = j_nome))
        # j_nome+' pegou uma nova mão')

    def resultadoRei(self, j1_nome: str, j2_nome: str):
        self.__addTexto(_('{name1} exchanged hands with {name2}').format(name1= j1_nome, nome2= j2_nome))
        # 'trocadas as mãos de ' + j1_nome + ' e ' + j2_nome)

    def resultadoPrincesa(self, j_nome: str):
        self.__addTexto(_('{name} tried to discard the Princess').format(name = j_nome))
        # j_nome+' tentou descartar a Princesa')

    def mostrarMao(self, cartasMao_tipo):
        xs = [-self.imagens_size[0]//2, 5+self.imagens_size[0]//2]
        for i in range(len(cartasMao_tipo)):
            self.btns_cartas[i].configure(image=self.imagens[cartasMao_tipo[i]])
            self.btns_cartas[i].place(x = self.centro[0]+xs[i],   y= self.size[1]-self.imagens_size[1]-20)
        self.root.update()

    def atualizarPlacar(self, placar):
        self.placar.set(placar)

    def exibirTopScore(self, score):
        self.scoreVar.set(score)
