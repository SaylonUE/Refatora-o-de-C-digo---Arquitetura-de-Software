# Atividade Prática: Refatoração de código

#### Matéria: Arquitetura de Software
#### Aluno: Saylon da Rocha Batista

### Atividade
O professora nos passou um código inicial que tinha um problema clássico de design: todas as funcionalidades estavam misturadas e englobadas em um único lugar (na classe `ProcessadorVenda`). 

Basicamente, um único método tinha a obrigação de fazer três coisas diferentes:
1. Calcular um dado valor (aplicar regras de desconto).
2. Salvar essa venda em um "banco de dados" (arquivo de texto) para um determinado cliente.
3. Enviar a confirmação com o valor final para o e-mail desse cliente.

## Oque foi realizado:
O objetivo da atividade foi separar as tarefas. Nós tiramos tudo daquela classe gigante e dividimos o sistema em componentes menores. 

Agora, cada parte do código cuida apenas da sua própria responsabilidade:
* **Uma parte só para as regras de negócio (`servico_venda`):** Fazer o cálculo do desconto e orquestrar o processo.
* **Uma parte só para o repositório (`repositorios`):** Salvar a venda (seja em arquivo ou na memória).
* **Uma parte só para a notificação (`notificadores`):** Enviar a mensagem para o cliente (seja por E-mail ou SMS).

Para que essas partes conversassem entre si sem ficarem dependentes umas das outras (sem acoplamento forte), nós utilizamos `abstrações`. O código principal `VendaService` não precisa saber como o dado é salvo ou *como* a mensagem é enviada, ele apenas usa a interface.


Com as funcionalidades separadas e independentes, o nosso código ficou muito mais flexível. 

Através dessa arquitetura, nós conseguimos adicionar facilmente novos métodos de envio e novas maneiras de salvar os dados no banco sem que elas estejam diretamente acopladas. Ou seja, se precisarmos mudar a forma como o e-mail é enviado, isso não vai quebrar a lógica de salvar a venda no banco de dados. Separamos as responsabilidades e deixamos o sistema pronto para crescer de forma organizada.
