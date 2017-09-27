import time
import sys

def main():
    while True:
        sys.stdout.write("Hello OpenShift!\n")
        sys.stdout.flush()
        time.sleep(5)

if __name__ == '__main__':
    main()
