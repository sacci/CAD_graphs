import numpy as np
import pandas as pd
inf = float('inf')

class Graph:
    def __init__(self, graph_txt):
        self.texto = graph_txt
        #lista de vertices
        self.nodos = []
        #dataframe com informacoes das arestas
        columns = ['origem','destino','distancia']
        self.data = pd.DataFrame(columns=columns)
        
    def montaGrafo(self):
        with open(self.texto) as fp:
            line = fp.readline()
            #nodo origem
            self.origem = line.split()[0] 
            #nodo destino
            self.destino = line.split()[-1] 
            cont = 1
            line = fp.readline()
            while (line):
                    nodos = line.split()
                    self.data.at[cont-1,'origem'] = nodos[0]
                    self.data.at[cont-1,'destino'] = nodos[1]
                    self.data.at[cont-1,'distancia'] = nodos[2]
                    cont +=1
                    line = fp.readline()
                    
        #monta lista de nodos do grafo, para facilitar algoritmo   
        with open(self.texto) as fp:
            linhas = 0
            for line in fp:
                words = line.split()
                for word in words:
                    if word not in self.nodos:
                        if linhas == 0:
                            self.nodos.append(word)
                        elif linhas > 0 and words[-1] != word:
                            self.nodos.append(word)
                linhas += 1
        self.nodos.sort()
            
                    
                    
    def Djisktra(self):
        #print("\nNodos objetivo\n")
        #print(self.objetivo)
        print("Nodo origem: ")
        print(self.origem)
        print("Nodo destino: ")
        print(self.destino)
        print("Dataframe de arestas")
        print(self.data)
        print("Lista de nodos")
        print(self.nodos)
        
        #inicializar distancias como desconhecidas
        distancias = [inf] * len(self.nodos)
        for i in range(len(self.nodos)):
            if int(self.nodos[i]) == int(self.origem):
                #distancia de origem a origem é zero
                distancias[i] = 0
        nodo_atual = self.origem
        #arrumar isso, botar pra funcionar com dataframe
        #if (nodo_atual,self.destino) in self.arestas:
        #    return self.arestas[(nodo_atual,self.destino)]
        lista_iterativa = self.nodos.copy()
        
        
              
        
        
    
    
    
graph = Graph("graph.txt")
graph.montaGrafo()
menor_caminho = graph.Djisktra()
print ("Menor caminho:")
print (menor_caminho)