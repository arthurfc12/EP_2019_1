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
        "adiamento do EP (boa sorte...)")
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
        if azar < 2:
            print('Indo para o seu próximo destino você encontra um jogador de rugby, que esta puto com você pelo que você fez com o amigo dele. Sua única escolha é lutar.')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_pequeno
            while vida_rugby_pequeno>0 and not game_over:
                print('Você tem {0} de vida'.format(vida))
                escolha= input('Você quer: Atacar | Fugir? ')
                if escolha == 'Atacar':
                    vida_rugby_pequeno= vida_rugby_pequeno - dano_seu
                    print()
                    if vida_rugby_pequeno>0:
                        print('O jogador de rugby agora tem {} de vida'.format(vida_rugby_pequeno))
                        print()
                        print('O jogador de rugby te bateu!')
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

########################## SUBCENA 2 ##########################################

    if not game_over:
        if azar < 2:
            print('Indo para o seu próximo destino você encontra um jogador de rugby. Desta vez voce encontra um jogador titular do time, que é mais grande e forte que os anteriores, e você tem que lutar!')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_titular
            while vida_rugby_titular>0 and not game_over:
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
        
print(main())