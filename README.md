# Solucionador do Problema das N-Rainhas

Este projeto, desenvolvido em Python, tem como objetivo resolver o clássico **Problema das N-Rainhas**, que consiste em posicionar `8` rainhas em um tabuleiro `8 x 8` de forma que nenhuma delas possa atacar outra.

---

## Abordagens Utilizadas

O projeto implementa quatro estratégias distintas para encontrar soluções viáveis para o problema:

* **Backtracking (Busca Exaustiva)**: Explora todas as possibilidades de forma recursiva. Ao encontrar uma configuração inválida, retrocede (backtrack) e tenta uma nova disposição até encontrar uma solução válida.
* **Hill Climbing (Subida de Encosta)**: Inicia com uma disposição aleatória das rainhas e tenta, iterativamente, mover uma única rainha de modo a reduzir o número de conflitos. Caso não consiga mais melhorar, reinicia o processo com uma nova configuração.
* **Algoritmo Genético**: Baseado em princípios da evolução natural, mantém uma população de soluções, aplicando seleção, cruzamento e mutação para gerar novas configurações, com o objetivo de convergir para uma solução ideal.
* **Simulated Annealing (Reaquecimento Simulado)**: Técnica inspirada no processo de recozimento de metais. Permite aceitar soluções piores no início da execução para evitar mínimos locais, reduzindo essa permissividade ao longo do tempo até estabilizar em uma solução adequada.

---

## Funcionalidades do Projeto

* Resolve o Problema das N-Rainhas utilizando **quatro algoritmos distintos**.
* Exibe graficamente a solução obtida utilizando **Matplotlib**.
* **Mensura o tempo de execução** de cada abordagem.
* Código modular e de fácil compreensão.

---

## Pré-Requisitos

Certifique-se de que os seguintes softwares estão instalados em seu ambiente:

* **Python 3.8 ou superior** – verifique com:

  ```bash
  python3 --version
  ```
* **Git** – verifique com:

  ```bash
  git --version
  ```

---

## Instalação e Execução

Siga as instruções abaixo para clonar e executar o projeto localmente:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ErnestoTSantos/EightQueens.git
   ```

2. **Acesse o diretório do projeto:**

   ```bash
   cd EightQueens
   ```

3. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   > O prefixo `(venv)` será exibido no terminal indicando que o ambiente está ativo.

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o projeto:**

   ```bash
   python3 main.py
   ```

---

## Estrutura do Projeto

* `chessboard.py` – Responsável pela criação do tabuleiro, verificação de conflitos e visualização gráfica.
* `queen_solver_base.py` – Classe base com funcionalidades comuns aos algoritmos.
* `solver_backtracking.py` – Implementação do algoritmo de **Backtracking**.
* `solver_hill_climbing.py` – Implementação do algoritmo de **Hill Climbing**.
* `solver_genetic.py` – Implementação do **Algoritmo Genético**.
* `solver_simulated_annealing.py` – Implementação do algoritmo de **Simulated Annealing**.
* `main.py` – Ponto de entrada para execução dos testes e visualização das soluções.
* `requirements.txt` – Lista de dependências necessárias.

---

## Autores

* Ernesto Terra dos Santos
* Marcus Apolinário
* Gabriel Fonseca
* Gabriel Antonietti
