Funcionalidade: Eu, como usuario
Desejo efetuar a busca de pacientes no sistema
Para visualizar seus dados e seus exames

    Contexto: Login do Usuario
              Dado que o Usuario se autentica
              E que o Usuario esta na tela de busca de pacientes

    Cenario: Usuario busca Paciente somente pelo nome
            Quando o usuario digita o nome do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o nome digitado

    Cenario: Usuario busca Paciente somente pelo prontuario
            Quando o usuario digita o prontuario do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o prontuario digitado

    Cenario: Usuario busca Paciente somente pelo nome da mae
            Quando o usuario digita o nome da mae do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o nome da mae digitado

    Cenario: Usuario busca Paciente somente pela data de nascimento
            Quando o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a data de nascimento digitada

    Cenario: Usuario busca Paciente somente pelo nome e prontuario
            Quando o usuario digita o nome do Paciente
            E o usuario digita o prontuario do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a nome e prontuario digitado

    Cenario: Usuario busca Paciente somente pelo nome e nome da mae
            Quando o usuario digita o nome do Paciente 
            E o usuario digita o nome da mae do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a nome e nome da mae digitado

    Cenario: Usuario busca Paciente somente pelo nome e data de nascimento
            Quando o usuario digita o nome do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a nome e data de nascimento digitado

    Cenario: Usuario busca Paciente somente pelo prontuario e nome da mae
            Quando o usuario digita o prontuario do Paciente
            E o usuario digita o nome da mae do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a prontuario e nome da mae digitado

    Cenario: Usuario busca Paciente somente pelo prontuario e data nascimento
            Quando o usuario digita o prontuario do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a prontuario e data nascimento digitado

    Cenario: Usuario busca Paciente somente pelo nome da mae e data nascimento
            Quando o usuario digita o nome da mae do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com a nome da mae e data nascimento digitado

    Cenario: Usuario busca Paciente somente pelo nome, prontuario e nome da mae
            Quando o usuario digita o nome do Paciente
            E o usuario digita o prontuario do Paciente
            E o usuario digita o nome da mae do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o nome, prontuario e nome da mae digitado

    Cenario: Usuario busca Paciente somente pelo nome, prontuario e data de nascimento
            Quando o usuario digita o nome do Paciente
            E o usuario digita o prontuario do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o nome, prontuario e data de nascimento digitado

    Cenario: Usuario busca Paciente somente pelo nome, nome da mae e data de nascimento
            Quando o usuario digita o nome do Paciente
            E o usuario digita o nome da mae do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o nome, nome da mãe e data de nascimento digitado

    Cenario: Usuario busca Paciente somente pelo prontuario, nome da mae e data de nascimento
            Quando o usuario digita o prontuario do Paciente
            E o usuario digita o nome da mae do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o prontuario, nome da mae e data de nascimento digitado

    Cenario: Usuario busca Paciente somente pelo nome, prontuario e nome da mae e data de nascimento
            Quando o usuario digita o nome do Paciente
            E o usuario digita o prontuario do Paciente
            E o usuario digita o nome da mae do Paciente
            E o usuario digita a data de nascimento do Paciente
            E clica em buscar
            Então o sistema retorna os Pacientes com o nome, prontuario, nome da mae e data de nascimento digitado

    Cenario: Usuario busca Paciente sem preencher os campos presentes
            Quando o usuario nao digita nenhum dos campos
            Entao o botao de busca deve estar desabilitado
