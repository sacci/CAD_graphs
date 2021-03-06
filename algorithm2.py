# -*- coding: utf-8 -*-
'''
Autor: Pedro Saccilotto
Implementação do Algoritmo de Dijkstra

Input: arquivo com formato correto (graph_dijkstra.txt), definido abaixo
Formato cabeçalho: primeira linha origem e destino (dois números)
Formato do grafo: uma aresta (direcionada) por linha, todos inteiros
nodo_origem nodo_destino distancia (três números)

Output: print listando vértices passados para o destino, assim como o valor do menor caminho
'''
#import numpy as np
import pandas as pd
inf = float('inf')

class Graph:
    def __init__(self, graph_txt):
        self.texto = graph_txt
        #lista de vertices (nodos)
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
            
                    
                    
    def Dijkstra(self):
        print("Nodo origem: "+self.origem)
        print("Nodo destino: "+self.destino)
        #print("Dataframe de arestas")
        #print(self.data)
        
        #inicializar distancias como desconhecidas
        distancias = [inf] * len(self.nodos)
        #array de bool que indica se nodo já foi escolhido
        foi_escolhido = [False] * len(self.nodos)
        #distancia de origem a origem é zero
        for i in range(len(self.nodos)):
            if int(self.nodos[i]) == int(self.origem):
                distancias[i] = 0
        #nodo_atual sera o nodo de menor distancia em cada iteracao do algoritmo
        nodo_atual = self.origem
        shortest_path_found = False
        shortest_path = 0
        print ("Caminho percorrido")  
        
        while shortest_path_found == False:
        
            print (nodo_atual)
            for i in range(len(distancias)):
                destino_iterativo = self.nodos[i]
                
                distancia_da_aresta = 0
                for j in range (len(self.data["ORIGEM"])):
                    if self.data.at[j,"ORIGEM"] == nodo_atual and self.data.at[j,"DESTINO"] == destino_iterativo:
                        distancia_da_aresta = self.data.at[j,"DISTANCIA"]
                    
            
                #se tiver origem->destino no dataframe, portanto se tiver aresta
                if distancia_da_aresta != 0:
                    #tem um numero já, checar se deve atualizar (checar se distancias[i] > distancia no dataframe)                  
                    if distancias[i] != 0 and distancias[i] != inf:
                        if int(distancias[i]) > int(distancia_da_aresta):
                            #atualiza
                            distancias[i] = int(distancia_da_aresta) + int(shortest_path)
                            
                    #valor atual eh infinito, entao qualquer valor eh menor e pode atualizar
                    if distancias[i] == inf:
                        distancias[i] = int(distancia_da_aresta) + int(shortest_path)


            menor_numero = -1
            index = -1
            for i in range(len(distancias)):
                if distancias[i] != 0 and menor_numero == -1 and foi_escolhido[i] == False:
                    menor_numero = distancias[i]
                    index = i
                elif distancias[i] != 0 and float(menor_numero) > float(distancias[i]) and foi_escolhido[i] == False:
                    menor_numero = distancias[i]
                    index = i
            
            foi_escolhido[index] = True

            #atualizar o nodo_atual para o nodo com menor distancia na lista
            nodo_atual = self.nodos[index]
            #atualizar shortest_path, que é menor distancia do nodo atual
            shortest_path = distancias[index]
            #checar se deve acabar o algoritmo, vendo se nodo_atual eh self.destino
            if int(nodo_atual) == int(self.destino):
                shortest_path_found = True
                print (nodo_atual)

        #retornar shortest_path
        return shortest_path                  
        
        
              
  
graph = Graph("graph_dijsktra.txt")
graph.montaGrafo()
menor_caminho = graph.Dijkstra()
print ("Menor caminho: " +str(menor_caminho))