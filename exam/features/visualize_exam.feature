Funcionalidade: Eu como usuario 
				Desejo visualizar o exame completo do paciente 
				Para poder atualiza-lo

	Contexto: Acessar o sistema
			  Dado que o usuario acessa a url "http://localhost:8000" 
			  E efetua o login no sistema
			  E realiza uma busca pelo nome do paciente "Maria"
			  E clica em Ver Paciente

	Cenario: O paciente nao possui exames cadastrados
        	 Quando o paciente nao possui exames
        	 Entao o sistema exibe a mensagem "O paciente não possui exames registrados."

    Cenario: O usuario visualiza o exame completo do paciente
    		 Quando o usuario visualiza os exames do paciente
    		 E clica em um exame escolhido
    		 E clica em Ver Exame
    		 Entao o sistema retorna o exame completo do paciente



