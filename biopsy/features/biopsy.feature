Funcionalidade:  Eu, como Auxiliar,
Desejo cadastrar uma nova biopsia 
Para dar início ao processo.

    Cenario: Usuario busca Paciente somente pelo nome
        Dado que o Usuario se autentica
        E que o Usuario esta na tela de busca de pacientes
        Quando o usuario digita o nome do Paciente
        E clica em buscar
        Então o sistema retorna os Pacientes com o nome digitado

    Cenário: O auxiliar cadastra um novo exame com sucesso
        Dado que o auxiliar acessa o sistema e esta autenticado
        E aparece a tela de cadastro de exame
        Quando o auxiliar digita todos os campos corretamente
        E clica em enviar
        Então o sistema cadastra o exame

    Cenário: O auxiliar cadastra um nova biopsia com sucesso
        Dado que o auxiliar acessa o sistema e esta autenticado
        E aparece a tela de cadastro de biopsia
        Quando o auxiliar digita todos os campos corretamente
        E clica em cadastrar
        Então o sistema cadastra a biopsia 

    Cenario: O usuario visualiza o exame completo de um paciente
        Dado que o usuario acessa o perfil do paciente
        Quando ele clica no exame desejado
        E clica em Ver Biopsia
        Entao o sistema exibe a biopsia completa do paciente