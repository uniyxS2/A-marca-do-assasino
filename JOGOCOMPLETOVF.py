import time
import os
import sys
import random
import re

#  CORES coloca assim ("eude viado",Nome da cor)

VERMELHO = "\033[31m"
CIANO = "\033[36m"
BRANCO = "\033[37m"
CINZA = "\033[90m"
RESET = "\033[0m"

LARGURA = 120


#  FUNCOES (Nao mecha nisso)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# LINHA SUPERIOR E INFERIOR
def linha():
    print(CINZA + "█" + "═" * (LARGURA - 2) + "█" + RESET)


# MOLDURA DAS LATERAIS

# REMOVE CODIGOS ANSI DAS CORES
def limpar_ansi(texto):
    return re.sub(r'\033\[[0-9;]*m', '', texto)

# MOLDURA CENTRALIZADA CERTA
def moldura(texto="", cor=BRANCO):

    texto_limpo = limpar_ansi(texto)

    tamanho = len(texto_limpo)

    espaco = LARGURA - tamanho - 2

    if espaco < 0:
        espaco = 0

    esquerda = espaco // 2
    direita = espaco - esquerda

    print(
        CINZA + "█" + RESET
        + (" " * esquerda)
        + cor + texto + RESET
        + (" " * direita)
        + CINZA + "█" + RESET
    )

# FUNDO SOMBRIO
def fundo():

    simbolos = ["░", "▒", ".", "█", " "]

    linha_fundo = ""

    for _ in range(LARGURA - 2):

        if random.randint(0, 10) == 0:
            linha_fundo += random.choice(simbolos)
        else:
            linha_fundo += " "

    print(CINZA + "█" + linha_fundo + "█" + RESET)


# ANIMACAO das letras
def animar(texto, delay=0.05, cor=BRANCO):

    espacos = " " * ((LARGURA - len(texto)) // 2)

    sys.stdout.write(espacos)

    for letra in texto:
        sys.stdout.write(cor + letra + RESET)
        sys.stdout.flush()
        time.sleep(delay)

    print()


# GLITCH (nao toca nisso aqui)
def glitch(texto):

    chars = ["#", "@", "%", "&", "?"]

    for _ in range(3):

        limpar()

        linha()
        fundo()

        bugado = ""

        for letra in texto:

            if random.randint(0, 5) == 0:
                bugado += random.choice(chars)
            else:
                bugado += letra

        moldura(bugado, VERMELHO)

        fundo()
        linha()

        time.sleep(0.08)

# FRASES SOMBRIAS (nao uso)
frases = [
    "ELE ESTA OBSERVANDO",
    "NAO OLHE PARA TRAS",
    "VOCE ESCUTOU ISSO?",
    "CORRA",
    "NAO CONFIE NELES",
    "ALGO ESTA ERRADO",
]


def game_over():
    
    limpar()
    
    linha()
    
    moldura(VERMELHO + " ██████   █████  ███    ███ ███████ " + RESET)
    moldura(VERMELHO + "██       ██   ██ ████  ████ ██      " + RESET)
    moldura(VERMELHO + "██   ███ ███████ ██ ████ ██ █████   " + RESET)
    moldura(VERMELHO + "██    ██ ██   ██ ██  ██  ██ ██      " + RESET)
    moldura(VERMELHO + " ██████  ██   ██ ██      ██ ███████ " + RESET)
    
    moldura("")

    moldura(VERMELHO + " ██████  ██    ██ ███████ ██████   " + RESET)
    moldura(VERMELHO + "██    ██ ██    ██ ██      ██   ██  " + RESET)
    moldura(VERMELHO + "██    ██ ██    ██ █████   ██████   " + RESET)
    moldura(VERMELHO + "██    ██  ██  ██  ██      ██   ██  " + RESET)
    moldura(VERMELHO + " ██████    ████   ███████ ██   ██  " + RESET)

    linha()
    
    linha()
    moldura(VERMELHO + "VOCÊ MORREU" + RESET)
    linha()
    time.sleep(3)
    sys.exit()





def atoprologo():
    
    limpar()
    
    
    linha()
    moldura("Uma investigação marcada por assassinatos,")
    time.sleep(1)
    moldura("Documento confidencial — Prefeitura Municipal da Vila Ravenscroft. Ano 1300.")
    time.sleep(2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()

    linha()
    moldura("Os investigadores designados por este documento estão autorizados a")
    time.sleep(1)
    moldura("conduzir uma investigação sigilosa sobre os recentes assassinatos ocorridos na vila")
    time.sleep(1.3)
    moldura("Devido ao medo entre os moradores e à falta de")
    time.sleep(1.4)
    moldura("respostas das autoridades locais, a prefeitura exige discrição absoluta.")
    time.sleep(1.5)
    moldura("Assinado. Seja bem-vindo ao caso, senhor [Investigador].")
    time.sleep(1.6)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
def ato1():
    
    linha()
    moldura("COMEÇO DO ATO - 1")
    linha

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("O Investigador chega à uma pequena vila da Inglaterra após receber uma carta misteriosa.")
    time.sleep(1)
    moldura("Os moradores assustados indicam o delegado Edward Blackwood.")
    time.sleep(1.2)
    moldura("Ele responde às perguntas com uma pressa estranha,")
    time.sleep(1.3)
    moldura("como se quisesse encerrar a conversa antes que ela avance demais.")
    time.sleep(1.4)
    moldura("Blackwood conta sobre três antigos casos envolvendo os primogênitos das famílias Whitmore,")
    time.sleep(1.5)
    moldura("Lancaster e Hawthorne.")
    time.sleep(1.6)
    linha()
    
    linha()
    moldura("Então ele revela: Agora temos um novo caso. A jovem Emi foi encontrada morta esta manhã.")
    time.sleep(1)
    moldura("O Investigador segue para a mansão de Emi.")
    time.sleep(1.2)
    moldura("Na sala, encontram o corpo de Emi, e sua mãe Kaori")
    time.sleep(1.3)
    moldura("após se casar com um mercador local — chorando ao lado do corpo.")
    time.sleep(1.4)
    moldura("uma viajante do Oriente que se estabeleceu em Ravenscroft anos atrás")
    time.sleep(1.5)
    moldura("Marcas de sangue levam até a cozinha.")
    time.sleep(1.6)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    

    while True:
        
        linha()
        moldura("[1] Examinar o corpo")
        moldura("[2] Conversar com Kaori")
        moldura("[3] Seguir as marcas de sangue")
        moldura("[4] Interrogar os criados da casa")
        moldura("[5] Continuar")
        linha()
        
        escolha = input(VERMELHO + "\n              >>> " + RESET)
            
        if escolha == "1":
        
            linha()
            moldura("Vocês encontram fragmentos de madeira, ")
            time.sleep(1)
            moldura("um tecido preto e um colar quebrado. O tempo gasto examinando o")
            time.sleep(1.2)
            moldura("corpo permite que Kaori se recomponha")
            time.sleep(1.3)
            moldura("e feche a expressão antes que vocês possam falar com ela.")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
            
        elif escolha == "2":
        
            linha()
            moldura("Kaori revela: '- Emi dizia ouvir passos durante a noite.'")
            time.sleep(1)
            moldura("'Ela acreditava que alguém vivia na mansão.' Ela confia em")
            time.sleep(1.2)
            moldura("vocês o suficiente para falar, mas o corpo de")
            time.sleep(1.3)
            moldura("Emi fica sem exame — algum vestígio físico pode se perder quando")
            time.sleep(1.4)
            moldura("os criados finalmente o cobrirem.")
            time.sleep(1.5)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
        
        elif escolha == "3":
        
            linha()
            moldura("As marcas terminam diante de um grande armário.")
            time.sleep(1)
            moldura("Há riscos recentes no chão. Kaori observa vocês em silêncio, ")
            time.sleep(1.2)
            moldura("sem que ninguém pergunte nada a ela.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
    
        elif escolha == "4":
        
            linha()
            moldura("Os criados estão apavorados demais para falar com clareza,")
            time.sleep(1)
            moldura("mas um deles murmura que ouviu uma discussão na noite anterior.")
            time.sleep(1.2)
            moldura("'- Uma voz de homem. Não era da casa,' ele diz, antes de se calar.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha == "5":
            break
        
    
        else:
            print("Opção inválida.")
    
    limpar()
    
    linha()
    moldura("A porta dos fundos está entreaberta.")
    linha()

    while True:
        
        linha()
        moldura("[1]  Vasculhar o jardim:")
        moldura("[2]  Examinar a cozinha novamente:")
        moldura("[3]  Continuar")
        linha()

        escolha2 = input(VERMELHO + "\n              >>> " + RESET)

        if escolha2 == "1":
            
            linha()
            moldura("No jardim, encontram uma adaga com a marca de assassino:")
            time.sleep(1)
            moldura("um símbolo antigo gravado na lâmina.")
            time.sleep(1.2)
            moldura("Mas as pegadas ao redor foram apagadas pela chuva da manhã.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha2 == "2":
            
            linha()
            moldura("Na cozinha encontram comida envenenada e uma nota.")
            time.sleep(1)
            moldura(" Na nota está escrito apenas um símbolo antigo.")
            time.sleep(1.2)
            moldura("O jardim, agora sob chuva, não será revisitado tão cedo.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha2 == "3":
            break
        
        input("Pressione ENTER para continuar...")
        limpar()
        
    linha()
    moldura("FIM DO ATO - 1")
    linha()
    limpar()

def ato2():

    linha()
    moldura("COMEÇO DO ATO - 2")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("O Investigador passa dias investigando as famílias fundadoras.")
    time.sleep(1)
    moldura("Whitmore, Lancaster, Hawthorne... todos relacionados aos antigos assassinatos.")
    time.sleep(1.2)
    moldura("Todos perderam seus primogênitos sob circunstâncias misteriosas.")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("Kaori, grata pela discrição no dia da morte de Emi, oferece uma pista:")
    time.sleep(1)
    moldura("'- Procure primeiro os Lancaster. Emi tinha medo deles.'")
    time.sleep(1.2)
    linha()
    
    input("Pressione ENTER para continuar...")

    limpar()
    
    
    while True:
        
        linha()
        moldura("[1] Os Whitmore:")
        moldura("[2] Os Lancaster:")
        moldura("[3] Os Hawthorne")
        moldura("[4] Continuar")
        linha()
        
        escolha3 = input(VERMELHO + "\n              >>> " + RESET)
        
        if escolha3 == 1:
            
            linha()
            moldura("Os Whitmore revelam um segredo famoso:")
            time.sleep(1)
            moldura(": o primogênito Samuel foi encontrado com a mesma marca de Emi.")
            time.sleep(1.2)
            moldura("Há trinta anos.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha3 == "2":
            
            linha()
            moldura("Confrontados com o nome de Emi, os Lancaster ficam visivelmente nervosos.")
            time.sleep(1)
            moldura("Admitem que seu filho desapareceu misteriosamente, mas escondem algo mais.")
            time.sleep(1.2)
            moldura("Seus olhares se cruzam antes de responder.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha3 == "3":
            
            linha()
            moldura("Os Hawthorne têm registros estranhos.")
            time.sleep(1)
            moldura("Seu primogênito Geoffrey foi encontrado em circunstâncias obscuras.")
            time.sleep(1.2)
            moldura("Seu corpo foi rapidamente enterrado de noite.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
    
        elif escolha3 == "4":
            break
    else:
        print("Opção inválida.")
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Reflexão sobre a teoria:")
    time.sleep(1)
    moldura("Serial killer tradicional → Você mantém a lógica investigativa.")
    time.sleep(1.2)
    moldura(" Isso soa bem diante do delegado, ")
    time.sleep(1.3)
    moldura("mas fecha sua mente para algumas das pistas mais estranhas que já reuniu.")
    time.sleep(1.4)
    moldura("As famílias se matando mutuamente → Você desconfia que há conflito entre as famílias.")
    time.sleep(1.5)
    moldura("A teoria não convence ninguém na vila, e alguns moradores passam a evitar suas perguntas.")
    time.sleep(1.6)
    moldura("Algo sobrenatural → Você começa a questionar sua própria sanidade.")
    time.sleep(1.7)
    moldura("Mas essa abertura mental também deixa você mais atento a detalhes que a lógica pura ignoraria.")
    time.sleep(1.8)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("FIM DO ATO - 2")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

def ato3():
    
    linha()
    moldura("COMEÇO DO ATO - 3")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

    linha()
    moldura("Analisando as pistas, você descobre que todas as vítimas tinham uma coisa em comum.")
    time.sleep(1)
    moldura("Todas frequentavam uma antiga biblioteca privada da vila.")
    time.sleep(1.2)
    moldura("Uma biblioteca que ninguém sabe onde fica.")
    time.sleep(1.3)
    linha()
    
    
    linha()
    moldura("Margaret, grata por sua discrição sobre Samuel, oferece ajuda:")
    time.sleep(1)
    moldura("Os registros da família podem apontar um caminho mais rápido.")
    time.sleep(1.2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    while True:
        
        linha()
        moldura("[1] Interrogar os moradores antigos ")
        moldura("[2] Procurar registros públicos:")
        moldura("[3] Rastrear os movimentos das vítimas:")
        moldura("[4] Pedir acesso aos arquivos privados dos Whitmore")
        moldura("[5] Continuar")
        linha()
        
        escolha4 = input(VERMELHO + "\n              >>> " + RESET)
        
        if escolha4 == "1":
            
            linha()
            moldura("Um homem idoso revela informações cruciais.")
            time.sleep(1)
            moldura("A biblioteca fica escondida sob a torre da antiga prefeitura.")
            time.sleep(1.2)
            moldura("Ele avisa: '- Não vá sozinho de noite.'")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha4 == "2":
            
            linha()
            moldura("Você encontra referências a uma 'Sala de Estudos Aurelius'")
            time.sleep(1)
            moldura("em pergaminhos guardados há mais de cem anos, muito antes da fundação de Ravenscroft.")
            time.sleep(1.2)
            moldura("Aurelius parece ser o nome de alguém importante para a história.")
            time.sleep(1.3)
            moldura("Mas os registros não dizem onde essa sala está — só que existe.")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha4 == "3":
            
            linha()
            moldura("Você descobre que as vítimas saíram de suas casas por noites consecutivas.")
            time.sleep(1)
            moldura("Sempre em direção ao norte da vila.")
            time.sleep(1.2)
            moldura("Sempre retornando antes do amanhecer.")
            time.sleep(1.3)
            moldura("Até a última noite, quando não voltaram.")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha4 == "4":
            
            linha()
            moldura("Nos arquivos dos Whitmore, ")
            time.sleep(1)
            moldura("Você encontra uma planta antiga da prefeitura com uma área marcada como ")
            time.sleep(1.2)
            moldura("'selada por ordem da família'.")
            time.sleep(1.3)
            moldura("É exatamente sob a torre.")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
        
        elif escolha4 == "5":
            break
        
        input("Pressione ENTER para continuar...")
        limpar()
        
    else:
        print("Opção inválida.")
            
    linha()
    moldura("Juntando todas as informações leva você a torre.")
    time.sleep(1)
    linha()
    
    linha()
    moldura("FIM DO ATO - 3")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()

    #fim ato3

def ato4():

    linha()
    moldura("COMEÇO DO ATO - 4")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você chega à antiga prefeitura no meio da noite.")
    time.sleep(1)
    moldura("A estrutura está aparentemente abandonada.")
    time.sleep(1.2)
    moldura("Mas há sinais recentes de atividade.")
    time.sleep(1.3)
    moldura("Graças ao mapa que já possui, você sabe exatamente onde ficam os pontos fracos da estrutura.")
    time.sleep(1.4)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
        
    linha()
    moldura("[1] Pela porta principal com força")
    moldura("[2] Procurando entrada discreta")
    moldura("[3] Esperando e observando")
    linha()
    
    escolha5 = input(VERMELHO + "\n              >>> " + RESET)
        
    if escolha5 == "1":
           
        linha()
        moldura("A porta cede facilmente.")
        time.sleep(1)
        moldura("Como se alguém quisesse que você entrasse.")
        time.sleep(1.2)
        moldura("O barulho ecoa — se havia alguém lá dentro, agora já sabe que você chegou.")
        time.sleep(1.3)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    
    elif escolha5 == "2":
        
        linha()
        moldura("Você encontra uma janela destrancada.")
        time.sleep(1)
        moldura("Entra silenciosamente, mas perde um tempo precioso procurando o caminho certo lá dentro.")
        time.sleep(1.2)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    elif escolha5 == "3":
            
        linha()
        moldura("Esperando nas sombras, você vê três pessoas encapuzadas entrarem pela torre.")
        time.sleep(1)
        moldura("Eles carregam velas e falam em sussurros.")
        time.sleep(1.2)
        moldura("Um deles manca ligeiramente ao subir os degraus")
        time.sleep(1.3)
        moldura(" — o mesmo jeito de andar que você notou em Blackwood.")
        time.sleep(1.4)
        moldura("Mas esperar tem um preço: o frio da noite cala fundo nos ossos.")
        time.sleep(1.5)
        moldura("Depois de um tempo você entra.")
        linha()
                
        input("Pressione ENTER para continuar...")
        limpar()
        
    else:
        print("Opção inválida.")
        
    linha()
    moldura("Escada em espiral descendo:")
    linha()
        
    linha()
    moldura("[1] Descer com cuidado")
    moldura("[2] Procurar outros cômodos")
    moldura("[3] Deixar a torre e buscar ajuda")
    linha()
        
    escolha6 = input(VERMELHO + "\n              >>> " + RESET)
        
    if escolha6 == "1":
            
        linha()
        moldura("Você desce.")
        time.sleep(1)
        moldura("O ar fica mais frio a cada degrau.")
        time.sleep(1.2)
        moldura("No final da escada, há uma porta de madeira envelhecida.")
        time.sleep(1.3)
        moldura("Há luz vermelha saindo por baixo dela.")
        time.sleep(1.4)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    elif escolha6 =="2":
            
        linha()
        moldura("Você explora os cômodos acima.")
        time.sleep(1)
        moldura("Encontra registros antigos sobre cerimônias e sacrifícios.")
        time.sleep(1.2)
        moldura("Mas o tempo gasto permite que quem está lá embaixo perceba sua presença.")
        time.sleep(1.3)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    elif escolha6 == "3":
            
        linha()
        moldura("Você sai da torre questionando se deveria ter agido sozinho.")
        time.sleep(1)
        moldura("A noite passa sem incidente, mas o delegado Blackwood pergunta, ")
        time.sleep(1.2)
        moldura("no dia seguinte, o porquê você foi visto perto da prefeitura.")
        time.sleep(1.3)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
    
    else:
        print("Opção inválida.")
        
        input("Pressione ENTER para continuar...")
        limpar()
        
    linha()
    moldura("FIM DO ATO - 4")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

def ato5():

    linha()
    moldura("COMEÇO DO ATO - 5")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

    linha()
    moldura("Você finalmente entra na câmara subterrânea.")
    time.sleep(1)
    moldura("É uma biblioteca, mas de natureza perturbadora.")
    time.sleep(1.2)
    moldura("As paredes estão cobertas de símbolos antigos.")
    time.sleep(1.3)
    moldura("Livros descrevem rituais esquecidos e segredos ancestrais.")
    time.sleep(1.4)
    linha()

    while True:
        
        linha()
        moldura("[1] Os Sacrifícios de Aurelius ")
        moldura("[2] Diário pessoal envelhecido:")
        moldura("[3] Grimório antigo:")
        moldura("[4] Continuar ")
        linha()
        
        escolha7 = input(VERMELHO + "\n              >>> " + RESET)
        
        if escolha7 == "1":
            linha()
            moldura("O livro descreve rituais de sacrifício realizados há séculos.")
            time.sleep(1)
            moldura("Aurelius era um mago que buscava imortalidade.")
            time.sleep(1.2)
            moldura("Ele acreditava que sacrifícios puros o mantinham vivo.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        elif escolha7 == "2":
            linha()
            moldura("O diário pertence a uma mulher que viveu na vila há mais de um século.")
            time.sleep(1)
            moldura("muito antes do nascimento de Emi.")
            time.sleep(1.2)
            moldura("Ela descreve encontros com 'O Guardião', uma figura encapuzada.")
            time.sleep(1.3)
            moldura("O Guardião a guiava em cerimônias noturnas.")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
        
        elif escolha7 == "3":
            linha()
            moldura("O grimório está escrito em uma língua antiga.")
            time.sleep(1)
            moldura("Mas você consegue traduzir algumas frases:")
            time.sleep(1.2)
            moldura("'Para manter a marca viva, novos sangues devem ser oferecidos.'")
            time.sleep(1.3)
            moldura("'A marca escolhe seus portadores através dos tempos.'")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
        
        elif escolha7 == "4":
            break
        
            input("Pressione ENTER para continuar...")
            limpar()
        
    else:
        print("Opção inválida.")
            
    linha()
    moldura("*Porta oculta na biblioteca:*")
    linha()

    linha()
    moldura("[1] Tentar abrir a porta")
    moldura("[2] Procurar chave/mecanismo")
    moldura("[3] Sair para preparar expedição")
    linha()
    
    escolha8 = input(VERMELHO + "\n              >>> " + RESET)

    if escolha8 == "1":
        linha()
        moldura("A porta não abre.")
        time.sleep(1)
        moldura("Mas você ouve passos se aproximando das escadas.")
        time.sleep(1.2)
        moldura("Você não está mais sozinho.")
        time.sleep(1.3)
        linha()
                
        input("Pressione ENTER para continuar...")
        limpar()
                
    elif escolha8 == "2":
        linha()
        moldura("Você procura sistematicamente e encontra uma chave.")
        time.sleep(1)
        moldura("antiga escondida em um compartimento secreto")
        time.sleep(1.2)
        moldura("A porta se abre, revelando um corredor ainda mais escuro.")
        time.sleep(1.3)
        moldura("A busca cuidadosa, porém, consome tempo")
        time.sleep(1.4)
        moldura("— e quem quer que tenha deixado a chave ali pode saber que ela sumiu.")
        time.sleep(1.5)
        linha()
                
        input("Pressione ENTER para continuar...")
        limpar()
                
    elif escolha8 == "3":    
        linha()
        moldura("Você sai rapidamente da biblioteca, carregando alguns livros para análise futura.")
        time.sleep(1)
        moldura("É a escolha mais segura, mas a porta oculta continua sem resposta.")
        time.sleep(1.2)
        linha()
                
        input("Pressione ENTER para continuar...")
        limpar()    

    linha()
    moldura("FIM DO ATO - 5")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

def ato6():

    linha()
    moldura("COMEÇO DO ATO - 6")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você retorna à mansão de Emi com seu conhecimento recém-adquirido.")
    time.sleep(1)
    moldura("Kaori o recebe, mas há algo diferente em seu olhar.")
    time.sleep(1.2)
    moldura("Ela sabe que você descobriu a verdade.")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("[1] Confrontar Kaori diretamente")
    moldura("[2] Fingir ignorância e observar")
    moldura("[3] Procurar evidências físicas")
    moldura("[4] Pedir que Kaori conte a verdade, como aliada")
    linha()
        
    escolha9 = input(VERMELHO + "\n              >>> " + RESET)
        
    if escolha9 == "1":
            
        linha()
        moldura("Kaori admite tudo entre lágrimas.")
        time.sleep(1)
        moldura("Emi foi escolhida pela marca como sacrifício.")
        time.sleep(1.2)
        moldura("Kaori acreditava que sacrificá-la salvaria a vila.")
        time.sleep(1.3)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    elif escolha9 == "2":
            
        linha()
        moldura("Você observa Kaori durante horas.")
        time.sleep(1)
        moldura("Ela começa a falar sozinha, mencionando A marca e O Guardião.")
        time.sleep(1.2)
        moldura("Ela descobre que você a está observando.")
        time.sleep(1.3)
        moldura("Kaori tenta fugir.")
        time.sleep(1.4)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    elif escolha9 == "3":
        linha()
        moldura("Você encontra um altar oculto em um quarto secreto.")
        time.sleep(1)
        moldura("Nele estão símbolos idênticos aos da biblioteca.")
        time.sleep(1.2)
        moldura("E oferendas de sangue envelhecidas.")
        time.sleep(1.3)
        moldura("Kaori observa a distância, sem impedir — como se quisesse ser encontrada.")
        time.sleep(1.4)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
            
    elif escolha9 == "4":
            
        linha()
        moldura("Kaori chora ao contar tudo, aliviada por não precisar mais esconder o peso que carrega sozinha.")
        time.sleep(1)
        moldura("'- Eu não sabia como te contar sem que você me odiasse,' ela diz.")
        time.sleep(1.2)
        moldura("Ela promete ajudar a encontrar o resto do culto — de dentro.")
        time.sleep(1.3)
        linha()
            
        input("Pressione ENTER para continuar...")
        limpar()
    else:
        linha()
        moldura("Opção inválida.")
        linha()

        escolha9 = input(VERMELHO + "\n              >>> " + RESET)

    linha()
    moldura("FIM DO ATO - 6")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar() 

def ato7():

    linha()
    moldura("COMEÇO DO ATO - 7")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

    linha()
    moldura("Meses se passaram desde suas descobertas.")
    time.sleep(1)
    moldura("Você continuou investigando o culto em segredo,")
    time.sleep(1.2)
    moldura("reunindo aliados e evidências, mas o rastro esfriou.")
    time.sleep(1.3)
    moldura("Você acreditava ter perdido a trilha.")
    time.sleep(1.4)
    moldura("Mas agora uma nova vítima aparece.")
    time.sleep(1.5)
    moldura("Outro corpo com a marca.")
    time.sleep(1.6)
    moldura("E desta vez, é em uma mansão que você conhece bem.")
    time.sleep(1.7)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Qual é a sua reação: ")
    linha()
    
    linha()
    moldura("[1] Raiva e determinação ")
    moldura("[2] Desespero")
    moldura("[3] Suspeita de armadilha")
    moldura("[4] Continuar")
    linha()
    
    escolha10 = input(VERMELHO + "\n              >>> " + RESET)
    
    if escolha10 == "1":
        
        limpar()
        
        linha()
        moldura("Você jura encontrar e destruir o culto de uma vez.")
        time.sleep(1)
        moldura("A determinação o cega para os riscos à sua frente.")
        time.sleep(1.2)
        linha()
        
        
        linha()
        moldura("Chegando na cena do crime você muito irritado anda para o portão dela, lá você encontra:")
        linha()
        
        input("Pressione ENTER para continuar...")
        
        linha()
        moldura("[1] Mapa para o norte:")
        moldura("[2] Carta com o símbolo da marca")
        moldura("[3] Pegadas estranhas")
        moldura("[4] Continuar")
        linha()
        
        escolha11 = input(VERMELHO + "\n              >>> " + RESET)
        
        while True:
            
            linha()
            moldura("[1] Mapa para o norte:")
            moldura("[2] Carta com o símbolo da marca")
            moldura("[3] Pegadas estranhas")
            moldura("[4] Continuar")
            linha()
            
            escolha11 = input(VERMELHO + "\n              >>> " + RESET)
            
        
            if escolha11 == "1":
                
                limpar()
                
                linha()
                moldura("O mapa marca claramente a localização de uma estrutura antiga.")
                time.sleep(1)
                moldura("Uma abadia esquecida no coração da floresta.")
                time.sleep(1.2)
                linha()
                
                input("Pressione ENTER para continuar...")
                limpar()
                
            elif escolha11 == "2":
                
                linha()
                moldura("A carta é uma provocação:")
                time.sleep(1)
                moldura("Sua obsessão o levará até nós. A marca aguarda.")
                time.sleep(1.2)
                linha()
                
                input("Pressione ENTER para continuar...")
                limpar()
                
            elif escolha11 == "3":
                
                linha()
                moldura("As pegadas são humanoides, mas deformadas.")
                time.sleep(1)
                moldura("Como se a pessoa caminhasse de forma não natural.")
                time.sleep(1.2)
                linha()
                
                input("Pressione ENTER para continuar...")
                limpar()
                
            elif escolha11 == "4":
                break
            
            input("Pressione ENTER para continuar...")
            limpar()
            
        else:
            print("Opção inválida.")
                   
                   
        linha()
        moldura("A casa explode repentinamente:")
        linha()
         
        linha()
        moldura("[1] Sair antes de cair:")
        moldura("[2] Ser derrubado pela explosão:")
        moldura("[3] Estar longe o suficiente")
        linha()
        
        escolha12 = input(VERMELHO + "\n              >>> " + RESET)
        
        if escolha12 == "1":
            
            limpar()
            
            linha()
            moldura("Você sai correndo, mas o fogo consome a prova.")
            time.sleep(1)
            moldura("As evidências que poderia ter reunido desaparecem.")
            time.sleep(1.2)
            linha()
            
            input("Pressione ENTER para continuar...")
            
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
        elif escolha12 == "2":
            
            limpar()
            
            linha()
            moldura("Você passa horas inconsciente.")
            time.sleep(1)
            moldura("Quando acorda no hospital, já é noite.")
            time.sleep(1.2)
            moldura("As provas se foram.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
            linha()
            moldura("FINAL 2 DO ATO - 7")
            linha()
            
        elif escolha12 == "3":
            
            limpar()
            
            linha()
            moldura("Você consegue documentar provas antes da explosão.")
            time.sleep(1)
            moldura("O conhecimento que você reúne será crucial")
            time.sleep(1.2)
            moldura(" — mas a distância também significa que não conseguiu ajudar quem estava lá dentro.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
    
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
            linha()
            moldura("FINAL 3 DO ATO - 7")
            linha()
            
        else:
            print("Opção inválida.")
    
    
    elif escolha10 == 2:
        
        linha()
        moldura("O medo toma conta de você, mas você sabe qual é o único caminho.")
        time.sleep(1)
        moldura("Mesmo com medo você não tem outra opcão.")
        time.sleep(1.2)
        moldura("Chegando no portão, você se deparra com algumas coisa: ")
        time.sleep(1.3)
        linha()
        
        input("Pressione ENTER para continuar...")
        limpar()
        
        linha()
        moldura("[1] Mapa para o norte:")
        moldura("[2] Carta com o símbolo da marca")
        moldura("[3] Pegadas estranhas")
        moldura("[4] Continuar")
        linha()
        
        escolha11 = input(VERMELHO + "\n              >>> " + RESET)
        
        while True:
            
            linha()
            moldura("[1] Mapa para o norte:")
            moldura("[2] Carta com o símbolo da marca")
            moldura("[3] Pegadas estranhas")
            moldura("[4] Continuar")
            linha()
        
            escolha11 = input(VERMELHO + "\n              >>> " + RESET)
                
                
            if escolha11 == "1":
                    
                    linha()
                    moldura("O mapa marca claramente a localização de uma estrutura antiga.")
                    time.sleep(1)
                    moldura("Uma abadia esquecida no coração da floresta.")
                    time.sleep(1.2)
                    linha()
                    
                    input("Pressione ENTER para continuar...")
                    limpar()
                    
            elif escolha11 == "2":
                    
                    linha()
                    moldura("A carta é uma provocação:")
                    time.sleep(1)
                    moldura("'Sua obsessão o levará até nós. A marca aguarda.'")
                    time.sleep(1.2)
                    linha()
                    
                    input("Pressione ENTER para continuar...")
                    limpar()
                    
            elif escolha11 == "3":
                    
                    linha()
                    moldura("As pegadas são humanóides, mas deformadas.")
                    time.sleep(1)
                    moldura("Como se a pessoa caminhasse de forma não natural.")
                    time.sleep(1.2)
                    linha()
                    
                    input("Pressione ENTER para continuar...")
                    limpar()
                    
            elif escolha11 == "4":
                    break
                
                    input("Pressione ENTER para continuar...")
                    limpar()
                
        else:
            print("Opção inválida.")
            
        linha()
        moldura("A casa explode repentinamente:")
        linha()
        
        linha()
        moldura("[1] Sair antes de cair")
        moldura("[2] Ser derrubado pela explosão")
        moldura("[3] Estar longe o suficiente")
        linha()
        
        escolha14 = input(VERMELHO + "\n              >>> " + RESET)
        
        if escolha14 == "1":
            
            limpar()
            input("Pressione ENTER para continuar...")
            
            
            linha()
            moldura("Você sai correndo, mas o fogo consome a prova.")
            time.sleep(1)
            moldura("As evidências que poderia ter reunido desaparecem.")
            time.sleep(1.2)
            linha()
            
            input("Pressione ENTER para continuar...")
            
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
        elif escolha14 == "2":
            
            linha()
            moldura("Você passa horas inconsciente.")
            time.sleep(1)
            moldura("Quando acorda no hospital, já é noite.")
            time.sleep(1.2)
            moldura("As provas se foram.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
            linha()
            moldura("FINAL 2 DO ATO - 7")
            linha()
            
        elif escolha14 == "3":
            
            linha()
            moldura("Você consegue documentar provas antes da explosão.")
            time.sleep(1)
            moldura("O conhecimento que você reúne será crucial,")
            time.sleep(1.2)
            moldura("mas a distância também significa que não conseguiu ajudar quem estava lá dentro.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
    
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
            linha()
            moldura("FINAL 3 DO ATO - 7")
            linha()
        
        
        elif escolha10 == "3":
        
            linha()
            moldura("Sua intuição pode salvá-lo — mas a hesitação também tem um custo.")
            time.sleep(1)
            moldura("Você chega depois de um tempo mas percebe algumas coisa para investigar: ")
            time.sleep(1.2)
            linha()
            
            input("Pressione ENTER para continuar...")
            limpar()
            
            linha()
            moldura("[1] Mapa para o norte:")
            moldura("[2] Carta com o símbolo da marca")
            moldura("[3] Pegadas estranhas")
            moldura("[4] Continuar")
            linha()
        
        escolha15 = input(VERMELHO + "\n              >>> " + RESET)
        
        while True:
            
            linha()
            moldura("[1] Mapa para o norte:")
            moldura("[2] Carta com o símbolo da marca")
            moldura("[3] Pegadas estranhas")
            moldura("[4] Continuar")
            linha()
            
            escolha15 = input(VERMELHO + "\n              >>> " + RESET)
                
            if escolha15 == "1":
                    
                    linha()
                    moldura("O mapa marca claramente a localização de uma estrutura antiga.")
                    time.sleep(1)
                    moldura("Uma abadia esquecida no coração da floresta.")
                    time.sleep(1.2)
                    linha()
                    
                    input("Pressione ENTER para continuar...")
                    limpar()
                    
            elif escolha15 == "2":
                    
                    linha()
                    moldura("A carta é uma provocação:")
                    time.sleep(1)
                    moldura("'Sua obsessão o levará até nós. A marca aguarda.'")
                    time.sleep(1.2)
                    linha()
                    
                    input("Pressione ENTER para continuar...")
                    limpar()
                    
            elif escolha15 == "3":
                    
                    linha()
                    moldura("As pegadas são humanóides, mas deformadas.")
                    time.sleep(1)
                    moldura("Como se a pessoa caminhasse de forma não natural.")
                    time.sleep(1.2)
                    linha()
                    
                    input("Pressione ENTER para continuar...")
                    limpar()
                    
            elif escolha15 == "4":
                    break
                
                    input("Pressione ENTER para continuar...")
                    limpar()
                
        else:
            print("Opção inválida.")
                    
        linha()
        moldura("A casa explode repentinamente:")
        linha()
        
        linha()
        moldura("[1] Sair antes de cair")
        moldura("[2] Ser derrubado pela explosão")
        moldura("[3] Estar longe o suficiente")
        linha()
        
        escolha14 = input(VERMELHO + "\n              >>> " + RESET)
        
        if escolha14 == "1":
            
            linha()
            moldura("Você sai correndo, mas o fogo consome a prova.")
            time.sleep(1)
            moldura("As evidências que poderia ter reunido desaparecem.")
            time.sleep(1.2)
            linha()
            
            input("Pressione ENTER para continuar...")
            
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
        elif escolha14 == "2":
            
            linha()
            moldura("Você passa horas inconsciente.")
            time.sleep(1)
            moldura("Quando acorda no hospital, já é noite.")
            time.sleep(1.2)
            moldura("As provas se foram.")
            time.sleep(1.3)
            linha()
            
            input("Pressione ENTER para continuar...")
            
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
            linha()
            moldura("FIM 2 DO ATO - 7")
            linha()
            
        elif escolha14 == "3":
            
            linha()
            moldura("Você consegue documentar provas antes da explosão.")
            time.sleep(1)
            moldura("O conhecimento que você reúne será crucial, ")
            time.sleep(1.2)
            moldura("mas a distância também significa")
            time.sleep(1.3)
            moldura("que não conseguiu ajudar quem estava lá dentro.")
            time.sleep(1.4)
            linha()
            
            input("Pressione ENTER para continuar...")
    
            linha()
            moldura("Uma coisa é clara: o culto quer que você os encontre.")
            time.sleep(1)
            moldura("E ele quer que você vá para aquela abadia.")
            time.sleep(1.2)
            moldura("A questão é: você terá forças para enfrentar o que o aguarda lá?")
            time.sleep(1.3)
            linha()
            
            linha()
            moldura("FIM 3 DO ATO - 7")
            linha()

    input("Pressione ENTER para continuar...")
    limpar()
#======================================================================================================================================================

def ato8():
    
    linha()
    moldura("COMEÇO DO ATO - 8")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você passa as próximas semanas reunindo informações.")
    time.sleep(1)
    moldura("A culpa pela morte de tantos inocentes pesa em seus ombros.")
    time.sleep(1.2)
    moldura("Mas você está mais determinado do que nunca. A abadia aguarda.")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("[1] Buscar reforços as autoridades:")
    moldura("[2] Investigar a história da abadia:")
    moldura("[3] Procurar aliados entre os moradores:")
    moldura("[4] Ir sozinho, sem volta mais ninguém:")
    linha()
       
    escolha16 = input(VERMELHO + "\n              >>> " + RESET)
    
    if escolha16 == "1":
   
        linha()
        moldura("O delegado Blackwood se recusa a ajudar.")
        time.sleep(1)
        moldura("'- Isso é loucura,' ele diz, evitando seu olhar.")
        time.sleep(1.2)
        moldura("Ele manca ao se levantar da cadeira.")
        time.sleep(1.3)
        moldura("O mesmo passo que você viu entre os encapuzados na torre.")
        time.sleep(1.4)
        moldura("Agora você tem certeza: Blackwood também está envolvido com o culto.")
        time.sleep(1.5)
        linha()
        
    elif escolha16 == "2":
    
        linha()
        moldura("Você encontra registros de uma abadia construída em 1200.")
        time.sleep(1)
        moldura("Ela era dedicada a 'Aurelius, o Eterno'.")
        time.sleep(1.2)
        moldura("Foi abandonada após acusações de práticas ocultistas.")
        time.sleep(1.3)
        linha()
    
    elif escolha16 == "3":
        
        linha()
        moldura("Você encontra pessoas dispostas a ajudar:")
        time.sleep(1)
        moldura("a mãe de Emi, Kaori, agora sua aliada, ou arrependida")
        time.sleep(1.2)
        moldura("do que aconteceu antes, oferece o que sabe do culto.")
        time.sleep(1.3)
        moldura("Um historiador que conhece os segredos da região.")
        time.sleep(1.4)
        moldura("Um combatente experiente que perdeu um familiar para o culto.")
        time.sleep(1.5)
        linha()
          
    elif escolha16 == "4":
          
        linha()
        moldura("Você decide não arriscar mais nenhuma vida além da sua")
        time.sleep(1)
        moldura("Ninguém saberá para onde você foi, caso não volte")
        time.sleep(1.2)
        moldura("É a decisão mais solitária que já tomou — e a mais perigosa.")
        time.sleep(1.3)
        linha()
          
    linha()
    moldura("Depois de tentar procurar aliados você volta a sua casa")
    time.sleep(1)
    moldura("Uma visita nortuna:")
    time.sleep(1.2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("A figura revela ser um antigo membro do culto")
    time.sleep(1)
    moldura("Ele oferece informações sobre a estrutura interna da abadia")
    time.sleep(1.2)
    moldura("'- Mas não confie em nada que veja lá', ele avisa.")
    time.sleep(1.3)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você finalmente sente que está pronto. Ou tão pronto quanto pode estar.")
    linha()
    
    linha()
    moldura("FIM DO ATO - 8")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
def ato9():

    linha()
    moldura("COMEÇO DO ATO - 9")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você parte sozinho em direção à floresta.")
    time.sleep(1)
    moldura("O mapa que encontrou leva você para o norte.")
    time.sleep(1.2)
    moldura("Não há ninguém para dividir o peso desta jornada.")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("[1] Rápido e direto")
    moldura("[2] Cautelosa e cuidadosa")
    moldura("[3] Investigativa")
    linha()
    
    escolha19 = input(VERMELHO + "\n              >>> " + RESET)
    
    if escolha19 == "1":
        
        linha()
        moldura("Você avança rapidamente pela floresta. Mas perde marcas importantes.")
        time.sleep(1)
        moldura("Você chega à abadia, mas sem inteligência tática.")
        time.sleep(1.2)
        linha()
        
    elif escolha19 == "2":
        
        linha()
        moldura("Você mapeia cada caminho.")
        time.sleep(1)
        moldura("Você encontra marcas antigas de passagem.")
        time.sleep(1.2)
        moldura("Rituais esquecidos deixaram sinais de sangue.")
        time.sleep(1.3)
        linha()
        
    elif escolha19 == "3":
        
        linha()
        moldura("Em um vilarejo pequeno, você ouve histórias.")
        time.sleep(1)
        moldura("A abadia era um lugar de 'nascimentos especiais'.")
        time.sleep(1.2)
        moldura("Mulheres grávidas desapareciam lá e voltavam... diferentes.")
        time.sleep(1.3)
        linha()
        
    
    linha()
    moldura("Você no meio do caminho encontra uma encruzilhada, o que fazer:")
    linha()

    linha()
    moldura("[1] Caminho óbvio")
    moldura("[2] Marcas antigas invisíveis")
    moldura("[3] Seguir a intuição")
    linha()
    
    escolha20 = input(VERMELHO + "\n              >>> " + RESET)
    
    if escolha20 == "1":
        
        linha()
        moldura("O caminho óbvio leva a uma armadilha.")
        time.sleep(1)
        moldura("Você consegue escapar, mas é uma situação perigosa.")
        time.sleep(1.2)
        linha()
        
    elif escolha20 == "2":
        
        linha()
        moldura("Você segue com precisão as marcas antigas.")
        time.sleep(1)
        moldura("O caminho é mais longo, mas seguro.")
        time.sleep(1.2)
        
    elif escolha20 == "3":
        
        linha()
        moldura("Sua intuição o guia através de um caminho silencioso.")
        time.sleep(1)
        moldura("Você sente estar sendo observado.")
        time.sleep(1.2)
        moldura("Mas ninguém sai dos arbustos.")
        time.sleep(1.3)
        linha()

    linha()
    moldura("FIM DO ATO - 9")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

#================================================================================================================================================================
def ato10():
    
    linha()
    moldura("COMEÇO DO ATO - 10")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("A abadia está diante de você. Seus muros antigos parecem sussurrar segredos.")
    time.sleep(1)
    moldura("Você sente o peso de meses de investigação convergindo neste lugar.")
    time.sleep(1.2)
    linha()
 
    linha()
    moldura("Como você entrarà?")
    moldura("[1] Pela porta principal")
    moldura("[2] Por uma janela destruida")
    moldura("[3] Por um tunel descoberto")
    linha()
 
    entrada_abadia = input(VERMELHO + "\n              >>> " + RESET)
    
    while entrada_abadia not in ["1", "2", "3"]:
        linha()
        moldura("escolha invalida. Escolha entre 1 2 3.")
        linha()
        entrada_abadia = input(VERMELHO + "\n              >>> " + RESET)
        
    if entrada_abadia == "1":
        linha()
        moldura("Você força a entrada. o som ecoa pela abadia")
        time.sleep(1.5)
        linha
        
        limpar()
        
    elif entrada_abadia == "2":
        linha()
        moldura("Você entra silenciosamente. A janela quebrada oferece proteção das sombras.")
        time.sleep(1.5)
        linha()
        
        limpar()
        
    else:
        linha()
        moldura("O tunel é úmido e cheira a morte. Você sente estar se aproximando do coração do culto.")
        time.sleep(1.5)
        linha()
        
        limpar()
        
    linha()
    moldura("Já dentro da abadia, você observa uma camara de meditação, bem próxima")
    time.sleep(1)
    moldura("a um santuario central, marcado como simbolo central")
    time.sleep(1.2)
    moldura("Você ouve passos se aproximando. O culto sabe que Você está aqui. A hora da verdade se aproxima.")
    time.sleep(1.3)
    moldura("Você está diante da verdade escondida há seculos")
    time.sleep(1.4)
    moldura("A marca permanece viva, mas e você.")
    time.sleep(1.5)
    moldura("continuará vivo nessa aventura?")
    time.sleep(1.6)
    linha()
    
    linha()
    moldura("FIM DO ATO - 10")
    linha()
    
    
    input("Pressione ENTER para continuar...")
    limpar()
    
# ===================================================================================================================
def ato11():

    linha()
    moldura("COMEÇO DO ATO - 11")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

    linha()
    moldura("Os passos se aproximam.")
    time.sleep(1)
    moldura("Você permanece escondido atrás de uma das colunas.")
    time.sleep(1.2)
    linha()


    linha()
    moldura("Trẽs figuras encapuzadas aparecem.")
    time.sleep(1.2)
    linha()


    linha()
    moldura("No centro está Edward Blackwood.")
    time.sleep(1.4)
    moldura("O delegado observa o altar no salão e")
    time.sleep(1.4)
    moldura("olha diretamente para você.")
    time.sleep(1.5)
    linha()

    limpar()

    linha()
    moldura("'- Eu sabia que você chegaria até aqui.'")
    time.sleep(1.4)
    linha()

    linha()
    moldura("Em seu rosto, apenas o cansaço evidente.")
    time.sleep(1.5)
    moldura("Blackwood tira o capuz lentamente.)")
    linha()

    linha()
    moldura("'— Durante meses, você procurou respostas.'")
    time.sleep(1.5)
    moldura("'- Encontrou a biblioteca. Encontrou os registros.'")
    time.sleep(1.5)
    moldura("'- Descobriu as famílias'.")
    time.sleep(1.5)
    linha()

    linha()
    moldura("Ele dá alguns passos em sua direção")
    time.sleep(1.5)
    moldura("'- Mas nunca entendeu o que estava procurando.'")
    time.sleep(1.5)
    linha()

    linha()
    moldura("Você apontou a arma para ele e pergunta: ")
    time.sleep(1.2)
    moldura("'- Você matou Emi?'")
    time.sleep(1.4)
    linha()

    linha()
    time.sleep(1.2)
    moldura("Blackwood fica em silêncio por segundos...")
    time.sleep(1.5)
    linha()

    limpar()

    linha()
    time.sleep(1.2)
    moldura("- Não.")
    time.sleep(1.3)
    linha()

    linha()
    time.sleep(1.2)
    moldura("'- Então quem a matou?' - você pergunta.")
    time.sleep(1.4)
    moldura("Blackwood olha para a passagem atrás do altar.")
    time.sleep(1.4)
    linha()

    linha()
    time.sleep(1.4)
    moldura("- A mesma coisa que matous os outros primogênitos.")
    time.sleep(1.4)
    moldura("Um dos encapuzados acende uma tocha.")
    time.sleep(1.4)
    linha()

    linha()
    time.sleep(1.4)
    moldura("Você enxerga uma escadaria descendo ainda mais.")
    time.sleep(1.4)
    moldura("Blackwood continua:")
    time.sleep(1.4)
    linha()

    linha()
    time.sleep(1.4)
    moldura("'- Nós não escolhemos quem recebe A Marca'.")
    time.sleep(1.4)
    moldura("'- A Marca escolhe.'")
    time.sleep(1.4)
    linha()

    limpar()

    linha()
    time.sleep(1.4)
    moldura("Você se lembra das palavras no grimório: ")
    time.sleep(1.4)
    moldura("'A Marca escolhe seus portadores através dos tempos'")
    time.sleep(1.4)
    moldura("Agora aquilo fazia sentido.")
    time.sleep(1.4)
    linha()

    linha()
    time.sleep(1.4)
    moldura("As vítimas não eram escolhidas aleatóriamente.")
    time.sleep(1.4)
    linha()

    limpar()

    linha()
    time.sleep(1.4)
    moldura("Whitmore, Lancaster, Hawthorne e agora, Emi.")
    time.sleep(1.4)
    linha()

    linha()
    time.sleep(1.4)
    moldura("Você pergunta: '- E Aurelius?'")
    time.sleep(1.4)
    moldura("'- Está esperando você!'")
    time.sleep(1.4)
    linha()
    time.sleep(0.5)

    limpar()

    linha()
    moldura("Nesse momento um dos encapuzados avança. E agora?")
    moldura("[1] Enfrentar os membros do culto.")
    moldura("[2] Seguir Blackwood sem lutar.")
    moldura("[3] Tentar fugir.")
    linha()

    acao_encapuzados = input(VERMELHO + "\n              >>> " + RESET)

    while acao_encapuzados not in ["1", "2", "3"]:
        linha()
        moldura("Opção inválida.")
        linha()
        acao_encapuzados = input(VERMELHO + "\n              >>> " + RESET)

    if acao_encapuzados == "1":
        linha()
        time.sleep(1.5)
        moldura("Você parte pra cima antes que eles possam")
        time.sleep(1.5)
        moldura("te cercar. A luta é rápida e brutal. Um deles")
        time.sleep(1.5)
        moldura("acaba caìdo, outro foge pela passagem junto")
        time.sleep(1.5)
        moldura("de Blackwood. Você vai atrás deles também.")
        linha()

        limpar()

    elif acao_encapuzados == "2":
        linha()
        time.sleep(1.5)
        moldura("Você destrai os cultistas com um barulho atrás")
        time.sleep(1.5)
        moldura("deles, enquanto corre pela passagem atrás de")
        time.sleep(1.5)
        moldura("Blackwood. Agora você está indo ao centro de tudo.")
        time.sleep(1.5)
        linha()

        limpar()
    else:
        linha()
        time.sleep(1.5)
        moldura("Ao tentar fugir, você é cercado pelos cultistas.")
        time.sleep(1.5)
        moldura("Sozinho, você morre, sem descobrir a verdade e")
        time.sleep(1.5)
        moldura("sem ajudar as famílias da cidade por ser covarde.")
        time.sleep(1.5)
        linha()
        time.sleep(1.5)
        game_over()

    linha()
    time.sleep(1.5)
    moldura("Você desce toda escadaria e uma porta de pedra surge.")
    time.sleep(1.5)
    moldura("Do outro lado, alguém começa a bater. Uma, duas, TRÊS VEZES.")
    time.sleep(1.5)
    linha()

    linha()
    time.sleep(1.5)
    moldura("Então, uma vez antiga sussura: ")
    time.sleep(1.5)
    linha()

    linha()
    time.sleep(1.5)
    moldura("'- Finalmente.' - E a porta começa a se abrir.")
    time.sleep(1.5)
    linha()

    linha()
    moldura("FIM DO ATO - 11")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

def ato12():

    linha()
    moldura("COMEÇO DO ATO - 12")
    linha()

    input("Pressione ENTER para começar...")
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("Você entra em uma sala circular.")
    time.sleep(1.5)
    moldura("Diferente das outras partes da abadia, aquele lugar está perfeitamente preservado.")
    time.sleep(1.5)
    moldura("No centro existe um grande círculo feito de pedra.")
    time.sleep(1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("Ao redor dele estão dezenas de nomes gravados nas paredes.")
    time.sleep(1.5)
    moldura("Samuel Whitmore")
    time.sleep(1.5)
    moldura("Geoffrey Hawthorne.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("O filho desaparecido dos Lancaster")
    time.sleep(1.5)
    moldura("E mais abaixo...")
    time.sleep(2.5)
    moldura("Emi.")
    time.sleep(1.5)
    linha()

    linha()
    time.sleep(1.5)
    moldura("Seu sangue gela.")
    time.sleep(1.5)
    moldura("Ao lado do nome dela existe uma data.")
    time.sleep(1.5)
    moldura("A mesma data da sua morte.")
    time.sleep(1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("Você entende.")
    time.sleep(1.5)
    moldura("O culto ja sabia que Emi seria sacraficada muito antes de Você chegar á vila.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Então uma voz surge atrás de Você")
    time.sleep(1.5)
    moldura("'- Não foi o culto que escolheu Emi'.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Você se vira.")
    time.sleep(1.5)
    moldura("Blackwood está parado diante da porta.")
    time.sleep(1.5)
    moldura("'- Foi Aurelius'.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Você pergunta:")
    time.sleep(1.5)
    moldura("'- Onde ele está?'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Blackwood aponta para o centro da sala.")
    time.sleep(1.5)
    moldura("'- Aqui.'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("O circulo de pedra começa a emitir uma luz fraca.")
    time.sleep(1.5)
    moldura("Uma figura aparece dentro dele.")
    time.sleep(1.5)
    linha()
    time.sleep(1.5)
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("sua pele está marcada por simbolos.")
    time.sleep(1.5)
    moldura("mas seus olhos permancem vivos.")
    time.sleep(1.5)
    moldura("'- Aurelius...'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("O homem sorri.")
    time.sleep(1.5)
    moldura("'- Meu nome sobreviveu por séculos'.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Você levanta a arma: ")
    time.sleep(1.5)
    moldura("'- Você é responsavel por todos aqueles assasinatos?'")
    time.sleep(1.5)
    moldura("'- Não'.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Aurelius responde calmamente.")
    time.sleep(1.5)
    moldura("'- Eu sou responsavel pelo primeiro'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Ele explica que, séculos atrás, buscou uma forma de escapar da morte.")
    time.sleep(1.5)
    moldura("O ritual funcionou apenas parcialmente.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Seu corpo continuou vivo, mas o ritual exigia sangue de pessoas pertences")
    time.sleep(1.5)
    moldura("as linhagens ligadas á fundação da vila.")
    time.sleep(1.5)
    moldura("As familias descobriram o segredo.")
    time.sleep(1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("Em vez de destruir Aurelius, fizeram um acordo.")
    time.sleep(1.5)
    moldura("Cada geração entregaria seus primogênitos quando a Marca surgisse.")
    time.sleep(1.5)
    moldura("Em troca, suas familias permaneceriam protegidas e a vila continuaria prosperando.")
    time.sleep(1.5)
    linha()

    linha()
    time.sleep(1.5)
    moldura("Foi assim que os assasinatos começaram.")
    time.sleep(1.5)
    moldura("Você pergunta:")
    time.sleep(1.5)
    moldura("'- Então as familias sabiam?'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Aurelius responde:")
    time.sleep(1.5)
    moldura("'- Algumas sabiam. Outras apenas obedeciam. E algumas tentaram fugir.'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Os Lancaster foram os primeiros a tentar quebrar o acordo.")
    time.sleep(1.5)
    moldura("Por isso seu primogênitos desapareceu.")
    time.sleep(1.5)
    moldura("Ele não morreu.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Foi levado para a abadia.")
    time.sleep(1.5)
    moldura("Mantido vivo como parte do ritual.")
    time.sleep(1.5)
    linha()

    linha()
    time.sleep(1.5)
    moldura("Você sente raiva crescer.")
    time.sleep(1.5)
    moldura("'- E Emi?'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Aurelius olha para o nome dela.")
    time.sleep(1.5)
    moldura("'- Emi foi a próxima.'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Blackwood abaixa a cabeça.")
    time.sleep(1.5)
    moldura("'- Kaori tentou impedir.'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Você imediatamente pensa nela.")
    time.sleep(1.5)
    moldura("Aurelius continua:")
    time.sleep(1.5)
    moldura("'- Ela participou do culto durante anos. Mas quando percebeu que a própria filha")
    time.sleep(1.5)
    moldura("havia sido escolhida, tentou quebrar o ciclo.'")
    time.sleep(1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("Isso explica o comportamento de Kaori")
    time.sleep(1.5)
    moldura("Ela não era simplesmente.")
    time.sleep(1.5)
    moldura("Era alguém pressa dentro de um sistema que ajudou a manter vivo.")
    time.sleep(1.5)
    linha()

    linha()
    time.sleep(1.5)
    moldura("Aurelius se aproxima.")
    time.sleep(1.5)
    moldura("'- Você acredita que pode destruir tudo isso?'")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Você responde:")
    time.sleep(1.5)
    moldura("'- Sim'.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("Ele sorri.")
    time.sleep(1.5)
    moldura("'- Então descubra primeiro onde está a chave'.")
    time.sleep(1.5)
    linha()
    
    linha()
    time.sleep(1.5)
    moldura("atrás dele, uma parede se abre.")
    time.sleep(1.5)
    moldura("Um pequeno corredor aparece.")
    time.sleep(1.5)
    moldura("Na parede existe uma inscrição:")
    time.sleep(1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    linha()
    time.sleep(1.5)
    moldura("'Aquele que conhece a verdade deve decidir o destino das familias'.")
    time.sleep(1.5)
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    time.sleep(1.5)
    moldura("Blackwood olha para Você.")
    time.sleep(1.5)
    moldura("'- È por isso que Você foi trazido até aqui'.")
    time.sleep(1.5)
    linha()
    
    linha()
    moldura("Você percebe algo terrivel.")
    time.sleep(1.5)
    moldura("Sua investigação nunca foi apenas uma investigação.")
    time.sleep(1.5)
    moldura("O culto estava guiando você desde o começo.")
    time.sleep(1.5)
    linha()
    
    linha()
    moldura("FIM DO ATO - 12")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()

def ato13():

    linha()
    moldura("COMEÇO DO ATO - 13")
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você atravessa o corredor")
    time.sleep (1)
    moldura("Blackwood tenta impedir sua passagem")
    time.sleep (1.2)
    moldura("Mas você consegue escapar e segue sozinho")
    time.sleep (1.3)
    moldura("O corredor termina em uma pequena sala escondida")
    time.sleep (1.4)
    moldura("Sobre uma mesa existem documentos, mapas e cartas.")
    time.sleep (1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Entre eles, você encontra um mapa antigo de Ravenscroft.")
    time.sleep (1)
    moldura("Algumas áreas estão marcadas com tinta vermelha.")
    time.sleep (1.2)
    moldura("Uma delas chama sua atenção.")
    time.sleep (1.3)
    moldura("Uma pequena sala escondida atrás dos antigos aposentos reais.")
    time.sleep (1.4)
    moldura("Ao lado do mapa existe uma anotação:")
    time.sleep (1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("'Somente o conselheiro conhece a localização da chave.'")
    time.sleep (1)
    moldura("Você lembra das histórias antigas sobre a vila.")
    time.sleep (1.2)
    moldura("Havia um conselheiro que desapareceu décadas atrás.")
    time.sleep (1.3)
    moldura("Seu nome era Elias Vane.")
    time.sleep (1.4)
    moldura("Oficialmente, ele havia abandonado Ravenscroft.")
    time.sleep (1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Mas os documentos mostram outra coisa.")
    time.sleep (1)
    moldura("Elias descobriu a existência de Aurelius.")
    time.sleep (1.2)
    moldura("Tentou destruir os registros.")
    time.sleep (1.3)
    moldura("E desapareceu antes de conseguir.")
    time.sleep (1.4)
    moldura("Você encontra outra folha.")
    time.sleep (1.5)
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Nela está escrita uma frase:")
    time.sleep (1)
    moldura("'Se eu desaparecer, procurem-me onde os mortos não podem ser enterrados'")
    time.sleep (1.2)
    moldura("Você entende a pista.")
    time.sleep (1.3)
    moldura("A antiga cripta da vila.")
    time.sleep (1.4)
    moldura("Você sai da sala e retorna pelos corredores da abadia.")
    time.sleep (1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("No caminho, encontra uma porta escondida.")
    time.sleep (1)
    moldura("Atrás dela existe uma passagem subterrânea que leva para fora da abadia.")
    time.sleep (1.2)
    moldura("Você segue o caminho.")
    time.sleep (1.3)
    moldura("Horas depois, chega à antiga cripta.")
    time.sleep (1.4)
    moldura("A porta está aberta.")
    time.sleep (1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você entra.")
    time.sleep (1.2)
    moldura("No fundo da cripta encontra uma cela.")
    time.sleep (1.3)
    moldura("E dentro dela está Elias Vane.")
    time.sleep (2)
    moldura("Muito mais velho do que você imaginava.")
    time.sleep (2.3)
    moldura("Mas vivo.")
    time.sleep (2.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Ele ergue os olhos.")
    time.sleep (1.2)
    moldura("' — Então finalmente alguém veio'.")
    time.sleep (1.3)
    moldura("Você explica o que descobriu.")
    time.sleep (1.4)
    moldura("Elias escuta em silêncio.")
    time.sleep (1.5)
    moldura("Quando você menciona Aurelius, ele demonstra medo.")
    time.sleep (1.6)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("' — Ele ainda está vivo?' ")
    time.sleep (1.2)
    moldura("você confirma.")
    time.sleep (1.3)
    moldura("Elias respira fundo.")
    time.sleep (1.4)
    moldura("' — Então o ciclo ainda não acabou'.")
    time.sleep (1.5)
    moldura("Ele conta que existe uma maneira de destruir Aurelius.")
    time.sleep (1.6)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Mas o ritual precisa ser interrompido no momento exato")
    time.sleep (1.2)
    moldura("em que a Marca é transferida.")
    time.sleep (1.3)
    moldura("Você pergunta:")
    time.sleep (1.4)
    moldura("'— Como?'")
    time.sleep (1.5)
    moldura("Elias aponta para um pequeno compartimento na parede.")
    time.sleep (1.6)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Dentro existe uma chave de pedra.")
    time.sleep (1.3)
    moldura("'— Essa é a chave.'")
    time.sleep (1.4)
    moldura("Você a segura.")
    time.sleep (1.5)
    moldura("Ela possui o mesmo símbolo encontrado na adaga do primeiro ato.")
    time.sleep (1.6)
    moldura("Elias continua:")
    time.sleep (1.7)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("'— A Marca não é apenas uma maldição.'")
    time.sleep (1.2)
    moldura("'— É um vínculo.'")
    time.sleep (1.3)
    moldura("'— Enquanto Aurelius estiver ligado às famílias, ele não poderá morrer.'")
    time.sleep (1.4)
    moldura("Você pergunta:")
    time.sleep (1.5)
    moldura("'— E como quebramos o vínculo?'")
    time.sleep (1.6)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Elias responde:")
    time.sleep (1.2)
    moldura("'— Destruindo o lugar onde o primeiro pacto foi feito.'")
    time.sleep (1.3)
    moldura("Você entende imediatamente.")
    time.sleep (1.4)
    moldura("A sala onde Aurelius está.")
    time.sleep (1.5)
    moldura("O centro da abadia.")
    time.sleep (1.6)
    moldura("Elias entrega a você um último documento.")
    time.sleep (1.7)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Nele estão os nomes das três famílias.")
    time.sleep (1.2)
    moldura("No final existe uma quarta assinatura.")
    time.sleep (1.3)
    moldura("A assinatura de Aurelius.")
    time.sleep (1.4)
    moldura("Mas há algo estranho.")
    time.sleep (1.5)
    moldura("Abaixo dela existe outra assinatura.")
    time.sleep (1.9)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Kaori.")
    time.sleep (1.4)
    moldura("Você fica em silêncio.")
    time.sleep (1.5)
    moldura("Elias percebe sua expressão.")
    time.sleep (1.6)
    moldura("'— Ela tentou quebrar o pacto.'")
    time.sleep (1.7)
    moldura("'— Mas chegou tarde demais.'")
    time.sleep (1.8)
    moldura("Ao longe, você ouve sinos.")
    time.sleep (1.9)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("A cerimônia começou.")
    time.sleep (1.5)
    moldura("Você guarda a chave.")
    time.sleep (1.6)
    moldura("Agora sabe exatamente o que precisa fazer.")
    time.sleep (1.7)
    moldura("Voltar para a abadia.")
    time.sleep (1.8)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    linha()
    moldura("FIM DO ATO - 13")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    
def ato14():
    
    linha()
    moldura("COMEÇO DO ATO - 14")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você retorna à abadia durante a noite")
    time.sleep(1)
    moldura("O lugar está completamente iluminado por tochas.")
    time.sleep(1.2)
    moldura("Centenas de velas cercam o santuário")
    time.sleep(1.3)
    moldura("Os membros do culto estão reunidos")
    time.sleep(1.4)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("No centro está Aurelius")
    time.sleep(1)
    moldura("Blackwood está ao lado dele")
    time.sleep(1.2)
    moldura("E Kaori também")
    time.sleep(1.3)
    moldura("Quando ela vê Você, seus olhos se enchem de lágrimas")
    time.sleep(1.4)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("'- Você não deveria estar aqui'")
    time.sleep(1)
    linha()
    
    linha()
    moldura("Você respode:")
    time.sleep(1)
    moldura("'- Eu descobri tudo'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Kaori abaixa a cabeça")
    time.sleep(1)
    moldura("'- Então sabe o porquê tentei impedir Emi'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Aurelius ergue a mão.")
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("Todos ficam em silêncio")
    time.sleep(1)
    moldura("'- O último descendente chegou'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Você percebe que ele está olhando para Você")
    time.sleep(1)
    moldura("A marca começa a aparecer em sua mão")
    time.sleep(1.2)
    moldura("Você sente uma dor intensa")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("Aurelius sorri:")
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("'- A investigação trouxe Você até mim'")
    time.sleep(1)
    moldura("Você entende a verdadeira armadilha")
    time.sleep(1.2)
    moldura("A marca não estava apenas procurando vitimas")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("Ela estava procurando alguém capaz de substituir Aurelius")
    time.sleep(1)
    moldura("Você foi conduzido até ali porque era o próximo recipiente")
    time.sleep(1.2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Blackwood se aproxima:")
    time.sleep(1)
    moldura("'- Se aceitar, tudo termina'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Você pergunta:")
    time.sleep(1)
    moldura("'- E as familías'")
    time.sleep(1.2)
    moldura("'- Livres'")
    time.sleep(1.3)
    moldura("'- E as mortes?'")
    time.sleep(1.4)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("Blackwood hesita")
    time.sleep(1)
    moldura("'- Também terminam'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Aurelius completa")
    time.sleep(1)
    moldura("'- Você pode acabar com séculos de sofrimento'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Kaori grita:")
    time.sleep(1)
    moldura("'- NÂO ESCUTE ELES!'")
    time.sleep(1.2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Blackwood tenta segurá-la")
    time.sleep(1.2)
    moldura("Você percebe que Kaori está carregando um pequeno frasco")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("Ela olha para você")
    time.sleep(1)
    moldura("'- É o sangue da Emi'")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("Você entende.")
    time.sleep(1)
    moldura("Kaori guardou uma última parte da filha")
    time.sleep(1.2)
    linha()
    
    linha()
    moldura("O sangue de Emi pode interromper o ritual porque ela foi a última.")
    time.sleep(1)
    moldura("A última escolhida pela marca")
    time.sleep(1.2)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("Você olha para a chave de pedra.")
    time.sleep(1)
    moldura("Depois para o circulo")
    time.sleep(1.2)
    moldura("e finalmente para Aurelius")
    time.sleep(1.3)
    moldura("Você sabe o que precisa fazer.")
    time.sleep(1.4)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("[1] Destruir o circulo")
    moldura("[2] Usar o sangue de Emi")
    moldura("[3] Aceitar a Marca")
    linha()
    
    escolhaato4 = input(VERMELHO + "\n              >>> " + RESET)
    
    if escolhaato4 == "1":
        
        linha()
        moldura("Você coloca a chave no centro do altar.")
        time.sleep(1)
        moldura("O simbolo começa a rachar")
        time.sleep(1.2)
        moldura("Aurelius grita.")
        time.sleep(1.3)
        linha()
        
        linha()
        moldura("Os membros do culto entram em pânico")
        time.sleep(1)
        moldura("As paredes da abadia começam a tremer.")
        time.sleep(1.2)
        linha()
        
        input("Pressione ENTER para continuar...")
        limpar()
        
        linha()
        moldura("Blackwood tenta impedir você")
        time.sleep(1)
        moldura("Kaori o enfrenta.")
        time.sleep(1.2)
        moldura("Você gira a chave")
        time.sleep(1.2)
        linha()
        
        linha()
        moldura("O circulo se parte.")
        time.sleep(1)
        moldura("Uma onda de energia atravessa a sala.")
        time.sleep(1.2)
        moldura("A marca em sua mão desaparece")
        time.sleep(1.3)
        linha()
        
        input("Pressione ENTER para continuar...")
        
        limpar()
        
        linha()
        moldura("Aurelius cai de joelhos.")
        time.sleep(1)
        moldura("Pela a primera vez em séculos ele parece verdadeiramente velho")
        time.sleep(1.2)
        linha()
        
    elif escolhaato4 == "2":
        
        linha()
        moldura("Kaori entrega o frasco.")
        time.sleep(1)
        moldura("Você derrama o sangue dentro do circulo.")
        time.sleep(1.2)
        moldura("A marca começa a desaparecer dos nomes gravados nas paredes.")
        time.sleep(1.3)
        linha()
        
        linha()
        moldura("Os membros das famílias começam a gritar.")
        time.sleep(1)
        moldura("Aurelius tenta impedir o ritual,")
        time.sleep(1.2)
        moldura("mas já é tarde.")
        time.sleep(1.3)
        moldura("O vínculo está sendo quebrado.")
        time.sleep(1.4)
        linha()
        
    elif escolhaato4 == "3":
        
        linha()
        moldura("Você aceita o vinculo")
        time.sleep(1)
        moldura("A dor desaparece.")
        time.sleep(1.2)
        moldura("Aurelius fecha os olhos")
        time.sleep(1.3)
        moldura("Durante alguns segundos, tudo fica em silêncio")
        time.sleep(1.4)
        linha()
        
        input("Pressione ENTER para continuar...")
        
        limpar()
        
        linha()
        moldura("Então Você percebe algo.")
        time.sleep(1)
        moldura("Aurelius começa a desaparecer.")
        time.sleep(1.2)
        moldura("Mas a marca permanece em você")
        time.sleep(1.3)
        moldura("Você se tornou o novo guardião")
        time.sleep(1.4)
        linha()
        
        linha()
        moldura("Kaori olha para voce horrorizada")
        time.sleep(1)
        moldura("Você percebe que venceu Aurelius.")
        time.sleep(1.2)
        moldura("Mas não destrui o ciclo.")
        time.sleep(1.3)
        linha()

        limpar()
        game_over()
    else:
        print("Opção inválida")
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("A abadia interira começa a desmoronar")
    time.sleep(1)
    moldura("Kaori permanece ao seu lado")
    time.sleep(1.2)
    moldura("'- VAMOS!'")
    time.sleep(1.3)
    linha()
    
    linha()
    moldura("Vocês correm")
    time.sleep(1)
    moldura("Atrás de Vocês, o coração da abadia desaparece sob toneladas de pedra")
    time.sleep(1.2)
    moldura("Quando chegam ao lado de fora, o silêncio toma conta da floresta")
    time.sleep(1.3)
    linha()
    
    input("Pressione ENTER para continuar...")
    
    limpar()
    
    linha()
    moldura("Não há vozes.")
    time.sleep(1)
    moldura(" Não há rituais.")
    time.sleep(1.2)
    moldura(" A marca em sua mão desapareceu")
    time.sleep(1.3)
    moldura("Mas ainda falta uma coisa.")
    time.sleep(1.4)
    moldura("Blackwood...")
    time.sleep(1.5)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("FIM DO ATO - 14")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
def ato15():
    
    linha()
    moldura("COMEÇO DO ATO - 15")
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    
    linha()
    moldura("Você retorna a Ravenscroft ao amanhecer.")
    time.sleep (1.5)
    moldura("A vila está diferente.")
    time.sleep (1.6)
    moldura("As pessoas começam a sair de suas casas.")
    time.sleep (1.7)
    moldura("Ninguém sabe exatamente o que aconteceu.")
    time.sleep (1.8)
    moldura("Mas todos sentem que alguma coisa mudou.")
    time.sleep (1.9)
    moldura("Blackwood não está mais na delegacia.")
    time.sleep (2)
    linha()

    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você o encontra na praça central.")
    time.sleep (1.5)
    moldura("Ele está sentado sozinho.")
    time.sleep (1.6)
    moldura("Sem o uniforme.")
    time.sleep (1.7)
    moldura("Sem armas.")
    time.sleep (1.8)
    moldura("Sem o símbolo do culto.")
    time.sleep (1.9)
    moldura("Você aponta sua arma.")
    time.sleep (2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("'— Acabou'.")
    time.sleep (1.5)
    moldura("Blackwood olha para você.")
    time.sleep (1.6)
    moldura("'— Sim'.")
    time.sleep (1.7)
    moldura("Você pergunta:")
    time.sleep (1.8)
    moldura("'— Quantas pessoas morreram?'")
    time.sleep (1.9)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Ele não responde.")
    time.sleep (1.5)
    moldura("Você insiste.")
    time.sleep (1.6)
    moldura("'— Quantas?'")
    time.sleep (1.7)
    moldura("Blackwood fecha os olhos.")
    time.sleep (1.8)
    moldura("'— Cento e vinte e sete'.")
    time.sleep (1.9)
    moldura("O silêncio pesa.")
    time.sleep (2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("'— E por quê?'")
    time.sleep (1.5)
    moldura("'— Porque acreditávamos que era necessário'.")
    time.sleep (1.6)
    moldura("Você olha para ele com desprezo.")
    time.sleep (1.7)
    moldura("'— Não era.'")
    time.sleep (1.8)
    moldura("Blackwood aceita as algemas sem resistência.")
    time.sleep (1.9)
    moldura("Antes de ser levado, ele pergunta:")
    time.sleep (2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("'— Aurelius morreu?'")
    time.sleep (1.5)
    moldura("Você olha para a floresta.")
    time.sleep (1.6)
    moldura("'— Sim'.")
    time.sleep (1.7)
    moldura("Blackwood sorri fracamente.")
    time.sleep (1.8)
    moldura("'— Então talvez tenhamos uma chance'.")
    time.sleep (1.9)
    moldura("Kaori se aproxima.")
    time.sleep (2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você não diz nada.")
    time.sleep (1,5)
    moldura("Ela também não.")
    time.sleep (1.6)
    moldura("Apenas olha para a filha pela última vez.")
    time.sleep (1.7)
    moldura("Os nomes dos antigos mortos são retirados dos registros secretos.")
    time.sleep (1,8)
    moldura("Os documentos das famílias são entregues às autoridades.")
    time.sleep (1.9)
    moldura("A verdade sobre Ravenscroft finalmente vem à tona.")
    time.sleep (2)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("As famílias Whitmore, Lancaster e Hawthorne não")
    time.sleep (1.5)
    moldura("são mais obrigadas a obedecer ao antigo pacto.")
    time.sleep (1.6)
    moldura("O culto desaparece.")
    time.sleep (1.7)
    moldura("E a abadia permanece em ruínas.")
    time.sleep (1.8)
    moldura("Sem Aurelius.")
    time.sleep (1.9)
    moldura("Sem a Marca.")
    time.sleep (2)
    linha()
    
    input("Pressionbe ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Sem sacrifícios.")
    time.sleep (1.5)
    moldura("Dias depois, você volta à mansão de Emi.")
    time.sleep (1.6)
    moldura("O quarto dela permanece exatamente como estava.")
    time.sleep (1.7)
    moldura("Sobre a mesa existe o colar quebrado encontrado")
    time.sleep (1.8)
    moldura("no primeiro dia da investigação.")
    time.sleep (1.9)
    linha()
    
    input("Pressione ENTER para continuar...")
    limpar()
    
    linha()
    moldura("Você o segura.")
    time.sleep (1.5)
    moldura("Agora entende por que aquela pequena peça parecia tão importante.")
    time.sleep (1.6)
    moldura("Emi não era apenas uma vítima.")
    time.sleep (1.7)
    linha()

    linha()
    moldura("Ela foi a última pessoa que")
    time.sleep(1)
    moldura("tentou quebrar o ciclo antes de você.")
    time.sleep(1.2)
    linha()
    

    linha()
    moldura("Você coloca o colar sobre a mesa.")
    time.sleep(1)
    moldura("Então escuta passos atrás de você...")
    time.sleep(1.2)
    linha()

    input("Pressione ENTER para continuar...")

    limpar()

    linha()
    moldura("É Kaori.")
    linha()

    linha()
    moldura("'- Obrigada'.")
    time.sleep(1)
    moldura("Você pergunta: ")
    time.sleep(1.2)
    moldura("'- Pelo quê?'")
    moldura("Ela olha para o quarto. '- Por ter dado à")
    time.sleep(1.3)
    moldura("minha filha uma chance de ser lembrada como")
    time.sleep(1.4)
    moldura("mais do que uma vítima'.")
    time.sleep(1.5)
    linha()

    linha()
    moldura("Você não responde. Apenas fecha a porta.")
    time.sleep(1)
    moldura("Quando sai da mansão, o sol começa a nascer")
    time.sleep(1.2)
    moldura("sobre Ravenscroft.")
    time.sleep(1.3)
    moldura("Pela primeira vez desde que chegou à vila,")
    time.sleep(1.4)
    moldura("não existe medo.")
    time.sleep(1.5)
    linha()

    linha()
    moldura("Nenhum símbolo aparece nas paredes.")
    time.sleep(1)
    moldura("Nenhum corpo é encontrado.")
    time.sleep(1.2)
    moldura("Nenhum sino toca durante a madrugada.")
    time.sleep(1.3)
    linha()

    linha()
    moldura("A Marca desapareceu.")
    linha()

    linha()
    moldura("E Aurelius finalmente morreu.")
    linha()

    linha()
    moldura("Mas, antes de deixar a vila, você encontra")
    moldura("uma última coisa...")
    time.sleep(1.2)
    linha()

    linha()
    moldura("No chão da antiga abadia existe uma pequena")
    time.sleep(1)
    moldura("pedra negra. Você a pega.")
    time.sleep(1.2)
    moldura("Por um instante, vê uma marca muito fraca nela.")
    time.sleep(1.3)
    linha()
    

    linha()
    moldura("Então a pedra se desfaz em pó entre seus dedos.")
    time.sleep(1)
    moldura("Você entende. O ciclo terminou, de verdade.")
    time.sleep(1.2)
    linha()

    linha()
    moldura("Você olha para a vila uma última vez. Depois,")
    time.sleep(1)
    moldura("segue o seu caminho. Tudo acabou, a verdade")
    time.sleep(1.2)
    moldura("foi descoberta. E os mortos finalmente podem descansar.")
    time.sleep(1.3)
    linha()

    linha()
    moldura("FIM.")
    linha()
    
    input("Pressione enter para terminar a investigação...")
    limpar()
    
#================================================================================================================================================================
# PRIMEIRA TELA

def bem_vindo():

    limpar()

    linha()

    fundo()

    moldura("██████╗ ███████╗███╗   ███╗", CIANO)
    moldura("██╔══██╗██╔════╝████╗ ████║", CIANO)
    moldura("██████╔╝█████╗  ██╔████╔██║", CIANO)
    moldura("██╔══██╗██╔══╝  ██║╚██╔╝██║", CIANO)
    moldura("██████╔╝███████╗██║ ╚═╝ ██║", CIANO)
    moldura("╚═════╝ ╚══════╝╚═╝     ╚═╝", CIANO)

    moldura()

    moldura("██╗   ██╗██╗███╗   ██╗██████╗  ██████╗ ", CIANO)
    moldura("██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗", CIANO)
    moldura("██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║", CIANO)
    moldura("╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║", CIANO)
    moldura(" ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝", CIANO)
    moldura("  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ", CIANO)
    
    moldura()
    
    moldura(" █████╗  ██████╗          ██╗ ██████╗  ██████╗  ██████╗ ", CIANO)
    moldura("██╔══██╗██╔═══██╗         ██║██╔═══██╗██╔════╝ ██╔═══██╗", CIANO)
    moldura("███████║██║   ██║         ██║██║   ██║██║  ███╗██║   ██║", CIANO)
    moldura("██╔══██║██║   ██║    ██   ██║██║   ██║██║   ██║██║   ██║", CIANO)
    moldura("██║  ██║╚██████╔╝    ╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝", CIANO)
    moldura("╚═╝  ╚═╝ ╚═════╝      ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝ ", CIANO)

    fundo()

    linha()

    time.sleep(3)


#  TITULO

def titulo():

    glitch("A MARCA DO ASSASSINO")

    limpar()

    linha()

    fundo()

    moldura(" █████╗ ", VERMELHO)
    moldura("██╔══██╗", VERMELHO)
    moldura("███████║", VERMELHO)
    moldura("██╔══██║", VERMELHO)
    moldura("██║  ██║", VERMELHO)

    moldura()

    moldura("███╗   ███╗ █████╗ ██████╗  ██████╗ █████╗ ", VERMELHO)
    moldura("████╗ ████║██╔══██╗██╔══██╗██╔════╝██╔══██╗", VERMELHO)
    moldura("██╔████╔██║███████║██████╔╝██║     ███████║", VERMELHO)
    moldura("██║╚██╔╝██║██╔══██║██╔══██╗██║     ██╔══██║", VERMELHO)
    moldura("██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╗██║  ██║", VERMELHO)
    
    moldura()
    
    moldura("██████╗  ██████╗ ", VERMELHO)
    moldura("██╔══██╗██╔═══██╗", VERMELHO)
    moldura("██║  ██║██║   ██║", VERMELHO)
    moldura("██║  ██║██║   ██║", VERMELHO)
    moldura("██████╔╝╚██████╔╝", VERMELHO)
    moldura("╚═════╝  ╚═════╝ ", VERMELHO)
    
    moldura()
    
    moldura(" █████╗ ███████╗███████╗ █████╗ ███████╗███████╗██╗███╗   ██╗ ██████╗ ", VERMELHO)
    moldura("██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║████╗  ██║██╔═══██╗", VERMELHO)
    moldura("███████║███████╗███████╗███████║███████╗███████╗██║██╔██╗ ██║██║   ██║", VERMELHO)
    moldura("██╔══██║╚════██║╚════██║██╔══██║╚════██║╚════██║██║██║╚██╗██║██║   ██║", VERMELHO)
    moldura("██║  ██║███████║███████║██║  ██║███████║███████║██║██║ ╚████║╚██████╔╝", VERMELHO)
    
    moldura()

    moldura()

    moldura()

    moldura("PRODUZIDO POR 2D", BRANCO)

    fundo()

    linha()

    time.sleep(3)


# MENU

def menu():

    while True:

        limpar()

        linha()

        fundo()

        moldura(" █████╗ ", VERMELHO)
        moldura("██╔══██╗", VERMELHO)
        moldura("███████║", VERMELHO)
        moldura("██╔══██║", VERMELHO)
        moldura("██║  ██║", VERMELHO)

        moldura()
        
        moldura("███╗   ███╗ █████╗ ██████╗  ██████╗ █████╗ ", VERMELHO)
        moldura("████╗ ████║██╔══██╗██╔══██╗██╔════╝██╔══██╗", VERMELHO)
        moldura("██╔████╔██║███████║██████╔╝██║     ███████║", VERMELHO)
        moldura("██║╚██╔╝██║██╔══██║██╔══██╗██║     ██╔══██║", VERMELHO)
        moldura("██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╗██║  ██║", VERMELHO)
        
        moldura()
        
        moldura("██████╗  ██████╗ ", VERMELHO)
        moldura("██╔══██╗██╔═══██╗", VERMELHO)
        moldura("██║  ██║██║   ██║", VERMELHO)
        moldura("██║  ██║██║   ██║", VERMELHO)
        moldura("██████╔╝╚██████╔╝", VERMELHO)
        moldura("╚═════╝  ╚═════╝ ", VERMELHO)
        
        moldura()
        
        moldura(" █████╗ ███████╗███████╗ █████╗ ███████╗███████╗██╗███╗   ██╗ ██████╗ ", VERMELHO)
        moldura("██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██║████╗  ██║██╔═══██╗", VERMELHO)
        moldura("███████║███████╗███████╗███████║███████╗███████╗██║██╔██╗ ██║██║   ██║", VERMELHO)
        moldura("██╔══██║╚════██║╚════██║██╔══██║╚════██║╚════██║██║██║╚██╗██║██║   ██║", VERMELHO)
        moldura("██║  ██║███████║███████║██║  ██║███████║███████║██║██║ ╚████║╚██████╔╝", VERMELHO)

        moldura()

        moldura(random.choice(frases), CINZA)

        moldura()

        moldura("[ 1 ] JOGAR", BRANCO)
        moldura("[ 2 ] TUTORIAL", BRANCO)
        moldura("[ 3 ] SAIR", BRANCO)

        fundo()

        linha()

        escolha = input(VERMELHO + "\n              >>> " + RESET)

#JOGAR

        if escolha == "1":

            for i in range(0, 101, 10):

                limpar()

                linha()

                fundo()

                moldura("CARREGANDO...", VERMELHO)

                moldura(f"{i}%", BRANCO)

                fundo()

                linha()

                time.sleep(0.2)

            print(VERMELHO + "\n              O JOGO COMECOU..." + RESET)

            time.sleep(2)
            
            atoprologo()
            
            ato1()
            
            ato2()
            
            ato3()
            
            ato4()
            
            ato5()
            
            ato6()
            
            ato7()

            ato8()

            ato9()

            ato10()

            ato11()

            ato12()

            ato13()

            ato14()

            ato15()

        # TUTORIAl

        elif escolha == "2":

            limpar()

            linha()

            fundo()

            moldura("TUTORIAL", CIANO)

            moldura()

            moldura("Para fazer suas escolhas durante o jogo você apenas usa os numeros", BRANCO)
            moldura("1, 2, 3, 4, 5", BRANCO)
            moldura("e para continuar o jogo apenas pressione ENTER", BRANCO)

            moldura()

            moldura("PRESSIONE ENTER PARA VOLTAR", CINZA)

            fundo()

            linha()

            input()

        # SAIR

        elif escolha == "3":

            limpar()

            linha()

            fundo()

            moldura("ENCERRANDO SISTEMA...", VERMELHO)

            fundo()

            linha()

            time.sleep(2)

            sys.exit()

        #  ERRO

        else:

            print(VERMELHO + "\n              OPÇÂO INVÁLIDA!" + RESET)

            time.sleep(2)


#  INICIO

bem_vindo()

titulo()

menu()
