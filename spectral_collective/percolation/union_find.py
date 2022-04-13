class UnionFind():
    def __init__(self, elements=[]):
        self.data = { x : { "parent" : x, "size" : 1 } 
                      for x in elements }

    def find(self, x):
        if not x in self.data:
            self.data[x] = { "parent" : x, "size" : 1 }
            return x
        else:
            y = self.data[x]["parent"]
            if y == x:
                return y
            else:
                return self.find(y)

    def size(self, x):
        y = self.find(x)
        return self.data[y]["size"]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if y == x:
            return

        sx = self.data[x]["size"]
        sy = self.data[y]["size"]

        if sx < sy:
            x, y = y, x

        self.data[y]["parent"] = x
        self.data[x]["size"] = sx + sy
