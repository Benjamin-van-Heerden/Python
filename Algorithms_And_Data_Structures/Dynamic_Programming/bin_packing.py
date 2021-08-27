def first_fit_decreasing(capacities, bin_max_capacity):
    # bins created at runtime - as many bins as needed
    solution_bins = []

    item_names = list(capacities.keys())
    sorted_items = sorted(item_names, key=lambda x: capacities[x], reverse=True)
    
    for item in sorted_items:
        bin_found = False
        item_cap = capacities[item]

        for index, actual_bin in enumerate(solution_bins):
            actual_bin_summed_size = sum([capacities[key] for key in actual_bin])
            if item_cap <= (bin_max_capacity - actual_bin_summed_size):
                solution_bins[index].append(item)
                bin_found = True
                break
        if not bin_found:
            solution_bins.append([item])

    return solution_bins



print(first_fit_decreasing({"item-1": 4, "item-2": 2, "item-3": 7, "item-4": 5, "item-5": 6, "item-6": 3}, 8))

