Funcionalidade: Eu, como usuario
Desejo efetuar a busca de pacientes no sistema
Para visualizar seus dados e seus exames

	Cenario: Usuario busca Paciente somente pelo nome
	Dado que o Usuario esta na tela de busca de pacientes
	Quando o usuario digita o nome do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com o nome digitado

	Cenario: Usuario busca Paciente somente pelo prontuario
	Dado que o Usuario esta na tela de busca de pacientes
	Quando o usuario digita o prontuario do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com o prontuario digitado

	Cenario: Usuario busca Paciente somente pelo nome da mae
	Dado que o Usuario esta na tela de busca de pacientes
	Quando o usuario digita o nome da mae do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com o nome da mae digitado

    #-------Implementando
	Cenario: Usuario busca Paciente somente pela data de nascimento
	Dado que o Usuario esta na tela de busca de pacientes
	Quando o usuario digita a data de nascimento do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a data de nascimento digitada

	Cenario: Usuario busca Paciente somente pelo nome e prontuario
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome e prontuario do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a nome e prontuario digitado

	Cenario: Usuario busca Paciente somente pelo nome e nome da mae
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome e nome da mae do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a nome e nome da mae digitado

	Cenario: Usuario busca Paciente somente pelo nome e data de nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome e data de nascimento do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a nome e data de nascimento digitado

	Cenario: Usuario busca Paciente somente pelo prontuario e nome da mae
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o prontuario e nome da mae do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a prontuario e nome da mae digitado

	Cenario: Usuario busca Paciente somente pelo prontuario e data nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o prontuario e data nascimento do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a prontuario e data nascimento digitado

	Cenario: Usuario busca Paciente somente pelo nome da mae e data nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome da mae e data nascimento do Paciente
	E clica em buscar
	Então o sistema retorna os Pacientes com a nome da mae e data nascimento digitado

	Cenario: Usuario busca Paciente somente pelo nome, prontuario e nome da mae
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome, prontuario e nome da mae
	E clica em buscar
	Então o sistema retorna os Pacientes com o nome, prontuario e nome da mãe digitado

	Cenario: Usuario busca Paciente somente pelo nome, prontuario e data de nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome, prontuario e data de nascimento
	E clica em buscar
	Então o sistema retorna os Pacientes com o nome, prontuario e data de nascimento digitado

	Cenario: Usuario busca Paciente somente pelo nome, nome da mae e data de nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome, nome da mae e data de nascimento
	E clica em buscar
	Então o sistema retorna os Pacientes com o nome, nome da mãe e data de nascimento digitado

	Cenario: Usuario busca Paciente somente pelo prontuario, nome da mae e data de nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o prontuario, nome da mae e data de nascimento
	E clica em buscar
	Então o sistema retorna os Pacientes com o prontuario, nome da mae e data de nascimento digitado

	Cenario: Usuario busca Paciente somente pelo nome, prontuario e nome da mae e data de nascimento
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario digita o nome, prontuario, nome da mae e data de nascimento
	E clica em buscar
	Então o sistema retorna os Pacientes com o nome, prontuario, nome da mae e data de nascimento digitado

	Cenario: Usuario busca Paciente sem preencher os campos presentes
	Dado que o Usuario esta autenticado
	E aparece a tela de busca
	Quando o usuario nao digita nenhum dos campos
	Entao o botao de busca deve estar desabilitado
