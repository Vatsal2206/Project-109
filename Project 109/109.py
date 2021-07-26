import plotly.graph_objects as gobj
import plotly.figure_factory as pff
import statistics as stc
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
data = df["reading score"].tolist()

# Mean
mean = stc.mean(data)
print('Mean : ',mean)

# Mode and Median
median = stc.median(data)
mode = stc.mode(data)

print('Median : ',median)
print('Mode : ',mode)

# Standard Deviation
stdDev = stc.stdev(data)
print('Standard Deviation : ',stdDev)

# Standard Deviation Start & End
first_stdDev_Start, first_stdDev_End = mean - (1 * stdDev) , mean + (1 * stdDev)
second_stdDev_Start, second_stdDev_End = mean - (2 * stdDev) , mean + (2 * stdDev)
third_stdDev_Start, third_stdDev_End = mean - (3 * stdDev) , mean + (3 * stdDev)

# Percentage of data

data_under_first_stdDev = [ result for result in data if result > first_stdDev_Start and result < first_stdDev_End ]

data_under_second_stdDev = [ result for result in data if result > second_stdDev_Start and result < second_stdDev_End ]

data_under_third_stdDev = [ result for result in data if result > third_stdDev_Start and result < third_stdDev_End ]

print("{}% of data lies within first standard deviation".format(len(data_under_first_stdDev) * 100 / len(data)))

print("{}% of data lies within second standard deviation".format(len(data_under_second_stdDev) * 100 / len(data)))

print("{}% of data lies within third standard deviation".format(len(data_under_third_stdDev) * 100 / len(data)))

# Plotting graph

graph = pff.create_distplot([data], ["Math Scores"], show_hist=False)
graph.add_trace(gobj.Scatter(x=[mean, mean], y = [0, 0.2], mode="lines", name="MEAN"))

graph.add_trace(gobj.Scatter(x=[first_stdDev_Start, first_stdDev_Start], y = [0, 0.2], mode="lines", name="STD DEV 1 START"))
graph.add_trace(gobj.Scatter(x=[first_stdDev_End, first_stdDev_End], y = [0, 0.2], mode="lines", name="STD DEV 1 END"))

graph.add_trace(gobj.Scatter(x=[second_stdDev_Start, second_stdDev_Start], y = [0, 0.2], mode="lines", name="STD DEV 2 START"))
graph.add_trace(gobj.Scatter(x=[second_stdDev_End, second_stdDev_End], y = [0, 0.2], mode="lines", name="STD DEV 2 END"))

graph.add_trace(gobj.Scatter(x=[third_stdDev_Start, third_stdDev_Start], y = [0, 0.2], mode="lines", name="STD DEV 3 START"))
graph.add_trace(gobj.Scatter(x=[third_stdDev_End, third_stdDev_End], y = [0, 0.2], mode="lines", name="STD DEV 3 END"))

graph.show()