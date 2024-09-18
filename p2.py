# lecture 2
input = [1,2,3,2.5] # input from previous neurons (hidden layers 4 neurons)
weights1 = [0.2,0.8,-0.5,1.0]# weights for input from four neurons of hidden layer(output neuron 1)
weights2 = [0.5,-0.91,0.26,-0.5] # weights for input from four neurons of hidden layer(output neuron 2)
weights3 = [-0.26,-0.27,0.17,0.87] # weights for input from four neurons of hidden layer(output neuron 3)

bias1 = 2 # # bias for 1st neuron in the output layer
bias2 = 3 # bias for 2nd neuron in the output layer
bias3 = 0.5 # bias for 3rd neuron in the output layer
output = [input[0]*weights1[0] + input[1]*weights1[1] + input[2]*weights1[2] + input[3]*weights1[3] + bias1,
input[0]*weights2[0] + input[1]*weights2[1] + input[2]*weights2[2] + input[3]*weights2[3] + bias2,
input[0]*weights3[0] + input[1]*weights3[1] + input[2]*weights3[2] + input[3]*weights3[3] + bias3]
print(output)
# each neuron has a unique set of weights and a unique bias for the inputs