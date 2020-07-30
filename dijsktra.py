import time

def dijkstra(graph, origin, destination, routes_results, weights_results):
    unvisited = graph
    costs = {}
    best_father = {}

    def costs_init(node):
        if node != origin:
            costs[node] = float('inf')
        else:
            costs[node] = 0
        return costs

    result = [costs_init(node) for node in graph]

    while len(unvisited) != 0:

        min_cost = ""

        for node in unvisited:
            if min_cost == "":
                min_cost = node
            elif costs[node] < costs[min_cost]:
                min_cost = node

        possibilities = graph[min_cost].items()

        for successor, weight in possibilities:

            if weight + costs[min_cost] < costs[successor]:
                costs[successor] = weight + costs[min_cost]
                best_father[successor] = min_cost

        del unvisited[min_cost]

    back_node = destination
    final_route = []

    while back_node != origin:
        final_route.append(back_node)
        back_node = best_father[back_node]

    final_route.append(back_node)

    weights_results.append(str(costs[destination]))
    final_route.reverse()
    list_to_str = '-'.join(map(str, final_route))
    routes_results.append(list_to_str)
    #time.sleep(4)
