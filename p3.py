input = [1,2,3,2.5] # input from previous neurons (hidden layers 4 neurons)
weights = [[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]] #nested list of all the weights

biases = [2, 3, 0.5] # list of biases for every neuron(output ke liye 3 neuron hai hence, 3 biases)

# zip is used to combine items of two lists index-wise
output_layer = []
for bias,weight in zip(biases,weights):
    neuron_output = 0
    for input_neuron,weightss in zip(input,weight): # yaha pe zip(input,weights) nahi kar sakte coz ye karne pe it will bind input with list of weights and not only weights
        neuron_output += input_neuron*weightss
    neuron_output += bias
    output_layer.append(neuron_output)

print(output_layer)