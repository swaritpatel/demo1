from mrjob.job import MRJob
from mrjob.step import MRStep

class MatrixMultiplication(MRJob):

    def mapper(self, _, line):
        # Parse the input matrix
        matrix_name, row, col, value = line.strip().split("\t")
        row, col, value = int(row), int(col), float(value)

        if matrix_name == "A":
            # Emit intermediate key-value pairs with the same key for each element in the row
            for k in range(self.matrix_size):
                yield (row, k), (col, value)
        else:
            # Emit intermediate key-value pairs with the same key for each element in the column
            for k in range(self.matrix_size):
                yield (k, col), (row, value)

    def reducer(self, key, values):
        # Multiply the corresponding elements and accumulate the result
        result = 0
        values_a, values_b = [], []

        for col_or_row, value in values:
            if col_or_row in values_a:
                result += value * values_b[values_a.index(col_or_row)]
            elif col_or_row in values_b:
                result += value * values_a[values_b.index(col_or_row)]
            elif len(values_a) < len(values_b):
                values_a.append(col_or_row)
                values_a.append(value)
            else:
                values_b.append(col_or_row)
                values_b.append(value)

        yield key, result

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init,
                   mapper=self.mapper,
                   reducer=self.reducer)
        ]

if __name__ == '__main__':
    MatrixMultiplication.run()
