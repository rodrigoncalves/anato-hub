Funcionalidade:  Eu, como Auxiliar,
Desejo cadastrar um novo pedido de exame de congelamento
Para dar início ao processo.

    Cenário: O auxiliar cadastra um novo exame com sucesso
        Dado que o auxiliar acessa o sistema e esta autenticado
        E cadastra o pedido de exame escolhendo a opção congelamento
        Quando o auxiliar digita todos os campos de congelamento corretamente
        E clica em cadastrar
        Então o sistema cadastra o exame e retorna uma mensagem "Exame salvo com sucesso"
