from abstracoes import IVendaRepository


class VendaArquivoRepository(IVendaRepository):
    def salvar(self, cliente: str, valor: float) -> None:
        with open("vendas.txt", "a") as f:
            f.write(f"{cliente}: {valor:.2f}\n")
        print(f"[BD] Venda salva no arquivo para {cliente}")

class VendaMemoriaRepository(IVendaRepository):
    def __init__(self):
        self.banco_dados_vendas = []

    def salvar(self, cliente: str, valor: float) -> None:
        self.banco_dados_vendas.append({"cliente": cliente, "valor": valor})
        print(f"[MEMORIA] Venda salva em memória para {cliente}")
