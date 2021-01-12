# Making a basic bokeh line graph

from bokeh.plotting import figure, output_file, show
import pandas


df=pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10

f=figure(plot_width=500,plot_height=400, tools='pan')
 
f.title.text="Temperature and Air Pressure"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Temperature (*C)"
f.yaxis.axis_label="Pressure (hPa)" 

f.circle(df["Temperature"],df["Pressure"], size=0.5)
output_file("Weather.html")
show(f)

