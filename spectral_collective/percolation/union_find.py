class UnionFind():
    def __init__(self, elements=[]):
        self.data = { x : { "parent" : x, "size" : 1 } 
                      for x in elements }

        self.biggest = None
        self.biggestsize = 0
        if len(elements) > 0:
            self.biggest = elements[0]
            self.biggestsize = 1

    def find(self, x):
        if not x in self.data:
            self.data[x] = { "parent" : x, "size" : 1 }

            if self.biggest == None:
                self.biggest = x
                self.biggestsize = 1

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

        if sx + sy > self.biggestsize:
            self.biggest = x
            self.biggestsize = sx + sy
