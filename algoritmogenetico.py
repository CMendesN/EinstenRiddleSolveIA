class House():
    def __init__(self, position) -> None:
        self.data = {"color": None, "nationality": None, "drink": None, "smoke": None, "pet": None }
        self.data["position"] = str(position) if str(position) is not None else None

    def Discribe(self):
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
    


if __name__ == '__main__':
    main()