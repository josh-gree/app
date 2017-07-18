# will read a csv and return the mean value of all numeric columns
import fire

import pandas as pd


def means(fname):
    try:
        df = pd.read_csv(fname,header=0)
    except Exception as e:
        print(e)
        return None
    
    cols = df.columns
    mean = df.mean(axis=0)
    return dict(mean)

if __name__ == '__main__':
  fire.Fire(means)