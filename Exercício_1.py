# Código feito por: Mariana Lopes Camilo (RA:2058804)

# Importando biblioteca de matemática (math) e biblioteca para plotar os gráficos (matplotlib), numpy para funções de
# arranjo de vetores e pandas para fazer a tabela.

import math
import numpy as np
import matplotlib.pyplot as plt
import pandas

# Vamos definir os valores dados no enunciado do exercício

N = 100  # número de iterações
w = 5  # largura da comporta em metros
R = 4  # raio do quarto de cilindro em metros
ro = 850  # gravidade específica do óleo em Kg/m³
g = float(9.81)  # aceleração da gravidade
pi = math.pi  # valor de pi proveniente da biblioteca math

fv = "ro*g*(R**2)*w*(math.sin(math.radians(x))-(math.sin(math.radians(x)))**2)"  # Função da Força Vertical obtida
# analiticamente, transformei em string pois a função eval(), que avaliará a expressão, usa strings
fh = "ro*g*(R**2)/3*(x)"

# Aqui vou deixar já criados os vetores para a apresentação da tabela:
Nt = []
deltax = []
FV = []
FH = []
F_total = []
Erro = []
F_analitica = 362963.83  # Força analítica disponível no PDF

# Método dos trapézios para a Força Vertical: O código utiliza o tamanho do passo, ou seja, h, para fazer a conta.
# Como o exercício pede um número N de iterações, definirei h = (xM-x0)/N

# Toda vez que i aparece no código, é usado como variável de iteração dos while's.
i = 0
while i < N:  # iteração para montar a tabela de 0 < N < 101
    x0 = float(0)  # limite inferior é x=0
    xM = float(pi / 2)  # limite superior é x= pi/2
    x = x0  # x inicial
    h = (xM - x0) / (i+1)
    integral = 0  # início da contagem
    integral += eval(fv)
    x += h

    while x < xM:
        integral += 2 * eval(fv)
        x += h
    x = xM
    integral += eval(fv)
    integral *= (h / 2)
    deltax.append(h)
    FV.append(integral)
    i += 1
    # Quando faço .append, estou adicionando o valor da integral nesse N e adicionando-o à lista de
    # vetores dos deltax, o mesmo para a força vertical.

# Método dos trapézios para a Força Horizontal:
i = 0
while i < N:
    x0 = float(0)  # limite inferior é x = 0
    xM = float(4)  # limite superior é x= 4
    x = x0  # x inicial
    h = (xM - x0) / (i+1)
    integral = 0  # início da contagem
    integral += eval(fh)
    x += h

    while x < xM:
        integral += 2 * eval(fh)
        x += h
    x = xM
    integral += eval(fh)
    integral *= (h / 2)
    FH.append(integral)
    i += 1

# Calcular as Forças resulantes para todos os N's e os Erros

# Aqui, utilizo a mesma função append para calcular a força resultante e o erro através de cada valor de cada vetor
# de Fv e Fh.
i = 0
while i < N:
    F_total.append(np.sqrt(np.power(FV[i], 2) + np.power(FH[i], 2)))
    Erro.append(abs(F_total[i] - F_analitica) * 100 / F_total[i])
    i += 1
dados = [np.arange(1, N + 1, 1), deltax, FH, FV, F_total, Erro]


# Esta é uma função para obter a transposta de uma matriz,
# fonte: https://www.codegrepper.com/code-examples/python/transpose+matrix+in+python+without+numpy
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T


dados = transpose(dados)
colunas = ['N', 'deltax', 'FH', 'FV', 'F', 'E %']

# df é a tabela

df = pandas.DataFrame(data=dados, columns=colunas)
print(df)
tfile = open('table.txt', 'a')  # Salva a tabela como .txt
tfile.write(df.to_string())
tfile.close()


# PLOT DO ERRO
x = deltax
y = Erro
plt.xlabel('Δx')
plt.ylabel('E %')
plt.title('Erro')
plt.plot(x,y)
plt.show()
