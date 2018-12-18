# -*- coding: utf-8 -*-
'''
Autor: Pedro Saccilotto
Implementação do Algoritmo de Prim

Input: arquivo com formato correto (graph_prim.txt), definido abaixo
Formato do grafo: uma aresta (não direcionada) por linha, todos inteiros
nodo1 nodo2 distancia (três números)

Output: comprimento do minimum spanning tree pelo algoritmo de prim
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
            cont = 1
            while (line):
                    nodos = line.split()
                    self.data.at[cont-1,'ORIGEM'] = nodos[0]
                    self.data.at[cont-1,'DESTINO'] = nodos[1]
                    self.data.at[cont-1,'DISTANCIA'] = nodos[2]
                    self.data.at[cont,'ORIGEM'] = nodos[1]
                    self.data.at[cont,'DESTINO'] = nodos[0]
                    self.data.at[cont,'DISTANCIA'] = nodos[2]
                    cont +=2
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
            
                    
                    
    def Prim(self):
        #print("Dataframe de arestas")
        #print(self.data)
        
        #inicializar distancias como desconhecidas
        distancias = [inf] * len(self.nodos)
        #array de bool que indica se nodo já foi escolhido
        foi_escolhido = [False] * len(self.nodos)
        #distancia de origem a origem é zero
        for i in range(len(self.nodos)):
            if int(self.nodos[i]) == int(self.nodos[0]):
                distancias[i] = 0
                foi_escolhido[i] = True
        #nodo_atual sera um dos nodos da lista de nodos origem
        nodos_origem = [self.nodos[0]]
        nodo_atual = nodos_origem[0]
        print("Nodo inicial: vertice "+str(nodo_atual))
        all_nodes_visited = False 
        
        while all_nodes_visited == False:
        
        #funcionamento parecido com dijkstra, a diferença é que haverá mais nodos origens ao longo da iteração... (lista de nodos visitados aumenta)


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
                        if int(distancias[i]) > int(distancia_da_aresta) and foi_escolhido[i] == False:
                            #atualiza
                            distancias[i] = int(distancia_da_aresta)
                                
                    #valor atual eh infinito, entao qualquer valor eh menor e pode atualizar
                    if distancias[i] == inf:
                        distancias[i] = int(distancia_da_aresta)


            menor_numero = -1
            index = -1
            for i in range(len(distancias)):
                if distancias[i] != 0 and menor_numero == -1 and foi_escolhido[i] == False:
                    menor_numero = distancias[i]
                    index = i
                elif distancias[i] != 0 and float(menor_numero) > float(distancias[i]) and foi_escolhido[i] == False:
                    menor_numero = distancias[i]
                    index = i

            #print("Aresta do vertice "+str(nodo_atual)+ " ate vertice "+str(self.nodos[index]))
            #print(distancias)
            foi_escolhido[index] = True
            #print (foi_escolhido)

            #atualizar o nodos_origem para o nodo com menor distancia na lista
            nodos_origem.append(self.nodos[index])
            nodo_atual = self.nodos[index]
            #checar se deve acabar o algoritmo, vendo se todos nodos foram visitados
            if len(nodos_origem) == len(self.nodos):
                all_nodes_visited = True

        menor_comprimento = 0
        for i in range(len(distancias)):
            menor_comprimento = distancias[i] + menor_comprimento
        #retornar comprimento
        return menor_comprimento                  
        
        
              
  
graph = Graph("graph_prim.txt")
graph.montaGrafo()
menor_comprimento = graph.Prim()
print ("Minimum Spanning Tree do grafo: " +str(menor_comprimento))