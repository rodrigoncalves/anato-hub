Funcionalidade: Eu, como usuario
Desejo atualizar um exame
Para inserir novas informacoes

    Cenario: Usuario atualiza um exame
    Dado que o usuario esta autenticado
    E que o usuario esta na tela de informacoes do exame
    Quando o usuario clica em editar
    E atualiza todos os campos
    E clica no botao Atualizar
    Entao o sistema apresenta a tela de informacoes do exame

    Cenario: Usuario preenche todos os campos menos o material recebido
    Dado que o usuario esta autenticado
    E que o usuario esta na tela de informacoes do exame
    Quando o usuario clica em editar
    E atualiza todos os campos e deixa o material recebido em branco
    E clica no botao Atualizar
    Entao o sistema apresenta uma mensagem de erro e nao volta pra tela de informacoes do exame

    Cenario: Usuario preenche todos os campos menos a hora do exame
    Dado que o usuario esta autenticado
    E que o usuario esta na tela de informacoes do exame
    Quando o usuario clica em editar
    E atualiza todos os campos e deixa a hora do exame em branco
    E clica no botao Atualizar
    Entao o sistema apresenta uma mensagem de erro e nao volta pra tela de informacoes do exame

    Cenario: Usuario preenche todos os campos menos o medico requisitante
    Dado que o usuario esta autenticado
    E que o usuario esta na tela de informacoes do exame
    Quando o usuario clica em editar
    E atualiza todos os campos e deixa o medico requisitante em branco
    E clica no botao Atualizar
    Entao o sistema apresenta uma mensagem de erro e nao volta pra tela de informacoes do exame

    Cenario: Usuario preenche todos os campos menos o medico responsavel
    Dado que o usuario esta autenticado
    E que o usuario esta na tela de informacoes do exame
    Quando o usuario clica em editar
    E atualiza todos os campos e deixa o medico responsavel em branco
    E clica no botao Atualizar
    Entao o sistema apresenta uma mensagem de erro e nao volta pra tela de informacoes do exame

    Cenario: Usuario atualiza apenas o medico requisitante
    Dado que o usuario esta autenticado
    E que o usuario esta na tela de informacoes do exame
    Quando o usuario clica em editar
    E atualiza apenas o campo de medico responsavel
    E clica no botao Atualizar
    Entao o sistema apresenta a tela de informacoes do exame
