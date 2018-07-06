import networkx as nx
import ndlib.models.epidemics.SISModel as sis
import ndlib.models.epidemics.SIModel as si
from bokeh.io import output_notebook, show
import ndlib.models.ModelConfig as mc
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
import csv

def sisModel(graph, iteration):
    # Model Selection
    sis_model = sis.SISModel(graph)

    # Model Configuration
    config = mc.Configuration()
    config.add_model_parameter('beta', 0.005)
    config.add_model_parameter('lambda', 0.01)
    config.add_model_parameter("percentage_infected", 0.01)
    sis_model.set_initial_status(config)

    # Simulation
    iterations = sis_model.iteration_bunch(iteration)
    trends = sis_model.build_trends(iterations)

    viz = DiffusionTrend(sis_model, trends)
    p = viz.plot(width=400, height=400)
    show(p)
