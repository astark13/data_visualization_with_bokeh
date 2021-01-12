# Making a basic bokeh line graph

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# prepare some data
#df=pandas.read_csv("data.csv")
#x=df["x"]
#y=df["y"]
df=pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
x=df["Year"]
y=df["Engineering"]

# prepare the output file
output_file("Line.html")

# create a figure object
f=figure()

#f=figure(plot_width=500,plot_height=400, tools='pan',logo=None)
 
#f.title.text="Cool Data"
#f.title.text_color="Gray"
#f.title.text_font="times"
#f.title.text_font_style="bold"
#f.xaxis.minor_tick_line_color=None
#f.yaxis.minor_tick_line_color=None
#f.xaxis.axis_label="Date"
#f.yaxis.axis_label="Intensity" 

# create line plot
f.line(x,y)

show(f)