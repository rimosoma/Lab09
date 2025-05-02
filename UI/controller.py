import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analyze(self, e):
        miglia = self._view.minimum_dtnc.value
        #controllo se la casella miglia non è vuota, e se è un numero
        if miglia is None or miglia == "" or not miglia.isdigit():
            self._view.create_alert("Inserire il numero di miglia")
            return
        miglia = int(miglia)
        edges = self._model.buildGrafo(miglia)
        numNodi = self._model.getNumNodi()
        numArchi = self._model.getNumArchi()

        self._view.txt_result.controls.append(ft.Text(f"Ecco i voli con almeno {miglia} miglia:"))
        self._view.txt_result.controls.append(ft.Text(f"Gli aereoporti considerati sono: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Le rotte considerati sono: {numArchi}"))
        n = 1
        for edge in edges:
            self._view.txt_result.controls.append(ft.Text(f"tratta {n}: {edge}"))
            n+=1

        self._view.update_page()
