#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:32:56 2024

@author: teijeiro
"""

import plotly.graph_objs as go
import pandas as pd
import numpy as np

FILE = 'Linregress_animation'

# Example data: a list of frames, each frame containing a set of 2D points
X = np.loadtxt('x.txt')
Y = np.loadtxt('y.txt')
hist = np.loadtxt('param_hist.txt')

# Create the figure
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=X,
    y=Y,
    mode='markers',
    marker=dict(size=10),
    name="scatter"
))

fig.add_trace(go.Scatter(
    x=X,
    y=Y,
    mode='markers',
    marker=dict(size=10, opacity=0.3),
    hoverinfo='skip',
    name="scatter"
))

XGRID = np.array([0., 1.])

# Add frames to the animation
frames = [go.Frame(
    data=[go.Scatter(
            x=XGRID,
            y=a*XGRID+b,
            mode='lines',
            line=dict(width=3)
        )],
    layout=go.Layout(annotations=[go.layout.Annotation(
            x=0.01,
            y=0.05,
            xref="x",
            yref="y",
            text=f"Loss: {np.mean(((a*X+b) - Y)**2):.2e}",
            xanchor='left',
            showarrow=False
            )
    ]),
    name=f'frame{i}'
) for i, (a, b) in enumerate(hist[::10,:])]






fig.frames = frames


fig.update_xaxes(range = [-0.1,1.1])
fig.update_yaxes(range = [-0.1,1.5])
fig.update_xaxes(fixedrange=True)
fig.update_yaxes(fixedrange=True)
fig.update_layout(
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20)
)


#Define animation settings
animation_settings = dict(
    frame=dict(duration=10, redraw=False),
    mode='immediate',
    transition=dict(duration=0, easing=None)
)


# Generate the animation

fig.show()

#%%
import plotly.io as pio
# Save the animation as a gif
pio.write_html(fig, f"{FILE}.html",
               config={'displayModeBar':False}, animation_opts=animation_settings,
               auto_play=True, include_mathjax=False, include_plotlyjs='directory',
               full_html=False)
