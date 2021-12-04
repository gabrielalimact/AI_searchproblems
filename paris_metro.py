import heapq

paris = [[0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],
         [0, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],
         [0, 0, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],
         [0, 0, 0, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],
         [0, 0, 0, 0, 0, 3, 2, 21, 25, 31, 28, 27, 16, 20],
         [0, 0, 0, 0, 0, 0, 4, 23, 28, 33, 41, 30, 17, 20],
         [0, 0, 0, 0, 0, 0, 0, 22, 25, 29, 38, 28, 13, 17],
         [0, 0, 0, 0, 0, 0, 0, 0, 9, 22, 18, 7, 25, 30],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 12, 23, 28],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 27, 20, 23],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 35, 39],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 37],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

connections = [[0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 9, 0, 0, 0, 0, 0, 11, 4, 0, 0, 0, 0],
               [0, 0, 0, 7, 0, 0, 0, 0, 10, 0, 0, 0, 13, 0],
               [0, 0, 0, 0, 13, 0, 0, 13, 0, 0, 0, 0, 11, 0],
               [0, 0, 0, 0, 0, 3, 2, 21, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 7, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

lines = [['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],  # AZUL
         ['E10', 'E2', 'E9', 'E8', 'E5', 'E7'],  # AMARELO
         ['E12', 'E8', 'E4', 'E13', 'E14'],  # VERDE
         ['E11', 'E9', 'E3', 'E13']]  # VERMELHO


class priority_queue:
    def __init__(self):
        self.stations = []

    def is_empty(self):
        if self.stations == []:
            return True
        else:
            return False

    def push(self, station, dist):
        heapq.heappush(self.stations, (dist, station))

    def pop(self):
        return heapq.heappop(self.stations)

    def border(self):
        return sorted(self.stations)

# função para saber dividir a string da estação e pegar so o inteiro


def find_station(station):
    st = station.split('E')
    return int(st[1])-1


# função que calcula h(n)
def calculate_h(next, goal):
    station1 = find_station(next)
    station2 = find_station(goal)

    if station1 >= station2:
        aux = station1
        station1 = station2
        station2 = aux

    h = paris[station1][station2]

    return h


# função que calcula g(n)
def calculate_g(start, end):
    station1 = find_station(start)
    station2 = find_station(end)

    if station1 >= station2:
        aux = station1
        station1 = station2
        station2 = aux

    g = paris[station1][station2]

    return g

# verificar as estaçẽs disponiveis para busca


def stations_avaibles(now, previous):
    station1 = find_station(now)
    station2 = find_station(previous)

    availables = []
    for i in range(len(connections[station1])):
        # não pode voltar a estação de inicio
        if connections[station1][i] != 0 and i > station1:
            st = 'E' + str(i+1)
            availables.append(st)
        if connections[i][station1] != 0 and i <= station1:
            st = 'E' + str(i+1)
            availables.append(st)

    return availables

# algoritmo de busca A*


def a_star_algorithm(start, end):
    path = {}
    dist = {}
    q = priority_queue()
    q.push(start, 0)
    dist[start] = 0
    path[start] = None
    nodes_list = []

    print_final_path(start, end, path, dist, nodes_list, q, 0)

    previous = start

    while(q.is_empty() == False):
        now = q.pop()[1]
        nodes_list.append(now)

        if now == end:
            break

        availables = stations_avaibles(now, previous)

        for next in availables:
            g = dist[now] + calculate_g(now, next)
            h = calculate_h(next, end)
            f = g + h

            if (next not in dist or g < dist[next]):
                dist[next] = g
                q.push(next, f)
                path[next] = now
        print_final_path(start, end, path, dist, nodes_list, q, 1)
    print_final_path(start, end, path, dist, nodes_list, q, 2)
# função para imprimir os caminhos


def print_final_path(start, end, path, dist, visited_node, q, line):
    final_path = []
    i = end
    lines_visited = ["", "", "", ""]
    tamanho = 0
    if line == 0:
        print("O percurso desejado é ir da estação {} até a {}.\n" .format(
            str(start), str(end)))
        print("Iniciando busca...\n")
    elif line > 0:
        print("Fronteira: {} ".format(str(q.border())))
        print("Estações expandidas: {}".format(
            str(visited_node)))

    if line == 2:
        while(path.get(i) != None):
            final_path.append(i)
            i = path[i]
        final_path.append(start)
        final_path.reverse()

        for i in range(0, len(final_path)):
            if final_path[i] in lines[0]:
                lines_visited[0] = "AZUL"
            elif final_path[i] in lines[1]:
                lines_visited[1] = "AMARELO"
            elif final_path[i] in lines[2]:
                lines_visited[2] = "VERDE"
            elif final_path[i] in lines[3]:
                lines_visited[3] = "VERMELHO"

        for i in range(0, 3):
            if lines_visited[i] != "":
                tamanho += 1

        tempo_extra = (tamanho-1)*4
        print("\n------------------------------------------------------------------\n")
        print("O menor caminho encontrado é: {}".format(final_path))
        print("Passando por {} estações, nas linhas {}".format(
            str(len(final_path)), lines_visited))
        print("Com a distância percorrida de: {} km.".format(str(dist[end])))

        print("Tempo estimado da viagem: {} minutos, sendo {} minutos de baldeação. ".format(
            str(((dist[end]/30)*60)+(tempo_extra)), tempo_extra))
# função main


def main():
    start = 'E1'
    end = 'E12'
    a_star_algorithm(start, end)


if __name__ == '__main__':
    main()
