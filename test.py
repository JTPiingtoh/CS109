from tqdm import tqdm

def generate_stems(
        seed: list,
        items: list,
        comb_list:list,

):
    '''
    When given a seed list of [0, 1, 2, ..., n],  p, where p n+1->size , generating a lists of "stems" where a stem =
    concat(seed, p)
    '''

    tip_index_list = 0

    for i in range(len(items)):

        if i + 1 >= len(items):
            return

        if items[i] == seed[-1]:
            tip_index_list = i + 1
            break

    combination = [""]

    while combination[-1] != items[-1]:
        combination = seed.copy()
        combination.append(items[tip_index_list])
        generate_stems(combination, items, comb_list)
        comb_list.append(combination)
        tip_index_list += 1


def combinations(
    items: list
):
    
    comb_list = []

    if len(items) == 1:
        return items.copy()

    for i in tqdm(range(0, len(items))):

        seed = [items[i]]
        comb_list.append(seed)
        generate_stems(seed, items, comb_list)

    return comb_list

    
items = [str(i) for i in range(4)]

comb_list = combinations(items)
            
print(comb_list)