# def convert(ratios, from_unit, to_unit, value):
#     if from_unit == to_unit:
#         return value

#     # Direct conversion check
#     if (from_unit, to_unit) in ratios:
#         return value / ratios[(from_unit, to_unit)]
    
#     if (to_unit, from_unit) in ratios:
#         return value * ratios[(to_unit, from_unit)]
#     #three_units 
#     if (from_unit, "glorp") in ratios:
#         # Convert from from_unit to glorp
#         value_in_glorp = value / ratios[(from_unit, "glorp")] 
#         # Now convert from glorp to to_unit if possible
#         if (to_unit,"glorp") in ratios:
#             return value_in_glorp * ratios[(to_unit,"glorp" )]
#     # Build a graph for indirect conversions
    

#     graph = {}
    
#     for (unit1, unit2), ratio in ratios.items():
#         if unit1 not in graph:
#             graph[unit1] = {}
#         if unit2 not in graph:
#             graph[unit2] = {}
#         graph[unit1][unit2] = ratio
#         graph[unit2][unit1] = 1 / ratio

#     # BFS for indirect conversion
#     queue = [(from_unit, value)]
#     visited = {from_unit}

#     while queue:
#         current_unit, current_value = queue.pop(0)

#         for neighbor, ratio in graph[current_unit].items():
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 new_value = current_value * ratio

#                 if neighbor == to_unit:
#                     return new_value

#                 queue.append((neighbor, new_value))




from collections import defaultdict

def convert(ratios, from_unit, to_unit, value):
    if from_unit == to_unit:
        return value

    if (from_unit, to_unit) in ratios:
        return value / ratios[(from_unit, to_unit)]
    
    if (to_unit, from_unit) in ratios:
        return value * ratios[(to_unit, from_unit)]
    
    graph = defaultdict(list)
    for (u, v), r in ratios.items():
        graph[u].append((v, 1 / r))
        graph[v].append((u, r))
    
    visited = set()

    def dfs(curr, target, acc):
        if curr == target:
            return acc
        visited.add(curr)
        for neighbor, factor in graph[curr]:
            if neighbor not in visited:
                result = dfs(neighbor, target, acc * factor)
                if result is not None:
                    return result
        return None

    conversion_factor = dfs(from_unit, to_unit, 1)
    if conversion_factor is None:
        return None
    return value * conversion_factor

