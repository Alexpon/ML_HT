# Homework 6

Experiments with Adaptive Boosting. </br>
Implement the AdaBoost-Stump algorithm as introduced in Lecture 208. Run the algorithm on the following set for training: </br>
* hw6_adaboost_train.dat *
and the following set for testing: </br>
* hw6_adaboost_test.dat *
Use a total of T = 300 iterations (please do not stop earlier than 300), and calculate Ein and Eout with the 0/1 error. </br>
For the decision stump algorithm, please implement the following steps. Any ties can be arbitrarily broken. </br>

(1) For any feature i, sort all the xn,i values to x[n],i such that x[n],i ≤ x[n+1],i.

(2) Consider thresholds within −∞ and all the midpoints ((x[n],i)+(x[n+1],i))/2 . Test those thresholds with s ∈ {−1, +1} to determine the best (s, θ) combination that minimizes Ein^u using feature i. in

(3) Pick the best (s, i, θ) combination by enumerating over all possible i.

For those interested, step 2 can be carried out in O(N) time only!! </br>
1. Plot a figure for t versus Ein(gt). What is Ein(g1) and what is α1?
2. From the figure in the previous question, should Ein(gt) be decreasing or increasing? Write down your observations and explanations.
3. Plot a figure for t versus Ein(Gt), where Gt(x) =  sigma(for τ=1 to t) ατ*gτ(x). That is, G = GT . What is Ein (G)?
N (t)
4. Plot a figure for t versus Ut, where Ut = sigma(n=1 to N)un^t . What is U2 and what is UT?
5. Plot a figure for t versus εt. What is the minimum value of εt?
6. Plot a figure for t versus Eout(gt) estimated with the test set. What is Eout(g1)?
7. Plot a figure for t versus Eout(Gt) estimated with the test set. What is Eout(G)?

Prof. Hsuan-Tien Lin <br />
Link: https://www.csie.ntu.edu.tw/~htlin/course/ml15fall/ <br />
Language: python <br />
