import networkx as nx
import ndlib.models.epidemics.SIModel as si
from bokeh.io import output_notebook, show
import ndlib.models.ModelConfig as mc
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
import csv

def siModel(graph, iteration):
    # Model Selection
    si_model = si.SIModel(graph)

    # Model Configuration
    config = mc.Configuration()
    config.add_model_parameter('beta', 0.005)
    config.add_model_parameter("percentage_infected", 0.001)
    si_model.set_initial_status(config)

    # Simulation
    iterations = si_model.iteration_bunch(iteration)
    trends = si_model.build_trends(iterations)

    viz = DiffusionTrend(si_model, trends)
    p = viz.plot(width=800, height=800)
    show(p)
