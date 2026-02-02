from src.domain.book import Book
from matplotlib import pyplot as plt
import pandas as pd


class ChartService():
    def bar_chart(self, x:str, y:str, data:dict[str, float]):
        if not isinstance(x, str) or not isinstance(y, str):
            raise TypeError('Expected a string, got something else')
        if not isinstance(data, dict) or not all(isinstance(k, str) for k in data):
            raise TypeError('Expected a dictionary of strings to floats, got something else')
        df = pd.DataFrame.from_dict(data=data, orient='index', columns=[y])
        ax = df.plot(kind='bar', legend=False)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        plt.tight_layout()
        plt.show()