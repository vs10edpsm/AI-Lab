def forward_checking(graph, domains, assignment, region):

    if len(assignment) == len(graph):
        return assignment

    for color in domains[region]:

        valid = True
        temp_domains = {r: domains[r][:] for r in domains}

        for neighbor in graph[region]:
            if neighbor in assignment and assignment[neighbor] == color:
                valid = False
                break

        if valid:
            assignment[region] = color

            for neighbor in graph[region]:
                if neighbor not in assignment and color in temp_domains[neighbor]:
                    temp_domains[neighbor].remove(color)

                    if not temp_domains[neighbor]:
                        valid = False
                        break

            if valid:
                next_region = None
                for r in graph:
                    if r not in assignment:
                        next_region = r
                        break

                result = forward_checking(graph, temp_domains, assignment, next_region)
                if result:
                    return result

        assignment.pop(region, None)

    return None


# Map graph (Australia example)
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']
domains = {region: colors[:] for region in graph}
solution = forward_checking(graph, domains, {}, 'WA')

print("Map Coloring Solution:")
print(solution)