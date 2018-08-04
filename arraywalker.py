class ArrayWalker:
    arr = []
    current = (0,0)
    path = []
    def read(self, filename):
        with open(filename) as f:
            for line in f:
                self.arr.append(list(map(lambda a: int(a), line.strip().split(';'))))
            f.close()
        self.curbig = self.arr[0][0]

    def nextstep(self, coordinates, biggest):
        if coordinates[0] != 0 and biggest < self.arr[coordinates[0]][coordinates[1]-1]:
            biggest = self.arr[coordinates[0]-1][coordinates[1]]
            result = (coordinates[0]-1,coordinates[1])
        if coordinates[1] != 0 and biggest < self.arr[coordinates[0]-1][coordinates[1]]:
            biggest = self.arr[coordinates[0]][coordinates[1]-1]
            result = (coordinates[0],coordinates[1]-1)
        if coordinates[0] < len(self.arr)-1 and biggest < self.arr[coordinates[0]+1][coordinates[1]]:
            biggest = self.arr[coordinates[0]+1][coordinates[1]]
            result = (coordinates[0]+1,coordinates[1])
        if coordinates[1] < len(self.arr[0])-1 and biggest < self.arr[coordinates[0]][coordinates[1]+1]:
            biggest = self.arr[coordinates[0]][coordinates[1]+1]
            result = (coordinates[0],coordinates[1]+1)
        if biggest <= self.curbig:
            result = False
        else:
            self.curbig = biggest
            self.path.append(biggest)
        return result

if __name__ == '__main__':
    aw = ArrayWalker()
    aw.read('/Users/Corrector/Documents/Личное/США/UCSC/Python/Oleg/array.txt')
    print(aw.arr)
    aw.current = aw.nextstep(aw.current, aw.curbig)
    while aw.current:
        aw.current = aw.nextstep(aw.current, aw.curbig)
    print(aw.path)
    