def main():
    import sys
    input = sys.stdin.read().splitlines()
    ptr = 0
    c = int(input[ptr])
    ptr += 1
    for _ in range(c):
        # Leer el número de estados
        n = int(input[ptr])
        ptr += 1
        
        # Leer el alfabeto
        alphabet = input[ptr].split()
        ptr += 1
        
        # Leer estados finales
        final_states = list(map(int, input[ptr].split()))
        ptr += 1
        
        # Leer transiciones
        transitions = {}
        states = list(range(n))
        for state in states:
            parts = list(map(int, input[ptr].split()))
            transitions[state] = {symbol: parts[i+1] for i, symbol in enumerate(alphabet)}
            ptr += 1
        
        # Minimizar el DFA
        equivalent_pairs = minimize_dfa(states, alphabet, final_states, transitions)
        
        # Imprimir pares equivalentes en orden lexicográfico
        equivalent_pairs_sorted = sorted(equivalent_pairs)
        print(' '.join(f"{p[0]} {p[1]}" for p in equivalent_pairs_sorted))

def minimize_dfa(states, alphabet, final_states, transitions):
    # Inicializar partición: F y Q-F
    F = set(final_states)
    non_F = set(states) - F
    partition = []
    if F:
        partition.append(F)
    if non_F:
        partition.append(non_F)
    
    changed = True
    while changed:
        changed = False
        new_partition = []
        for group in partition:
            # Dividir el grupo en subgrupos basados en transiciones
            split_groups = split(group, partition, alphabet, transitions)
            new_partition.extend(split_groups)
            if len(split_groups) > 1:
                changed = True
        partition = new_partition
    
    # Generar pares de estados equivalentes (orden lexicográfico)
    equivalent_pairs = []
    for group in partition:
        group_list = sorted(group)
        for i in range(len(group_list)):
            for j in range(i + 1, len(group_list)):
                equivalent_pairs.append((group_list[i], group_list[j]))
    return equivalent_pairs

def split(group, partition, alphabet, transitions):
    if len(group) == 1:
        return [group]
    
    # Para cada símbolo del alfabeto, verificar si las transiciones dividen el grupo
    split_dict = {}
    for state in group:
        key = []
        for symbol in alphabet:
            next_state = transitions[state][symbol]
            # Encontrar el índice del grupo al que pertenece next_state
            for i, p in enumerate(partition):
                if next_state in p:
                    key.append(i)
                    break
        key_tuple = tuple(key)
        if key_tuple not in split_dict:
            split_dict[key_tuple] = set()
        split_dict[key_tuple].add(state)
    
    return list(split_dict.values())

if __name__ == "__main__":
    main()