from notificadores import NotificadorEmail
from repositorios import VendaArquivoRepository
from servico_venda import VendaService


if __name__ == "__main__":
    repositorio = VendaArquivoRepository()
    notificador = NotificadorEmail()
    venda_service = VendaService(repositorio, notificador)

    venda_service.processar("Saylon Batista", 200.0, "saylon.batista@aluno.uepa.br")
