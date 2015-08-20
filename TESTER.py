test.py

# Check whether Graphlab can read the csv:
import graphlab as gl
data = gl.SFrame.read_csv('synthetic_gold_data.csv')
print 'graphlab SFrame:'
print data.head()