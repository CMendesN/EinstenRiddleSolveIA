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
        self.numero = num 
    
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
    for i in range(len(individuo)):
        ponto = 0
        #  1 : O Norueguês vive na primeira casa.
        if(individuo[i].matriz[Col_Nacionality() + 0]== 3):
            ponto = ponto +1
        else:
            ponto = ponto -0    
        #  2: O Inglês vive na casa Vermelha.
        if( getHouseByColor(individuo,i,4) != None):
            if (individuo[i].matriz[Col_Nacionality() + getHouseByColor(individuo,i,4)] == 2):
                ponto = ponto +1
            else:
                ponto = ponto -0   
        #  3: O Sueco tem Cachorros como animais de estimação.
        if(getHouseByNacionality(individuo,i,4)!= None):
            if (individuo[i].matriz[Col_Pet() + getHouseByNacionality(individuo,i,4)] == 0) :
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 4 :O Dinamarquês bebe Chá.
        if(getHouseByNacionality(individuo,i,1)!= None):
            if (individuo[i].matriz[Col_Drink() + getHouseByNacionality(individuo,i,1)] == 3):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 5: A casa Verde fica do lado esquerdo da casa Branca.
        if(getHouseByColor(individuo,i,3) != None):
            if (individuo[i].matriz[Col_Color() + getHouseByColor(individuo,i,3)+ 1] == 2):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 6: O homem que vive na casa Verde bebe Café.
        if(getHouseByColor(individuo,i,3) != None):
            if (individuo[i].matriz[Col_Drink() + getHouseByColor(individuo,i,3)] == 1):
                ponto = ponto +1
            else:
                ponto = ponto -0   
        # 7: O homem que fuma Pall Mall cria Pássaros.
        if(getHouseBySmoke(individuo,i,3) != None):
            if (individuo[i].matriz[Col_Pet() + getHouseBySmoke(individuo,i,3)] == 3):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 8: O homem que vive na casa Amarela fuma Dunhill.
        if(getHouseByColor(individuo,i,0) != None):
            if (individuo[i].matriz[Col_Smoke() + getHouseByColor(individuo,i,0)] == 2):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 9: O homem que vive na casa do meio bebe Leite.
        if (individuo[i].matriz[Col_Drink() + 2] == 4):
            ponto = ponto +1
        else:
            
            ponto = ponto -0    
        # 10: O homem que fuma Blends vive ao lado do que tem Gatos.
        if(getHouseBySmoke(individuo,i,0)!= None and getHouseByPet(individuo,i,2) != None):
            if (abs(getHouseBySmoke(individuo,i,0) - getHouseByPet(individuo,i,2)) == 1):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 11: O homem que cria Cavalos vive ao lado do que fuma Dunhill.
        if(getHouseBySmoke(individuo,i,2)!= None and getHouseByPet(individuo,i,1) != None):
            if (abs(getHouseBySmoke(individuo,i,2) - getHouseByPet(individuo,i,1)) == 1):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 12: O homem que fuma BlueMaster bebe Cerveja.
        if(getHouseBySmoke(individuo,i,1) != None):
            if (individuo[i].matriz[Col_Drink() + getHouseBySmoke(individuo,i,1)] == 2):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 13: O Alemão fuma Prince.
        if(getHouseByNacionality(individuo,i,0) != None):
            if (individuo[i].matriz[Col_Smoke() + getHouseByNacionality(individuo,i,0)] == 4):
                ponto = ponto +1
            else:
                ponto = ponto -0    
        # 14: O Norueguês vive ao lado da casa Azul.
        if(getHouseByNacionality(individuo,i,3)!= None and getHouseByColor(individuo,i,1) != None):
            if (abs(getHouseByNacionality(individuo,i,3) - getHouseByColor(individuo,i,1)) == 1):
                ponto = ponto +1
            else:
                
                ponto = ponto -0    
        # 15: O homem que fuma Blends é vizinho do que bebe Água.
        if(getHouseBySmoke(individuo,i,0)!= None and getHouseByDrink(individuo,i,0) != None):    
            if (abs(getHouseBySmoke(individuo,i,0) - getHouseByDrink(individuo,i,0)) == 1):
                ponto = ponto +1
            else:
                
                ponto = ponto -0    
        
        individuo[i].ponto = ponto
        
    
        
cross_list = []       
def SelectParent(population, currGen):
       
        global cross_list
        for i in range(len(individuo)):
            fitness =int(((individuo[i].ponto/15)*10))
            for j in range(fitness):
                cross_list.append(i)
        random.shuffle(cross_list)
        #del(cross_list[population-int(population*0.2):len(cross_list)]) 
        
def CrossOver(population, currGen):             
        if (len(cross_list)%2 != 0):
               del cross_list[len(cross_list)-1]
        
                
        for k in range(int(population/2)):
            a = random.randint(0, len(cross_list)-1)
            b = random.randint(0, len(cross_list)-1)
            child_1 = House()
            child_2 = House()          
            midpoint = random.randint(1, 4)
            midpoint = midpoint * 5                
            child_1.matriz = individuo[cross_list[a]].matriz[0:midpoint] + individuo[cross_list[b]].matriz[midpoint:25]
            child_2.matriz = individuo[cross_list[b]].matriz[0:midpoint] + individuo[cross_list[a]].matriz[midpoint:25]
            individuo.insert(k, child_1)
            individuo.insert(k+1,child_2)    
        
        cross_list.clear()
        
def CrossOver2(population, currGen):             
        if (len(cross_list)%2 != 0):
               del cross_list[len(cross_list)-1]
        
                
        for k in range(int(len(cross_list)/2)):
            cross = random.random()
            if( cross < 0.81):
                individuo.append(House())
                individuo.append(House())
                individuo[len(individuo) - 2].matriz = individuo[cross_list[k]].matriz[0:10] + individuo[cross_list[len(cross_list)-1-k]].matriz[10:25]
                individuo[len(individuo) - 1].matriz = individuo[cross_list[len(cross_list)-1-k]].matriz[0:10] + individuo[cross_list[k]].matriz[10:25]
                
        cross_list.clear()


def mutacao1(i):
    #g = random.randint(1,2)
    #for q in range(g):    
        selacaoDaCasa = Rng()
        selacaoDoTipo = Rng()
        posicaoDaTroca = selacaoDoTipo * 5 + selacaoDaCasa
        trocaDeDado = Rng()
        temp = individuo[i].matriz[posicaoDaTroca]
        for k in range(5):        
                if individuo[i].matriz[selacaoDoTipo * 5 + k] == trocaDeDado :
                    individuo[i].matriz[posicaoDaTroca] = individuo[i].matriz[selacaoDoTipo * 5 + k]
                    individuo[i].matriz[selacaoDoTipo * 5 + k] = temp
                    break

def mutacao2(k):
    selacaoDoTipo = Rng()
    valores = random.sample(const_list, len(const_list))
    for i in range(5):
        individuo[k].matriz[selacaoDoTipo * 5 + i] = valores[i]

def mutacao3(k):
    for j in range(5):
        moeda = random.randint(0,1)        
        if(moeda == 1):    
            #valores =  Rng()#random.sample(const_list, len(const_list))
            for i in range(5):
                valores =  Rng()
                individuo[k].matriz[j * 5 + i] = valores

def mutacao4(k):
    for i in range(5):
        for j in range(5):
            moeda = 1# random.randint(0,1)
            if(moeda == 1):
                trocaDeDado = Rng() #1
                while trocaDeDado == individuo[k].matriz[i*5+j]:
                    trocaDeDado = Rng()
                temp = individuo[k].matriz[i*5+j] #3
                for m in range(5):   
                    if individuo[k].matriz[i*5+m] == trocaDeDado:
                        individuo[k].matriz[i*5+j] = individuo[k].matriz[i*5+m]
                        individuo[k].matriz[i*5+m] = temp
                        break
     
def Mutation(population, currGen):
        
        for i in range(len(individuo)):
            mutar = random.random()
            if(mutar < 0.02):
                #print(len(individuo))
                mutacao1(i)
                            
flag = 0
def Suvivors(population, currGen):
    sort()
    
    del(individuo[population-int(population*0.80):len(individuo)])
    ''' 
    global flag 
    flag = flag + 1
    #if(flag%15==0):
    
    for i in range(len(individuo), population):
            individuo.insert(i, House())
            for linha in range(5):
                valores = random.sample(const_list, len(const_list))
                for coluna in range(5):        
                    individuo[i].matriz.append(valores[coluna])
    Evaluation(population, currGen)
    
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
    individuo.clear()
    individuo.extend(individuoSort)
    individuo.reverse()
    
def main():
    stop = st.StopWatch()
    currGen = 0
    lastGen = 1000
    population = 500
    stop.start()
    Init_population(population, currGen)    
    Evaluation(population, currGen)
    while currGen != lastGen:
        currGen = currGen + 1
        SelectParent(population, currGen)
        CrossOver(population, currGen)
        Mutation(population, currGen)
        Evaluation(population, currGen)                
        Suvivors(population, currGen)
        if(currGen%16 == 0):
            print("Melhor da geracao: ",individuo[0].numero, "Pontos: ", individuo[0].ponto)
        if(individuo[0].ponto == 15):            
            break
    
    #for i in range(int(len(individuo)*0.2)):
    #    print(individuo[i].matriz,"\n", individuo[i].ponto)
    if(individuo[0].ponto == 15):
            print("sucesso")
    else:            
            print("falha")
    
    print("Melhor individuo: ",individuo[0].numero,"\n",individuo[0].matriz,"\n", "Pontos: ", individuo[0].ponto)
    stop.stop()
    print(stop.getElapsedTime(), "seconds" )


if __name__ == '__main__':
    main()