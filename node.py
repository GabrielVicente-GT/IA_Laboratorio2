class Node(object):
    def __init__(self, key, value):
        self.name = key
        self.parents = []
        self.value = value
        
    def probability(self, value, valueDado):
        parent_values = [valueDado[parent.name] for parent in self.parents]
        i = 0
        for pv in parent_values:
            i = i * 2 + pv
        return self.value[i][value]