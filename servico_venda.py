from abstracoes import INotificador, IVendaRepository


class VendaService:
    def __init__(self, repositorio: IVendaRepository, notificador: INotificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def processar(self, cliente: str, valor: float, email_cliente: str) -> float:
        if valor <= 0:
            raise ValueError("Valor inválido")

        valor_com_desconto = valor * 0.9 if valor > 100 else valor

        self.repositorio.salvar(cliente, valor_com_desconto)
        self.notificador.enviar(email_cliente,f"Venda de R$ {valor_com_desconto:.2f} confirmada!")

        return valor_com_desconto
