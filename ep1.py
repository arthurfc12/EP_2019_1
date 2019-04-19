
cenarios = {
        'catraca_opcoes': {"Paquerar segurança": "Você tentará cortejar a/o segurança usando seu charme para te deixar passar sem a carteirinha", 
                          "Pular catraca": "Você tentará saltar por cima da catraca sem ser pego",
                          "Pedir": "Você pedirá accesso para a pessoa na secretaria"},
        'catraca_consequencias': {'Paquerar segurança': 'Após dar em cima da/do segurança ela/ele não te deixou entrar e de sobra te avisou que você é feio/feia demais.',
                                'Pular catraca': 'Na sua tentativa de pular o seu pé ficou preso na catraca e você deu de cara no chão. Você teve que ir para o hospital e não pode falar com o professor.'},
        
        
        
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
    if not game_over:
        print("Dilema da catraca")
        print("-----------------")
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
                print('A sua escolha foi a certa!')
            elif escolha == 'Paquerar segurança':
                print(cenarios['catraca_consequencias']['Paquerar segurança'])
                game_over=True
            elif escolha == 'Pular catraca':
                print(cenarios['catraca_consequencias']['Pular catraca'])
                game_over=True
        else:
            print('Como a sua escolha não estava nas opções ou você não sabe escrever direito você morreu de um ataque cardíaco repentino.')
            game_over=True
    else:
        print()
        game_over = True
        
        
print(main())