#eu alterei
import random


class House():
    def __init__(self, position) -> None:
        #alterar essa para uma matriz onde as casas sao as colunas(j) e os dados da casa sao as linhas(i) assim da para usar o i * m + j
        self.data = {"color": None, "nationality": None, "drink": None, "smoke": None, "pet": None }
        self.data["position"] = str(position) if str(position) is not None else None

    def Discribe(self):
        #impressao das casas, vai alterar tbm pq nao sei se faz sentido isso aqui
        pos = self.data["position"]
        col = self.data["color"]
        prs = self.data["person"]
        pet = self.data["pet"]
        drk = self.data["drink"]
        smk = self.data["smoke"]
        print("House #" + str(pos) + ":\t" + col + ",\t" + prs + ",\t" + pet + ",\t" + drk + ",\t" + smk)
    
    def isEmpty(self):
        if not None in self.data.values():
            return False
        else:
            return True


def Init_population(population, genAtual):
    '''
    for i in range(population):
        for j in range(pos):        
            gerar col
            gerar prs
            gerar pet
            gerar drk
            gerar smk

    '''
    pass

def Evaluation(population, genAtual):
    '''
    avaliar de acordo as perguntas
    '''
    pass
def SelectParent(population, currGen):
    '''
    salvar os iram fazer parte da proxima geracao
    '''
    pass
def CrossOver(population, currGen):
    '''
    fazer a trocar uniform
    '''
    pass
def Mutation(population, currGen):
    '''
    se ocorrer alterar alguns valores de posicao
    1 forma da mutacao permutar um parametro
    selacaoDaCasa = Rng()
    selacaoDoTipo = Rng()
    posicaoDaTroca = selacaoDoTipo * m + selacaoDeCasa
    trocaDeDado = Rng()
    temp = House.data[posicaoDaTroca]
    for i in range(4):        
        if House.data[selacaoDoTipo * m + i] == trocaDado :
            House.data[posicaoDaTroca] = House.data[selacaoDoTipo * m + i]
            House.data[selacaoDoTipo * m + i] = temp
            break

    2 forma troca todos os parametro da de um tipo
    selacaoDoTipo = Rng()
    []valores = {0,1,2,3}
    valores.embaralhar
    for i in range(4):
         House.data[selacaoDoTipo * m + i] = valores[i]
    '''     
    pass     
def Suvivors(population, currGen):
    '''
    pegar as melhores avaliacoes
    '''
    pass

def main():
    currGen = 0
    lastGen = 100
    population = 100
    Init_population(population, currGen)
    Evaluation(population, currGen)
    while currGen == lastGen:
        currGen = currGen + 1
        SelectParent(population, currGen)
        CrossOver(population, currGen)
        Mutation(population, currGen)
        Evaluation(population, currGen)
        Suvivors(population, currGen)
    
def Rng():
    return random(0,4)


if __name__ == '__main__':
    main()