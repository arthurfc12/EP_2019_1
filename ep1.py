from numpy import random

cenarios = {
        'catraca_opcoes': {"Paquerar segurança": "Você tentará cortejar a/o segurança usando seu charme para te deixar passar sem a carteirinha", 
                          "Pular catraca": "Você tentará saltar por cima da catraca sem ser pego",
                          "Pedir": "Você pedirá accesso para a pessoa na secretaria"},
        'catraca_consequencias': {'Paquerar segurança': 'Após dar em cima da/do segurança ela/ele não te deixou entrar e de sobra te avisou que você é feio/feia demais. Você ficou com tanta vergonha que decidiu largar o Insper',
                                'Pular catraca': 'Na sua tentativa de pular o seu pé ficou preso na catraca e você deu de cara no chão. Você teve que ir para o hospital e não pode falar com o professor.'},
        'briga_opcoes': {'Brigar': 'Você estufa o peito e sai pra briga.',
                         'Fugir': 'Você corre o mais rápido possivel para tentar escapar do jogador.'},
        'briga_consequencias': {'Fugir': 'Obviamente, o jogador de rugbi te alcançou. Ele te fez coçegas até você morrer.'},
        'bola_opcoes': {'Arriscar': 'Você arrisca e vai tentar pegar a bola para te ajudar em combates.',
                        'Relevar': 'Você vai embora sem pegar a bola de futebol americano.'},
        'bola_consequencias': {'Arriscar1': 'Você consegui pegar a bola sem ninguem te encher o saco! Vai ser uma potente arma nas suas batalhas.',
                               'Arriscar2': 'A professora viu você atrapalhando a aula e te mandou para o diretor que te jubilou do Insper.',
                               'Relevar': 'Você não pegou a bola, mas nada de ruim aconteceu contigo pelo menos!'},
        'direcao_opcoes':{'Esquerda': 'Você vira a esquerda no corredor',
                          'Direita': 'Você vira a direita no corredor'},
        'direcao_consequencias': {'Esquerda': 'Você encontra um jaleco! O jaleco faz com que você possa fugir de uma luta uma única vez. Para fazer isso é só escrever Inventario durante uma luta e selecionar o jaleco que você poderá fugir!',
                                  'Direita': 'Você acaba na sala de IntruMed onde você encontra um capacitor. Você percebe que a qualquer momento de uma luta você pode usa-lo para aumentar sua vida, mas somente uma vez! Para fazer isso é só escrever Inventario e seleciona-lo'},
        'inventario': {'Capacitor': 'Sua vida aumentou 50 pontos!',
                       'Jaleco': 'Voce fugiu da luta após colocar o jaleco pois os jogadores confundiram você com um mecânico'},
        'teletransportador_consequencias': {'Ibiza': 'Você acertou! Seu professor estava tentando tirar folga de alunos como você que não param de encher o saco! Você tera alguns minutos para conversar com ele antes que os alunos te teletransportem de volta',
                                            'Outra': 'Você errou! Agora vão te teletransportar para o vestiario dos jogadores de rugby!'},
        'profe_encontro': {'Fala': 'Não acredito que você veio me encher o saco aqui, mas devido ao seu esforço vou te dar uma chance de adiar o EP1. Caso você saiba qual é a sala virando a direita de DesSoft você deverá se teletransportar para lá e achar um bilhete que eu escrevi, so então vou adiar o EP.'},                   
        'final': {'Certo': 'Você acertou! Você achou o bilhete no chão da sala de IntruMed, nele estava escrito: O EP é e sempre foi para a semana que vem. FIM. Voce ganhou!',
                  'Errado': 'Como você não sabia a sala o teletransportador explodiu e você morreu :('},
        }




opcoes=[]
escolha= "nenhuma"



print("Na hora do sufoco!")
print("------------------")
print()
print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
print()
print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte)...")
print()



def main():
    game_over = False
    vida= 100
    dano_seu= random.randint(10, 41)
    vida_rugby_pequeno = 20
    dano_rugby_pequeno = random.randint(1, 11)
    azar= random.randint(0,6)
    bola= False
    dano_bola= random.randint(20,61)
    vida_rugby_titular = 40
    dano_rugby_titular = random.randint(8, 21)
    inventário = ['Sair']
    luta_rugby=False
    encontro= False
    vida_rugby_capitao = 130
    dano_rugby_capitao = random.randint(15, 70)
    
########################## CENA 1 #############################################

    if not game_over:
        print("Dilema da catraca")
        print("-----------------")
        print()
        print("Você chegou no Insper e está do lado da catraca quando você descobre que esqueceu a carteirinha.")
        print()
        print('As suas opções são: ')
        print()
        opcoes= cenarios['catraca_opcoes'].keys()
        for key, value in cenarios['catraca_opcoes'].items():
            print("{}: {}".format(key, value))
            print()
        escolha = input("Qual é a sua escolha? ")
        if escolha in opcoes:
            if escolha == 'Pedir':
                print()
                print('A pessoa na secretaria, como de rotina, te passou um cartão para você poder entrar no Insper.')
            elif escolha == 'Paquerar segurança':
                print()
                print(cenarios['catraca_consequencias']['Paquerar segurança'])
                game_over=True
            elif escolha == 'Pular catraca':
                print()
                print(cenarios['catraca_consequencias']['Pular catraca'])
                game_over=True
        else:
            print()
            print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
            game_over=True

    
    print()
    print()
    
    
########################## CENA 2 #############################################

    if not game_over:
        print('O primeiro ataque')
        print('-----------------')
        print()
        print('Após conseguir passar na catraca você se tromba com um jogador de rugby. Ele fica bravão e quer entrar em uma briga com você.')
        print()
        print('As suas opções são: ')
        print()
        opcoes= cenarios['briga_opcoes'].keys()
        for key, value in cenarios['briga_opcoes'].items():
            print("{}: {}".format(key, value))
            print()
        escolha = input("Qual é a sua escolha? ")
        if escolha in opcoes:
            if escolha == 'Fugir':
                print()
                print(cenarios['briga_consequencias']['Fugir'])
                game_over=True
            elif escolha == 'Brigar':
                print()
                while vida_rugby_pequeno>0:
                    print('O jogador de rugby tem {} de vida'.format(vida_rugby_pequeno))
                    print()
                    print('Você tem {0} de vida'.format(vida))
                    escolha= input('Você quer: Atacar | Fugir? ')
                    if escolha == 'Atacar':
                        vida_rugby_pequeno= vida_rugby_pequeno - dano_seu
                        print()
                        if vida_rugby_pequeno>0:
                            print('O jogador de rugby agora tem {} de vida'.format(vida_rugby_pequeno))
                            print('O jogador de rugby te bateu!')
                            vida= vida - dano_rugby_pequeno
                            print('Você agora tem {0} de vida'.format(vida))
                            print()
                        elif vida_rugby_pequeno <= 0:
                            print('Você matou o jogador de rugby e agora pode seguir adiante, mas cuidado, agora tem um time todo de rugby atrás de você!')
                            print()
                            print('Após vencer o jogador de rugby você pega o seu protetor bucal. Agora você tem 150 de vida!')
                            vida= 150
                    elif escolha == 'Fugir':
                        print()
                        print(cenarios['briga_consequencias']['Fugir'])
                        game_over=True
                        vida_rugby_pequeno= 0
                vida_rugby_pequeno = 20
        else:
            print()
            print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
            game_over=True

    
    print()
    print()
        
########################## SUBCENA 1 ##########################################
    
    if not game_over:
        if azar < 3:
            print('Indo para o seu próximo destino você encontra um jogador de rugby, que esta puto com você pelo que você fez com o amigo dele. Sua única escolha é lutar.')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_pequeno
            while vida_rugby_pequeno>0 and vida>0 and not game_over:
                print('O jogador de rugby tem {} de vida'.format(vida_rugby_pequeno))
                print()
                print('Você tem {0} de vida'.format(vida))
                escolha= input('Você quer: Atacar | Fugir? ')
                if escolha == 'Atacar':
                    vida_rugby_pequeno= vida_rugby_pequeno - dano_seu
                    print()
                    if vida_rugby_pequeno>0:
                        print('O jogador de rugby agora tem {} de vida'.format(vida_rugby_pequeno))
                        print()
                        print('O jogador de rugby te bateu!')
                        print()
                        vida= vida - dano_rugby_pequeno
                        if vida<0:
                            print('O jogador de rugby te matou :(')
                            game_over=True
                    elif vida_rugby_pequeno <= 0:
                        print('Você matou o jogador de rugby e agora pode seguir adiante!')
                        print()
                elif escolha == 'Fugir':
                    print()
                    print(cenarios['briga_consequencias']['Fugir'])
                    game_over=True
                    vida_rugby_pequeno= 0
                else:
                    print()
                    print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
                    game_over=True
            vida_rugby_pequeno = 20

########################## CENA 3 #############################################
        
    if not game_over:
        print('Sala de DesSoft')
        print('---------------')
        print()
        print('Como você está a procura do professor de DesSoft, você decide procurar por ele na sala onde ele te da aula. No entanto, quando você olha na sala esta tendo a aula de outra materia com outro professor. Decepcionado, voce vai ir a outra aula procurar ele mas você vê no fundo dessa aula em andamento uma bola de futebol americano, uma potencial arma muito útil contra seus inimigos do rugby.')
        print()
        print('As suas opções são: ')
        print()
        opcoes= cenarios['bola_opcoes'].keys()
        for key, value in cenarios['bola_opcoes'].items():
            print("{}: {}".format(key, value))
            print()
        escolha = input("Qual é a sua escolha? ")
        if escolha in opcoes:
            if escolha == 'Arriscar':
                if azar<4:
                    print()
                    print(cenarios['bola_consequencias']['Arriscar1'])
                    bola= True
                else:
                    print()
                    print(cenarios['bola_consequencias']['Arriscar2'])
                    game_over= True
            elif escolha == 'Relevar':
                print()
                print(cenarios['bola_consequencias']['Relevar'])
        else:
            print()
            print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
            game_over=True
        print()
        
########################## SUBCENA 2 ##########################################

    if not game_over:
        if azar < 3:
            print('Indo para o seu próximo destino você encontra um jogador de rugby. Desta vez voce encontra um jogador titular do time, que é mais grande e forte que os anteriores, e você tem que lutar!')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_titular
            while vida_rugby_titular>0 and not game_over:
                print('O jogador de rugby tem {} de vida'.format(vida_rugby_titular))
                print()
                print('Você tem {0} de vida'.format(vida))
                escolha= input('Você quer: Atacar | Fugir? ')
                if escolha == 'Atacar':
                    if not bola:
                        vida_rugby_titular= vida_rugby_titular - dano_seu
                    else:
                        vida_rugby_titular= vida_rugby_titular - dano_bola
                    print()
                    if vida_rugby_titular>0:
                        print('O jogador de rugby agora tem {} de vida'.format(vida_rugby_titular))
                        print()
                        print('O jogador de rugby te bateu!')
                        print()
                        vida= vida - dano_rugby_titular
                        if vida<0:
                            print('O jogador de rugby te matou :(')
                            game_over=True
                    elif vida_rugby_titular <= 0:
                        print('Você matou o jogador de rugby e agora pode seguir adiante!')
                        print()
                elif escolha == 'Fugir':
                    print()
                    print(cenarios['briga_consequencias']['Fugir'])
                    game_over=True
                    vida_rugby_titular= 0
                else:
                    print()
                    print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
                    game_over=True
            vida_rugby_titular = 40

########################## CENA 4 #############################################

    if not game_over:
        print()
        print('Esquerda ou Direita')
        print('-------------------')
        print()
        print('Saindo da sala que você usualmente tem DesSoft você vê que tem a opção de ir ou para a esquerda no corredor ou para a direita')
        print()
        print('As suas opções são: ')
        print()
        opcoes= cenarios['direcao_opcoes'].keys()
        for key, value in cenarios['direcao_opcoes'].items():
            print("{}: {}".format(key, value))
            print()
        escolha = input("Qual é a sua escolha? ")
        if escolha in opcoes:
            if escolha == 'Direita':
                print()
                print(cenarios['direcao_consequencias']['Direita'])
                inventário.append('Capacitor')
            elif escolha == 'Esquerda':
                print()
                print(cenarios['direcao_consequencias']['Esquerda'])
                inventário.append('Jaleco')
        else:
            print()
            print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
            game_over=True
        print()

########################## SUBCENA 3 ##########################################

    if not game_over:
        if azar < 5:
            print('Indo para o seu próximo destino você encontra um jogador de rugby. O jogador titular do time e é mais grande e forte que de costume, e você tem que lutar!')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_titular
            while vida_rugby_titular>0 and not game_over:
                print('O jogador de rugby tem {} de vida'.format(vida_rugby_titular))
                print()
                print('Você tem {0} de vida'.format(vida))
                escolha= input('Você quer: Atacar | Fugir | Inventario? ')
                if escolha == 'Atacar':
                    if not bola:
                        vida_rugby_titular= vida_rugby_titular - dano_seu
                    else:
                        vida_rugby_titular= vida_rugby_titular - dano_bola
                    print()
                    if vida_rugby_titular>0:
                        print('O jogador de rugby agora tem {} de vida'.format(vida_rugby_titular))
                        print()
                        print('O jogador de rugby te bateu!')
                        vida= vida - dano_rugby_titular
                        if vida<0:
                            print('O jogador de rugby te matou :(')
                            game_over=True
                    elif vida_rugby_titular <= 0:
                        print('Você matou o jogador de rugby e agora pode seguir adiante!')
                        print()
                elif escolha == 'Fugir':
                    print()
                    print(cenarios['briga_consequencias']['Fugir'])
                    game_over=True
                    vida_rugby_titular= 0
                elif escolha == 'Inventario':
                    print()
                    print(inventário)
                    escolha=input('Que item você deseja escolher? ')
                    if escolha in inventário:
                        if escolha == 'Jaleco':
                            print()
                            print(cenarios['inventario']['Jaleco'])
                            vida_rugby_titular=0
                            inventário.remove('Jaleco')
                        elif escolha == 'Capacitor':
                            print()
                            print(cenarios['inventario']['Capacitor'])
                            vida = vida +50
                            print('Você agora tem {0} de vida'.format(vida))
                            inventário.remove('Capacitor')
                        elif escolha == 'Sair':
                            print()
                            escolha= input('Você quer: Atacar | Fugir | Inventario? ')
                    else:
                        print()
                        print('Ou esse item não existe ou você escreveu errado. Tente novamente')
                        escolha= input('Você quer: Atacar | Fugir | Inventario? ')
                else:
                    print()
                    print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
                    game_over=True
            vida_rugby_titular = 40
    
########################## CENA 5 #############################################

    if not game_over:
        print()
        print('A procura continua')
        print('------------------')
        print()
        print('Como o aluno dedicado que você é, você decide ir até a biblioteca para ver se encontra o professor. Chegando lá você descobre que em um dos aquários os alunos de engenharia acabaram de inventar um teletransportador! Eles pediram que você seja o primeiro a testar. No entanto, eles dizem, você tem que saber exatamente onde está o professor de DesSoft, caso contrário vão te teletransportar para o vestiario dos jogadores de rugby!')
        print()
        escolha= input('Em que lugar está o professor de DesSoft? A resposta etá na frase: Iguana boa ignorou zebra azul. ')
        print()
        if escolha=='Ibiza':
            print(cenarios['teletransportador_consequencias']['Ibiza'])
            print()
            encontro= True
        else:
            print(cenarios['teletransportador_consequencias']['Outra'])
            luta_rugby=True



########################## Cena 6 #############################################
    
    
    
    if not game_over and not luta_rugby:
       print()
       print('O encontro')
       print('----------')
       print()
       print('Você achou o professor no meio da praia e ele disse:')
       print(cenarios['profe_encontro']['Fala'])
       print()
       print('Os alunos, logo depois da fala do professor, te teletransportaram de volta ao aquário')
       print()
       
########################## Subcena 4 ##########################################

    if not game_over and not encontro:
        print()
        print('Você foi teletransportado para o vestiario do time. O capitão do time en†ão vem a você e diz: Se você me vencer em batalha eu digo onde está o seu professor de DesSoft.')
        print()
        while vida_rugby_capitao>0 and not game_over:
            print('O jogador de rugby tem {} de vida'.format(vida_rugby_capitao))
            print()
            print('Você tem {0} de vida'.format(vida))
            escolha= input('Você quer: Atacar | Fugir | Inventario? ')
            if escolha == 'Atacar':
                if not bola:
                    vida_rugby_capitao= vida_rugby_capitao - dano_seu
                else:
                    vida_rugby_capitao= vida_rugby_capitao - dano_bola
                print()
                if vida_rugby_capitao>0:
                    print('O jogador de rugby agora tem {} de vida'.format(vida_rugby_capitao))
                    print()
                    print('O jogador de rugby te bateu!')
                    print()
                    vida= vida - dano_rugby_capitao
                    if vida<=0:
                        print('O jogador de rugby te matou :(')
                        game_over=True
                elif vida_rugby_capitao <= 0:
                    print('Você matou o jogador de rugby e, no seu último suspiro, ele te disse que seu professor estava em Ibiza.')
                    print()
            elif escolha == 'Fugir':
                print()
                print(cenarios['briga_consequencias']['Fugir'])
                game_over=True
                vida_rugby_capitao= 0
            elif escolha == 'Inventario':
                print()
                print(inventário)
                escolha=input('Que item você deseja escolher? ')
                if escolha in inventário:
                    if escolha == 'Jaleco':
                        print()
                        print(cenarios['inventario']['Jaleco'])
                        vida_rugby_capitao=0
                        inventário.remove('Jaleco')
                    elif escolha == 'Capacitor':
                        print()
                        print(cenarios['inventario']['Capacitor'])
                        vida = vida +50
                        print('Você agora tem {0} de vida'.format(vida))
                        inventário.remove('Capacitor')
                    elif escolha == 'Sair':
                        print()
                        escolha= input('Você quer: Atacar | Fugir | Inventario? ')
                else:
                    print()
                    print('Ou esse item não existe ou você escreveu errado. Tente novamente')
                    escolha= input('Você quer: Atacar | Fugir | Inventario? ')
            else:
                print()
                print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
                game_over=True
        vida_rugby_capitao = 130
        print()
        print('Segundos depois os alunos te teleportam de volta para a sala da teletransportadora. Lá você fala para eles te teletransportarem para Ibiza.')

########################## Cena 6(2) ##########################################


    if not game_over and luta_rugby:
       print()
       print('O encontro')
       print('----------')
       print()
       print('Você achou o professor no meio da praia e ele disse:')
       print(cenarios['profe_encontro']['Fala'])
       print()
       print('Os alunos, logo depois da fala do professor, te teletransportaram de volta ao aquário')
       print()

########################## Cena 7 ##########################################
       
    if not game_over:
        print()
        print('Última escolha')
        print('--------------')
        print()
        print('Você avisa aos alunos que você precisa se teletransportar para a sala a direita da sala de DesSoft. No entanto ninguem sabe qual é, então cabe a você avisar o nome da sala. Caso você não informe o nome certo a máquina de teletransporte irá explodir e você irá morrer.')
        print()
        escolha=input('Qual é o nome da sala a direita da de DesSoft? ')
        if escolha == 'InstruMed' or escolha=='Instrumentacao e Medicao' or escolha == 'instrumed' or escolha=='instrumentacao e medicao' or escolha=='Sala de InstruMed' or escolha=='Sala de Instrumentacao e Medicao':
            print()
            print(cenarios['final']['Certo'])
        else:
            print()
            print(cenarios['final']['Errado'])
            game_over= True
        
        
        

print(main())


















