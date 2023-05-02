import random

while True:
    # Definir o número mínimo e máximo de estrelas
    min_stars = 3
    max_stars = 4

    # Inicializar a linha de estrelas com pontos em todos os espaços
    line = "🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n🟦🟦🟦🟦🟦\n"

    # Obter uma lista dos espaços vazios na linha
    empty_spaces = [i for i in range(25) if line[i] == "🟦"]

    # Escolher um número aleatório de estrelas para adicionar
    num_stars = random.randint(min_stars, max_stars)

    # Se houver mais espaços vazios do que estrelas, adicionar estrelas aleatoriamente
    if len(empty_spaces) >= num_stars:
        for i in range(num_stars):
            index = random.choice(empty_spaces)
            line = line[:index] + "⭐" + line[index+1:]
            empty_spaces.remove(index)
    else:
        # Se houver mais estrelas do que espaços vazios, preencher os espaços restantes com pontos
        for i in range(len(empty_spaces)):
            index = empty_spaces[i]
            line = line[:index] + "⭐" + line[index+1:]
        for i in range(num_stars - len(empty_spaces)):
            index = random.choice([x for x in range(25) if x not in empty_spaces])
            line = line[:index] + "⭐" + line[index+1:]

line.strip()