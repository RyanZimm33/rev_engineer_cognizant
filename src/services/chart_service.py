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
    
    def scatter_chart(self, x:str, y:str, data:dict[float, float]):
        if not isinstance(x, str) or not isinstance(y, str):
            raise TypeError('Expected a string, got something else')
        if not isinstance(data, dict) or not all(isinstance(k, float) for k in data):
            raise TypeError('Expected a dictionary of floats to floats, got something else')
        df = pd.DataFrame(list(data.items()), columns=[x, y])
        df[x] = df[x].astype(float)
        df[y] = df[y].astype(float)
        ax = df.plot.scatter(x=x, y=y, legend=False)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        plt.tight_layout()
        plt.show()
    
    def line_chart(self, x:str, y:str, data:dict[int, int]):
        if not isinstance(x, str) or not isinstance(y, str):
            raise TypeError('Expected a string, got something else')
        if not isinstance(data, dict) or not all(isinstance(k, int) for k in data):
            raise TypeError('Expected a dictionary of ints to ints, got something else')
        df = pd.DataFrame.from_dict(data=data, orient='index', columns=[y])
        ax = df.plot(legend=False)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        plt.tight_layout()
        plt.show()

    def pie_chart(self, data: dict[str, int]):
        if not isinstance(data, dict) or not all(isinstance(k, str) for k in data):
            raise TypeError('Expected a dictionary of strings to ints, got something else')
        plt.pie(list(data.values()), labels=list(data.keys()))
        plt.show()
        