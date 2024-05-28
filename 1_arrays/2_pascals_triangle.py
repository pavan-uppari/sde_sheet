class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        for _ in range(2, numRows+1):
            result.append(self.next_pascal_row(result[-1]))
        return result


    def next_pascal_row(self, row: list[int]):
        result = [1]
        for i in range(1, len(row)):
            result.append(row[i] + row[i-1])
        result.append(1)
        return result
        
        