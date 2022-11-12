#eu alterei
import random


class House():
    def __init__(self, position) -> None:
        #alterar essa para uma matriz onde as casas sao as colunas(j) e os dados da casa sao as linhas(i) assim da para usar o i * m + j
        self.data = {"color": None, "nationality": None, "drink": None, "smoke": None, "pet": None }
        self.data["position"] = str(position) if str(position) is not None else None
        self.matriz = matriz = []

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
const_list = [0,1,2,3,4]

def Init_population(population, genAtual):
    
    for i in range(population):
        for linha in range(4):
            valores = random.sample(const_list, len(const_list))
            for coluna in range(4):        
                matriz[linha * 5 + coluna] = valores[coluna]
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
def getHouseByColor (color):
        for i in range(4):
            if(matriz[0* 5 + i] == color):
                return i
def getHouseByNacionality (nacionality):
        for i in range(4):
            if(matriz[1* 5 + i] == nacionality):
                return i

def getHouseByDrink (drink):
        for i in range(4):
            if(matriz[2* 5 + i] == drink):
                return i
def getHouseBySmoke (smoke):
        for i in range(4):
            if(matriz[3* 5 + i] == smoke):
                return i
def getHouseByPet (pet):
        for i in range(4):
            if(matriz[4* 5 + i] == pet):
                return i
def Evaluation(population, genAtual):
        
        # O Norueguês vive na primeira casa.
        if(matriz[Col_Nacionality() + 0]== 3):
            pass # ponto = ponto +1
        # O Inglês vive na casa Vermelha.
        if (matriz[Col_Nacionality() + getHouseByColor(4)] == 2):
            pass # ponto = ponto +1
        # O Sueco tem Cachorros como animais de estimação.
        if (matriz[Col_Pet() + getHouseByNacionality(4)] == 0) :
            pass  # ponto = ponto +1
        # O Dinamarquês bebe Chá.
        if (matriz[Col_Drink() + getHouseByNacionality(1)] == 3):
            pass  # ponto = ponto +1
        # A casa Verde fica do lado esquerdo da casa Branca.
        if (matriz[Col_Color() + getHouseByColor(3)+ 1] == 2):
            pass  # ponto = ponto +1
        # O homem que vive na casa Verde bebe Café.
        if (matriz[Col_Drink() + getHouseByColor(3)] == 2):
            pass  # ponto = ponto +1
        # O homem que fuma Pall Mall cria Pássaros.
        if (matriz[Col_Pet() + getHouseBySmoke(3)] == 3):
            pass  # ponto = ponto +1
        # O homem que vive na casa Amarela fuma Dunhill.
        if (matriz[Col_Smoke() + getHouseByColor(0)] == 2):
            pass  # ponto = ponto +1
        # O homem que vive na casa do meio bebe Leite.
        if (matriz[Col_Drink() + 2] == 4):
            pass  # ponto = ponto +1
        # O homem que fuma Blends vive ao lado do que tem Gatos.
        if (abs(getHouseBySmoke(0) - getHouseByPet(2)) == 1):
            pass  # ponto = ponto +1
        # O homem que cria Cavalos vive ao lado do que fuma Dunhill.
        if (abs(getHouseBySmoke(2) - getHouseByPet(1)) == 1):
            pass  # ponto = ponto +1
        # O homem que fuma BlueMaster bebe Cerveja.
        if (matriz[Col_Drink() + getHouseBySmoke(1)] == 2):
            pass  # ponto = ponto +1
        # O Alemão fuma Prince.
        if (matriz[Col_Smoke() + getHouseByNacionality(0)] == 4):
            pass   # ponto = ponto +1
        # O Norueguês vive ao lado da casa Azul.
        if (abs(getHouseByNacionality(3) - getHouseByColor(1)) == 1):
            pass  # ponto = ponto +1
        # O homem que fuma Blends é vizinho do que bebe Água.
        if (abs(getHouseBySmoke(0) - getHouseByDrink(0)) == 1):
            pass  # ponto = ponto +1
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
def Rng():
        return random(0,4)

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
        
    


if __name__ == '__main__':
    main()