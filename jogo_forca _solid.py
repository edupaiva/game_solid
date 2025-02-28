import random

class JogoForca:
    def __init__(self):
        self.pessoas = ['Eduardo', 'Julianna', 'Laura', 'Alice', 'Isis', 'Vera', 'Assis', 'Carlos', 'Marcia', 'Elaine', 'Karol', 'Levi', 'Elissa', 'Lucas']
        self.pessoa_sorteada = random.choice(self.pessoas).upper()
        self.total_letras = len(self.pessoa_sorteada)
        self.palavra_oculta = "-" * self.total_letras
        self.letras_sorteadas = []
        self.max_tentativas = 6

    def verificar_letra(self, letra):
        """
        Verifica se a letra está na palavra sorteada e atualiza a palavra oculta.
        """
        if letra in self.letras_sorteadas:
            print("⚠️ Você já escolheu essa letra antes. Tente outra!")
            return False
        
        self.letras_sorteadas.append(letra)

        if letra in self.pessoa_sorteada:
            self.atualizar_palavra_oculta(letra)
            return True
        else:
            self.max_tentativas -= 1
            print(f"❌ Letra não encontrada. Você tem mais {self.max_tentativas} tentativas.")
            return False

    def atualizar_palavra_oculta(self, letra):
        """
        Atualiza a palavra oculta revelando as letras corretas.
        """
        nova_palavra_oculta = [
            letra if self.pessoa_sorteada[i] == letra else self.palavra_oculta[i]
            for i in range(self.total_letras)
        ]
        self.palavra_oculta = "".join(nova_palavra_oculta)

    def jogo_acabou(self):
        """
        Verifica se o jogo acabou por vitória ou derrota.
        """
        if self.palavra_oculta == self.pessoa_sorteada:
            print(f"🎉 Parabéns! A palavra era: {self.pessoa_sorteada}")
            return True
        elif self.max_tentativas == 0:
            print(f"💀 Tentativas esgotadas! Você perdeu! A palavra era: {self.pessoa_sorteada}")
            return True
        return False

    def jogar(self):
        """
        Loop principal do jogo.
        """
        while not self.jogo_acabou():
            print(f"\nA palavra possui ({self.total_letras}) letras: {self.palavra_oculta}")
            letra = input("Digite uma letra: ").strip().upper()
            if len(letra) != 1 or not letra.isalpha():
                print("⚠️ Entrada inválida! Digite apenas uma única letra.")
                continue

            self.verificar_letra(letra)


# Inicia o jogo
if __name__ == "__main__":
    jogo = JogoForca()
    jogo.jogar()
