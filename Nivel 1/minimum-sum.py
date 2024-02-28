def min_sum(list):
    min_val = min(list)
    
    return min_val * (len(list)-1)

list = [7, 2, 3, 4, 5, 6]

print(min_sum(list))
