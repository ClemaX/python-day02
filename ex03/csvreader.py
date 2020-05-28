import csv


class CsvReader():
    def __init__(
            self,
            filename=None,
            sep=',',
            header=False,
            skip_top=0,
            skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_bottom = -skip_bottom if skip_bottom > 0 else None
        self.skip_top = skip_top

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError as e:
            return None
        else:
            start = self.skip_top
            end = self.skip_bottom
            self.body = self.file.readlines()[start:end]
            if self.header:
                self.header_data = csv.reader(self.body[0], delimiter=self.sep)
                start = 1
            else:
                self.header_data = None
                start = 0
            self.data = list(csv.reader(self.body[start:], delimiter=self.sep))
            if self.data:
                cols = 0
                if self.header:
                    cols = len(self.header_data)
                else:
                    cols = len(self.data[0])
                if not all(len(row) == cols for row in self.data):
                    return None
            return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header_data
