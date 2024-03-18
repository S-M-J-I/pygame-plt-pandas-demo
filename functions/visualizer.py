import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab
from constants import *


def plot_graph(data, title, query, target='sellingprice'):
    fig = pylab.figure(figsize=[GRAPH_WIDTH, GRAPH_HEIGHT], dpi=DPI)

    ax = fig.gca()
    ax.bar(data[query], data[target])
    ax.set_title(title)
    ax.set_xlabel(f"Selling Price")
    ax.set_ylabel(f"{query.title()}")
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    plt.tight_layout()
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    image_data = renderer.tostring_rgb()

    return image_data
