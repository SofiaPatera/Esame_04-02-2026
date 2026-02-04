import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self._lista_nodi = []
        self._lista_archi = []

    def build_graph(self, role: str):
        self.G.clear()
        self._lista_nodi = DAO.leggi_nodi(role)
        self.G.add_nodes_from(self._lista_nodi)
        self._lista_archi = DAO.leggi_archi()
        for u,v,peso in self._lista_archi:
            self.G.add_edge(u,v, weight= peso)

    def classifica(self):
        pass

    def get_ruolo(self):
        return DAO.leggi_ruolo()

