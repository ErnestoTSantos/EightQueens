# Solucionador do Problema das 8 Rainhas com Múltiplas Abordagens

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

Este projeto oferece implementações em Python para resolver o clássico Problema das 8-Rainhas.

São apresentadas três abordagens algorítmicas distintas para encontrar uma solução para o problema:
* **Backtracking (Recursivo)**: Um método de busca exaustiva que é garantido para encontrar todas as soluções possíveis.
* **Hill Climbing com Reinício Aleatório (Busca Local)**: Uma heurística de otimização rápida que busca melhorar iterativamente uma solução aleatória.
* **Algoritmo Genético**: Uma meta-heurística inspirada na evolução natural, que evolui uma população de soluções candidatas.

## Funcionalidades

* Três implementações de algoritmos distintos para resolver o problema.
* Código estruturado em Orientação a Objetos para clareza, reutilização e manutenção.
* Visualização gráfica das soluções encontradas utilizando a biblioteca `matplotlib`.
* Medição do tempo de execução para análise de performance de cada algoritmo.
* Código limpo e comentado para fins educativos.

## Pré-requisitos

Antes de começar, garanta que tem os seguintes programas instalados no seu sistema Linux ou MacOs.

1.  **Python 3.8 ou superior**
    * Para verificar a sua versão, abra o terminal e execute:
        ```bash
        python3 --version
        ```

2.  **PIP (Gerenciador de Pacotes do Python)**
    * Para verificar:
        ```bash
        pip3 --version
        ```

3.  **Git**
    * Para verificar se o Git está instalado:
        ```bash
        git --version
        ```

## Como Instalar e Configurar o Projeto

Siga este passo a passo no seu terminal Linux.

#### 1. Clonar o Repositório
Primeiro, clone este repositório para a sua máquina local. `git@github.com:ErnestoTSantos/EightQueens.git` utilizando o ssh do projeto.

```bash
git clone URL_DO_SEU_REPOSITORIO
```

#### 2. Entrar na Pasta do Projeto
Navegue para o diretório que acabou de ser criado:
```bash
cd nome-do-repositorio
```
*(Substitua `nome-do-repositorio` pelo nome da pasta do seu projeto)*

#### 3. Criar e Ativar um Ambiente Virtual (Recomendado)
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto e não interferir com outras instalações Python no seu sistema.

* Para criar o ambiente virtual (será criada uma pasta `venv`):
    ```bash
    python3 -m venv venv
    ```
* Para ativar o ambiente:
    ```bash
    source venv/bin/activate
    ```
    *(Após a ativação, o seu prompt do terminal deverá mostrar `(venv)` no início)*

#### 4. Instalar as Dependências
Com o ambiente virtual ativo, instale a única dependência externa do projeto, a `matplotlib`.

```bash
pip install matplotlib
```

## Estrutura dos Arquivos

---

* `chessboard.py`: Define a classe `ChessBoard`, que representa um tabuleiro, calcula ataques e sabe como se desenhar.
* `solver.py`: Define a classe abstrata `QueenSolver`, que serve como um "molde" para todos os solvers e contém a lógica para medir o tempo.
* `solver_backtracking.py`: Implementação do algoritmo de Backtracking.
* `solver_hill_climbing.py`: Implementação do algoritmo Hill Climbing.
* `solver_genetic.py`: Implementação do Algoritmo Genético.

## Autores

---

* Ernesto Terra dos Santos
* Marcus Apolinário
* Gabriel Fonseca
* Gabriel Antonietti