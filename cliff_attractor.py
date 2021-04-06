import numpy as np, pandas as pd, datashader as ds
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis
from numba import jit
from math import sin, cos, sqrt, fabs
import numpy.random
from PIL import Image
import xarray as xr

from colorcet import palette
palette["viridis"]=viridis
palette["inferno"]=inferno


@jit(nopython=True)
def Clifford(x, y, a, b, c, d, *o):
    return np.sin(a * y) + c * np.cos(a * x), np.sin(b * x) + d * np.cos(b * y)


n=10000000

@jit(nopython=True)
def trajectory_coords(fn, x0, y0, a, b=0, c=0, d=0, e=0, f=0, n=n):
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = x0, y0
    for i in np.arange(n-1):
        x[i+1], y[i+1] = fn(x[i], y[i], a, b, c, d, e, f)
    return x,y

def trajectory(fn, x0, y0, a, b=0, c=0, d=0, e=0, f=0, n=n):
    x, y = trajectory_coords(fn, x0, y0, a, b, c, d, e, f, n)
    return pd.DataFrame(dict(x=x,y=y))


#TEST
# df = trajectory(Clifford, 0, 0, -1.3, -1.3, -1.8, -1.9)
#
#
# cvs = ds.Canvas(plot_width = 200, plot_height = 200)
# agg = cvs.points(df, 'x', 'y')
# #print(agg.values[190:195,190:195],"\n")
# ds.transfer_functions.Image.border=0
# img = tf.shade(agg, cmap = viridis).to_pil()
#
# #img = Image.new(mode = "RGB", size = (300,300))
# img.save('img.png')


def init_plot(fn, vals, n=n, cmap=viridis, label=True):
    """Return a Datashader image by collecting `n` trajectory points for the given attractor `fn`"""
    lab = ("{}, "*(len(vals)-1)+" {}").format(*vals) if label else None
    df  = trajectory(fn, *vals, n=n)
    cvs = ds.Canvas(plot_width = 500, plot_height = 500)
    agg = cvs.points(df, 'x', 'y')
    return agg



#finds some nice inital conditions thats it
def gen_random():
    im = [0]
    empty_min=249200
    empty = 250001
    func = Clifford#Symmetric_Icon#De_Jong#Svensson
    #how intresting/colorful #1e12 lower limit
    while empty > empty_min:#np.array(im).sum() < 1e12:
      rvals=np.c_[np.zeros((1,2)), numpy.random.random((1,6))*4-2]
      #rvals = np.c_[np.ones((num,2))*0.01, numpy.random.random((num,6))*4-2]
      #print(rvals[0])
      vals = list(rvals[0])
      agg = init_plot(func, rvals[0], n=2000)
      print('loop', np.count_nonzero(np.array(agg.values)==0))
      empty = np.count_nonzero(np.array(agg.values)==0)
    #con = np.count_nonzero(im==0)
    #print(np.array(im).max())
    return rvals[0]


#take inital conditions and makes a nice agg
def make_detailed(vals, n=n, cmap=viridis, label=True):
    """Return a Datashader image by collecting `n` trajectory points for the given attractor `fn`"""
    imgs = []
    m = 1000000
    vals[0] = 0
    vals[1] = 0
    cvs = ds.Canvas(plot_width = 500, plot_height = 500)
    agg_sum = 0
    #for i in np.geomspace(200, m, 100).astype(int):
    for i in range(100):
      #print(i)
      lab = ("{}, "*(len(vals)-1)+" {}"+' n:'+str((1+i)*m)).format(*vals) if label else None
      df  = trajectory(Clifford, *vals, n=m)
      vals[0] = df.iloc[m-1].x
      vals[1] = df.iloc[m-1].y

      agg = cvs.points(df, 'x', 'y')
      agg_sum = agg.values + agg_sum
      #imgs.append(tf.shade(agg, cmap=color_map, name=lab)) #palette[color_map]
      #imgs.append(tf.shade(xr.DataArray(agg_sum), cmap=palette['fire'], name=lab)) #palette[color_map]

    return xr.DataArray(agg_sum)#imgs


def make_pretty(color, vals, agg):
    if vals == '': #or agg == None
        vals = gen_random()
        agg = make_detailed(Clifford, vals)
    if color == '':
        color = 'fire'
    lab = ("{}, "*(len(vals)-1)+" {}").format(*vals) if vals else None
    img = tf.shade(xr.DataArray(agg), cmap=palette[color], name=lab)
    img = tf.set_background(img,'black')
    return img


#vals = gen_random()
#im, a, df = init_plot(Clifford, vals, n=10000000)

#im = im.to_pil()
#im.save('im.png')
#plot(func, vals=[["kbc"]+list(rvals[i]) for i in range(len(rvals))], label=True) #NOTEBOOK TO FILE

#color_map = palette['inferno']
#img = tf.shade(a,cmap=color_map).to_pil()
#img.save('img.png')



# img = tf.shade(agg, cmap = viridis).to_pil()
#
# #img = Image.new(mode = "RGB", size = (300,300))
# img.save('img.png')
