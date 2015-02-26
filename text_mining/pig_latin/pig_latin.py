"""
"""

def process_text(filename):
    """Print out given file in Pig Latin"""

    fp = open(filename)
    for line in fp:
        for word in line.split():
            # Process into Pig Latin
            print word

    fp.close()

process_text('alice.txt')
#if __name__ == "__main__":
  #  import sys
   # filename = sys.argv[1]
    #process_text(filename)