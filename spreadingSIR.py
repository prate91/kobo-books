import networkx as nx
import ndlib.models.epidemics.SIRModel as sir
from bokeh.io import output_notebook, show
import ndlib.models.ModelConfig as mc
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
import csv

def sirModel(graph, iteration):
    # Model Selection
    sir_model = sir.SIRModel(graph)

    # Model Configuration
    config = mc.Configuration()
    config.add_model_parameter('beta', 0.005)
    config.add_model_parameter('gamma', 0.01)
    config.add_model_parameter("percentage_infected", 0.01)
    sir_model.set_initial_status(config)

    # Simulation
    iterations = sir_model.iteration_bunch(iteration)
    trends = sir_model.build_trends(iterations)

    viz = DiffusionTrend(sir_model, trends)
    p = viz.plot(width=800, height=800)
    show(p)
