import plotly.offline as po
import plotly.graph_objs as go
import numpy as np
from numpy import *
import scipy
import Main_calculation
import sympy as sy
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def choosen_color_plotly(number_color):
    color_list=['sandybrown', 'darkorange', 'whitesmoke', 'gainsboro', 'maroon', 'darkred', 'steelblue', 'darkslateblue', 'oldlace', 'lemonchiffon',
                 'lightseagreen', 'lightgoldenrodyellow', 'navy', 'blanchedalmond', 'dimgray', 'thistle', 'ghostwhite', 'darkmagenta', 'paleturquoise',
                  'lightgreen', 'rebeccapurple', 'linen', 'lightsteelblue', 'darkgreen', 'deepskyblue', 'blueviolet', 'black', 'aliceblue', 'slateblue',
                  'mediumblue', 'rosybrown', 'chartreuse', 'forestgreen', 'seashell', 'dimgrey', 'wheat', 'lightblue', 'limegreen', 'aquamarine', 'lightyellow',
                  'plum', 'burlywood', 'orange', 'papayawhip', 'lime', 'lightcoral', 'darkslategrey', 'chocolate', 'powderblue', 'darkorchid', 'mediumorchid', 'brown',
                  'darkgray', 'turquoise', 'coral', 'mediumslateblue', 'darkseagreen', 'lavender', 'green', 'magenta', 'ivory', 'palegreen', 'aqua', 'peru',
                  'indianred', 'navajowhite', 'orangered', 'lightpink', 'floralwhite', 'yellowgreen', 'mistyrose', 'hotpink', 'gray', 'midnightblue', 'seagreen',
                  'lightslategrey', 'mediumturquoise', 'mediumvioletred', 'darkgrey', 'goldenrod', 'sienna', 'lightgrey', 'indigo', 'antiquewhite', 'beige', 'cyan',
                  'mediumspringgreen', 'lightskyblue', 'orchid', 'cadetblue', 'firebrick', 'lavenderblush', 'darkgoldenrod', 'darkviolet', 'white', 'darkslategray',
                  'mediumpurple', 'fuchsia', 'royalblue', 'mediumaquamarine', 'honeydew', 'mintcream', 'greenyellow', 'snow', 'yellow', 'slategray', 'saddlebrown', 'tomato',
                  'lawngreen', 'deeppink', 'gold', 'olivedrab', 'khaki', 'dodgerblue', 'darkcyan', 'olive', 'grey', 'slategrey', 'palevioletred', 'lightslategray', 'bisque',
                  'silver', 'teal', 'peachpuff', 'salmon', 'violet', 'tan', 'pink', 'palegoldenrod', 'blue', 'lightgray', 'mediumseagreen', 'darksalmon', 'azure', 'cornsilk',
                  'skyblue', 'purple', 'crimson', 'moccasin', 'darkturquoise', 'darkblue', 'springgreen', 'red', 'lightsalmon', 'darkolivegreen', 'darkkhaki', 'cornflowerblue',
                  'lightcyan']
   
    l=[]
    for i in range(number_color):
       color = np.random.choice(color_list)
       l.append(color)
    return l

def choosen_color_rgb(number_color):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'w',
              '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']
    
    l=[]
    for i in range(number_color):
       color = np.random.choice(colors)
       l.append(color)
    return l
   


def SimpleIntegrateplot(func,llim,hlim):

    def funcvalue(x):
      try:
        return float(func(x))
      except:
         return float(func(abs(x)))
    x=np.linspace(llim-2,hlim+5,1000)
    y=[float(funcvalue(i)) for i in x]

    fil1=np.where(llim<=x,x,hlim+2)
    fil2=np.where(hlim>=fil1,True,False)
    x_line=x[fil2]
    y_line=[float(funcvalue(i)) for i in x_line]
    
    color1,color2=choosen_color_plotly(2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_line, y=y_line, fill='tozeroy', mode='lines', name='Area',line=dict(color=color1, width=2)))
    fig.add_trace(go.Scatter(x=x.tolist(),y=list(y),mode="lines",line=dict(color=color2, width=3),name="line"))

    fig.update_layout(
       title=f"Area of {llim} to {hlim}",
    title_font=dict(size=24, color='red', family='Arial'),
    xaxis_title="X-axis",
    yaxis_title="Y-axis" )
    
    df=pd.DataFrame({"x":x,"y":y})
    st.markdown('<h3 style="color:red;">Graph of Given Function</h3>', unsafe_allow_html=True)
    st.write("")
    st.line_chart(data=df,x="x",y="y",color=tuple(int(i) for i in np.random.randint(0,255,3)),width=5)
    return fig


def doubleIntegrateplot(d_limit_func1,d_limit_func2,llim,hlim):
    def func1value(x):
      try:
        return float(d_limit_func1(x))
      except:
         return float(d_limit_func1(abs(x)))
      
    def func2value(x):
      try:
        return float(d_limit_func2(x))
      except:
         return float(d_limit_func2(abs(x)))

    x=np.linspace(llim*0.05,hlim*0.05,1000)
    y1=[float(func1value(i)) for i in x]
    y2=[float(func2value(i)) for i in x]
    
    plt.style.use("dark_background")
    st.markdown('<h3 style="color:red;">Graph of Given Functions</h3>', unsafe_allow_html=True)
    st.write("")
    color1_rgb,color2_rgb=choosen_color_rgb(2)
    df = pd.DataFrame({"x": x, "y1": y1})
    df1 = pd.DataFrame({"x": y2, "y2": x})
    pltfig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(x, y1, linewidth=2,color=color1_rgb)
    ax.plot(y2, x, linewidth=2.0,color=color2_rgb)
    ax.grid(True, linewidth=0.2)
    pltfig.tight_layout()
    st.pyplot(pltfig)

    color1,color2=choosen_color_plotly(2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x.tolist(),y=list(y1),mode="lines",line=dict(color=color1, width=3),name="line 1"))
    fig.add_trace(go.Scatter(x=list(y2),y=list(x),mode="lines",line=dict(color=color2, width=3),name="line 2"))
    fig.update_layout(title=f"Interactive Graph",title_font=dict(size=26, color='red', family='Arial'),
       xaxis_title="X-axis",
       yaxis_title="Y-axis" )
    
    return fig


def doubleIntegrate_Fxy_plot(d_limit_func):
    def funcvalue(x,y):
      try:
        return d_limit_func(x,y)
      except:
         return d_limit_func(abs(x),abs(y))

    x=np.linspace(-10,10,200)
    y=np.linspace(-10,10,200)
    x, y = np.meshgrid(x, y)
    z=funcvalue(x,y)

    colorlist = ["Viridis","Cividis","Blues","Greens","Reds","Inferno","Plasma",
               "Magma","Turbo","RdBu","Spectral","Coolwarm","Twilight","HSV","Electric"]
    color=np.random.choice(colorlist)
  
    fig = go.Figure()
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y,colorscale=color)])
    fig.update_layout(title=f"3D Plot of f(x, y)",title_font=dict(size=25, color='red', family='Arial'),
        width=900,height=700,
        scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="f(x, y)"))
    
    return fig
