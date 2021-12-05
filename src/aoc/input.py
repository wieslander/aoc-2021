import os

class Input:
    def __init__(self, day, input_file=None):
        with self._open(day, input_file) as f:
            self._data = f.read()

    def _open(self, day, input_file=None):
        path = input_file
        if path is None:
            filename = f"{day:02d}.txt"
            path = os.path.join("inputs", filename)
        return open(path)

    def data(self):
        return self._data

    def lines(self, transform=None):
        lines = self._data.split('\n')
        if transform:
            return [transform(l.strip()) for l in lines if l != '']
        else:
            return lines
