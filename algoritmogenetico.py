#eu alterei
import random
import StopWatch as st
from functools import cmp_to_key
class House:
    def __init__(self):
        #alterar essa para uma matriz onde as casas sao as colunas(j) e os dados da casa sao as linhas(i) assim da para usar o i * m + j
        self.matriz = matriz = []
        self.ponto = 0        
        
        
        '''
        self.data = {"color": None, "nationality": None, "drink": None, "smoke": None, "pet": None }
        self.data["position"] = str(position) if str(position) is not None else None
        self.matriz = matriz = []
        '''
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

def compare( this, other):
        if(this.ponto < other.ponto):
            return -1
        if(this.ponto == other.ponto):
            return 0
        if(this.ponto > other.ponto):
            return 1

const_list = [0,1,2,3,4]
individuo = []

def Init_population(population, genAtual):
    
    for i in range(0, population):
        individuo.insert(i, House())
        for linha in range(5):
            valores = random.sample(const_list, len(const_list))
            for coluna in range(5):        
                individuo[i].matriz.append(valores[coluna])
                '''
                gerar col
                gerar prs
                gerar pet
                gerar drk
                gerar smk
                '''
    '''
    '''
    
    pass

def Col_Color():
    return 0 * 5
def Col_Nacionality():
    return 1 * 5
def Col_Drink():
    return 2 * 5
def Col_Smoke():
    return 3 * 5
def Col_Pet():
    return 4 * 5
def getHouseByColor (individuo, k, color):
        for i in range(5):
            if(individuo[k].matriz[0* 5 + i] == color):
                return i
def getHouseByNacionality (individuo, k, nacionality):
        for i in range(5):
            if(individuo[k].matriz[1* 5 + i] == nacionality):
                return i

def getHouseByDrink (individuo, k, drink):
        for i in range(5):
            if(individuo[k].matriz[2* 5 + i] == drink):
                return i
def getHouseBySmoke (individuo, k, smoke):
        for i in range(5):
            if(individuo[k].matriz[3* 5 + i] == smoke):
                return i
def getHouseByPet (individuo, k, pet):
        for i in range(5):
            if(individuo[k].matriz[4* 5 + i] == pet):
                return i
def Evaluation(population, genAtual):
    for i in range(population):
        individuo[i].ponto = 0
        # O Norueguês vive na primeira casa.
        if(individuo[i].matriz[Col_Nacionality() + 0]== 3):
            individuo[i].ponto = individuo[i].ponto +1
        # O Inglês vive na casa Vermelha.
        if (individuo[i].matriz[Col_Nacionality() + getHouseByColor(individuo,i,4)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
        # O Sueco tem Cachorros como animais de estimação.
        if (individuo[i].matriz[Col_Pet() + getHouseByNacionality(individuo,i,4)] == 0) :
            individuo[i].ponto = individuo[i].ponto +1
        # O Dinamarquês bebe Chá.
        if (individuo[i].matriz[Col_Drink() + getHouseByNacionality(individuo,i,1)] == 3):
            individuo[i].ponto = individuo[i].ponto +1
        # A casa Verde fica do lado esquerdo da casa Branca.
        if (individuo[i].matriz[Col_Color() + getHouseByColor(individuo,i,3)+ 1] == 2):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que vive na casa Verde bebe Café.
        if (individuo[i].matriz[Col_Drink() + getHouseByColor(individuo,i,3)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que fuma Pall Mall cria Pássaros.
        if (individuo[i].matriz[Col_Pet() + getHouseBySmoke(individuo,i,3)] == 3):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que vive na casa Amarela fuma Dunhill.
        if (individuo[i].matriz[Col_Smoke() + getHouseByColor(individuo,i,0)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que vive na casa do meio bebe Leite.
        if (individuo[i].matriz[Col_Drink() + 2] == 4):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que fuma Blends vive ao lado do que tem Gatos.
        if (abs(getHouseBySmoke(individuo,i,0) - getHouseByPet(individuo,i,2)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que cria Cavalos vive ao lado do que fuma Dunhill.
        if (abs(getHouseBySmoke(individuo,i,2) - getHouseByPet(individuo,i,1)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que fuma BlueMaster bebe Cerveja.
        if (individuo[i].matriz[Col_Drink() + getHouseBySmoke(individuo,i,1)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
        # O Alemão fuma Prince.
        if (individuo[i].matriz[Col_Smoke() + getHouseByNacionality(individuo,i,0)] == 4):
            individuo[i].ponto = individuo[i].ponto +1
        # O Norueguês vive ao lado da casa Azul.
        if (abs(getHouseByNacionality(individuo,i,3) - getHouseByColor(individuo,i,1)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
        # O homem que fuma Blends é vizinho do que bebe Água.
        if (abs(getHouseBySmoke(individuo,i,0) - getHouseByDrink(individuo,i,0)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
        '''
        avaliar de acordo as perguntas
        '''
        
    return sort()
        # qualquer coisa da de criar um merge sort da vida.
        
def SelectParent(population, currGen):
        
        for i in range(100):
            del individuo[i]
        '''
        salvar os iram fazer parte da proxima geracao
        '''
        pass
def CrossOver(population, currGen):
        '''
        fazer a trocar pelas linhas. 
        exemplo pegar a cor e a nacionalide de um e botar com a bebido o cigarro e o animal de outro.
        assim evitando bugar a matriz com valores repetidos e excluindo outros.
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
def Rng():
        return random(0,4)
def sort():
    individuoSort = sorted(individuo, key = cmp_to_key(compare))
    for i in range(len(individuoSort)):
        individuo[i] = individuoSort[i]
    individuo.reverse()
    
def main():
    stop = st.StopWatch()
    currGen = 0
    lastGen = 1
    population = 100
    stop.start()
    Init_population(population, currGen)    
    Evaluation(population, currGen)
    while currGen == lastGen:
        currGen = currGen + 1
        SelectParent(population, currGen)
        CrossOver(population, currGen)
        Mutation(population, currGen)
        Evaluation(population, currGen)        
        if(individuo[0].ponto == 15):
            break
        Suvivors(population, currGen)

    
    for i in range(population):
        print(individuo[i].matriz,"\n", individuo[i].ponto)

    print("Melhor individuo:\n",individuo[0].matriz,"\n", individuo[0].ponto)
    stop.stop()
    print(stop.getElapsedTime(), "seconds" )


if __name__ == '__main__':
    main()