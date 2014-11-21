Funcionalidade:  Eu, como Auxiliar,
Desejo cadastrar uma nova biopsia 
Para dar início ao processo.

    Contexto: Usuario entra no sistema e realiza a busca
        Dado que o usuario entra no sistema
        E realiza uma busca de paciente
        E escolhe o paciente
        E cadastra um exame do tipo Biopsia

    Cenário: O auxiliar cadastra um nova biopsia com sucesso
        Quando aparece a tela de cadastro de biopsia
        E o auxiliar digita todos os campos corretamente
        E clica em cadastrar
        Então o sistema cadastra a biopsia