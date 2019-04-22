from numpy import random
import pygame

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
        'teleporte_opcoes':{'Catraca':'Você volta para o local do começo da jornada', 'DSoft':'Você volta para a sala de DSoft', 'Corredor':'Você volta ao corredor do quarto andar e continua sua jornada',},
        'teleporte_consequencias':{'Catraca':'Ao chegar na catraca você decide passar no balcão e acaba encontrando o recepcionista. Você tem direito a fazer uma pergunta a ele!', 'DSoft':'Você passa com mais cuidado na sala de DSoft e encontra um carregador, use-o apenas uma vez apenas para encontrar itens escondidos','Corredor':'Você decide não gastar mais tempo e segue rumo ao seu destino'},  
        'balcao_opcoes':{'Historia':'O recepcionista irá te contar uma história inspiradora','Convencer':'você tentará convencer o recepcionista a te dar alguma coisa'},
        'balcao_consequencias':{'Historia':'Você ainda é muito novo para ficar pegando DP garoto, siga seus sonhos e entregue o trabalho!!!','Convencer1':'O recepcionista te dá um fora','Convencer2':'O recepcionista te concebe um capacitor!'}

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
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load("SONIC.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)
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
    resposta_recepcionista = random.randint(0,1)
    
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
        if azar < 3:
            print('Indo para o seu próximo destino você encontra um jogador de rugby, que esta puto com você pelo que você fez com o amigo dele. Sua única escolha é lutar.')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_pequeno
            while vida_rugby_pequeno>0 and vida>0 and not game_over:
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
        if azar < 3:
            print('Indo para o seu próximo destino você encontra um jogador de rugby. Desta vez voce encontra um jogador titular do time, que é mais grande e forte que os anteriores, e você tem que lutar!')
            print()
            print('O jogador de rugby te bateu de surpresa!')
            print()
            vida= vida- dano_rugby_titular
            while vida_rugby_titular>0 and not game_over:
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
        print("A aventura do herói continua em sua jornada pelo adiamento do EP de DSoft...")
        print("Após sua luta com o jogador de Rugby, o herói tira uma pausa para descansar. Durante sua pausa, em meio à tudo que ocorreu até agora, o herói se lembra das dificuldades que teve que superar para chegar onde está agora.")
        print("---------")
        print("~Você agora terá a oportunidade de se teleportar para uma das salas que visitou até o momento e encontrar monstros, prêmios ou uma outra surpresa...~")
        opcoes = cenarios['teleporte_opcoes'].keys()
        for key, value in cenarios['teleporte_opcoes'].items():
             print("{}: {}".format(key, value))
             print()
        escolha = input("Para onde desejas ir?")
        if escolha in opcoes:
            if escolha == 'DSoft':
                print()
                print(cenarios['teleporte_consequencias']['Dsoft'])
                inventário.append("Carregador")
            elif escolha == 'Catraca':
                print()
                print(cenarios['teleporte_consequencias']['Catraca'])
                opcoes = cenarios['balcao_opcoes'].keys()
                for key, value in cenarios['balcao_opcoes'].items():
                    print("{}: {}".format(key, value))
                    print()
                escolha = input("O que desejas perguntar?")
                if escolha in opcoes:
                    if escolha == 'Historia':
                        print()
                        print(cenarios['balcao_consequencias']['Historia'])
                    elif escolha == 'Convencer':
                        print()
                        if resposta_recepcionista == 1:
                            print(cenarios['balcao_consequencias']['Convencer2'])
                            inventário.append("Capacitor")
                        else:
                            print(cenarios['balcao_consequencias']['Convencer1'])
            elif escolha == 'Corredor':
                print()
                print(cenarios['teleporte_consequencias']['Corredor'])
        else:
            print('Escreva certo da próxima vez...')
            game_over = True


                
########################## CENA 6 #############################################
    
    
    
    if not game_over:
        print()
        print("Após sua breve pausa para teleportar para uma sala, o jogador decide voltar a embarcar na sua viajem para o adiamento do EP")
        print("Apenas o futuro dirá como irá se desenrolar a história do nosso herói...")
        print("Obrigado por jogar a primeira versão do jogo. Um agradecimento especial ao Dudu, que salvou demais no desenvolvimento do código e ao professor Toshi, que se tudo der certo nos concebe uma notinha boa ;) . Valeu!!")
                        
                        




















