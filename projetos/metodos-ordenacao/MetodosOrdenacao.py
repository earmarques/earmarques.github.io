<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>MetodosOrdenacao API documentation</title>
<meta name="description" content="" />
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" crossorigin>
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" crossorigin>
<link rel="stylesheet preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" crossorigin>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" crossorigin></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>MetodosOrdenacao</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">#coding=utf-8

 ###################################################
#                                                  #
# Author: Éder A. R. Marques                       #
# Email:  earmarques@gmail.com                     #
# Local:  São José do Rio Preto/SP Brazil          #
# Date:   28/10/2020                               #
#                                                  #
# Versioned for Python 2 from the Professor&#39;s      #
# original C code.                                 #
# ------------------------------------------------ #
# Professor: Carlos Magnus Carlson Filho           #
# Course:    Estruturas de Dados                   #
# Program:   Análise e Desenvolvimento de Sistemas #
# College:   Fatec Rio Preto                       #
#                                                  #
##################################################


import random
from datetime import datetime


# Cabeçalho     ----------------------------------------------------------------------------------------

#print(&#34;\033[1;30m{:_^80}&#34;.format(&#34;  Métodos de Ordenação  &#34;))
#print(&#34;\033[0;30m&#34;)
print(&#34;\n\n&#34;)
print(&#34;\033[1;{:_^80}&#34;.format(&#34;  Métodos de Ordenação  &#34;))
print(&#34;\033[0;&#34;)





# Constantes    --------------------------------------------------------------------------------------

# Constantes para escolha do método de ordenação
BOLHA_DIRETO =              1
BOLHA_INVERTIDO =           2
INSERCAO =                  3
SELECAO  =                  4
MESCLAGEM_NAO_RECURSIVO =   5
MESCLAGEM_RECURSIVO =       6
QUICK_RECURSIVO =           7
QUICK_RECURSIVO_CAUDAL_1 = 71
QUICK_RECURSIVO_CAUDAL_2 = 72
MUDAR_METODO =              8
SAIR =                      9

# Constantes para escolha do tipo de teste do método de ordenção
FIXO =                 1
GRANDE_1_ALEATORIO =   2
GRANDE_2_ALEATORIO =   3
GRANDE_1_DECRESCENTE = 4
GRANDE_2_DECRESCENTE = 5


# ==================================================================================================
# Menus de Interação com o Usuário              --------------------------------------------------------------

# Método de Ordenação   ------------------------------------------------------------------------------

def escolhe_metodo():

        &#34;&#34;&#34; Retorna o método escolhido para o teste.

        Apresenta uma menu de opções para que o usuário escolha o método de ordenação.

        Opções:
                1  - Bolha direto    (bubble sort)    - esquerda-&gt;direita
                2  - Bolha invertido (bubble sort)    - direita-&gt;esquerda
                3  - Inserção     (insertion sort)
                4  - Seleção      (selection sort)
                5  - Mesclagem    (merge sort)        - não recursivo
                6  - Mesclagem    (merge sort)        - recursivo
                7  - Partição     (quick sort)        - recursivo
                71 - Partição     (quick sort tail 1) - recursivo
                72 - Partição     (quick sort tail 2) - recursivo
                9  - Sair do programa

        Returns:
                int: A escolha do usuário.
        &#34;&#34;&#34;
        escolha = None

        # Exibição das opções
        print(&#39;_{:-&lt;47}&#39;.format(&#39;&#39;))
        print(&#39;{}&#39;.format(&#39;Escolha do método de ordenação a ser executado:&#39;))
        print(&#39;{:-&lt;47}&#39;.format(&#39;&#39;))
        print(&#39;  1 - Bolha direto    (bubble sort)    - esquerda-&gt;direita&#39;)
        print(&#39;  2 - Bolha invertido (bubble sort)    - direita-&gt;esquerda&#39;)
        print(&#39;  3 - Inserção     (insertion sort)&#39;)
        print(&#39;  4 - Seleção      (selection sort)&#39;)
        print(&#39;  5 - Mesclagem    (merge sort)        - não recursivo&#39;)
        print(&#39;  6 - Mesclagem    (merge sort)        - recursivo&#39;)
        print(&#39;  7 - Partição     (quick sort)        - recursivo&#39;)
        print(&#39; 71 - Partição     (quick sort tail 1) - recursivo&#39;)
        print(&#39; 72 - Partição     (quick sort tail 2) - recursivo&#39;)
        print(&#39;  9 - Sair do programa&#39;)

        # Obtenção, via teclado, da escolha do usuário
        escolha = int(input(&#39;\nInforme a opção desejada: &#39;))

        return escolha


# Tipo de Teste de Carga - Benchmark    --------------------------------------------------------------

def escolhe_teste():

        &#34;&#34;&#34; Retorna o tipo de teste escolhido.

        Apresenta uma menu de opções para que o usuário escolha do tipo de teste de carga
        para fazer análise de desempenho do método de ordenação escolhido.

        Opões:
                1 - Vetor fixo para validação do método de ordenação
                2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente
                3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente
                4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes
                5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes
                8 - Voltar à escolha do método de ordenação
                9 - Sair do programa

        Returns:
                int: A escolha do usuário.
        &#34;&#34;&#34;
        escolha = None;

        # Exibição das opções
        print(&#39;\n{:-&lt;41}&#39;.format(&#39;&#39;))
        print(&#39;{}&#39;.format(&#39;Escolha do tipo de teste a ser executado:&#39;))
        print(&#39;{:-&lt;41}&#39;.format(&#39;&#39;))

        print(&#39; 1 - Vetor fixo para validação do método de ordenação&#39;)
        print(&#39; 2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente&#39;)
        print(&#39; 3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente&#39;)
        print(&#39; 4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes&#39;)
        print(&#39; 5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes&#39;)
        print(&#39; 8 - Voltar à escolha do método de ordenação&#39;)
        print(&#39; 9 - Sair do programa&#39;)

        # Obtenção, via teclado, da escolha do usuário
        escolha = int(input(&#39;\nInforme a opção desejada:&#39;))

        return escolha


# ==================================================================================================
# Montagem dos Vetores de Testes        ------------------------------------------------------------------

# 8 Elementos Aleatórios        --------------------------------------------------------------------------

def monta_vetor_FIXO(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR FIXO e o imprime antes da ordenação.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor pequeno para validação dos métodos.
        &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor V1 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        V1 = [89, 44, 75, 66, 11, 38, 93, 56]

        #V1 = [3,0,1,8,7,2,5,4,9,6]      # vetor da dança húngara: https://www.youtube.com/watch?v=ywWBy6J5gz8

        print(&#39;Valor de V1: {}&#39;.format(V1))

        return V1


# 20.000 Elementos - Ordem Decrescente          ----------------------------------------------------------

def monta_vetor_GRANDE_1_DECRESCENTE(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 1 e o preenche com números decrescentes.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 20.000 elementos em ordem descrescente.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T1 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T1=[]
        for i in range(20000):
                T1.append(20000 - i)

        print(&#39;\nVocê escolheu gerar vetores com números decrescentes !&#39;)
        print(&#39;Primeiro elemento de T1: {}&#39;.format( T1[0] ))
        print(&#39;Último   elemento de T1: {}&#39;.format( T1[19999] ))

        return T1


# 40.000 Elementos - Ordem Decrescente          ----------------------------------------------------------

def monta_vetor_GRANDE_2_DECRESCENTE(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 2 e o preenche com números decrescentes.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 40.000 elementos em ordem descrescente.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T2 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T2=[]
        for i in range(40000):
                T2.append(40000 - i)

        print(&#39;\nVocê escolheu gerar vetores com números decrescentes !&#39;)
        print(&#39;Primeiro elemento de T2: {}&#39;.format( T2[0] ))
        print(&#39;Último   elemento de T2: {}&#39;.format( T2[39999] ))

        return T2


# 20.000 Elementos - Aleatórios         ------------------------------------------------------------------

def monta_vetor_GRANDE_1_ALEATORIO(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 1 e o preenche com números aleatórios.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 20.000 elementos aleatórios.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T1 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T1=[]
        for i in range(20000):
                T1.append( random.randint(1, 20000) )

        print(&#39;\nVocê escolheu gerar vetores com números aleatórios !&#39;)
        print(&#39;Primeiro elemento de T1: {}&#39;.format( T1[0] ))
        print(&#39;Último   elemento de T1: {}&#39;.format( T1[19999] ))

        return T1


# 40.000 Elementos - Aleatórios         ------------------------------------------------------------------

def monta_vetor_GRANDE_2_ALEATORIO(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 2 e o preenche com números aleatórios.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 40.000 elementos aleatórios.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T2 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T2=[]
        for i in range(40000):
                T2.append( random.randint(1, 40000) )

        print(&#39;\nVocê escolheu gerar vetores com números aleatórios !&#39;)
        print(&#39;Primeiro elemento de T2: {}&#39;.format( T2[0] ))
        print(&#39;Último   elemento de T2: {}&#39;.format( T2[39999] ))

        return T2


# ==================================================================================================
#       Métodos de Ordenação    ----------------------------------------------------------------------------

# Bubble Sort   --------------------------------------------------------------------------------------

def bubble_sort(vetor, imprimir=False):

        &#34;&#34;&#34; Método da BOLHA - Bubble Sort - Percurso Esquerda -&gt; Direita.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        # Auxiliar para interromper o loop - se não houver troca de posição o vetor está ordenado
        trocou = True           # inicia com true só para entrar no loop
        n = len(vetor)          # número de elementos no vetor
        barra = n                       # posição da barra, inicialmente após o último elemento

        # loop de passos
        while trocou:
                # reinicializa porque se supõe que neste passo ainda não houve troca
                trocou = False
                # recua a barra em uma posição
                barra -= 1

                if imprimir: print(&#39;Passo {}&#39;.format(n - barra))

                # loop de trocas dentro do passo, até a barra
                for i in range(barra):

                        if vetor[i] &gt; vetor[i + 1]:

                                # troca a posição dos dois elementos adjacentes
                                temp = vetor[i]
                                vetor[i] = vetor[i + 1]
                                vetor[i + 1] = temp
                                trocou = True

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor


# Bubble Sort Invertido         --------------------------------------------------------------------------

def bubble_sort_invertido(vetor, imprimir=False):

        &#34;&#34;&#34; Método da BOLHA - Bubble Sort - Percurso Direita -&gt; Esquerda.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        # Auxiliar para interromper o loop - se não houver troca de posição o vetor está ordenado
        trocou = True           # inicia com true só para entrar no loop
        n = len(vetor)          # número de elementos no vetor
        barra = -1                      # posição da barra, inicialmente antes do primeiro elemento

        # loop de passos
        while trocou:
                # reinicializa porque se supõe que neste passo ainda não houve troca
                trocou = False
                # avança a barra em uma posição
                barra += 1

                if imprimir: print(&#39;Passo {}&#39;.format(barra + 1))

                # loop de trocas dentro do passo, até a barra
                for i in range(n - 1, barra, -1):

                        if vetor[i] &lt; vetor[i - 1]:

                                # troca a posição dos dois elementos adjacentes
                                temp = vetor[i]
                                vetor[i] = vetor[i - 1]
                                vetor[i - 1] = temp
                                trocou = True

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor



# Insertion Sort        ----------------------------------------------------------------------------------

def insertion_sort(vetor, imprimir=False):

        &#34;&#34;&#34; Método da INSERÇÃO - Insertion Sort.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        n = len(vetor)          # número de elementos no vetor
        barra = 0                       # posição da barra, inicialmente no primeiro elemento

        # loop de passos
        for passo in range(1, n):

                if imprimir: print(&#39;Passo {}&#39;.format(passo))

                # avança a barra em uma posição
                barra += 1;

                # Corro todos os elementos do fim para trás até a posição da barra,
                # se o vetor[barra] for menor que o antecessor, troco de posição e
                # comparo com anterior seguinte, levando o elemento (se menor) até a sua posição correta
                for i in range(barra, 0, -1):
                        # da barra pra trás, todos os elementos já estão em ordem crescente,
                        # se o elemento for maior que seu antecessor ele já está na posição correta,
                        # posso interromper o loop e ir ao próximo elemento
                        if vetor[i - 1] &lt; vetor[i]:
                                break

                        # troca a posição dos dois elementos adjacentes
                        temp = vetor[i]
                        vetor[i] = vetor[i - 1]
                        vetor[i - 1] = temp

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor


# Selection Sort        ----------------------------------------------------------------------------------

def selection_sort(vetor, imprimir=False):

        &#34;&#34;&#34; Método da SELEÇÃO - Selection Sort.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        # Variáveis auxiliares
        indice_menor = -1
        n = len(vetor)          # número de elementos no vetor
        barra = -1                      # posição da barra, inicialmente antes do primeiro elemento


        # loop de passos
        for passo in range(1, n):

                if imprimir: print(&#39;Passo {}&#39;.format(passo))

                # avança a barra em uma posição
                barra += 1;
                # encontra o menor valor dentre os elementos não ordenados
                menor = vetor[barra]
                indice_menor = barra
                for i in range(barra + 1, n):
                        if vetor[i] &lt; menor:
                                menor = vetor[i]
                                indice_menor = i

                # troca o menor com o elemento ao lado direito da barra
                vetor[indice_menor] = vetor[barra]
                vetor[barra] = menor

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor


# Merge Sort    --------------------------------------------------------------------------------------

def merge_sort(metade_esquerda, metade_direita, imprimir=False):

        &#34;&#34;&#34; Método da MESCLAGEM - Merge Sort.

        Por não ser o recursivo e ordena as duas metades primeiramente para depois mesclar
        os elementos em ordem crescente.

        Args:
                metade_esquerda (list): primeira metade
                metade_direita (list): segunda metade
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: Um vetor ordenado.
        &#34;&#34;&#34;
        i = j = passo = 0
        tamanho_metade_esquerda = len(metade_esquerda)
        tamanho_metade_direita  = len(metade_direita)

        # Para garantir que as duas metades estejam ordenadas, passamos os vetores pelo Bubble Sort.
        # Se estiverem previamente ordenadas, o método bubble sort vai descobrir em apenas uma
        # passada pelo vetor e retornará rapidamente.
        metade_esquerda = bubble_sort(metade_esquerda, imprimir)
        metade_direita  = bubble_sort(metade_direita,  imprimir)

        # Cria o vetor que receberá os elementos ordenados
        vetor = list(metade_esquerda)
        vetor.extend(metade_direita)


        # Compara as duas metades sequencialmentes e adiciona no vetor de forma crescente.
        # OBS IMPORTANTE|=&gt; as duas metades precisam já estarem ordenadas

        while passo &lt; (tamanho_metade_esquerda + tamanho_metade_direita):

                if imprimir: print(&#39;Passo {}&#39;.format(passo + 1))

                # Comparo os elementos de ambos os lados
                if metade_esquerda[i] &lt;= metade_direita[j]:
                        # guardo o de menor valor que está do lado esquerdo
                        vetor[passo] = metade_esquerda[i]
                        # ando pra frente no vetor do lado esquerdo
                        i += 1
                        # se já terminei de fazer comparações com a primeira metade, do lado esquerdo
                        if i == tamanho_metade_esquerda:
                                # copio o resto dos elementos da segunda metade do lado direito
                                while j &lt; tamanho_metade_direita:
                                        passo += 1
                                        vetor[passo] = metade_direita[j]
                                        j += 1
                else:
                        # guardo o de menor valor que está do lado direito
                        vetor[passo] = metade_direita[j]
                        # ando pra frente no vetor do lado direito
                        j += 1
                        # se já terminei a segunda metade, do lado direito
                        if j == tamanho_metade_direita:
                                # copio os elementos restantes da metade esquerda
                                while i &lt; tamanho_metade_esquerda:
                                        passo += 1
                                        vetor[passo] = metade_esquerda[i]
                                        i += 1

                passo += 1

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor


# Merge Sort - Serviço Completo --------------------------------------------------------------------

def merge_sort_full_service(vetor, imprimir=False):

        &#34;&#34;&#34; Método da MESCLAGEM - Merge Sort.

        Divide o vetor em duas metades e invoca o #merge_sort() para fazer efetivamente a ordenação.

        Args:
                vetor (list): Vetor que será ordenado.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: Um novo vetor ordenado.
        &#34;&#34;&#34;
        tamanho = len(vetor)
        meio = int(tamanho / 2)
        metade_esquerda = vetor[:meio]
        metade_direita  = vetor[meio:tamanho]

        if imprimir:
                print(&#39;metade_esquerda: {}&#39;.format(metade_esquerda))
                print(&#39;metade_direita:  {}&#39;.format(metade_direita))

        # retorna um novo vetor ordenado
        return merge_sort(metade_esquerda, metade_direita, imprimir)


# Merge Sort Recursivo  ----------------------------------------------------------------------------

def merge_sort_recursivo(vetor, imprimir=False):

        &#34;&#34;&#34; Método da MESCLAGEM - Merge Sort - Versão Recursiva.

        Divide o vetor em duas metades e invoca o merge_sort recursivamente para fazer efetivamente a ordenação.

        Args:
                vetor (list): Vetor que será ordenado.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor ordenado.
        &#34;&#34;&#34;
        if imprimir: print(&#39;ENTRADA - Elementos do vetor: {}&#39;.format(vetor))

        tamanho = len(vetor)

        # CASO BASE: tamanho == 1 (nada a fazer)
        if tamanho == 1:
                return vetor

        # RECURSÃO

        meio = int(tamanho / 2)
        metade_esquerda = vetor[:meio]
        metade_direita  = vetor[meio:tamanho]

        tamanho_metade_esquerda = len(metade_esquerda)
        tamanho_metade_direita = len(metade_direita)


        if imprimir:
                print(&#39;ENTRADA - Elementos da metade esquerda: {}&#39;.format(metade_esquerda))
                print(&#39;ENTRADA - Elementos da metade direita:  {}\n&#39;.format(metade_direita))


        # Recursividade - Aciona a ordenação recursiva para cada metade

        metade_esquerda = merge_sort_recursivo(metade_esquerda, imprimir)
        metade_direita = merge_sort_recursivo(metade_direita, imprimir)


        # Mescla as metades, reconstruindo o vetor ordenadamente

        i = j = passo = 0

        while passo &lt; tamanho:

                if imprimir: print(&#39;Passo {}&#39;.format(passo + 1))

                # Comparo os elementos de ambos os lados
                if metade_esquerda[i] &lt;= metade_direita[j]:
                        # guardo o de menor valor que está do lado esquerdo
                        vetor[passo] = metade_esquerda[i]
                        # ando pra frente no vetor do lado esquerdo
                        i += 1
                        # se já terminei de fazer comparações com a primeira metade do lado esquerdo
                        if i == tamanho_metade_esquerda:
                                # copio o resto dos elementos da segunda metade do lado direito que já estão ordenados
                                while j &lt; tamanho_metade_direita:
                                        passo += 1
                                        vetor[passo] = metade_direita[j]
                                        j += 1
                else:
                        # guardo o de menor valor que está do lado direito
                        vetor[passo] = metade_direita[j]
                        # ando pra frente no vetor do lado direito
                        j += 1
                        # Se já terminei a segunda metade, é porque já copie todos os elementos do lado direito
                        # para o vetor final ordenado e todos os demais restantes do lado esquerdo são valores maiores.
                        # Não há mais nenhum elemento do lado direito que seja menor que do lado esquerdo.
                        if j == tamanho_metade_direita:
                                # copio os elementos restantes da metade esquerda
                                while i &lt; tamanho_metade_esquerda:
                                        passo += 1
                                        vetor[passo] = metade_esquerda[i]
                                        i += 1

                passo += 1

        if imprimir: print(&#39;\nSAÍDA - Elementos do vetor: {}\n&#39;.format(vetor))

        # retorna o vetor ordenado
        return vetor


# Particionador do Quick Sort   ----------------------------------------------------------------------

def particionar(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Particionador do Quick Sort

        Pega o elemento do vetor cujo indice(posição) é dado por &#39;inicio&#39;, ``vetor[inicio]``,
        e encontra a posição correta do elemento e retorna o índice referente a posição correta.
        Chamaremos este elemento que estamos procurando sua posição simplesmente de &#39;elemento_investigado&#39;.

        O algoritmo usa duas barras para correr o vetor no intevalo dos índices [inicio ao fim(inclusive)].
        A barra da extremidade esquerda avança para a direita até encontrar o elemento subsequente que seja
        maior que o elemento_investigado. A barra da direita recua para a esquerda até encontrar
        um elemento que seja menor que o elemento_investigado. Nessa situação, teremos::

                elemento_esquerda &gt; elemento_investigado &gt; elemento_direita, logo,
                elemento_esquerda &gt; elemento_direita

        isto é, está fora de ordem, e o algoritmo já os troca de posição ordenando-os, depois prossegue
        em direção ao centro até as barras volantes se encontrarem.

        A condição de parada ocorre quando a barra da esquerda atropela a direita, ficando com um valor maior.
        A barra da direita estará com o índice da posição correta, sendo ele o valor retornado pela função.

        Sinteticamente expresso de uma maneira formal matemática seria::

                Recebe vetor v[p..r] com p &lt; r. Rearranja os elementos do vetor e
                devolve j em p..r tal que v[p..j-1] &lt;= v[j] &lt; v[j+1..r].

        Args:
                vetor (list): Vetor que será ordenado e particionado logicamente.
                inicio(int): Índice inicial do intervalo de pesquisa e que determina o elemento cuja posição
                correta será retornada como a posição do particionamento.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      int: A posição do particionamento do vetor.
        &#34;&#34;&#34;
        elemento = vetor[inicio]                # ..a ser investigado qual o seu posicionamento correto no vetor
        barra_esquerda = inicio + 1             # posicionada no elemento adjacente seguinte
        barra_direita = fim                             # posicionada no último elemento

        while barra_esquerda &lt;= barra_direita:

                # Encontra o elemento subsequente que seja maior que o elemento investigado
                if vetor[barra_esquerda] &lt;= elemento:
                        barra_esquerda += 1

                # Encontra, do fim para o começo, o elemento que seja menor que o elemento investigado
                elif vetor[barra_direita] &gt; elemento:
                        barra_direita -= 1

                # |=&gt; vetor[barra_direita] &lt;= elemento &lt; vetor[barra_esquerda] =&gt;
                # logo, vetor[barra_direita] &lt; vetor[barra_esquerda], isto é, está fora da ordem crescente,
                # o menor tem de ficar a esquerda e o maior a direita, vamos trocá-los de posição
                else:
                        temp = vetor[barra_esquerda]
                        vetor[barra_esquerda] = vetor[barra_direita]
                        vetor[barra_direita] = temp
                        # A posição correta do elemento investigado está entre as barras, continuando a procura
                        barra_esquerda += 1             # avança uma posição
                        barra_direita  -= 1             # recua  uma posição

        # A posição correta do elemento é dado pela barra_direita
        posicao_correta = barra_direita

        # Vamos trocar de posição, fazendo backup do elemento que está ocupando o lugar
        # do nosso elemento investigado para o início do vetor
        vetor[inicio] = vetor[posicao_correta]
        vetor[posicao_correta] = elemento               # copia o elemento para sua posição correta

        if imprimir: print(&#39;\nValor de V1: {}&#39;.format(vetor))


        return posicao_correta


# Quick Sort Recursivo  ----------------------------------------------------------------------------

def quick_sort(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Quick Sort - Recursão comum.

        Recebe um vetor vetor[inicio..fim], com inicio &lt;= fim + 1,
        e rearranja o vetor em ordem crescente.

        Args:
                vetor (list): Vetor que será ordenado.
                inicio(int): Índice inicial do intervalo de pesquisa.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      None: Nada retorna. Opera diretamente com a referência do vetor.
        &#34;&#34;&#34;
        posicao_correta_elemento_inicio = -1

        if inicio &lt; fim:        # indices
                posicao_particao = particionar(vetor, inicio, fim, imprimir)

                # partição esquerda
                quick_sort(vetor, inicio, posicao_particao - 1, imprimir)
                # partição direita
                quick_sort(vetor, posicao_particao + 1, fim, imprimir)


# Quick Sort Recursivo Caudal - Versão 1        ----------------------------------------------------------

def quick_sort_tail_1(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Quick Sort Recursivo Caudal - Versão 1

        A recursividade ocorre em uma partição de cada vez.

        Args:
                vetor (list): Vetor que será ordenado.
                inicio(int): Índice inicial do intervalo de pesquisa.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      None: Nada retorna. Opera diretamente com a referência do vetor.
        &#34;&#34;&#34;
        while inicio &lt; fim:

                posicao_particao = particionar(vetor, inicio, fim, imprimir)

                # Ordena SEPARADAMENTE elementos &#39;antes&#39; e &#39;depois&#39; da partição
                quick_sort_tail_1(vetor, inicio, posicao_particao - 1, imprimir)

                inicio = posicao_particao + 1



# Quick Sort Recursivo Caudal - Versão 2        ----------------------------------------------------------

def quick_sort_tail_2(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Quick Sort Recursivo Caudal - Versão 2

        Melhor otimizada em relação a memória, a recursividade ocorre em apenas uma partição, e esta
        partição é a menor, fazendo com que a profundidade das chamadas recursivas seja mais rasa.

        Requer espaço auxiliar O(Log n) no pior caso.

        Args:
                vetor (list): Vetor que será ordenado.
                inicio(int): Índice inicial do intervalo de pesquisa.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      None: Nada retorna. Opera diretamente com a referência do vetor.


        .. _See below link for complete running code:
                https://ide.geeksforgeeks.org/qrlM31
        &#34;&#34;&#34;
        while inicio &lt; fim:

                posicao_particao = particionar(vetor, inicio, fim, imprimir)

                # Se parte à esquerda é menor, tratá-la recursivamente
                # e lidar com a parte à dreita iterativamente &#39;while&#39;
                if posicao_particao - inicio &lt; fim - posicao_particao:

                        quick_sort_tail_2(vetor, inicio, posicao_particao - 1, imprimir)

                        inicio = posicao_particao + 1

                # Caso contrário: recursão à direita, iteração à esquerda
                else:
                        quick_sort_tail_2(vetor, posicao_particao + 1, fim, imprimir)

                        fim = posicao_particao - 1



# ==================================================================================================
# Método main() - Execução de Testes    --------------------------------------------------------------

def main():

        &#34;&#34;&#34; Método main() - Execução de Testes &#34;&#34;&#34;

        # Dicionário cujas chaves representam o método de ordenação escolhido
        metodos_ordenacao = {
                1 : &#39;BOLHA (esquerda-&gt;direita)&#39;,
                2 : &#39;BOLHA (direita-&gt;esquerda)&#39;,
                3 : &#39;INSERCAO&#39;,
                4 : &#39;SELECAO&#39;,
                5 : &#39;MESCLAGEM (nao recursivo)&#39;,
                6 : &#39;MESCLAGEM (recursivo)&#39;,
                7 : &#39;QUICKSORT (recursivo)&#39;,
                71: &#39;QUICK_RECURSIVO_CAUDAL_1&#39;,
                72: &#39;QUICK_RECURSIVO_CAUDAL_2&#39;

        }
        # Dicionário cujas chaves representam o tipo de teste de carga escolhido
        tipos_teste = {
                1 : &#39;FIXO&#39;,
                2 : &#39;GRANDE_1_ALEATORIO&#39;,
                3 : &#39;GRANDE_2_ALEATORIO&#39;,
                4 : &#39;GRANDE_1_DECRESCENTE&#39;,
                5 : &#39;GRANDE_2_DECRESCENTE&#39;
        }

        # Montando as opções dos menus
        opcoes_menu_metodo_ordenacao = dict(metodos_ordenacao)          # cópia
        opcoes_menu_metodo_ordenacao.update( { 9 : &#39;SAIR&#39;} )

        opcoes_menu_tipo_teste = dict(tipos_teste)
        opcoes_menu_tipo_teste.update({
                8 : &#39;MUDAR_METODO&#39;,
                9 : &#39;SAIR&#39;
        })


        # Armazenar as escolhas realizadas pelo usuário
        escolhas = {&#39;metodo&#39; : -1, &#39;teste&#39; : -1}

        # OBS|=&gt; Em Python 2.x não é possível atribuir novos valores a variáveis declaradas
        # em um escopo superior; ao tentar fazê-lo o que ocorre é declarar uma nova variável local
        # de mesmo nome. A forma que escolhemos para contornar o problema foi declarar um dicionário
        # e alterar o valor associado a chave. Escopo interno não pode fazer atribuição à variáveis
        # não locais, mas pode modificar objetos (dict) que variáveis não locais se referem.
        #
        # Os dicionários main#escolhas e o acionar_teste#vetor foram utilizados com essa finalidade.
        # Python 3 resolveu esse incoveniente sem ferir o princípio pythônico do -
        # &#34;explicit is better than implicit&#34;, acrescentando as palavras chaves: global e nonlocal.


        # Executar Testes a Partir das Escolhas         --------------------------------------------------------

        # Esta função é utilizada meramente para fazer a interação com o usuário, logo,
        # pertence a camada de apresentação e não deve fazer parte do módulo.
        # Em função do exposto, evitamos a exposição da função #acionar_teste() fazendo
        # sua definição dentro do próprio contexto do método #main().

        def acionar_teste(escolhas):

                vetor = {&#39;vetor&#39;: None}


                # Carregamento do Vetor ------------------------------------------------------------------------

                if escolhas[&#39;teste&#39;] == FIXO:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_FIXO( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_1_ALEATORIO:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_1_ALEATORIO( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_1_DECRESCENTE:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_1_DECRESCENTE( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_2_ALEATORIO:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_2_ALEATORIO( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_2_DECRESCENTE:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_2_DECRESCENTE( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )


                # único teste que imprime os passos da ordenação
                eh_teste_fixo = escolhas[&#39;teste&#39;] == FIXO


                # Executando os Testes - Benchmark      ------------------------------------------------------------

                # Ordenação por BOLHA (esquerda-&gt;direita)

                if escolhas[&#39;metodo&#39;] == BOLHA_DIRETO:
                        if eh_teste_fixo:
                                bubble_sort(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                bubble_sort(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por BOLHA (direita-&gt;esquerda)

                elif escolhas[&#39;metodo&#39;] == BOLHA_INVERTIDO:
                        if eh_teste_fixo:
                                bubble_sort_invertido(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                bubble_sort_invertido(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por INSERÇÃO

                elif escolhas[&#39;metodo&#39;] == INSERCAO:
                        if eh_teste_fixo:
                                insertion_sort(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                insertion_sort(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por SELEÇÃO

                elif escolhas[&#39;metodo&#39;] == SELECAO:
                        if eh_teste_fixo:
                                selection_sort(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                selection_sort(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por MESCLAGEM NÃO RECURSIVO

                elif escolhas[&#39;metodo&#39;] == MESCLAGEM_NAO_RECURSIVO:
                        if eh_teste_fixo:
                                merge_sort_full_service(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                merge_sort_full_service(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por MESCLAGEM RECURSIVO

                elif escolhas[&#39;metodo&#39;] == MESCLAGEM_RECURSIVO:
                        if eh_teste_fixo:
                                merge_sort_recursivo(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                merge_sort_recursivo(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por QUICKSORT (PARTIÇÃO)

                elif escolhas[&#39;metodo&#39;] == QUICK_RECURSIVO:
                        vetor = vetor[&#39;vetor&#39;]
                        inicio = 0
                        fim = len(vetor) - 1
                        if eh_teste_fixo:
                                quick_sort(vetor, inicio, fim, True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                quick_sort(vetor, inicio, fim)
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por QUICKSORT CAUDAL 1 (PARTIÇÃO)

                elif escolhas[&#39;metodo&#39;] == QUICK_RECURSIVO_CAUDAL_1:
                        vetor = vetor[&#39;vetor&#39;]
                        inicio = 0
                        fim = len(vetor) - 1
                        if eh_teste_fixo:
                                quick_sort_tail_1(vetor, inicio, fim, True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                quick_sort_tail_1(vetor, inicio, fim)
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por QUICKSORT CAUDAL 1 (PARTIÇÃO)

                elif escolhas[&#39;metodo&#39;] == QUICK_RECURSIVO_CAUDAL_2:
                        vetor = vetor[&#39;vetor&#39;]
                        inicio = 0
                        fim = len(vetor) - 1
                        if eh_teste_fixo:
                                quick_sort_tail_2(vetor, inicio, fim, True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                quick_sort_tail_2(vetor, inicio, fim)
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )


        # Loop Principal do Programa    --------------------------------------------------------------------
        # Interação com o usuário através do menu de opções

        while True:
                # Escolha do método de ordenação a ser executado
                escolhas[&#39;metodo&#39;] = escolhe_metodo()

                if escolhas[&#39;metodo&#39;] not in opcoes_menu_metodo_ordenacao:
                        print(&#39;\nOpção INVÁLIDA !  Tente novamente...\n&#39;)

                elif not escolhas[&#39;metodo&#39;] == SAIR:
                        while True:
                                # Escolha do tipo de teste a ser executado
                                escolhas[&#39;teste&#39;] = escolhe_teste()

                                if escolhas[&#39;teste&#39;] == MUDAR_METODO:
                                        print(&#39;\nEscolheu voltar à escolha do método de ordenação !&#39;)
                                        break

                                elif escolhas[&#39;teste&#39;] == SAIR:
                                        print(&#39;\nEscolheu SAIR !\n\n&#39;)
                                        escolhas[&#39;metodo&#39;] = SAIR       # deixar o loop externo saber da intenção
                                        break

                                elif escolhas[&#39;teste&#39;] not in opcoes_menu_tipo_teste:
                                        print(&#39;\nOpção INVÁLIDA !  Tente novamente...\n&#39;)

                                else:
                                        acionar_teste(escolhas)

                # Se pediu pra sair no loop interno, obedeça e saia da execução do programa
                if escolhas[&#39;metodo&#39;] == SAIR:
                        break

# Boa educação
if __name__ == &#39;__main__&#39;:
        main()</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="MetodosOrdenacao.bubble_sort"><code class="name flex">
<span>def <span class="ident">bubble_sort</span></span>(<span>vetor, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da BOLHA - Bubble Sort - Percurso Esquerda -&gt; Direita.</p>
<p>Args:
vetor (list): Vetor a ser ordenado.
n (int): Tamanho da porção do vetor que ainda não está ordenada.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: O vetor fornecido como parâmetro ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def bubble_sort(vetor, imprimir=False):

        &#34;&#34;&#34; Método da BOLHA - Bubble Sort - Percurso Esquerda -&gt; Direita.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        # Auxiliar para interromper o loop - se não houver troca de posição o vetor está ordenado
        trocou = True           # inicia com true só para entrar no loop
        n = len(vetor)          # número de elementos no vetor
        barra = n                       # posição da barra, inicialmente após o último elemento

        # loop de passos
        while trocou:
                # reinicializa porque se supõe que neste passo ainda não houve troca
                trocou = False
                # recua a barra em uma posição
                barra -= 1

                if imprimir: print(&#39;Passo {}&#39;.format(n - barra))

                # loop de trocas dentro do passo, até a barra
                for i in range(barra):

                        if vetor[i] &gt; vetor[i + 1]:

                                # troca a posição dos dois elementos adjacentes
                                temp = vetor[i]
                                vetor[i] = vetor[i + 1]
                                vetor[i + 1] = temp
                                trocou = True

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.bubble_sort_invertido"><code class="name flex">
<span>def <span class="ident">bubble_sort_invertido</span></span>(<span>vetor, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da BOLHA - Bubble Sort - Percurso Direita -&gt; Esquerda.</p>
<p>Args:
vetor (list): Vetor a ser ordenado.
n (int): Tamanho da porção do vetor que ainda não está ordenada.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: O vetor fornecido como parâmetro ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def bubble_sort_invertido(vetor, imprimir=False):

        &#34;&#34;&#34; Método da BOLHA - Bubble Sort - Percurso Direita -&gt; Esquerda.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        # Auxiliar para interromper o loop - se não houver troca de posição o vetor está ordenado
        trocou = True           # inicia com true só para entrar no loop
        n = len(vetor)          # número de elementos no vetor
        barra = -1                      # posição da barra, inicialmente antes do primeiro elemento

        # loop de passos
        while trocou:
                # reinicializa porque se supõe que neste passo ainda não houve troca
                trocou = False
                # avança a barra em uma posição
                barra += 1

                if imprimir: print(&#39;Passo {}&#39;.format(barra + 1))

                # loop de trocas dentro do passo, até a barra
                for i in range(n - 1, barra, -1):

                        if vetor[i] &lt; vetor[i - 1]:

                                # troca a posição dos dois elementos adjacentes
                                temp = vetor[i]
                                vetor[i] = vetor[i - 1]
                                vetor[i - 1] = temp
                                trocou = True

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.escolhe_metodo"><code class="name flex">
<span>def <span class="ident">escolhe_metodo</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"><p>Retorna o método escolhido para o teste.</p>
<p>Apresenta uma menu de opções para que o usuário escolha o método de ordenação.</p>
<h2 id="opcoes">Opções</h2>
<p>1
- Bolha direto
(bubble sort)
- esquerda-&gt;direita
2
- Bolha invertido (bubble sort)
- direita-&gt;esquerda
3
- Inserção
(insertion sort)
4
- Seleção
(selection sort)
5
- Mesclagem
(merge sort)
- não recursivo
6
- Mesclagem
(merge sort)
- recursivo
7
- Partição
(quick sort)
- recursivo
71 - Partição
(quick sort tail 1) - recursivo
72 - Partição
(quick sort tail 2) - recursivo
9
- Sair do programa</p>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>int</code></dt>
<dd>A escolha do usuário.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def escolhe_metodo():

        &#34;&#34;&#34; Retorna o método escolhido para o teste.

        Apresenta uma menu de opções para que o usuário escolha o método de ordenação.

        Opções:
                1  - Bolha direto    (bubble sort)    - esquerda-&gt;direita
                2  - Bolha invertido (bubble sort)    - direita-&gt;esquerda
                3  - Inserção     (insertion sort)
                4  - Seleção      (selection sort)
                5  - Mesclagem    (merge sort)        - não recursivo
                6  - Mesclagem    (merge sort)        - recursivo
                7  - Partição     (quick sort)        - recursivo
                71 - Partição     (quick sort tail 1) - recursivo
                72 - Partição     (quick sort tail 2) - recursivo
                9  - Sair do programa

        Returns:
                int: A escolha do usuário.
        &#34;&#34;&#34;
        escolha = None

        # Exibição das opções
        print(&#39;_{:-&lt;47}&#39;.format(&#39;&#39;))
        print(&#39;{}&#39;.format(&#39;Escolha do método de ordenação a ser executado:&#39;))
        print(&#39;{:-&lt;47}&#39;.format(&#39;&#39;))
        print(&#39;  1 - Bolha direto    (bubble sort)    - esquerda-&gt;direita&#39;)
        print(&#39;  2 - Bolha invertido (bubble sort)    - direita-&gt;esquerda&#39;)
        print(&#39;  3 - Inserção     (insertion sort)&#39;)
        print(&#39;  4 - Seleção      (selection sort)&#39;)
        print(&#39;  5 - Mesclagem    (merge sort)        - não recursivo&#39;)
        print(&#39;  6 - Mesclagem    (merge sort)        - recursivo&#39;)
        print(&#39;  7 - Partição     (quick sort)        - recursivo&#39;)
        print(&#39; 71 - Partição     (quick sort tail 1) - recursivo&#39;)
        print(&#39; 72 - Partição     (quick sort tail 2) - recursivo&#39;)
        print(&#39;  9 - Sair do programa&#39;)

        # Obtenção, via teclado, da escolha do usuário
        escolha = int(input(&#39;\nInforme a opção desejada: &#39;))

        return escolha</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.escolhe_teste"><code class="name flex">
<span>def <span class="ident">escolhe_teste</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"><p>Retorna o tipo de teste escolhido.</p>
<p>Apresenta uma menu de opções para que o usuário escolha do tipo de teste de carga
para fazer análise de desempenho do método de ordenação escolhido.</p>
<h2 id="opoes">Opões</h2>
<p>1 - Vetor fixo para validação do método de ordenação
2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente
3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente
4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes
5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes
8 - Voltar à escolha do método de ordenação
9 - Sair do programa</p>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>int</code></dt>
<dd>A escolha do usuário.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def escolhe_teste():

        &#34;&#34;&#34; Retorna o tipo de teste escolhido.

        Apresenta uma menu de opções para que o usuário escolha do tipo de teste de carga
        para fazer análise de desempenho do método de ordenação escolhido.

        Opões:
                1 - Vetor fixo para validação do método de ordenação
                2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente
                3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente
                4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes
                5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes
                8 - Voltar à escolha do método de ordenação
                9 - Sair do programa

        Returns:
                int: A escolha do usuário.
        &#34;&#34;&#34;
        escolha = None;

        # Exibição das opções
        print(&#39;\n{:-&lt;41}&#39;.format(&#39;&#39;))
        print(&#39;{}&#39;.format(&#39;Escolha do tipo de teste a ser executado:&#39;))
        print(&#39;{:-&lt;41}&#39;.format(&#39;&#39;))

        print(&#39; 1 - Vetor fixo para validação do método de ordenação&#39;)
        print(&#39; 2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente&#39;)
        print(&#39; 3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente&#39;)
        print(&#39; 4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes&#39;)
        print(&#39; 5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes&#39;)
        print(&#39; 8 - Voltar à escolha do método de ordenação&#39;)
        print(&#39; 9 - Sair do programa&#39;)

        # Obtenção, via teclado, da escolha do usuário
        escolha = int(input(&#39;\nInforme a opção desejada:&#39;))

        return escolha</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.insertion_sort"><code class="name flex">
<span>def <span class="ident">insertion_sort</span></span>(<span>vetor, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da INSERÇÃO - Insertion Sort.</p>
<p>Args:
vetor (list): Vetor a ser ordenado.
n (int): Tamanho da porção do vetor que ainda não está ordenada.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: O vetor fornecido como parâmetro ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def insertion_sort(vetor, imprimir=False):

        &#34;&#34;&#34; Método da INSERÇÃO - Insertion Sort.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        n = len(vetor)          # número de elementos no vetor
        barra = 0                       # posição da barra, inicialmente no primeiro elemento

        # loop de passos
        for passo in range(1, n):

                if imprimir: print(&#39;Passo {}&#39;.format(passo))

                # avança a barra em uma posição
                barra += 1;

                # Corro todos os elementos do fim para trás até a posição da barra,
                # se o vetor[barra] for menor que o antecessor, troco de posição e
                # comparo com anterior seguinte, levando o elemento (se menor) até a sua posição correta
                for i in range(barra, 0, -1):
                        # da barra pra trás, todos os elementos já estão em ordem crescente,
                        # se o elemento for maior que seu antecessor ele já está na posição correta,
                        # posso interromper o loop e ir ao próximo elemento
                        if vetor[i - 1] &lt; vetor[i]:
                                break

                        # troca a posição dos dois elementos adjacentes
                        temp = vetor[i]
                        vetor[i] = vetor[i - 1]
                        vetor[i - 1] = temp

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.main"><code class="name flex">
<span>def <span class="ident">main</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"><p>Método main() - Execução de Testes</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def main():

        &#34;&#34;&#34; Método main() - Execução de Testes &#34;&#34;&#34;

        # Dicionário cujas chaves representam o método de ordenação escolhido
        metodos_ordenacao = {
                1 : &#39;BOLHA (esquerda-&gt;direita)&#39;,
                2 : &#39;BOLHA (direita-&gt;esquerda)&#39;,
                3 : &#39;INSERCAO&#39;,
                4 : &#39;SELECAO&#39;,
                5 : &#39;MESCLAGEM (nao recursivo)&#39;,
                6 : &#39;MESCLAGEM (recursivo)&#39;,
                7 : &#39;QUICKSORT (recursivo)&#39;,
                71: &#39;QUICK_RECURSIVO_CAUDAL_1&#39;,
                72: &#39;QUICK_RECURSIVO_CAUDAL_2&#39;

        }
        # Dicionário cujas chaves representam o tipo de teste de carga escolhido
        tipos_teste = {
                1 : &#39;FIXO&#39;,
                2 : &#39;GRANDE_1_ALEATORIO&#39;,
                3 : &#39;GRANDE_2_ALEATORIO&#39;,
                4 : &#39;GRANDE_1_DECRESCENTE&#39;,
                5 : &#39;GRANDE_2_DECRESCENTE&#39;
        }

        # Montando as opções dos menus
        opcoes_menu_metodo_ordenacao = dict(metodos_ordenacao)          # cópia
        opcoes_menu_metodo_ordenacao.update( { 9 : &#39;SAIR&#39;} )

        opcoes_menu_tipo_teste = dict(tipos_teste)
        opcoes_menu_tipo_teste.update({
                8 : &#39;MUDAR_METODO&#39;,
                9 : &#39;SAIR&#39;
        })


        # Armazenar as escolhas realizadas pelo usuário
        escolhas = {&#39;metodo&#39; : -1, &#39;teste&#39; : -1}

        # OBS|=&gt; Em Python 2.x não é possível atribuir novos valores a variáveis declaradas
        # em um escopo superior; ao tentar fazê-lo o que ocorre é declarar uma nova variável local
        # de mesmo nome. A forma que escolhemos para contornar o problema foi declarar um dicionário
        # e alterar o valor associado a chave. Escopo interno não pode fazer atribuição à variáveis
        # não locais, mas pode modificar objetos (dict) que variáveis não locais se referem.
        #
        # Os dicionários main#escolhas e o acionar_teste#vetor foram utilizados com essa finalidade.
        # Python 3 resolveu esse incoveniente sem ferir o princípio pythônico do -
        # &#34;explicit is better than implicit&#34;, acrescentando as palavras chaves: global e nonlocal.


        # Executar Testes a Partir das Escolhas         --------------------------------------------------------

        # Esta função é utilizada meramente para fazer a interação com o usuário, logo,
        # pertence a camada de apresentação e não deve fazer parte do módulo.
        # Em função do exposto, evitamos a exposição da função #acionar_teste() fazendo
        # sua definição dentro do próprio contexto do método #main().

        def acionar_teste(escolhas):

                vetor = {&#39;vetor&#39;: None}


                # Carregamento do Vetor ------------------------------------------------------------------------

                if escolhas[&#39;teste&#39;] == FIXO:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_FIXO( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_1_ALEATORIO:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_1_ALEATORIO( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_1_DECRESCENTE:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_1_DECRESCENTE( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_2_ALEATORIO:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_2_ALEATORIO( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )

                elif escolhas[&#39;teste&#39;] == GRANDE_2_DECRESCENTE:
                        print(&#39;\nEscolheu teste VETOR {} !&#39;.format( tipos_teste[escolhas[&#39;teste&#39;]] ))
                        vetor[&#39;vetor&#39;] = monta_vetor_GRANDE_2_DECRESCENTE( metodos_ordenacao[escolhas[&#39;metodo&#39;]] )


                # único teste que imprime os passos da ordenação
                eh_teste_fixo = escolhas[&#39;teste&#39;] == FIXO


                # Executando os Testes - Benchmark      ------------------------------------------------------------

                # Ordenação por BOLHA (esquerda-&gt;direita)

                if escolhas[&#39;metodo&#39;] == BOLHA_DIRETO:
                        if eh_teste_fixo:
                                bubble_sort(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                bubble_sort(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por BOLHA (direita-&gt;esquerda)

                elif escolhas[&#39;metodo&#39;] == BOLHA_INVERTIDO:
                        if eh_teste_fixo:
                                bubble_sort_invertido(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                bubble_sort_invertido(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por INSERÇÃO

                elif escolhas[&#39;metodo&#39;] == INSERCAO:
                        if eh_teste_fixo:
                                insertion_sort(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                insertion_sort(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por SELEÇÃO

                elif escolhas[&#39;metodo&#39;] == SELECAO:
                        if eh_teste_fixo:
                                selection_sort(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                selection_sort(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por MESCLAGEM NÃO RECURSIVO

                elif escolhas[&#39;metodo&#39;] == MESCLAGEM_NAO_RECURSIVO:
                        if eh_teste_fixo:
                                merge_sort_full_service(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                merge_sort_full_service(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por MESCLAGEM RECURSIVO

                elif escolhas[&#39;metodo&#39;] == MESCLAGEM_RECURSIVO:
                        if eh_teste_fixo:
                                merge_sort_recursivo(vetor[&#39;vetor&#39;], True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                merge_sort_recursivo(vetor[&#39;vetor&#39;])
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por QUICKSORT (PARTIÇÃO)

                elif escolhas[&#39;metodo&#39;] == QUICK_RECURSIVO:
                        vetor = vetor[&#39;vetor&#39;]
                        inicio = 0
                        fim = len(vetor) - 1
                        if eh_teste_fixo:
                                quick_sort(vetor, inicio, fim, True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                quick_sort(vetor, inicio, fim)
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por QUICKSORT CAUDAL 1 (PARTIÇÃO)

                elif escolhas[&#39;metodo&#39;] == QUICK_RECURSIVO_CAUDAL_1:
                        vetor = vetor[&#39;vetor&#39;]
                        inicio = 0
                        fim = len(vetor) - 1
                        if eh_teste_fixo:
                                quick_sort_tail_1(vetor, inicio, fim, True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                quick_sort_tail_1(vetor, inicio, fim)
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )

                # Ordenação por QUICKSORT CAUDAL 1 (PARTIÇÃO)

                elif escolhas[&#39;metodo&#39;] == QUICK_RECURSIVO_CAUDAL_2:
                        vetor = vetor[&#39;vetor&#39;]
                        inicio = 0
                        fim = len(vetor) - 1
                        if eh_teste_fixo:
                                quick_sort_tail_2(vetor, inicio, fim, True)
                        else:
                                print(&#39;\nOrdenando...&#39;)
                                abre_cronometro = datetime.now()
                                # Aciona ordenação
                                quick_sort_tail_2(vetor, inicio, fim)
                                fecha_cronometro = datetime.now()
                                diferenca = fecha_cronometro - abre_cronometro
                                print(&#39;            Levou {:.3f} segundos para calcular\n&#39;.format(diferenca.total_seconds()) )


        # Loop Principal do Programa    --------------------------------------------------------------------
        # Interação com o usuário através do menu de opções

        while True:
                # Escolha do método de ordenação a ser executado
                escolhas[&#39;metodo&#39;] = escolhe_metodo()

                if escolhas[&#39;metodo&#39;] not in opcoes_menu_metodo_ordenacao:
                        print(&#39;\nOpção INVÁLIDA !  Tente novamente...\n&#39;)

                elif not escolhas[&#39;metodo&#39;] == SAIR:
                        while True:
                                # Escolha do tipo de teste a ser executado
                                escolhas[&#39;teste&#39;] = escolhe_teste()

                                if escolhas[&#39;teste&#39;] == MUDAR_METODO:
                                        print(&#39;\nEscolheu voltar à escolha do método de ordenação !&#39;)
                                        break

                                elif escolhas[&#39;teste&#39;] == SAIR:
                                        print(&#39;\nEscolheu SAIR !\n\n&#39;)
                                        escolhas[&#39;metodo&#39;] = SAIR       # deixar o loop externo saber da intenção
                                        break

                                elif escolhas[&#39;teste&#39;] not in opcoes_menu_tipo_teste:
                                        print(&#39;\nOpção INVÁLIDA !  Tente novamente...\n&#39;)

                                else:
                                        acionar_teste(escolhas)

                # Se pediu pra sair no loop interno, obedeça e saia da execução do programa
                if escolhas[&#39;metodo&#39;] == SAIR:
                        break</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.merge_sort"><code class="name flex">
<span>def <span class="ident">merge_sort</span></span>(<span>metade_esquerda, metade_direita, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da MESCLAGEM - Merge Sort.</p>
<p>Por não ser o recursivo e ordena as duas metades primeiramente para depois mesclar
os elementos em ordem crescente.</p>
<p>Args:
metade_esquerda (list): primeira metade
metade_direita (list): segunda metade
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: Um vetor ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def merge_sort(metade_esquerda, metade_direita, imprimir=False):

        &#34;&#34;&#34; Método da MESCLAGEM - Merge Sort.

        Por não ser o recursivo e ordena as duas metades primeiramente para depois mesclar
        os elementos em ordem crescente.

        Args:
                metade_esquerda (list): primeira metade
                metade_direita (list): segunda metade
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: Um vetor ordenado.
        &#34;&#34;&#34;
        i = j = passo = 0
        tamanho_metade_esquerda = len(metade_esquerda)
        tamanho_metade_direita  = len(metade_direita)

        # Para garantir que as duas metades estejam ordenadas, passamos os vetores pelo Bubble Sort.
        # Se estiverem previamente ordenadas, o método bubble sort vai descobrir em apenas uma
        # passada pelo vetor e retornará rapidamente.
        metade_esquerda = bubble_sort(metade_esquerda, imprimir)
        metade_direita  = bubble_sort(metade_direita,  imprimir)

        # Cria o vetor que receberá os elementos ordenados
        vetor = list(metade_esquerda)
        vetor.extend(metade_direita)


        # Compara as duas metades sequencialmentes e adiciona no vetor de forma crescente.
        # OBS IMPORTANTE|=&gt; as duas metades precisam já estarem ordenadas

        while passo &lt; (tamanho_metade_esquerda + tamanho_metade_direita):

                if imprimir: print(&#39;Passo {}&#39;.format(passo + 1))

                # Comparo os elementos de ambos os lados
                if metade_esquerda[i] &lt;= metade_direita[j]:
                        # guardo o de menor valor que está do lado esquerdo
                        vetor[passo] = metade_esquerda[i]
                        # ando pra frente no vetor do lado esquerdo
                        i += 1
                        # se já terminei de fazer comparações com a primeira metade, do lado esquerdo
                        if i == tamanho_metade_esquerda:
                                # copio o resto dos elementos da segunda metade do lado direito
                                while j &lt; tamanho_metade_direita:
                                        passo += 1
                                        vetor[passo] = metade_direita[j]
                                        j += 1
                else:
                        # guardo o de menor valor que está do lado direito
                        vetor[passo] = metade_direita[j]
                        # ando pra frente no vetor do lado direito
                        j += 1
                        # se já terminei a segunda metade, do lado direito
                        if j == tamanho_metade_direita:
                                # copio os elementos restantes da metade esquerda
                                while i &lt; tamanho_metade_esquerda:
                                        passo += 1
                                        vetor[passo] = metade_esquerda[i]
                                        i += 1

                passo += 1

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.merge_sort_full_service"><code class="name flex">
<span>def <span class="ident">merge_sort_full_service</span></span>(<span>vetor, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da MESCLAGEM - Merge Sort.</p>
<p>Divide o vetor em duas metades e invoca o #merge_sort() para fazer efetivamente a ordenação.</p>
<p>Args:
vetor (list): Vetor que será ordenado.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: Um novo vetor ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def merge_sort_full_service(vetor, imprimir=False):

        &#34;&#34;&#34; Método da MESCLAGEM - Merge Sort.

        Divide o vetor em duas metades e invoca o #merge_sort() para fazer efetivamente a ordenação.

        Args:
                vetor (list): Vetor que será ordenado.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: Um novo vetor ordenado.
        &#34;&#34;&#34;
        tamanho = len(vetor)
        meio = int(tamanho / 2)
        metade_esquerda = vetor[:meio]
        metade_direita  = vetor[meio:tamanho]

        if imprimir:
                print(&#39;metade_esquerda: {}&#39;.format(metade_esquerda))
                print(&#39;metade_direita:  {}&#39;.format(metade_direita))

        # retorna um novo vetor ordenado
        return merge_sort(metade_esquerda, metade_direita, imprimir)</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.merge_sort_recursivo"><code class="name flex">
<span>def <span class="ident">merge_sort_recursivo</span></span>(<span>vetor, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da MESCLAGEM - Merge Sort - Versão Recursiva.</p>
<p>Divide o vetor em duas metades e invoca o merge_sort recursivamente para fazer efetivamente a ordenação.</p>
<p>Args:
vetor (list): Vetor que será ordenado.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: O vetor ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def merge_sort_recursivo(vetor, imprimir=False):

        &#34;&#34;&#34; Método da MESCLAGEM - Merge Sort - Versão Recursiva.

        Divide o vetor em duas metades e invoca o merge_sort recursivamente para fazer efetivamente a ordenação.

        Args:
                vetor (list): Vetor que será ordenado.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor ordenado.
        &#34;&#34;&#34;
        if imprimir: print(&#39;ENTRADA - Elementos do vetor: {}&#39;.format(vetor))

        tamanho = len(vetor)

        # CASO BASE: tamanho == 1 (nada a fazer)
        if tamanho == 1:
                return vetor

        # RECURSÃO

        meio = int(tamanho / 2)
        metade_esquerda = vetor[:meio]
        metade_direita  = vetor[meio:tamanho]

        tamanho_metade_esquerda = len(metade_esquerda)
        tamanho_metade_direita = len(metade_direita)


        if imprimir:
                print(&#39;ENTRADA - Elementos da metade esquerda: {}&#39;.format(metade_esquerda))
                print(&#39;ENTRADA - Elementos da metade direita:  {}\n&#39;.format(metade_direita))


        # Recursividade - Aciona a ordenação recursiva para cada metade

        metade_esquerda = merge_sort_recursivo(metade_esquerda, imprimir)
        metade_direita = merge_sort_recursivo(metade_direita, imprimir)


        # Mescla as metades, reconstruindo o vetor ordenadamente

        i = j = passo = 0

        while passo &lt; tamanho:

                if imprimir: print(&#39;Passo {}&#39;.format(passo + 1))

                # Comparo os elementos de ambos os lados
                if metade_esquerda[i] &lt;= metade_direita[j]:
                        # guardo o de menor valor que está do lado esquerdo
                        vetor[passo] = metade_esquerda[i]
                        # ando pra frente no vetor do lado esquerdo
                        i += 1
                        # se já terminei de fazer comparações com a primeira metade do lado esquerdo
                        if i == tamanho_metade_esquerda:
                                # copio o resto dos elementos da segunda metade do lado direito que já estão ordenados
                                while j &lt; tamanho_metade_direita:
                                        passo += 1
                                        vetor[passo] = metade_direita[j]
                                        j += 1
                else:
                        # guardo o de menor valor que está do lado direito
                        vetor[passo] = metade_direita[j]
                        # ando pra frente no vetor do lado direito
                        j += 1
                        # Se já terminei a segunda metade, é porque já copie todos os elementos do lado direito
                        # para o vetor final ordenado e todos os demais restantes do lado esquerdo são valores maiores.
                        # Não há mais nenhum elemento do lado direito que seja menor que do lado esquerdo.
                        if j == tamanho_metade_direita:
                                # copio os elementos restantes da metade esquerda
                                while i &lt; tamanho_metade_esquerda:
                                        passo += 1
                                        vetor[passo] = metade_esquerda[i]
                                        i += 1

                passo += 1

        if imprimir: print(&#39;\nSAÍDA - Elementos do vetor: {}\n&#39;.format(vetor))

        # retorna o vetor ordenado
        return vetor</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.monta_vetor_FIXO"><code class="name flex">
<span>def <span class="ident">monta_vetor_FIXO</span></span>(<span>metodo_ordenacao)</span>
</code></dt>
<dd>
<div class="desc"><p>Procedimento que monta o VETOR FIXO e o imprime antes da ordenação.</p>
<pre><code>Args:
        metodo_ordenacao (str): O nome do método.
</code></pre>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>list</code></dt>
<dd>Um vetor pequeno para validação dos métodos.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def monta_vetor_FIXO(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR FIXO e o imprime antes da ordenação.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor pequeno para validação dos métodos.
        &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor V1 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        V1 = [89, 44, 75, 66, 11, 38, 93, 56]

        #V1 = [3,0,1,8,7,2,5,4,9,6]      # vetor da dança húngara: https://www.youtube.com/watch?v=ywWBy6J5gz8

        print(&#39;Valor de V1: {}&#39;.format(V1))

        return V1</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.monta_vetor_GRANDE_1_ALEATORIO"><code class="name flex">
<span>def <span class="ident">monta_vetor_GRANDE_1_ALEATORIO</span></span>(<span>metodo_ordenacao)</span>
</code></dt>
<dd>
<div class="desc"><p>Procedimento que monta o VETOR GRANDE 1 e o preenche com números aleatórios.</p>
<pre><code>Args:
        metodo_ordenacao (str): O nome do método.
</code></pre>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>list</code></dt>
<dd>Um vetor de 20.000 elementos aleatórios.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def monta_vetor_GRANDE_1_ALEATORIO(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 1 e o preenche com números aleatórios.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 20.000 elementos aleatórios.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T1 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T1=[]
        for i in range(20000):
                T1.append( random.randint(1, 20000) )

        print(&#39;\nVocê escolheu gerar vetores com números aleatórios !&#39;)
        print(&#39;Primeiro elemento de T1: {}&#39;.format( T1[0] ))
        print(&#39;Último   elemento de T1: {}&#39;.format( T1[19999] ))

        return T1</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.monta_vetor_GRANDE_1_DECRESCENTE"><code class="name flex">
<span>def <span class="ident">monta_vetor_GRANDE_1_DECRESCENTE</span></span>(<span>metodo_ordenacao)</span>
</code></dt>
<dd>
<div class="desc"><p>Procedimento que monta o VETOR GRANDE 1 e o preenche com números decrescentes.</p>
<pre><code>Args:
        metodo_ordenacao (str): O nome do método.
</code></pre>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>list</code></dt>
<dd>Um vetor de 20.000 elementos em ordem descrescente.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def monta_vetor_GRANDE_1_DECRESCENTE(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 1 e o preenche com números decrescentes.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 20.000 elementos em ordem descrescente.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T1 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T1=[]
        for i in range(20000):
                T1.append(20000 - i)

        print(&#39;\nVocê escolheu gerar vetores com números decrescentes !&#39;)
        print(&#39;Primeiro elemento de T1: {}&#39;.format( T1[0] ))
        print(&#39;Último   elemento de T1: {}&#39;.format( T1[19999] ))

        return T1</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.monta_vetor_GRANDE_2_ALEATORIO"><code class="name flex">
<span>def <span class="ident">monta_vetor_GRANDE_2_ALEATORIO</span></span>(<span>metodo_ordenacao)</span>
</code></dt>
<dd>
<div class="desc"><p>Procedimento que monta o VETOR GRANDE 2 e o preenche com números aleatórios.</p>
<pre><code>Args:
        metodo_ordenacao (str): O nome do método.
</code></pre>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>list</code></dt>
<dd>Um vetor de 40.000 elementos aleatórios.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def monta_vetor_GRANDE_2_ALEATORIO(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 2 e o preenche com números aleatórios.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 40.000 elementos aleatórios.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T2 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T2=[]
        for i in range(40000):
                T2.append( random.randint(1, 40000) )

        print(&#39;\nVocê escolheu gerar vetores com números aleatórios !&#39;)
        print(&#39;Primeiro elemento de T2: {}&#39;.format( T2[0] ))
        print(&#39;Último   elemento de T2: {}&#39;.format( T2[39999] ))

        return T2</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.monta_vetor_GRANDE_2_DECRESCENTE"><code class="name flex">
<span>def <span class="ident">monta_vetor_GRANDE_2_DECRESCENTE</span></span>(<span>metodo_ordenacao)</span>
</code></dt>
<dd>
<div class="desc"><p>Procedimento que monta o VETOR GRANDE 2 e o preenche com números decrescentes.</p>
<pre><code>Args:
        metodo_ordenacao (str): O nome do método.
</code></pre>
<h2 id="returns">Returns</h2>
<dl>
<dt><code>list</code></dt>
<dd>Um vetor de 40.000 elementos em ordem descrescente.</dd>
</dl></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def monta_vetor_GRANDE_2_DECRESCENTE(metodo_ordenacao):

        &#34;&#34;&#34; Procedimento que monta o VETOR GRANDE 2 e o preenche com números decrescentes.

        Args:
                metodo_ordenacao (str): O nome do método.

    Returns:
      list: Um vetor de 40.000 elementos em ordem descrescente.
    &#34;&#34;&#34;
        print(&#39;\n------------------------------------&#39;)
        print(&#39;Inicializando dados do vetor T2 para: {}&#39;.format(metodo_ordenacao))
        print(&#39;------------------------------------&#39;)

        T2=[]
        for i in range(40000):
                T2.append(40000 - i)

        print(&#39;\nVocê escolheu gerar vetores com números decrescentes !&#39;)
        print(&#39;Primeiro elemento de T2: {}&#39;.format( T2[0] ))
        print(&#39;Último   elemento de T2: {}&#39;.format( T2[39999] ))

        return T2</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.particionar"><code class="name flex">
<span>def <span class="ident">particionar</span></span>(<span>vetor, inicio, fim, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Particionador do Quick Sort</p>
<p>Pega o elemento do vetor cujo indice(posição) é dado por 'inicio', <code>vetor[inicio]</code>,
e encontra a posição correta do elemento e retorna o índice referente a posição correta.
Chamaremos este elemento que estamos procurando sua posição simplesmente de 'elemento_investigado'.</p>
<p>O algoritmo usa duas barras para correr o vetor no intevalo dos índices [inicio ao fim(inclusive)].
A barra da extremidade esquerda avança para a direita até encontrar o elemento subsequente que seja
maior que o elemento_investigado. A barra da direita recua para a esquerda até encontrar
um elemento que seja menor que o elemento_investigado. Nessa situação, teremos::</p>
<pre><code>      elemento_esquerda &gt; elemento_investigado &gt; elemento_direita, logo,
      elemento_esquerda &gt; elemento_direita
</code></pre>
<p>isto é, está fora de ordem, e o algoritmo já os troca de posição ordenando-os, depois prossegue
em direção ao centro até as barras volantes se encontrarem.</p>
<p>A condição de parada ocorre quando a barra da esquerda atropela a direita, ficando com um valor maior.
A barra da direita estará com o índice da posição correta, sendo ele o valor retornado pela função.</p>
<p>Sinteticamente expresso de uma maneira formal matemática seria::</p>
<pre><code>      Recebe vetor v[p..r] com p &lt; r. Rearranja os elementos do vetor e
      devolve j em p..r tal que v[p..j-1] &lt;= v[j] &lt; v[j+1..r].
</code></pre>
<p>Args:
vetor (list): Vetor que será ordenado e particionado logicamente.
inicio(int): Índice inicial do intervalo de pesquisa e que determina o elemento cuja posição
correta será retornada como a posição do particionamento.
fim(int): Índice final do intervalo de pesquisa.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
int: A posição do particionamento do vetor.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def particionar(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Particionador do Quick Sort

        Pega o elemento do vetor cujo indice(posição) é dado por &#39;inicio&#39;, ``vetor[inicio]``,
        e encontra a posição correta do elemento e retorna o índice referente a posição correta.
        Chamaremos este elemento que estamos procurando sua posição simplesmente de &#39;elemento_investigado&#39;.

        O algoritmo usa duas barras para correr o vetor no intevalo dos índices [inicio ao fim(inclusive)].
        A barra da extremidade esquerda avança para a direita até encontrar o elemento subsequente que seja
        maior que o elemento_investigado. A barra da direita recua para a esquerda até encontrar
        um elemento que seja menor que o elemento_investigado. Nessa situação, teremos::

                elemento_esquerda &gt; elemento_investigado &gt; elemento_direita, logo,
                elemento_esquerda &gt; elemento_direita

        isto é, está fora de ordem, e o algoritmo já os troca de posição ordenando-os, depois prossegue
        em direção ao centro até as barras volantes se encontrarem.

        A condição de parada ocorre quando a barra da esquerda atropela a direita, ficando com um valor maior.
        A barra da direita estará com o índice da posição correta, sendo ele o valor retornado pela função.

        Sinteticamente expresso de uma maneira formal matemática seria::

                Recebe vetor v[p..r] com p &lt; r. Rearranja os elementos do vetor e
                devolve j em p..r tal que v[p..j-1] &lt;= v[j] &lt; v[j+1..r].

        Args:
                vetor (list): Vetor que será ordenado e particionado logicamente.
                inicio(int): Índice inicial do intervalo de pesquisa e que determina o elemento cuja posição
                correta será retornada como a posição do particionamento.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      int: A posição do particionamento do vetor.
        &#34;&#34;&#34;
        elemento = vetor[inicio]                # ..a ser investigado qual o seu posicionamento correto no vetor
        barra_esquerda = inicio + 1             # posicionada no elemento adjacente seguinte
        barra_direita = fim                             # posicionada no último elemento

        while barra_esquerda &lt;= barra_direita:

                # Encontra o elemento subsequente que seja maior que o elemento investigado
                if vetor[barra_esquerda] &lt;= elemento:
                        barra_esquerda += 1

                # Encontra, do fim para o começo, o elemento que seja menor que o elemento investigado
                elif vetor[barra_direita] &gt; elemento:
                        barra_direita -= 1

                # |=&gt; vetor[barra_direita] &lt;= elemento &lt; vetor[barra_esquerda] =&gt;
                # logo, vetor[barra_direita] &lt; vetor[barra_esquerda], isto é, está fora da ordem crescente,
                # o menor tem de ficar a esquerda e o maior a direita, vamos trocá-los de posição
                else:
                        temp = vetor[barra_esquerda]
                        vetor[barra_esquerda] = vetor[barra_direita]
                        vetor[barra_direita] = temp
                        # A posição correta do elemento investigado está entre as barras, continuando a procura
                        barra_esquerda += 1             # avança uma posição
                        barra_direita  -= 1             # recua  uma posição

        # A posição correta do elemento é dado pela barra_direita
        posicao_correta = barra_direita

        # Vamos trocar de posição, fazendo backup do elemento que está ocupando o lugar
        # do nosso elemento investigado para o início do vetor
        vetor[inicio] = vetor[posicao_correta]
        vetor[posicao_correta] = elemento               # copia o elemento para sua posição correta

        if imprimir: print(&#39;\nValor de V1: {}&#39;.format(vetor))


        return posicao_correta</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.quick_sort"><code class="name flex">
<span>def <span class="ident">quick_sort</span></span>(<span>vetor, inicio, fim, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Quick Sort - Recursão comum.</p>
<p>Recebe um vetor vetor[inicio..fim], com inicio &lt;= fim + 1,
e rearranja o vetor em ordem crescente.</p>
<p>Args:
vetor (list): Vetor que será ordenado.
inicio(int): Índice inicial do intervalo de pesquisa.
fim(int): Índice final do intervalo de pesquisa.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
None: Nada retorna. Opera diretamente com a referência do vetor.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def quick_sort(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Quick Sort - Recursão comum.

        Recebe um vetor vetor[inicio..fim], com inicio &lt;= fim + 1,
        e rearranja o vetor em ordem crescente.

        Args:
                vetor (list): Vetor que será ordenado.
                inicio(int): Índice inicial do intervalo de pesquisa.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      None: Nada retorna. Opera diretamente com a referência do vetor.
        &#34;&#34;&#34;
        posicao_correta_elemento_inicio = -1

        if inicio &lt; fim:        # indices
                posicao_particao = particionar(vetor, inicio, fim, imprimir)

                # partição esquerda
                quick_sort(vetor, inicio, posicao_particao - 1, imprimir)
                # partição direita
                quick_sort(vetor, posicao_particao + 1, fim, imprimir)</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.quick_sort_tail_1"><code class="name flex">
<span>def <span class="ident">quick_sort_tail_1</span></span>(<span>vetor, inicio, fim, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Quick Sort Recursivo Caudal - Versão 1</p>
<p>A recursividade ocorre em uma partição de cada vez.</p>
<p>Args:
vetor (list): Vetor que será ordenado.
inicio(int): Índice inicial do intervalo de pesquisa.
fim(int): Índice final do intervalo de pesquisa.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
None: Nada retorna. Opera diretamente com a referência do vetor.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def quick_sort_tail_1(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Quick Sort Recursivo Caudal - Versão 1

        A recursividade ocorre em uma partição de cada vez.

        Args:
                vetor (list): Vetor que será ordenado.
                inicio(int): Índice inicial do intervalo de pesquisa.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      None: Nada retorna. Opera diretamente com a referência do vetor.
        &#34;&#34;&#34;
        while inicio &lt; fim:

                posicao_particao = particionar(vetor, inicio, fim, imprimir)

                # Ordena SEPARADAMENTE elementos &#39;antes&#39; e &#39;depois&#39; da partição
                quick_sort_tail_1(vetor, inicio, posicao_particao - 1, imprimir)

                inicio = posicao_particao + 1</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.quick_sort_tail_2"><code class="name flex">
<span>def <span class="ident">quick_sort_tail_2</span></span>(<span>vetor, inicio, fim, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Quick Sort Recursivo Caudal - Versão 2</p>
<p>Melhor otimizada em relação a memória, a recursividade ocorre em apenas uma partição, e esta
partição é a menor, fazendo com que a profundidade das chamadas recursivas seja mais rasa.</p>
<p>Requer espaço auxiliar O(Log n) no pior caso.</p>
<p>Args:
vetor (list): Vetor que será ordenado.
inicio(int): Índice inicial do intervalo de pesquisa.
fim(int): Índice final do intervalo de pesquisa.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
None: Nada retorna. Opera diretamente com a referência do vetor.</p>
<p>.. _See below link for complete running code:
<a href="https://ide.geeksforgeeks.org/qrlM31">https://ide.geeksforgeeks.org/qrlM31</a></p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def quick_sort_tail_2(vetor, inicio, fim, imprimir=False):

        &#34;&#34;&#34; Quick Sort Recursivo Caudal - Versão 2

        Melhor otimizada em relação a memória, a recursividade ocorre em apenas uma partição, e esta
        partição é a menor, fazendo com que a profundidade das chamadas recursivas seja mais rasa.

        Requer espaço auxiliar O(Log n) no pior caso.

        Args:
                vetor (list): Vetor que será ordenado.
                inicio(int): Índice inicial do intervalo de pesquisa.
                fim(int): Índice final do intervalo de pesquisa.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      None: Nada retorna. Opera diretamente com a referência do vetor.


        .. _See below link for complete running code:
                https://ide.geeksforgeeks.org/qrlM31
        &#34;&#34;&#34;
        while inicio &lt; fim:

                posicao_particao = particionar(vetor, inicio, fim, imprimir)

                # Se parte à esquerda é menor, tratá-la recursivamente
                # e lidar com a parte à dreita iterativamente &#39;while&#39;
                if posicao_particao - inicio &lt; fim - posicao_particao:

                        quick_sort_tail_2(vetor, inicio, posicao_particao - 1, imprimir)

                        inicio = posicao_particao + 1

                # Caso contrário: recursão à direita, iteração à esquerda
                else:
                        quick_sort_tail_2(vetor, posicao_particao + 1, fim, imprimir)

                        fim = posicao_particao - 1</code></pre>
</details>
</dd>
<dt id="MetodosOrdenacao.selection_sort"><code class="name flex">
<span>def <span class="ident">selection_sort</span></span>(<span>vetor, imprimir=False)</span>
</code></dt>
<dd>
<div class="desc"><p>Método da SELEÇÃO - Selection Sort.</p>
<p>Args:
vetor (list): Vetor a ser ordenado.
n (int): Tamanho da porção do vetor que ainda não está ordenada.
imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
Defaults to False.</p>
<p>Returns:
list: O vetor fornecido como parâmetro ordenado.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def selection_sort(vetor, imprimir=False):

        &#34;&#34;&#34; Método da SELEÇÃO - Selection Sort.

        Args:
                vetor (list): Vetor a ser ordenado.
                n (int): Tamanho da porção do vetor que ainda não está ordenada.
                imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
                Defaults to False.

        Returns:
      list: O vetor fornecido como parâmetro ordenado.
        &#34;&#34;&#34;
        # Variáveis auxiliares
        indice_menor = -1
        n = len(vetor)          # número de elementos no vetor
        barra = -1                      # posição da barra, inicialmente antes do primeiro elemento


        # loop de passos
        for passo in range(1, n):

                if imprimir: print(&#39;Passo {}&#39;.format(passo))

                # avança a barra em uma posição
                barra += 1;
                # encontra o menor valor dentre os elementos não ordenados
                menor = vetor[barra]
                indice_menor = barra
                for i in range(barra + 1, n):
                        if vetor[i] &lt; menor:
                                menor = vetor[i]
                                indice_menor = i

                # troca o menor com o elemento ao lado direito da barra
                vetor[indice_menor] = vetor[barra]
                vetor[barra] = menor

                if imprimir: print(&#39;Valor de V1: {}&#39;.format(vetor))

        # retorna vetor ordenado
        return vetor</code></pre>
</details>
</dd>
</dl>
</section>
<section>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="MetodosOrdenacao.bubble_sort" href="#MetodosOrdenacao.bubble_sort">bubble_sort</a></code></li>
<li><code><a title="MetodosOrdenacao.bubble_sort_invertido" href="#MetodosOrdenacao.bubble_sort_invertido">bubble_sort_invertido</a></code></li>
<li><code><a title="MetodosOrdenacao.escolhe_metodo" href="#MetodosOrdenacao.escolhe_metodo">escolhe_metodo</a></code></li>
<li><code><a title="MetodosOrdenacao.escolhe_teste" href="#MetodosOrdenacao.escolhe_teste">escolhe_teste</a></code></li>
<li><code><a title="MetodosOrdenacao.insertion_sort" href="#MetodosOrdenacao.insertion_sort">insertion_sort</a></code></li>
<li><code><a title="MetodosOrdenacao.main" href="#MetodosOrdenacao.main">main</a></code></li>
<li><code><a title="MetodosOrdenacao.merge_sort" href="#MetodosOrdenacao.merge_sort">merge_sort</a></code></li>
<li><code><a title="MetodosOrdenacao.merge_sort_full_service" href="#MetodosOrdenacao.merge_sort_full_service">merge_sort_full_service</a></code></li>
<li><code><a title="MetodosOrdenacao.merge_sort_recursivo" href="#MetodosOrdenacao.merge_sort_recursivo">merge_sort_recursivo</a></code></li>
<li><code><a title="MetodosOrdenacao.monta_vetor_FIXO" href="#MetodosOrdenacao.monta_vetor_FIXO">monta_vetor_FIXO</a></code></li>
<li><code><a title="MetodosOrdenacao.monta_vetor_GRANDE_1_ALEATORIO" href="#MetodosOrdenacao.monta_vetor_GRANDE_1_ALEATORIO">monta_vetor_GRANDE_1_ALEATORIO</a></code></li>
<li><code><a title="MetodosOrdenacao.monta_vetor_GRANDE_1_DECRESCENTE" href="#MetodosOrdenacao.monta_vetor_GRANDE_1_DECRESCENTE">monta_vetor_GRANDE_1_DECRESCENTE</a></code></li>
<li><code><a title="MetodosOrdenacao.monta_vetor_GRANDE_2_ALEATORIO" href="#MetodosOrdenacao.monta_vetor_GRANDE_2_ALEATORIO">monta_vetor_GRANDE_2_ALEATORIO</a></code></li>
<li><code><a title="MetodosOrdenacao.monta_vetor_GRANDE_2_DECRESCENTE" href="#MetodosOrdenacao.monta_vetor_GRANDE_2_DECRESCENTE">monta_vetor_GRANDE_2_DECRESCENTE</a></code></li>
<li><code><a title="MetodosOrdenacao.particionar" href="#MetodosOrdenacao.particionar">particionar</a></code></li>
<li><code><a title="MetodosOrdenacao.quick_sort" href="#MetodosOrdenacao.quick_sort">quick_sort</a></code></li>
<li><code><a title="MetodosOrdenacao.quick_sort_tail_1" href="#MetodosOrdenacao.quick_sort_tail_1">quick_sort_tail_1</a></code></li>
<li><code><a title="MetodosOrdenacao.quick_sort_tail_2" href="#MetodosOrdenacao.quick_sort_tail_2">quick_sort_tail_2</a></code></li>
<li><code><a title="MetodosOrdenacao.selection_sort" href="#MetodosOrdenacao.selection_sort">selection_sort</a></code></li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>
