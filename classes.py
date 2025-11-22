import random 

class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        tipo_ataque = ""
        tipo_lower = self.tipo.lower()

        if tipo_lower == 'mago':
            tipo_ataque = 'magia'
        elif tipo_lower == 'guerreiro':
            tipo_ataque = 'espada'
        elif tipo_lower == 'monge':
            tipo_ataque = 'artes marciais'
        elif tipo_lower == 'ninja':
            tipo_ataque = 'shuriken'
        else:
            tipo_ataque = 'ataque desconhecido e nada efetivo'
        
        print(f"O {self.tipo} chamado **{self.nome}** atacou usando {tipo_ataque}")

print("--- PREPARANDO O GRUPO DE HEROIS ---")


grupo_de_herois = [
    Heroi("Frieren", 1300, "Mago"),
    Heroi("Arthur", 30, "Guerreiro"),
    Heroi("Rock Lee", 33, "Monge"),
    Heroi("Kakashi", 33, "Ninja"),
    Heroi("Gandalf", 2000, "Mago"),
    Heroi("Desconhecido", 1000, "")
]

print("--- A BATALHA COMEÇOU ---")

for turno in range(1, 4):
    heroi_sorteado = random.choice(grupo_de_herois)
    
    print(f"Turno {turno}: ", end="")
    heroi_sorteado.atacar()
