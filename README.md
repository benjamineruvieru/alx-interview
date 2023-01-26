# 0x00. Pascal's Triangle


## Tasks

### [0. Pascal's Triangle](./0-pascal_triangle.py)
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- [x] Returns an empty list if `n <= 0`
- [x] You can assume `n` will be always an integer

```sh
$ cat 0-main.py
```
```py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```
```sh
$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```