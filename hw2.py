from program import Program
import sys

def main(filename):
    program = Program(filename=filename)
    program.print_tokens()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage:" + str(sys.argv[0]) + " source-code-file"
        sys.exit(1)
    else:
        main(sys.argv[1])
