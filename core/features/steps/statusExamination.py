from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not


@given(u'que o auxiliar acessa o sistema na pagina do paciente e esta autenticado')
def accessing_the_system(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/paciente/1')

@given(u'aparece a tela com a listagem de exames do paciente')
def show_listing_of_examinations(context):
	context.driver.title | should | equal_to('Matheus Souza Fernandes | Anato HUB')

@when(u'o  auxiliar clica no exame de biopsia')
def show_biopsy(context):
	context.driver.find_element_by_link_text('Biopsia').click()

@then(u'abre os dados do exame')
def show_examination(context):
	assert True    

@then(u'mostra o status como Em Macroscopia')
def status_examination(context):
    id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Em Macroscopia')
    context.driver.close()


@then(u'mostra o status como Em Processamento')
def status_examination(context):
    id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Em Processamento')
    context.driver.close()

@then(u'mostra o status como Com o residente')
def status_examination(context):
    id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Com o residente')
    context.driver.close()

@then(u'mostra o status como Com o staff')
def status_examination(context):
    id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Com o staff')
    context.driver.close()

@then(u'mostra o status como Liberado')
def status_examination(context):
    id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Liberado')
    context.driver.close()

@when(u'o  auxiliar clica no exame de citologia geral')
def show_general_cytology(context):
	context.driver.find_element_by_link_text('Citologia Geral').click()

@when(u'o  auxiliar clica no exame de citologia ginecologica')
def show_gynecological_cytology(context):
	context.driver.find_element_by_link_text('Citologia Ginecologica').click()

@when(u'o  auxiliar clica no exame de Imuno-Histoquimica')
def show_Immunohistochemistry(context):
	context.driver.find_element_by_link_text('Imuno-Histoquimica').click()

@then(u'mostra o status como Em estudo previo')
def status_examination(context):
    id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Em estudo previo')
    context.driver.close()

@when(u'o  auxiliar clica no exame de Necropsia')
def show_necropsy(context):
	context.driver.find_element_by_link_text('Necropsia').click()

@then(u'mostra o status como Selecao de amostras')
def status_examination(context):
   id_status = context.driver.find_element_by_id('Status') 
    status = id_status.text
    status | should | equal_to('Selecao de amostras')
    context.driver.close()
