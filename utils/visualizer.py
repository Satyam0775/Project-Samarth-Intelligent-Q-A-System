import matplotlib.pyplot as plt

def plot_trend(df, x_col, y_col, title):
    plt.figure(figsize=(8,5))
    plt.plot(df[x_col], df[y_col], marker='o')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()
