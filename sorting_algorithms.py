class ExtendedList(list):

    def swap(self, i_1, i_2):
        if i_1 >= len(self) or i_1 < 0 or i_2 >= len(self) or i_2 < 0:
            raise IndexError("List index out of range.")

        # This function alters the list by swapping the elements at the given indexes.
        self[i_2], self[i_1] = self[i_1], self[i_2]
        return self

    def bubble_sort(self):
        _sorted = False
        while not _sorted:
            _sorted = True
            for i in range(len(self)-1):
                i_1 = i
                i_2 = i + 1
                if self[i_1] > self[i_2]:
                    self.swap(i_1, i_2)
                    _sorted = False
        return self

    def merge_sort(self):
        pass
