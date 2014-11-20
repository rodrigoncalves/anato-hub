Funcionalidade: Eu, como usuario,
Desejo efetuar login no sistema
Para poder utiliza-lo

    Contexto: Acessar o sistema
    Dado que o usuario acessa a url "http://localhost:8000/" e aparece a tela de login

    Cenário: Usuario se autentica no sistema com sucesso
        Quando o usuario digita seu nome: "admin"
        E digita a sua senha: "1234"
        E clica em Entrar
        Então autentica o usuario com sucesso

    Cenário: Usuario digita apenas o nome de usuario
        Quando o usuario digita seu nome: "admin"
        Então o sistema nao permite que o botao entrar seja clicado

    Esquema do Cenário: Usuario digita um par usuario/senha invalido
        Quando o usuario digita seu nome: "<user>"
        E digita a sua senha: "<password>"
        E clica em Entrar
        Então o sistema retorna a mensagem de erro "Nome de usuário ou senha incorretos."

        Exemplos:
        | user                  | password          |
        | admin                 | 123               |
        | adm                   | 1234              |

    Cenário: Usuario digita apenas a senha
        Quando digita a sua senha: "1234"
        Então o sistema nao permite que o botao entrar seja clicado