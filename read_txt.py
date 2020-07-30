vertices = []
edges = []

def read_txt():
    file = open("example.txt")
    for line in file.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        verify_format(line)
        file.close()
    show_info()


def verify_format(line_txt):
    global vertices
    if line_txt.count(",") == 0:
        vertices.append(line_txt)
    else:
        line_txt = line_txt.split(",")
        edges_distribution(line_txt)


def edges_distribution(line_txt):
    global edges
    streetraffic = line_txt[3]
    valor = traffic_value(streetraffic)
    edges.append((line_txt[0], line_txt[1], int(line_txt[2]) + valor))


def traffic_value(streetraffic):
    weight = 0
    if streetraffic == "medium":
        weight = 2
    elif streetraffic == "heavy":
        weight = 4
    else:
        weight = 0
    return weight
