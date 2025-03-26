import sys
import pandas as pd
from pandas.errors import (
        EmptyDataError,
        ParserError
        )


def load(path: str) -> pd.DataFrame:
    try:
        with open(path,'r') as f:
            df = pd.read_csv(f)
            dim = df.shape
            print(f"Loading dataset of dimensions {dim}")
            return df
    
    except OSError as e:
        print (f"{type(e).__name__}: Could not open/read file: {path}")
        sys.exit()
    except EmptyDataError as e:
        print (f"{type(e).__name__}: File {path} is empty.")
        sys.exit()
    except ParserError as e:
        print (f"{type(e).__name__}: Issue parsing the {path} file.")
        sys.exit()
    except UnicodeDecodeError as e:
        print (f"{type(e).__name__}: Probably the file: {path} is not UTF-8.")
        sys.exit()
