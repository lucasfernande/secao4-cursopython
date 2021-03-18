from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

maquina = MaquinaDeEscrever()
caneta = Caneta('Bic')
escritor = Escritor('João')
escritor.ferramenta = caneta # associando o escritor com a caneta ou maquina

escritor.ferramenta.escrever() # executando o método da classe caneta através do escritor

