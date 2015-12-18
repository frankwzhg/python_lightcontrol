import serial, struct
import sys

def command_excute(argv):
    print argv[1]
    if argv[1] == "close":
        print "close"

if __name__ == "__main__":

    command_excute(sys.argv)