from bokeh.plotting import figure
from bokeh.io import output_file, show

x=[3,7.5,10]
y=[3,6,9]


output_file("Triangle.html")

f=figure()
f.triangle(x, y, size=[10,20,25],color="#99D594", fill_color=None)

#f.circle(x, y, size=20)

show(f)
