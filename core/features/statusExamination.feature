Funcionalidade: Eu, como Auxiliar/Medico, 
Desejo ver o status do exame 
Para saber em que parte da analise ele se encontra.

	Cenário: Exame biopsia no status 'Em Macroscopia'
	Dado que o auxiliar/medico acessa o sistema e esta autenticado
	E aparece de listagens de exames do paciente
	Quando o  auxiliar clica no exame de biopsia
	Então o abre os dados do exame e mostra o status como Em Macroscopia 

	Cenário: Exame biopsia no status 'Em Processamento'
	Dado que o auxiliar/medico acessa o sistema e esta autenticado
	E aparece de listagens de exames do paciente
	Quando o  auxiliar clica no exame de biopsia
	Então o abre os dados do exame e mostra o status como Em Processamento

	Cenário: Exame biopsia no status 'Com o residente'
	Dado que o auxiliar/medico acessa o sistema e esta autenticado
	E aparece de listagens de exames do paciente
	Quando o  auxiliar clica no exame de biopsia
	Então o abre os dados do exame e mostra o status como Com o residente

	Cenário: Exame biopsia no status 'Com o staff'
	Dado que o auxiliar/medico acessa o sistema e esta autenticado
	E aparece de listagens de exames do paciente
	Quando o  auxiliar clica no exame de biopsia
	Então o abre os dados do exame e mostra o status como Com o staff

	Cenário: Exame biopsia no status 'Liberado'
	Dado que o auxiliar/medico acessa o sistema e esta autenticado
	E aparece de listagens de exames do paciente
	Quando o  auxiliar clica no exame de biopsia
	Então o abre os dados do exame e mostra o status como Liberado