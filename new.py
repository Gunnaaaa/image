from bokeh.plotting import figure ,output_file,show 

import numpy as np 


'''
x=np.arange(0,10,1) 
y1=x**2
y2=x**3
y3=x**4

p=figure(title="simple",x_axis_label="x",y_axis_label="y") 

p.line(x,y1,legend="quad function",line_width=2,color="red")
p.line(x,y2,legend="quadratic function",line_width=2,color="green")
p.line(x,y3,legend="quadrat function",line_width=2,color="yellow")

show(p)
'''
x=[1,2,3,4,5]
y=[2,4,6,8,10]
output_file('line.html')

fig=figure(title="line",x_axis_label='x',y_axis_label="y",color="red")
fig.line(x,y)

show(fig)
