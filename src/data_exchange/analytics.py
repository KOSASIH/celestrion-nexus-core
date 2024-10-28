import numpy as np
import pandas as pd

class DataAnalytics:
    def __init__(self, data):
        self.data = data

    def summarize_data(self):
        """Generates a summary of the data."""
        df = pd.DataFrame(self.data)
        summary = {
            "mean": df.mean(),
            "median": df.median(),
            "std_dev": df.std(),
            "min": df.min(),
            "max": df.max()
        }
        return summary

    def visualize_data(self):
        """Visualizes the data using matplotlib."""
        import matplotlib.pyplot as plt

        df = pd.DataFrame(self.data)
        df.plot(kind='line')
        plt.title('Data Visualization')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.show()

# Example usage
if __name__ == "__main__":
    sample_data = [
        {"temperature": 22.5, "pressure": 1013},
        {"temperature": 23.0, "pressure": 1012},
        {"temperature": 21.5, "pressure": 1015},
        {"temperature": 22.0, "pressure": 1011}
    ]
    
    analytics = DataAnalytics(sample_data)
    summary = analytics.summarize_data()
    print("Data Summary:", summary)
    analytics.visualize_data()
