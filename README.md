# 🍄 Meu Jogo do Mario 

Um protótipo simples de jogo de plataforma estilo Mario, desenvolvido em Pygame, com foco na implementação de mecânicas básicas de movimento, inimigos, itens e um sistema de fases com dificuldade progressiva.

## ✨ Funcionalidades

* **Mario Grande e Pequeno:** O Mario pode mudar de tamanho ao coletar cogumelos e encolher ao ser atingido por inimigos.
* **Movimento e Pulo:** Controles responsivos para movimentação lateral e pulo.
* **Inimigos:**
    * **Goombas:** Se movem horizontalmente e podem ser esmagados ou causar dano ao Mario.
    * **Plantas Carnívoras:** Surgem de dentro de canos e se movem verticalmente, causando dano se o Mario as tocar.
* **Itens:**
    * **Blocos de Item:** Blocos amarelos que podem liberar Estrelas ou Cogumelos.
    * **Estrelas:** Itens colecionáveis que podem dar pontos ou outras vantagens futuras (atualmente apenas colecionáveis).
    * **Cogumelos:** Transformam o Mario de pequeno para grande.
* **Sistema de Vidas:** O Mario possui vidas, que são perdidas ao ser atingido quando pequeno, ou ao cair em um abismo.
* **Fases Progressivas:** O jogo avança por fases, onde a dificuldade dos inimigos (velocidade e densidade) e a densidade de canos aumentam, enquanto a geração de blocos de item permanece constante.
* **Tela de Título e Game Over:** Estados de jogo básicos para iniciar e encerrar a partida.
* **Sistema de Conquistas:** Pequenas conquistas que são desbloqueadas ao realizar certas ações no jogo, como mover-se, pular, esmagar Goombas, etc.
* **Transição de Fase:** Uma tela de transição indica o avanço para o próximo nível.

## 🎮 Como Jogar

1.  **Pré-requisitos:**
    * Python 3.x instalado.
    * A biblioteca `pygame` instalada. Você pode instalá-la via pip:
        ```bash
        pip install pygame
        ```

2.  **Baixar o Projeto:**
    * Você pode clonar este repositório:
        ```bash
        git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
        cd NOME_DO_REPOSITORIO
        ```
    * Ou baixar o arquivo `.zip` e extrair.

3.  **Estrutura de Arquivos:**
    Certifique-se de que a estrutura de arquivos seja semelhante a esta:
    ```
    NOME_DO_REPOSITORIO/
    ├── seu_codigo_do_jogo.py  # Renomeie para algo como 'main.py' ou 'mario_game.py'
    ├── README.md
    └── assets/
        ├── mario_parado_1.png
        ├── mario_andando_1.png
        ├── ... (todas as suas imagens)
        ├── mario_theme.mp3
        └── game_over.mp3
    ```
    **Importante:** Verifique se o nome do seu arquivo principal (`seu_codigo_do_jogo.py`) está correto. Sugiro renomeá-lo para `main.py` para clareza.

4.  **Executar o Jogo:**
    Abra um terminal (ou Git Bash/Prompt de Comando) na pasta raiz do projeto e execute o arquivo Python:
    ```bash
    python seu_codigo_do_jogo.py
    ```

### Controles:

* **Setas Esquerda/Direita:** Mover o Mario.
* **Espaço:** Pular (na tela de título, inicia o jogo; na tela de Game Over, reinicia).

## 🏗️ Estrutura do Código

O código está organizado em seções lógicas:

* **Inicialização e Configurações:** Configura a janela, o clock e estados do jogo.
* **Carregamento de Recursos:** Carrega todas as imagens (sprites), música e sons do diretório `assets`.
* **Constantes e Variáveis Globais:** Define tamanhos de sprites, velocidades base, estados de jogo e contadores.
* **Classes de Entidades:** `Pipe`, `PiranhaPlant`, `Goomba`, `GoalFlag`, `ItemBlock`, `Star`, `Mushroom` encapsulam a lógica e o desenho de cada elemento.
* **Funções Auxiliares:**
    * `reset_game()`: Reinicia o estado do jogo para uma nova partida.
    * `populate_world()`: Gera os inimigos, canos e blocos de item no mundo, com escalonamento de dificuldade por fase.
    * `unlock_achievement()`: Gerencia o sistema de conquistas.
* **Loop Principal do Jogo:** Contém a lógica de atualização do jogo (eventos, movimento, colisões, atualização de entidades) e a rotina de desenho, alternando entre os estados do jogo (Título, Jogando, Game Over, Transição de Fase).
