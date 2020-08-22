class ExtendedList(list):

    def merge_sort(self):
        pass

    def swap(self, index=0):
        if index < len(self):
            self[index], self[index + 1] = self[index + 1], self[index]
        else:
            raise IndexError()
