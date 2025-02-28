import random

class JogoForca:
    """
    Classe que representa o jogo da forca.

    O jogo sorteia um nome de uma lista de participantes e permite ao jogador tentar adivinhar as letras dentro de um limite de tentativas.
    """

    def __init__(self) -> None:
        """
        Inicializa o jogo da forca com uma lista de nomes, sorteia um nome aleatório e define os atributos do jogo.
        """
        self.pessoas: list[str] = ['Eduardo', 'Julianna', 'Laura', 'Alice', 'Isis', 'Vera', 'Assis', 'Carlos', 
                                   'Marcia', 'Elaine', 'Karol', 'Levi', 'Elissa', 'Lucas']
        self.pessoa_sorteada: str = random.choice(self.pessoas).upper()
        self.total_letras: int = len(self.pessoa_sorteada)
        self.palavra_oculta: str = "-" * self.total_letras
        self.letras_sorteadas: list[str] = []
        self.max_tentativas: int = 6

    def verificar_letra(self, letra: str) -> bool:
        """
        Verifica se a letra digitada pelo jogador está na palavra sorteada.
        Caso positivo, a palavra oculta será atualizada.
        Caso negativo, uma tentativa será descontada.

        Parâmetros:
        - letra (str): Letra digitada pelo usuário.

        Retorna:
        - bool: True se a letra estiver correta, False se estiver errada.
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

    def atualizar_palavra_oculta(self, letra: str) -> None:
        """
        Atualiza a palavra oculta, revelando todas as ocorrências da letra encontrada.

        Parâmetros:
        - letra (str): Letra encontrada pelo jogador.
        """
        nova_palavra_oculta: list[str] = [
            letra if self.pessoa_sorteada[i] == letra else self.palavra_oculta[i]
            for i in range(self.total_letras)
        ]
        self.palavra_oculta = "".join(nova_palavra_oculta)

    def jogo_acabou(self) -> bool:
        """
        Verifica se o jogo acabou, seja por vitória ou derrota.

        Retorna:
        - bool: True se o jogo terminou, False caso contrário.
        """
        if self.palavra_oculta == self.pessoa_sorteada:
            print(f"🎉 Parabéns! A palavra era: {self.pessoa_sorteada}")
            return True
        elif self.max_tentativas == 0:
            print(f"💀 Tentativas esgotadas! Você perdeu! A palavra era: {self.pessoa_sorteada}")
            return True
        return False

    def jogar(self) -> None:
        """
        Método principal que executa o loop do jogo, permitindo que o usuário tente adivinhar a palavra até o fim das tentativas.
        """
        while not self.jogo_acabou():
            print(f"\nA palavra possui ({self.total_letras}) letras: {self.palavra_oculta}")
            letra: str = input("Digite uma letra: ").strip().upper()
            
            if len(letra) != 1 or not letra.isalpha():
                print("⚠️ Entrada inválida! Digite apenas uma única letra.")
                continue

            self.verificar_letra(letra)


# Inicia o jogo se o script for executado diretamente
if __name__ == "__main__":
    jogo = JogoForca()
    jogo.jogar()
