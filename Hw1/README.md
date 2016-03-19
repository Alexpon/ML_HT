# Homework 1

First, we use an artificial data set to study PLA. <br /><br />

Each line of the data set contains one (xn,yn) with xn ∈ R4. The first 4 numbers of the line contains the components of xn orderly, the last number is yn. Please initialize your algorithm with w = 0 and take sign(0) as −1. As a friendly reminder, remember to add x0 = 1 as always! <br /><br />

1. Implement a version of PLA by visiting examples in the na ̈ıve cycle using the order of examples in the data set. Run the algorithm on the data set. What is the number of updates before the algorithm halts? What is the index of the example that results in the “last” mistake? <br /><br />

2. Implement a version of PLA by visiting examples in fixed, pre-determined random cycles throughout the algorithm. Run the algorithm on the data set. Please repeat your experiment for 2000 times, each with a different random seed. What is the average number of updates before the algorithm halts? Plot a histogram ( https://en.wikipedia.org/wiki/Histogram ) to show the number of updates versus frequency. <br /><br />

3. Implement a version of PLA by visiting examples in fixed, pre-determined random cycles throughout the algorithm, while changing the update rule to be <br />
*wt+1 ← wt + ηyn(t)xn(t)* <br />
with η = 0.5. Note that your PLA in the previous problem corresponds to η = 1. Please repeat your experiment for 2000 times, each with a different random seed. What is the average number of updates before the algorithm halts? Plot a histogram to show the number of updates versus frequency. Compare your result to the previous problem and briefly discuss your findings. <br /><br />

Prof. Hsuan-Tien Lin <br />
Link: https://www.csie.ntu.edu.tw/~htlin/course/ml15fall/ <br />
Language: python <br />
