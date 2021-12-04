import random


table = [
    [0, 30, 84, 56, None, 70, None, 75, None, 80],
    [30, 0, 65, None, None, None, 70, None, None, 40],
    [84, 65, 0, 74, 52, 55, None, 60, 143, 48],
    [56, None, 74, 0, 135, None, None, 20, None, None],
    [None, None, 52, 135, 0, 70, None, 122, 98, 80],
    [70, None, 55, None, 70, 0, 63, None, 82, 35],
    [None, 70, None, None, None, 63, 0, None, 120, 57],
    [75, None, 135, 20, 122, None, None, 0, None, None],
    [None, None, 143, None, 98, 82, 120, None, 0, None],
    [80, 40, 48, None, 80, 35, 57, None, None, 0]
]


def is_valid(solution):
    for i in range(0, len(solution)-1):
        if table[solution[i]][solution[i+1]] is None:
            return False
    return True


# cria um solução inicial aleatória que seja válida, partindo da cidade que o usuário escolher
def random_solution(first_city):
    cities = list(range(10))
    path = []

    for i in range(len(cities)):
        random_city = cities[random.randint(0, len(cities)-1)]
        path.append(random_city)
        cities.remove(random_city)

    if is_valid(path):
        while path[0] != first_city:
            path.insert(0, path.pop())

        path.append(first_city)
        return path
    else:
        return random_solution(first_city)


def path_length(solution):  # calcula o tamanho da rota
    length = 0
    for i in range(len(solution)-1):
        if table[solution[i % 10]][solution[(i+1) % 10]] is not None:
            length += table[solution[i % 10]][solution[(i+1) % 10]]

    return length


def hill_climbing(solution):
    count = 500
    aux = solution[:]
    print('Começando com a solução aleatória: ', solution)
    print()
    while count > 0:
        i = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        j = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        neighbour = solution[:]
        neighbour[i], neighbour[j] = neighbour[j], neighbour[i]

        if is_valid(neighbour):
            if path_length(neighbour) < path_length(solution):
                print(solution, "->", neighbour)
                print(path_length(solution),
                      "->", path_length(neighbour))
                solution = neighbour[:]
        count -= 1

    if solution == aux:
        print('Não houve melhora, a solução inicial já é o melhor caminho... \n')
    return solution


def main():
    city = int(input('Digite a cidade de origem: '))
    solution = random_solution(city-1)
    best_solution = hill_climbing(solution)
    distance = path_length(best_solution)

    for i in range(0, len(best_solution)):
        best_solution[i] += 1
    print('===============================RESULTADO===============================')
    print('Melhor solução: ', best_solution)
    print('Distância: {} km'.format(distance))


if __name__ == "__main__":
    main()
