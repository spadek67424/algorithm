from heapq import heapify, heappush, heappop
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)

total_number = 100
step = 10
def algo(input):
    minheap = []
    for i in range(len(input)):
        heappush(minheap, input[i])
    while len(minheap) != 1:
         first = heappop(minheap)
         second = heappop(minheap)
         heappush(minheap, (first[0] + second[0] , str("(" + first[1] + "+" + second[1] + ")" )))
    print(heappop(minheap))
         
def initialize(inputnum):
    num = []
    for n in range(0, inputnum):
        num.append(n)
    input = np.random.randint(10,1500,50000)
    return num, input

def visualization(x_data, y_data, plot_name, legend_name):
    plt.plot(x_data, y_data, label = legend_name)
    plt.legend()
    plt.ylabel('Second')
    plt.xlabel('number of n')
    plt.savefig(plot_name)


if __name__ == "__main__":
    init = []
    for n in range(1, total_number, step):
        init.append(np.int64(n))
    #print(init)
    compute_performance = list()
    theory_performance = np.log(init) * np.array(init)
    for inputnum in init:
        num, array = initialize(inputnum)
        input = []
        for i in range(len(num)):
            input.append((array[i % 50000], str(i)))
        print(input)
        start = timer()
        algo(input)
        end = timer()
        print((end - start))
        compute_performance.append((end-start) * 7007153)
    print(theory_performance)
    visualization(init, theory_performance,  "./pic/theory.png", "Theorical_peformance")
    visualization(init, compute_performance,  "./pic/compute.png", "computational_performance")

   