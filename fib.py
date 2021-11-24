import argparse

parser = argparse.ArgumentParser(description='Fib Numbers are fun')
parser.add_argument('--number', dest='number', type=int, help='Number of fibs to return')
args = parser.parse_args()
number = args.number

def main(number):
    count = number + 1
    range = [0,1]
    print(0) # this is why +1 to number
    while len(range) < count:
        print(range[-1])
        range.append( range[-1] + range[-2] )

if __name__== "__main__":
  main(number)