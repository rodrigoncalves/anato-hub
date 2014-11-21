Funcionalidade:  Eu, como Auxiliar,
Desejo cadastrar uma nova necropsia 
Para dar início ao processo.

    Contexto: Usuario entra no sistema e realiza a busca
        Dado que o usuario entra no sistema
        E realiza uma busca de paciente
        E escolhe o paciente
        E cadastra um exame do tipo Necropsia

    Cenário: O auxiliar cadastra um nova necropsia com sucesso
        Quando aparece a tela de cadastro de necropsia
        E o auxiliar digita todos os campos corretamente
        E clica em cadastrar
        Então o sistema cadastra a necropsia