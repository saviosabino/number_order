from django.db import models
from django.contrib.auth.models import User


class Order:
    def __init__(self, alist):
        self.lst = []
        self.lst += alist

    def calcMedia(self):
        self.media = 0
        lst, m = self.lst, self.media
        for x in lst: m += x
        m = float(m) / len(lst)
        return m

    def _quicksort(self,lst):
        if len(lst) <= 1: return lst
        lless, lgreater = [], []
        pivot = lst.pop()
        for x in lst:
            if x <= pivot: lless.append(x)
            else: lgreater.append(x)
        return self._quicksort(lless) + [pivot] + self._quicksort(lgreater)

    def quicksort(self):
        self.lst = self._quicksort(self.lst)
        return self.lst

    def bubblesort(self):
        lst = self.lst
        swap = True
        while swap:
            swap = False
            for x in range(1, len(lst)):
                if lst[x - 1] > lst[x]:
                    lst[x - 1], lst[x] = lst[x], lst[x - 1]
                    swap = True
        return lst

    def pythonsort(self):
        lst = self.lst
        lst.sort()
        return lst

