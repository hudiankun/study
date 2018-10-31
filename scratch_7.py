#调用函数scratch_6,函数必须与此文档在同一文件夹
from  scratch_6 import c_to_f  #或者 import scratch_6
celsius=float(input("Enter a temperature in Celsius:"))
fahrenheit=c_to_f(celsius) #或者 fahrenheit=scratch_6.c_to_f(celsius)
print("That's ",fahrenheit,"degrees Fahrenheit")