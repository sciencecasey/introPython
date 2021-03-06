'''
Created on Mar 3, 2021

@author: CaseyJayne
An iterative pascal triangle method and a recursive method using inside function
'''


def pascal(n: int):
    """
    @param n: the number of rows in the triangle 
    """
    if n == 1:
        print("1")  # base 1
    elif n < 1:
        print("requires positive integer as param")
    else:
        print("1")
        triangle = []
        items = 0
        # tot_row = log(n, 2) # number of total rows
        row = 1  # which row should we be on
        while len(triangle) <= n:
            if len(triangle) < row:
                # no row yet!make row
                triangle.append([1])
                items += 1  # total item count
            elif len(triangle[row - 1]) == row:
                # row already full
                row += 1  # move to nest row
            elif len(triangle[row - 1]) == (row - 1):
                # last item in row, add a 1
                triangle[row - 1].append(1)
                # print the row
                print(*triangle[row - 1])
                items += 1
                row += 1
            else:
                index = len(triangle[row - 1])
                amt = triangle[row - 2][index] + triangle[row - 2][index - 1]
                triangle[row - 1].append(amt)
                items += 1

    # in_pascal(n, triangle, 0)


def pascal_recurs(rows: int) -> list:
    if rows < 1:
        print("error enter positive integer")
    else:
        triangle = [[1]]

        def inside(triangle, tot_rows, cur_row):
            if cur_row > tot_rows:
                # full, complete triangle
                # base case
                return triangle

            if len(triangle) - 1 < cur_row:
                # no row at current position
                # make new row
                triangle.append([1])
            elif len(triangle[cur_row]) == cur_row:
                # last item in row, add a 1
                triangle[cur_row].append(1)
                # next row
                cur_row += 1
            else:
                # add based on previous
                index = len(triangle[cur_row])
                amt = triangle[cur_row - 1][index - 1] + triangle[cur_row - 1][index]
                triangle[cur_row].append(amt)

            return inside(triangle, tot_rows, cur_row)

        return inside(triangle, tot_rows=rows - 1, cur_row=1)  # one less row for zero index


def print_tri(triangle: list):
    for row in range(len(triangle)):
        print(*triangle[row])


def main():
    # pascal(10)
    print_tri(pascal_recurs(10))
    # print(pascal_recus(1))
    # print(pascal_recus(3))
    print(pascal(10))


if __name__ == '__main__':
    main()
