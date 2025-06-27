🐍 Jogo da Cobrinha com Pygame

Um jogo clássico da cobrinha implementado em Python usando Pygame, desenvolvido com princípios de programação orientada a objetos e código limpo. Este projeto apresenta um visual retrô com tabuleiro marrom e verde em xadrez, jogabilidade suave e uma interface intuitiva com pausa/início e reinício após o fim do jogo.

🏋️‍♂️ Estilo e Temática Divertida

Para deixar o jogo mais descontraído e personalizado, o grupo resolveu estilizar a clássica cobrinha com uma brincadeira: o personagem principal é uma foto do professor da disciplina — conhecido por gostar de treinar musculação — e o objetivo do jogo é "comer" pesos de academia espalhados pelo tabuleiro.
Essa escolha trouxe leveza e bom humor à proposta, tornando a experiência mais divertida e única para quem joga.


A cada peso coletado:

- Um som é reproduzido, simulando a pegada de um novo item.

- O corpo do personagem cresce, seguindo a lógica original do jogo da cobrinha.

---

## Funcionalidades

- Jogabilidade clássica da cobrinha.

- Design orientado a objetos para facilitar a manutenção.
 
- Código limpo e bem documentado com docstrings em inglês.

- Fundo em estilo retrô com padrão xadrez marrom e bordas verdes.

- Células da cobrinha e da comida menores que os quadrados do fundo, criando um efeito de contorno elegante.

- O jogo começa após pressionar uma tecla.

- Exibe a mensagem "Game Over" sem fechar a janela.

- Opção de reiniciar o jogo após perder.

- Controles responsivos e animações suaves.

---

## Requisitos

- Python 3.7 ou newer
- [Pygame](https://www.pygame.org/news)

---

## Instalação

1. Clone do repositório:

```bash
git clone https://github.com/yourusername/snake-pygame.git
cd snake-pygame

2. Cire um ambiente virtual (opcional mas recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install pygame
```

---

## Estrutura do Projeto

```
snake-pygame/
│
├── game.py          # Main game script to run the game
├── snake.py         # Snake class and related logic
├── food.py          # Food class and related logic
├── settings.py      # Settings to run snake game
├── main.py          # Run game code
└── README.md        # This file
```

---

## Como rodar

Rode o script principal do jogo:

```bash
python main.py
```

* O jogo começará com uma tela preta e a mensagem:

  > *Pressione qualquer tecla para começar*

* Use as setas do teclado ou as teclas WASD para controlar a cobrinha.

* Coma os pesos de academia para crescer.

* Evite bater nas paredes ou no próprio corpo da cobrinha.

* Quando o jogo terminar, uma mensagem de Game Over será exibida.

* Pressione R para reiniciar o jogo.

---

🎉 Divirta-se jogando o clássico Jogo da Cobrinha!
