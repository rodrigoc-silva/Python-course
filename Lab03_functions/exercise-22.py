
#This program shows how many birds there are in each state.

def texas() -> None:
    '''function output how many birds Texas has'''
    bird = 5000
    print("Texas has", bird, "birds")


def california() -> None:
    '''function output how many birds California has'''
    bird = 8000
    print("California has", bird, "birds")


def main():
    texas()
    california()

if __name__=="__main__":
    main()


# case 1
# Texas has 5000 birds
# California has 8000 birds

# case 2
# Texas has 8000 birds
# California has 5000 birds

# case 3
# Texas has -5000 birds
# California has -8000 birds

# case 4
# Texas has 0 birds
# California has 0 birds

# case 5
# Texas has 1000 birds
# California has -1000 birds