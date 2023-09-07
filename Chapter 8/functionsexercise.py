first = ["john", "Evan", "Jordan", "Max"]
last = ["smith", "Smith", "williams", "Bell"]

def full_names(first, last):
    names = []
    for name in range(len(first)):
        names.append(first[name] + " " + last[name])
    return names

print(full_names(first, last))




#expectd output ["john", "Evan", "Jordan", "Max"]