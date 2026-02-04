import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        role = self._view.dd_ruolo.value()
        self._model.G(role)
        self._view.list_risultato.controls.clear()
        self._view.list_risultato.controls.append(ft.Text(f"Numero nodi: {self._model.G.number_of_nodes()}, archi: {self._model.G.number_of_edges()}"))
        self._view.update()

    def handle_classifica(self, e):
        pass

    def handle_dd_ruolo(self):
        lista_ruoli = self._model.get_ruolo()
        self._view.dd_ruolo.options.clear()
        for ruolo in lista_ruoli:
            self._view.dd_ruolo.options.append(ft.dropdown.Option(ruolo))
        self._view.update()