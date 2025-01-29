import matplotlib

matplotlib.use('TkAgg')
import pandas as pd

FILE_NAME = "data.xlsx"


def main():
    df = pd.read_excel(FILE_NAME)
    df.head(2)
    print()


if __name__ == "__main__":
    main()
