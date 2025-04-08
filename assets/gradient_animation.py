import numpy as np
import plotly.graph_objects as go

def f(x):
    return x**2 + 0.5 * np.sin(5*x)

def grad_f(x):
    return 2*x + 2.5 * np.cos(5*x)

#Adam simulation

alpha = 0.015         # learning rate
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8

x = 2.9             # starting at x=2.5 so that non-convexity appears on the path
m, v = 0.0, 0.0     # first and second moment initializations
num_iterations = 120

x_history = [x]
m_history = [m]
v_history = [v]
f_history = [f(x)]

for t in range(1, num_iterations+1):
    g = grad_f(x)

    # Update biased first moment estimate.
    m = beta1 * m + (1 - beta1) * g
    # Update biased second raw moment estimate.
    v = beta2 * v + (1 - beta2) * (g ** 2)
    # Compute bias-corrected first moment.
    m_hat = m / (1 - beta1**t)
    # Compute bias-corrected second raw moment.
    v_hat = v / (1 - beta2**t)

    # Non-adaptive gradient descent:
    x = x - alpha * g
    # Update the parameter.
    #x = x - alpha * m_hat / (np.sqrt(v_hat) + epsilon)

    x_history.append(x)
    f_history.append(f(x))
    m_history.append(m)
    v_history.append(v)

x_vals = np.linspace(-3, 3, 500)
y_vals = f(x_vals)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", line=dict(width=2, color='#626dfa'), hoverinfo='skip', name="f(x)"))
fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", line=dict(width=2, color='#626dfa', shape='spline'), hoverinfo='skip', name="f(x)"))

frames=[
go.Frame(
data=[
    go.Scatter(x=[x_history[i]], y=[f_history[i]],
               mode="markers+text",
               marker=dict(size=20, color="darkred"),
               text=[""],#[f"Momentum: {m_history[i]:.2f}"],
               textposition="top center")
    ],
    name=str(i)
    )
        for i in range(1, len(x_history))
]

fig.frames = frames

fig.update_layout(
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20)
)

#Define animation settings
animation_settings = dict(
    frame=dict(duration=40, redraw=False),
    mode='immediate',
    transition=dict(duration=0, easing=None)
)

#fig.show()

#%%
import plotly.io as pio
# Save the animation as a gif
pio.write_html(fig, "gd_optimization.html",
               config={'displayModeBar':False}, animation_opts=animation_settings,
               auto_play=True, include_mathjax=False, include_plotlyjs='directory',
               full_html=False)
