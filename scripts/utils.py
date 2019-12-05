import tensorflow as tf
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as plt

def weight_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, name=name)

def bias_variable(shape, name):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name=name)

def morphs(activations, labels, skip=2, last_layer=False):
    #If last dimension is something other than 2, change it. otherwise 0.
    trace_list = []
    n_rows = 1 if ((len(activations)) < 10) else -(-len(activations)//10)
    fig = tools.make_subplots(rows=n_rows, cols=(10))
    last_dim = (2 if last_layer==False else 0)
    for i in range(1, len(activations)-last_dim+1, skip):
        #print((-(-i//10)), i%10, i-1, (i//2)+1)
        #if labels == 0:
        #        fig.append_trace(go.Scatter(x=activations[i-1][:,0], y = activations[i-1][:,1] , mode='markers', -(-i//10), (10 if i%10==0 else i%10)))
        #else:
        fig.append_trace(go.Scatter(x=activations[i-1][:,0], y = activations[i-1][:,1] , mode='markers', marker=dict(color=labels)), -(-i//10), (10 if i%10==0 else i%10))
    fig['layout'].update(height=n_rows*300)
    plot(fig)
