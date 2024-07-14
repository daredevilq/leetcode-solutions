import random

class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False

        self.arr.append(val)
        self.set[val] = len(self.arr) - 1
        
        return True


    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        
        index = self.set.get(val)
        self.arr[index] = self.arr[-1]
        self.set[self.arr[-1]] = index
        self.arr.pop()
        self.set.pop(val)

        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


print(random.randint(0,2))
