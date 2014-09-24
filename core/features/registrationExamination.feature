Funcionalidade:  Eu, como Auxiliar, 
Desejo cadastrar um novo pedido de exame 
Para dar início ao processo.

	Cenário: O auxiliar cadastra um novo exame com sucesso
		Dado que o auxiliar acessa o sistema e está autenticado
		E aparece a tela de cadastro de exame
		Quando o  auxiliar digita todos os campos corretamente
		E clica em cadastrar
		Então o sistema cadastra o exame
		E retorna uma mensagem "Exame cadastrado com sucesso"

	Cenário: O auxiliar tenta cadastrar um novo exame com campo obrigatório faltando
		Dado que o auxiliar acessa o sistema e está autenticado
		E aparece a tela de cadastro de exame
		Quando o  auxiliar digita somente alguns campos obrigatorios 
		E clica em cadastrar
		Então o sistema nao cadastra o exame
		E retorna uma mensagem "Campo obrigatorio nao preenchido"
	
	Cenário: O auxiliar tenta cadastrar um novo exame com preenchimento de algum campo incorreto
		Dado que o auxiliar acessa o sistema e está autenticado
		E aparece a tela de cadastro de exame
		Quando o  auxiliar digita algum campo incorretamete
		E clica em cadastrar
		Então o sistema nao cadastra o exame 
		E retorna uma mensagem de campo incorreto
	

