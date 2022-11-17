#eu alterei
import random
import StopWatch as st
from functools import cmp_to_key
#bota variavel global para numeração de individuos
num = 0
class House:
    def __init__(self):
        #alterar essa para uma matriz onde as casas sao as colunas(j) e os dados da casa sao as linhas(i) assim da para usar o i * m + j
        self.matriz = matriz = []
        self.ponto = 0       
        global num
        num = num +1
        self.numero = num # preciso de algo que faça i + population * genatual
        # ja que todas as funcoes usam population e genatual entao da para utilizar para dizer qual o numero dele
        '''
        self.data = {"color": None, "nationality": None, "drink": None, "smoke": None, "pet": None }
        self.data["position"] = str(position) if str(position) is not None else None
        self.matriz = matriz = []
        '''
    
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
        for i in range(0,5):
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
    for i in range(0,population):
        individuo[i].ponto = 0
        #  1 : O Norueguês vive na primeira casa.
        if(individuo[i].matriz[Col_Nacionality() + 0]== 3):
            individuo[i].ponto = individuo[i].ponto +1
            
        #  2: O Inglês vive na casa Vermelha.
        if (individuo[i].matriz[Col_Nacionality() + getHouseByColor(individuo,i,4)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
            
        #  3: O Sueco tem Cachorros como animais de estimação.
        if (individuo[i].matriz[Col_Pet() + getHouseByNacionality(individuo,i,4)] == 0) :
            individuo[i].ponto = individuo[i].ponto +1
            
        # 4 :O Dinamarquês bebe Chá.
        if (individuo[i].matriz[Col_Drink() + getHouseByNacionality(individuo,i,1)] == 3):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 5: A casa Verde fica do lado esquerdo da casa Branca.
        if (individuo[i].matriz[Col_Color() + getHouseByColor(individuo,i,3)+ 1] == 2):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 6: O homem que vive na casa Verde bebe Café.
        if (individuo[i].matriz[Col_Drink() + getHouseByColor(individuo,i,3)] == 1):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 7: O homem que fuma Pall Mall cria Pássaros.
        if (individuo[i].matriz[Col_Pet() + getHouseBySmoke(individuo,i,3)] == 3):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 8: O homem que vive na casa Amarela fuma Dunhill.
        if (individuo[i].matriz[Col_Smoke() + getHouseByColor(individuo,i,0)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 9: O homem que vive na casa do meio bebe Leite.
        if (individuo[i].matriz[Col_Drink() + 2] == 4):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 10: O homem que fuma Blends vive ao lado do que tem Gatos.
        if (abs(getHouseBySmoke(individuo,i,0) - getHouseByPet(individuo,i,2)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 11: O homem que cria Cavalos vive ao lado do que fuma Dunhill.
        if (abs(getHouseBySmoke(individuo,i,2) - getHouseByPet(individuo,i,1)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 12: O homem que fuma BlueMaster bebe Cerveja.
        if (individuo[i].matriz[Col_Drink() + getHouseBySmoke(individuo,i,1)] == 2):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 13: O Alemão fuma Prince.
        if (individuo[i].matriz[Col_Smoke() + getHouseByNacionality(individuo,i,0)] == 4):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 14: O Norueguês vive ao lado da casa Azul.
        if (abs(getHouseByNacionality(individuo,i,3) - getHouseByColor(individuo,i,1)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
            
        # 15: O homem que fuma Blends é vizinho do que bebe Água.
        if (abs(getHouseBySmoke(individuo,i,0) - getHouseByDrink(individuo,i,0)) == 1):
            individuo[i].ponto = individuo[i].ponto +1
            
        
        '''
        avaliar de acordo as perguntas
        '''
        
    return sort()
        # qualquer coisa da de criar um merge sort da vida.
        
def SelectParent(population, currGen):
        
        #for i in range(100):
         #   del individuo[i]
        '''
        salvar os iram fazer parte da proxima geracao
        '''
        pass
def CrossOver(population, currGen):
        cross_list = []
        
        for i in range(len(individuo)):
            cross = random.random()
            if(cross < 0.81):
                cross_list.append(i)
        
        if (len(cross_list)%2 != 0):
               del cross_list[len(cross_list)-1]
        
        random.shuffle(cross_list)        
        for k in range(int(len(cross_list)/2)):            
            if(k < len(cross_list)-1):
                individuo.append(House())
                individuo.append(House())
                individuo[len(individuo) - 2].matriz = individuo[cross_list[k]].matriz[0:10] + individuo[cross_list[len(cross_list)-1-k]].matriz[10:25]
                individuo[len(individuo) - 1].matriz = individuo[cross_list[len(cross_list)-1-k]].matriz[0:10] + individuo[cross_list[k]].matriz[10:25]
                #k = k+1
                '''
                for j in range(len(individuo[cross_list[k]].matriz)):
                    if j < 10:
                        individuo[len(individuo) - 2].matriz.insert(j, individuo[cross_list[k]].matriz[j])
                    if j >= 10:
                        individuo[len(individuo) - 1].matriz.insert(j, individuo[cross_list[k]].matriz[j])                    
                k=k+1
                for m in range(len(individuo[cross_list[k]].matriz)):
                    if m < 10:
                        individuo[len(individuo) - 1].matriz.insert(m, individuo[cross_list[k]].matriz[m])
                    if m >= 10:
                        individuo[len(individuo) - 2].matriz.insert(m, individuo[cross_list[k]].matriz[m]) 
                '''
               # print(individuo[len(individuo) - 2].matriz,"\n")
               # print(individuo[len(individuo) - 1].matriz,"\n")
        cross_list.clear()
        '''
        fazer a trocar pelas linhas. 
        exemplo pegar a cor e a nacionalide de um e botar com a bebido o cigarro e o animal de outro.
        assim evitando bugar a matriz com valores repetidos e excluindo outros.
        '''
        pass
def mutacao1(i):
    selacaoDaCasa = Rng()
    selacaoDoTipo = Rng()
    posicaoDaTroca = selacaoDoTipo * 5 + selacaoDaCasa
    trocaDeDado = Rng()
    temp = individuo[i].matriz[posicaoDaTroca]
    for k in range(4):        
            if individuo[i].matriz[selacaoDoTipo * 5 + k] == trocaDeDado :
                individuo[i].matriz[posicaoDaTroca] = individuo[i].matriz[selacaoDoTipo * 5 + k]
                individuo[i].matriz[selacaoDoTipo * 5 + k] = temp
                break
def mutacao2(k):
    selacaoDoTipo = Rng()
    valores = random.sample(const_list, len(const_list))
    for i in range(5):
        individuo[k].matriz[selacaoDoTipo * 5 + i] = valores[i]
    
def Mutation(population, currGen):
        
        for i in range(len(individuo)):
            mutar = random.random()
            if(mutar < 0.02):
                
                if mutar<0.005:
                    
                    mutacao2(i)
                else:
                    
                    mutacao1(i)
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
        []valores = {0,1,2,3,4}
        valores.embaralhar
        for i in range(4):
            House.data[selacaoDoTipo * m + i] = valores[i]
        '''     
        pass     
flag = 0
def Suvivors(population, currGen):
    del(individuo[population-int(population*0.2):len(individuo)])
    global flag 
    flag = flag + 1
    if(flag%15==0):
        
        for i in range(len(individuo), population):
            individuo.insert(i, House())
            for linha in range(5):
                valores = random.sample(const_list, len(const_list))
                for coluna in range(5):        
                    individuo[i].matriz.append(valores[coluna])
    '''
    resposta=[0,1,4,3,2,3,1,2,0,4,0,3,4,1,2,2,0,3,4,1,2,1,3,4,0]
    individuo.insert(len(individuo), House())
    for k in range(25):
        individuo[len(individuo)-1].matriz.append(resposta[k])
        
        pegar as melhores avaliacoes
    '''
        
def Rng():
        return random.randint(0,4)
def sort():
    individuoSort = sorted(individuo, key = cmp_to_key(compare))
    for i in range(len(individuoSort)):
        individuo[i] = individuoSort[i]
    individuo.reverse()
    
def main():
    stop = st.StopWatch()
    currGen = 0
    lastGen = 1000000
    population = 100
    stop.start()
    Init_population(population, currGen)    
    Evaluation(population, currGen)
    while currGen != lastGen:
        currGen = currGen + 1
        SelectParent(population, currGen)
        CrossOver(population, currGen)
        Mutation(population, currGen)
        Evaluation(population, currGen)        
        if(individuo[0].ponto == 15):
            break
        #print("Melhor da geracao: ",individuo[0].numero, "Pontos: ", individuo[0].ponto)
        Suvivors(population, currGen)
        
    
    for i in range(len(individuo)):
        print(individuo[i].matriz,"\n", individuo[i].ponto)
    print(len(individuo))
    
    print("Melhor individuo: ",individuo[0].numero,"\n",individuo[0].matriz,"\n", "Pontos: ", individuo[0].ponto)
    stop.stop()
    print(stop.getElapsedTime(), "seconds" )


if __name__ == '__main__':
    main()