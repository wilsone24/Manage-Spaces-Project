class graph:
    def __init__(self, rutaimg:str, fecha:str)->None:
        """Constructor de la clase graph

        Args:
            rutaimg (str): Ruta de la imagen
            fecha (str): Fecha de la imagen
        """
        self.rutaimg = rutaimg
        self.fecha = fecha


class Report:
    def __init__(self)->None:
        """Constructor de la clase Report
        """
        self.graphs = []
        self.year = '2023'

    def addGraph(self, graph:str)->None:
        """Función para agregar un gráfico al reporte

        Args:
            graph (str): objeto de tipo grafico
        """
        self.graphs.append(graph)

Reporte = Report()
