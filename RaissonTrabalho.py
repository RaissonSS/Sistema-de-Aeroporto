import matplotlib.pyplot as plt
import time
from math import inf
from os import system

# TRABALHO DE LABORATÓRIO DE ALGORITMO 1
# Raisson Silveira de Souza - 1°Semestre de SI

# ------------------------------ BIBLIOTECA PESSOAL ------------------------------------------------------------


def intro(titulo='n', *msg):
    # Cria um título com margens adaptáveis ao tamanho do mesmo e mensagens opcionais abaixo
    if titulo != 'n':
        lin = '-' * (5 + len(titulo))
        print(f'{lin:^120}')
        print(f"{titulo:^120}")
        print(f'{lin:^120}')
    lista = msg
    for x in lista:
        centra(x)


def esp(x=0):
    # Cria espaços em branco substituindo o uso de vários prints ou print('\n\n\n')
    print('\n' * (x-1))


def centra(msg, tam=120):
    # Cria um print exibindo a mensagem no meio do prompt de comando
    print(f"{msg.center(tam)}") 


def menu(queb=0, queb2=0, queb3=0, titulo='n', subt='n', titf='n', *opcoes):
    # Cria um menu com margem adaptável, subtitulo e titulo final opcionais e opções numeradas
    # Possui também a possibilidade de quebrar até 3 linhas da numeração das opções
    lista = opcoes
    num = len(lista)
    if titulo != 'n':
        intro(titulo)
    if subt != 'n':
        centra(subt)
    for x in range(0, num):
        if queb != 0 or queb2 != 0 or queb3 != 0:
            if x + 1 < 10:
                print(f"""{f"[ 0{x+1} ] {lista[x]} {' ' * (45 - (len(lista[x]))) }":>90}""")
                if queb == x + 1 or queb2 == x + 1 or queb3 == x + 1:
                    print()
            if x + 1 >= 10:
                print(f"""{f"[ {x+1} ] {lista[x]} {' ' * (45 - (len(lista[x])))}":>90}""")
                if queb == x + 1 or queb2 == x + 1 or queb3 == x + 1:
                    print()
        else:
            if x + 1 < 10:
                print(f"""{f"[ 0{x+1} ] {lista[x]} {' ' * (45 - (len(lista[x]))) }":>90}""")
            if x + 1 >= 10:
                print(f"""{f"[ {x+1} ] {lista[x]} {' ' * (45 - (len(lista[x])))}":>90}""")
    if titf != 'n':
        centra(titf)


def LeiaInt(maximo=inf, minimo=1, msg='Sua opção >>> ', msg_erro='Digite um número!'):
    # Pode ler um número inteiro desde certo valor até outro que pode ser infinito, possui tratamento de erro integrado
    while True:
        try:
            x = CentraInput(msg)
            x = int(x)
        except:
            centra(msg_erro)
            esp()
        else:
            if x > maximo or x < minimo:
                centra('Fora do limite!')
                esp()
            else:
                return x


'''def LeiaTempo(msg, maximo=inf, minimo=1, msg_erro='Digite um número!'):
    while True:
        try:
            x = CentraInput(msg)
            x = int(x)
        except:
            centra(msg_erro)
            esp()
        else:
            if x > maximo or x < minimo:
                centra('Fora do limite!')
                esp()
            else:
                return x'''


def SleepSys(tempo=0, apagar=0):
    # Faz o sistema aguardar determinados segundos e dá refresh na tela do terminal
    if tempo != 0:
        time.sleep(tempo)
    if apagar != 0:
        system("cls")


def CentraInput(msg):
    # Exibe um input no centro da tela do prompt de comando, funciona como a função centra()
    msg = msg.center(120).rstrip()
    x = input(f'{msg} ')
    return x


# ------------------------------ TRABALHO ----------------------------------------------------------------------


def Verificacao(id):
    # Realiza uma rápida verificação se há um código com zeros a esquerda já cadastrados
    # Fiz essa verificação adicional devido a uma alteração tardia do método de adicionamento dos códigos das aeronaves
    id_achado = id_verificado = False
    if len(aeroporto) == 0:
        return False, None
    else:
        id = str(str(id).zfill(6))
        while True:
            esp()
            for cod in aeroporto:
                if str(id) == str(cod[0]):
                    id_achado = True
                    id_verificado = str(cod[0])
                    break

            if id_achado == True:
                return True, id_verificado
            if id_achado == False:
                return False, None


def IDcheck():
    # Verifica e armazena um código válido de avião, possui tratamento de erro integrado
    
    centra('Digite o códido de identificação da aeronave.')
    
    while True:
        valores = tuple()
        parar = verify = False
        codigo = None
        try:
            msg = CentraInput('ID do avião:')
            x = int(msg.strip())
            if len(str(x)) < 6:
                valores = Verificacao(x)
                verify = valores[0]
                codigo = valores[1]
            if x == 999:
                parar = True
                break
            if len(str(x)) > 6 or len(str(x)) < 1 or x < 0:
                raise Exception("ID inválida!")
        except:
            centra('ID inválido! Tente novamente!')
            esp()
        else:
            if verify == False:
                break
            else:
                centra(f'ID {codigo} já cadastrado!')
                esp()
        del valores, verify, codigo

    if parar == True:
        return 999
    else:
        if len(str(x)) < 6:
            esp()
            centra(f'{6 - len(str(x))} zeros foram adicionados antes de {x}')
        x = str(str(x).zfill(6))
        return x


def IDcheckRetirada():
    # Verifica e armazena um código válido de avião, possui tratamento de erro integrado
    centra('Digite o códido de identificação da aeronave.')
    while True:
        try:
            msg = CentraInput('ID do avião:')
            x = int(msg.strip())
            if x == 999:
                break
            if len(str(x)) > 6 or len(str(x)) < 1 or x < 0:
                raise Exception("ID inválida!")
        except:
            centra('ID inválido! Tente novamente! b')
            esp()
        else:
            x = str(str(x).zfill(6))
            break
    return x


def FormatData(tempo):
    # Formata uma data fornecida para que seja melhor apresentável, 9/10/2022 vira 09/10/2022
    dia = str(time.localtime(tempo).tm_mday)
    mes = str(time.localtime(tempo).tm_mon)
    ano = str(time.localtime(tempo).tm_year)
    if len(dia) == 2 and len(mes) == 2:
        return f'{dia}/{mes}/{ano}'
    elif len(dia) == 1 and len(mes) == 2:
        return f'0{dia}/{mes}/{ano}'
    elif len(dia) == 2 and len(mes) == 1:
        return f'{dia}/0{mes}/{ano}'
    else:
        return f'0{dia}/0{mes}/{ano}'


def Cadastro(espera=False):
    # Realiza o cadastro de um avião, além de verificar se o ID do mesmo já não foi antes cadastrado
    # Através do atributo "espera", a função adiciona, exclusivamente, na lista de espera
    parar = False
    esp()
    centra('Digite 999 para CANCELAR.')
    while True:
        rep = fim = False
        id = IDcheck()
        if id == 999:
            parar = True
            break

        if len(aeroporto) == 0:
            break
        else:
            for cod in aeroporto:
                if id == cod[0]:
                    centra('ID já existente, tente outra!')
                    esp()
                    rep = True
            fim = True
        if fim == True and rep == False:
            break

    esp()
    if parar:
        centra('Operação de cadastro cancelada!')
    else:
        assert len(str(id)) == 6, 'ID acima de 6.'  # ASSERT
        entrada = time.localtime(dataJ).tm_hour
        if espera:
            aeroporto_espera.append((id, dataJ, entrada))
            centra(f'Avião de ID {id} cadastrado na lista de ESPERA!')
        else:
            aeroporto.append((id, dataJ, entrada))
            centra(f'Avião de ID {id} estacionado e cadastrado!')
    esp()
    
    assert len(aeroporto) < 6, 'Tamanho do aeroporto além do limite.'
    assert len(aeroporto_espera) < 2, 'Tamanho da lista de espera além do limite.'


def SolicitarVaga():
    # Verifica a possibilidade de cadastro de aviões ou não, e permite, se for o caso
    # Retorna se houve um estacionamento com sucesso
    if len(aeroporto) < 4:
        centra('Vagas disponíveis! Cadastre o avião.')
        Cadastro()
        return 1

    elif len(aeroporto) == 4:
        centra('Última vaga disponível! Cadastre o avião.')
        Cadastro()
        return 1

    elif len(aeroporto) == 5 and len(aeroporto_espera) == 1:
        centra('Não há vagas disponíveis neste aeroporto, procure outro!')
        esp()
        return 0

    else:
        centra('Apenas uma vaga na lista de espera! Cadastre o avião.')
        Cadastro(True)
        return 1
    

def RetirarAeronave():
    # Realiza a retirada de um avião, verificando sua ID
    # Retorna: Lucro com estacionamento, contagem de retiradas, Lucro no tempo atual e tempo atual
    if len(aeroporto) == 0:
        centra('Não há nenhum avião estacionado para retirar!')
        esp()
        return 0, 0, None, None

    else:
        MostrarAeronaves(True)
        id_achado = False
        parar = False
        while True:
            id = IDcheckRetirada()
            esp()
            if id == 999:
                parar = True
                break
            
            for num, cod in enumerate(aeroporto):
                if str(id) == str(cod[0]):
                    id_achado = True
                    tempo = cod[1]
                    break

            if id_achado:
                break
            else:
                centra(f'Avião de id: {id} não encontrado, tente novamente.')
                esp()

        if parar:
            centra('Operação de retirada cancelada!')
            esp()
            return 0, 0, None, None
        else:
            assert len(str(id)) == 6, 'ID acima de 6.'  # ASSERT
            del aeroporto[num]

            if len(aeroporto) == 4 and len(aeroporto_espera) == 1:
                aeroporto.append(aeroporto_espera[0])
                aeroporto_espera.clear()

            diferenca = dataJ - tempo
            dias = 0
            while diferenca >= 86400:
                diferenca -= 86400
                dias += 1

            centra(f'Avião de ID {id} foi retirado!')
            
            if dias == 0:
                centra('Valor a pagar: R$127.00')
                esp()
                return 127, 1, 127, dataJ
            
            elif dias > 30:
                centra(f'Valor a pagar: R${dias*115:.2f}')
                esp()
                assert dias * 115 > 0, 'Erro na data!'
                return dias * 115, 1, dias * 115, dataJ

            elif dias <= 30:
                centra(f'Valor a pagar: R${dias*127:.2f}')
                esp()
                assert dias * 127 > 0, 'Erro na data!'
                return dias * 127, 1, dias * 127, dataJ


def RetirarTudo():
    # Pode retirar todos os aviões estacionados
    # Retorna: Lucro com estacionamento, contagem de retiradas, lucro no tempo atual, tempo atual
    if len(aeroporto) == 0:
        centra('Não há nenhum avião estacionado para retirar!')
        esp()
        return 0, 0, None, None
    else:
        menu(0,0,0, 'Você tem certeza que deseja retirar todas as aeronaves?', 'n', 'n', 'Sim', 'Não')
        x = LeiaInt(2)
        esp()
        if x == 1:
            caixa = tot = caixa_temporario = 0
            for info in aeroporto:
                tempo = (info[1])

                diferenca = dataJ - tempo
                dias = caixa_temporario = 0
                while diferenca >= 86400:
                    diferenca -= 86400
                    dias += 1

                if dias == 0:
                    caixa += 127
                    caixa_temporario = 127
        
                elif dias > 30:
                    caixa += dias * 115
                    caixa_temporario = dias * 115

                elif dias <= 30:
                    caixa += dias * 127
                    caixa_temporario = dias * 127
                
                tot += 1
                assert caixa > 0 and caixa_temporario > 0, 'Erro na data! '

                centra(f'Avião de ID {info[0]} foi retirado!')
                centra(f'Valor a ser pago: R${caixa_temporario:.2f}')
                esp()
                SleepSys(1, 0)
            
            aeroporto.clear()
            if len(aeroporto_espera) == 1:
                aeroporto.append(aeroporto_espera[0])
                aeroporto_espera.clear()
            return caixa, tot, caixa, dataJ
        else:
            esp()
            return 0, 0, None, None


def MostrarAeronaves(retirar=False):
    # Mostra, de forma ordenada e alinhada, todas as informações dos aviões tanto estacionados como em espera
    # Com o atributo "retirar", é adaptado para permancer ativo sem o refresh do terminal (uso especial ao retirar aviões)
    if len(aeroporto) == 0:
        centra('Não há nenhum avião estacionado!')
        esp()
    else:
        centra('Aviões:')
        esp()
        print(f'{" " * 20} N  |   ID   |  Data de estacionamento | Hora de estacionamento |')
        #                  1°   111111          18/6/2022                   18hrs          
        for num, info in enumerate(aeroporto):
            print(' ' * 20, f'{num+1}°   {info[0]}          {FormatData(info[1])}                  {info[2]}hrs        ')

            
        esp()
        if len(aeroporto_espera) == 1 and retirar == False:
            id = aeroporto_espera[0][0]
            data = aeroporto_espera[0][1]
            hora = aeroporto_espera[0][2]
            centra('Avião em espera:')
            esp()
            print(' ' * 20, f'6°   {id}          {FormatData(data)}                  {hora}hrs        ')

        if retirar == False:
            input('\n\nPressione ENTER para voltar...')
            esp(2)
            SleepSys(0, 1)


def AdiantarTempo():
    # Avança no tempo, seja em dias, meses ou anos, adicionando o tempo requerido em forma de segundos para a variável de tempo
    menu(0,0,0, 'Adiantar tempo', 'Escolha o que quer adiantar no tempo', 'n',
         'Dias', 'Meses de 30 dias', 'Anos de 365 dias', 'Cancelar')
    esp()
    opc = LeiaInt(4)
    
    if opc == 1:
        # x = LeiaTempo('Digite quantos DIAS deseja avançar:')
        x = LeiaInt(inf, 1, 'Digite quantos DIAS deseja avançar:')
        data = x * 86400
    
    elif opc == 2:
        # x = LeiaTempo('Digite quantos MESES deseja avançar:')
        x = LeiaInt(inf, 1, 'Digite quantos MESES deseja avançar:')
        data = x * 2592000

    elif opc == 3:
        # x = LeiaTempo('Digite quantos ANOS deseja avançar:')
        x = LeiaInt(inf, 1, 'Digite quantos ANOS deseja avançar:')
        data = x * 31536000

    elif opc == 4:
        centra('Operação de avanço de tempo cancelada!')
        esp()
        data = 0

    SleepSys(1, 1)
    return data


def MostrarTempo(tempo):
    # Mostra informações do tempo atual do algoritmo
    centra(f'A data do algoritmo é {FormatData(tempo)}.')
    centra(f'A hora do algoritmo é {time.localtime(tempo).tm_hour}hrs.')
    esp()


def Grafico():
    # Mostra um gráfico do lucro adquirido em cada data que houve retirada de avião
    '''
    O gráfico possui 2 listas próprias que armazenam coordenadamente os ganhos e datas de cada retirada,
    mas caso não haja uma retirada com sucesso, eles armazenam None, que é corrigido e não avaliado
    na realização do gráfico.
    '''
    grafico_dinheiro = list()
    grafico_tempo = list()

    if len(g_caixa) == 0 and len(g_data) == 0:
        centra('Realize um cadastro e uma retirada para a criação de um gráfico!')
        esp()

    else:
        for v in g_caixa:
            if v != None:
                grafico_dinheiro.append(v)
        for v in g_data:
            if v != None:
                grafico_tempo.append(FormatData(v))
        
        fim = len(grafico_tempo)

        plt.plot(grafico_tempo, grafico_dinheiro, 'ok')
        plt.axis([grafico_tempo[0], grafico_tempo[fim-1], 0, caixa+500])
        plt.ylabel('Lucro')
        plt.xlabel('Tempo')
        plt.grid(True)
        plt.show()


dataJ = time.time()  # variável que contém o tempo atual em segundos
aeroporto = list()  # lista do aeroporto
aeroporto_espera = list()  # lista dos aviões em espera
caixa = tot_estacionamentos = tot_retiradas = 0  # caixa, total de estacionamentos e total de retiradas

g_caixa = list()  # armazenamento dos lucros nas datas em que houve retiradas
g_data = list()  # armazenamento das datas em que houve lucro

while True:
    menu(0,0,0, 'Sistema de Aeroporto', FormatData(dataJ), 'n', 'Solicitar Vaga', 'Retirar Aeronave', 'Retirar todas as Aeronaves',
    'Mostrar todas as Aeronaves', 'Adiantar o tempo', 'Mostrar o tempo', 'Grafico', 'Sair')
    opc = LeiaInt(8)
    SleepSys(0.5, 1)
    esp(2)
    
    if opc == 1:
        # Chama a função que solicita vaga, retorna 1 se estacionado com sucesso, ou 0 caso contrário
        tot_estacionamentos += SolicitarVaga()

    elif opc == 2:
        # Chama a função que retira aeronave, retorna o valor adquirido com a retirada e o contador, pode ser 0 se não
        # haver retirada, retorna também os valores individuais das datas e dinheiros de cada retirada
        retornado = RetirarAeronave()
        caixa += retornado[0]
        tot_retiradas += retornado[1]
        g_caixa.append(retornado[2])
        g_data.append(retornado[3])

    elif opc == 3:
        # Chama a função que retira todas as aeronaves, retorna valores iguais a função de retirar aeronaves individualmente
        retornado = RetirarTudo()
        caixa += retornado[0]
        tot_retiradas += retornado[1]
        g_caixa.append(retornado[2])
        g_data.append(retornado[3])

    elif opc == 4:
        # Chama a função que mostra ( ou não, caso não haja ) todas as aeronaves
        MostrarAeronaves()

    elif opc == 5:
        # Chama a função que adianta o tempo do algoritmo e retorna o valor avançado em segundos
        dataJ += AdiantarTempo()

    elif opc == 6:
        # Chama a função que mostra as informações do algoritmo baseadas nos segundos
        MostrarTempo(dataJ)

    elif opc == 7:
        # Chama uma função que mostra um gráfico que contém todos os ganhos de acordo com o avanço do tempo em cada retirada
        Grafico()

    elif opc == 8:
        menu(0,0,0, 'Deseja realmente sair?', 'n', 'n', 'Sim', 'Não')
        x = LeiaInt(2)
        SleepSys(0, 1)
        if  x == 1:
            break

intro('Informações finais do Aeroporto:', f'Lucro com os estacionamentos: R${caixa:.2f}.',
      f'Número de estacionamentos: {tot_estacionamentos}', f'Número de retiradas: {tot_retiradas}')
