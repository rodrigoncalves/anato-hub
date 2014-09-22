Funcionalidade: Eu, como usuario,
Desejo efetuar login no sistema
Para poder utiliza-lo

    Cenário: Usuario se autentica no sistema com sucesso
        Dado que o usuario acessa o sistema
        E aparece a tela de login
        Quando o usuario digita seu nome
        E digita a sua senha
        Então autentica o usuario com sucesso

    Cenário: Usuario digita um login invalido
        Dado que o usuario acessa o sistema
        E aparece a tela de login
        Quando o usuario digita seu nome
        E digita a sua senha
        Então o sistema nao consegue autenticar o usuario no LDAP
        E retorna uma mensagem "Login invalido"

    Cenário: Usuario digita apenas o nome de usuario
        Dado que o usuario acessa o sistema
        E aparece a tela de login
        Quando o usuario digita somente seu nome
        Então o sistema nao permite que o botao entrar seja clicado

    Cenário: Usuario digita apenas a senha
        Dado que o usuario acessa o sistema
        E aparece a tela de login
        Quando o usuario digita somente sua senha
        Então o sistema nao permite que o botao entrar seja clicado