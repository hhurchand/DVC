from utils.constants import get_config
from pathlib import Path
import pandas as pd
from typing import List

class DataLoader:
    def __init__(self):
        pass
    def get_raw_data(self,path: str, columns: List) -> pd.DataFrame:
        with open(path) as f:
            return pd.read_csv(f)[columns]



if __name__ == "__main__":

    config = get_config()
    path = Path(config["raw_data_config"]["raw_data"])
    columns = config["raw_data_config"]["columns"]
    df = DataLoader().get_raw_data(path=path,columns=columns)
    print(df)
