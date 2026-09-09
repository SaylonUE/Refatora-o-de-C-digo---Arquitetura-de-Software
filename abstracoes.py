from abc import ABC, abstractmethod


class INotificador(ABC):

    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        pass


class IVendaRepository(ABC):

    @abstractmethod
    def salvar(self, cliente: str, valor: float) -> None:
        pass
