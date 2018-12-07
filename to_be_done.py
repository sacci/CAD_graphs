import numpy as np
import pandas as pd
inf = float('inf')

class Graph:
    def __init__(self, graph_txt):
        self.texto = graph_txt
        #lista de vertices
        self.nodos = []
        #dataframe com informacoes das arestas
        columns = ['ORIGEM','DESTINO','DISTANCIA']
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
                    self.data.at[cont-1,'ORIGEM'] = nodos[0]
                    self.data.at[cont-1,'DESTINO'] = nodos[1]
                    self.data.at[cont-1,'DISTANCIA'] = nodos[2]
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
        #distancia de origem a origem é zero
        for i in range(len(self.nodos)):
            if int(self.nodos[i]) == int(self.origem):
                distancias[i] = 0
        #nodo_atual sera o nodo de menor distancia em cada iteracao do algoritmo
        nodo_atual = self.origem
        shortest_path_found = False
        shortest_path = 0
        
        while shortest_path_found == False:
        
            for i in range(len(distancias)):
                destino_iterativo = self.nodos[i]
                
                #USAR for j in range (0,len(data["ORIGEM"])):
                distancia_da_aresta = 0
                for j in range (len(self.data["ORIGEM"])):
                    if self.data.at[j,"ORIGEM"] == nodo_atual and self.data.at[j,"DESTINO"] == destino_iterativo:
                        distancia_da_aresta = self.data.at[j,"DISTANCIA"]
                    
            
                #se tiver origem->destino no dataframe, portanto se tiver aresta
                if (distancia_da_aresta != 0):

                    #tem um numero já, checar se deve atualizar (checar se distancias[i] > distancia no dataframe)                  
                    if distancias[i] != 0 and distancias[i] != inf:
                        if distancias[i] > distancia_da_aresta:
                            #atualiza
                            distancias[i] = distancia_da_aresta + shortest_path
                            
                    #valor atual eh infinito, entao qualquer valor eh menor e pode atualizar
                    if distancias[i] == inf:
                        distancias[i] = distancia_da_aresta


                    #remover do dataframe o record que foi iterados

            #atualizar o nodo_atual para o nodo com menor distancia na lista
            #atualizar shortest_path, que é menor distancia do nodo atual

            #checar se deve acabar o algoritmo, vendo se nodo_atual eh self.destino
            #se sim, shortest_path_found = True e botar distancias[i] do destino na variavel shortest_path
            
        #retornar shortest_path
                
        
        
              
  
graph = Graph("graph.txt")
graph.montaGrafo()
menor_caminho = graph.Djisktra()
print ("Menor caminho:")
print (menor_caminho)