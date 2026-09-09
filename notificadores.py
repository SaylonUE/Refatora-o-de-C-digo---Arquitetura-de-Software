from abstracoes import INotificador


class NotificadorEmail(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-MAIL] Enviando e-mail para {destinatario}: {mensagem}")


class NotificadorSMS(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[SMS] Enviando SMS para {destinatario}: {mensagem}")
