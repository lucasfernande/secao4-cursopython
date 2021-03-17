from pessoa import Pessoa

p1 = Pessoa('Lucas', 19)
p2 = Pessoa('Mariana', 20)

p1.comer('Maçã')
p1.falar('Carros') # erro, pois não pode comer falando
p1.terminarComer()
p1.falar('Carros')
p1.comer('Bolacha')
p1.pararFalar()
p1.comer('Bolacha')


