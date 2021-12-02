import os

class Input:
    def __init__(self, day):
        with self._open(day) as f:
            self._data = f.read()

    def _open(self, day):
        filename = f"{day:02d}.txt"
        return open(os.path.join("inputs", filename))

    def data(self):
        return self._data

    def lines(self, transform=None):
        lines = self._data.split('\n')
        if transform:
            return [transform(l.strip()) for l in lines if l != '']
        else:
            return lines
