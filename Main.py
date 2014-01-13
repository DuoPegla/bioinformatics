from MSA import MSA
from InputOutput import InputData, OutputData
from Hypercube import Hypercube
import time

print ("INFO: Starting Multiple Sequence Alignment.")
execution_times = dict()
start_time = time.clock()
input_data = InputData("./input1.txt")
end_time = time.clock()
execution_times["input"] = end_time - start_time

start_time = time.clock()
hypercube = Hypercube(input_data.sequences)
end_time = time.clock()
execution_times["hypercube"] = end_time - start_time


msa = MSA(hypercube)
start_time = time.clock()
msa.align()
end_time = time.clock()
execution_times["MSA"] = end_time - start_time

for output in msa.output:
    print (output)

output_data = OutputData("./output.txt", msa.output)

print ("INFO: Execution time [s]: {0}".format(execution_times))
print ("INFO: Done.")
