from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self) -> str:
        return f"Marca: {self._marca} | Modelo: {self._modelo} | Tipo: {self._tipo} | O veículo está {'ligado' if self._ligado else 'desligado'}"