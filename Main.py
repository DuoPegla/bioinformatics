from MSA import MSA
from InputOutput import InputData, OutputData
from Hypercube import Hypercube
import time
import resource

def memory_usage():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss /float(1000)

print ("INFO: Starting Multiple Sequence Alignment.")
performance = dict()
start_time = time.clock()
input_data = InputData("./input1.txt")
end_time = time.clock()
performance["input"] = (end_time - start_time, memory_usage())

start_time = time.clock()
hypercube = Hypercube(input_data.sequences)
end_time = time.clock()
performance["hcube"] = (end_time - start_time, memory_usage())


msa = MSA(hypercube)
start_time = time.clock()
msa.align()
end_time = time.clock()
performance["MSA"] = (end_time - start_time, memory_usage())

for output in msa.output:
    print (output)

output_data = OutputData("./output.txt", msa.output)

print ("INFO: Performance: (Execution time [s], Memory usage [MB])")
for p in performance:
    print ("\t{0}: {1} s, {2} MB".format(p, performance[p][0], performance[p][1]))
print ("INFO: Done.")
