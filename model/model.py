import networkx as nx
from matplotlib import pyplot as plt
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._airportsDict = DAO.get_airports()         #dizionario di id-oggetto aereoporto


    def buildGrafo(self, MinMiglia):
        listaDiTriple = DAO.getAllEdgesPesati()
        for tripla in listaDiTriple:
            aer1 = self._airportsDict[tripla[0]]
            aer2 = self._airportsDict[tripla[1]]
            miglia = tripla[2]
            if miglia > MinMiglia:
                self._grafo.add_edge(aer1, aer2, weight=miglia)

        #--------------------------------------------------------------------------------------
        # 2) Calcolo le posizioni dei nodi con un algoritmo di layout
        #    spring_layout usa una forza di repulsione/attrazione
        pos = nx.spring_layout(self._grafo)

        # 3) Disegno nodi e archi
        nx.draw_networkx_nodes(self._grafo, pos,
                               node_color='lightblue',
                               node_size=50)
        nx.draw_networkx_edges(self._grafo, pos,
                               width=0.5)

        # 4) Disegno le etichette dei nodi
        #nx.draw_networkx_labels(self._grafo, pos,
         #                       font_size=4,
          #                      font_color='black')

        # 5) Se vuoi disegnare i pesi degli archi
        #edge_labels = nx.get_edge_attributes(self._grafo, 'weight')
        #nx.draw_networkx_edge_labels(self._grafo, pos, font_size=6, edge_labels=edge_labels)

        # 6) Rimuovo gli assi e mostro
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        #--------------------------------------------------------------------------------------
        return self._grafo.edges


    def getNumNodi(self):
        return self._grafo.number_of_nodes()

    def getNumArchi(self):
        return self._grafo.number_of_edges()

if __name__ == "__main__":
    MinMiglia = 100
    model = Model()
    model.buildGrafo(MinMiglia)