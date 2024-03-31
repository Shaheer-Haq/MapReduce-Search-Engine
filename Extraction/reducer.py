import sys

def reducer():
    for line in sys.stdin:
        print(line.strip())

if __name__ == "__main__":
    reducer()

