import random

# ========== Classe do Jogador ==========
class Jogador:
    def __init__(self):
        self.vida = 100
        self.inventario = []
        self.pontuacao = 0

# ========== Funções auxiliares ==========
def mostrar_inventario(jogador):
    print("\nInventario:")
    if jogador.inventario:
        for item in jogador.inventario:
            print(f"- {item}")
    else:
        print("Senha do guardião.")
    print("")

# ========== Sistema de Combate ==========
def combate(jogador, inimigo):
    print(f"\nVocê enfrenta {inimigo['nome']}!")

    while jogador.vida > 0 and inimigo['vida'] > 0:
        print(f"\nSua Vida: {jogador.vida} | Vida do {inimigo['nome']}: {inimigo['vida']}")
        acao = input("Atacar ou Fugir? ")

        if acao == "atacar":
            dano = random.randint(5, 15)
            inimigo['vida'] -= dano
            print(f"Você causou {dano} de dano!")

            if inimigo['vida'] > 0:
                dano_inimigo = random.randint(3, 10)
                jogador.vida -= dano_inimigo
                print(f"{inimigo['nome']} causou {dano_inimigo} de dano!")
        elif acao == "fugir":
            print("Você fugiu do combate.")
            return False
        else:
            print("Comando inválido.")

    if jogador.vida > 0:
        print("Você venceu o combate!")
        jogador.pontuacao += 50
        return True
    else:
        print("Você foi derrotado.")
        return False

# ========== NPC (Diálogo com o Guardião) ==========
def falar_com_guardiao(jogador):
    print("\nGuardião: Você não passará sem a senha!")
    resposta = input("Digite a senha: ")

    if resposta == "sombras":
        print("Guardião: Correto. Tome esta chave ela lhe permitira abrir todas as portas da fortaleza.")
        jogador.inventario.append("Chave mestra")
        jogador.pontuacao += 20
    else:
        print("Guardião: Resposta errada. Vá embora!")

# ========== Enigma ==========
def sala_do_enigma(jogador):
    print("\nUma aura estranha como se fosse uma parede invisivel bloquea o caminho. Uma charada está escrita:")
    print("\"O que é mais leve que uma pluma, mas ninguém consegue segurar por muito tempo?\"")
    resposta = input("Resposta: ")

    if "respiração" in resposta:
        print("A aura se dicipa e o caminho e liberado!")
        jogador.pontuacao += 30
        return True
    else:
        print("Nada acontece. Talvez a resposta esteja errada.")
        return False

# ========== Cenas ==========
def cena_inicial(jogador):
    print("""\nVocê acorda em uma cela úmida, com baixa iluminação uma dor de cabeça danada , não lembra quem e você, nem seu próprio nome, nem onde vc esta,
no quarto tem um bolsa, deixada no canto da sala você verifica a bolsa dentro dela contem apenas um bilhite escrito " a senha do guardião e sombras" na hora você fica sem entender, 
você pega a bolsa e da mais uma olhada em volta nao tem mais nada a nao ser o vazio, mais tem uma porta misteriosa à sua frente entao você descide ir explorar para descobrir onde você esta e o que esta acontencendo.""")
    while True:
        acao = input("Digite 'sair' para explorar a porta e descobrir onde esta ou 'inventário' para conferir o que tem em sua bolsa: ")
        if acao == "inventario":
            mostrar_inventario(jogador)
        elif acao == "sair":
            return cena_corredor
        else:
            print("Comando inválido.")

def cena_corredor(jogador):
    print("\nVocê vai andando e encontra um corredor com dois caminhos: esquerda e direita.")
    escolha = input("Ir para 'esquerda' ou 'direita'? ")

    if escolha == "esquerda":
        return cena_combate
    elif escolha == "direita":
        return cena_guardiao
    else:
        print("Escolha inválida.")
        return cena_corredor

def cena_combate(jogador):
    inimigo = {"nome": "Rato Gigante", "vida": 30}
    combate(jogador, inimigo)
    return cena_corredor

def cena_guardiao(jogador):
    falar_com_guardiao(jogador)
    return cena_enigma

def cena_enigma(jogador):
    if sala_do_enigma(jogador):
        print("\nVocê avança para a sala final com sucesso.")
        return cena_final
    
    else:
        print("\nVocê retorna ao corredor.")
        return cena_corredor

def cena_final(jogador):
    print("\nVocê encontra uma escada levando para fora da fortaleza.")
    acao2=input("voce tem a chave que o guardiao lhe deu voce gostaria de 'explorar' mais a fortaleza e descobri o que se passa dentro dela, ou escolher 'ir embora' e deixar isso pra la?:")
    if acao2 == "explorar":
        print("voce pega a chave que o guardiao lhe confio e volta pra dentro da caverna pra viver mais aventuras")
        return cena_final_alternativo
    
    elif acao2 == "ir embora":
        print("Parabéns! Você sobreviveu.")
    print(f"Pontuação final: {jogador.pontuacao}")
    if "Chave mestra" in jogador.inventario:
        print("Final Comum: Você escolheu ir embora e deixar tudo pra lá.")
    
    return None

    
def cena_final_alternativo(jogador):
    print("\nVocê entra denovo na fortaleza que aventuras macabras o aguardao?....")
    print(f"Pontuação final: {jogador.pontuacao}")
    if "Chave mestra" in jogador.inventario:
        print("Final Especial: O Guardião confiou em você e lhe entregou a chave que abra as portas da fortaleza.")
    
    return None



# ========== Início do Jogo ==========
def iniciar_jogo():
    jogador = Jogador()
    cena_atual = cena_inicial

    while cena_atual is not None:
        cena_atual = cena_atual(jogador)

# ========== Execução ==========
if __name__ == "__main__":
    iniciar_jogo()
