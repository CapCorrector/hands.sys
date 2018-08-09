class ArrayWalker:
    def __init__(self):
        self.arr = []
        self.current = (0,0)
        self.path = []
    def read(self, filename):
        with open(filename) as f:
            for line in f:
                self.arr.append(list(map(lambda a: int(a), line.strip().split(';'))))
        self.curbig = self.arr[0][0]

    def nextstep(self):
        poss_moves = []
        self.arr[self.current[0]][self.current[1]] = False
        if self.current[0] != 0 and self.arr[self.current[0]-1][self.current[1]]:
            poss_moves.append([self.arr[self.current[0]-1][self.current[1]], (-1,0)])
        if self.current[1] != 0 and self.arr[self.current[0]][self.current[1]-1]:
            poss_moves.append([self.arr[self.current[0]][self.current[1]-1], (0,-1)])
        if self.current[0] < len(self.arr)-1 and self.arr[self.current[0]+1][self.current[1]]:
            poss_moves.append([self.arr[self.current[0]+1][self.current[1]], (1,0)])
        if self.current[1] < len(self.arr[0])-1 and self.arr[self.current[0]][self.current[1]+1]:
            poss_moves.append([self.arr[self.current[0]][self.current[1]+1], (0,1)])
        poss_moves.sort(reverse=True)
        if poss_moves == [] or (len(poss_moves) > 1 and poss_moves[0][0] == poss_moves[1][0]):
            result = False
        else:
            deltax = poss_moves[0][1][1]
            deltay = poss_moves[0][1][0]
            self.path.append(self.arr[self.current[0]+deltay][self.current[1]+deltax])
            result = [self.current[0]+deltay,self.current[1]+deltax]
        return result

if __name__ == '__main__':
    aw = ArrayWalker()
    aw.read('/Users/Corrector/Documents/Личное/США/UCSC/Python/Oleg/array.txt')
    print(aw.arr)
    aw.current = aw.nextstep()
    while aw.current:
        aw.current = aw.nextstep()
    print(aw.path)
    print(aw.arr)
    