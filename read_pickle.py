import pandas as pd
#import sys
#print(sys.prefix)
def read_pickle_file(file):
    pickle_data = pd.read_pickle(file)
    return pickle_data