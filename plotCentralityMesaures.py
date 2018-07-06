import matplotlib
import matplotlib.pyplot as plt

def plotCentrality(fileinput, graph):
    centrality = []
    degrees = []
    with open(fileinput) as f:
        lines = f.read().splitlines()
    for line in lines:
        l = line.split('\t')
        deg = graph.degree(l[0])
        centrality.append(float(l[1]))
        degrees.append(deg)
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(degrees, centrality, 'o')
    ax.semilogx()
    title = fileinput + " distribution"
    ax.set_title(title)
    plt.show()


