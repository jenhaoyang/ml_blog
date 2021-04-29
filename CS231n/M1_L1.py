
import numpy as np

x = np.array([-15, 22, -44, 56, 1])
x_array = np.transpose(np.array([[-15, 22, -44, 56, 1],
                                 [-15, 22, -44, 56, 1]]))
y = 2
y_array = np.array([2, 2])
W = np.array([[0.01, -0.05, 0.1, 0.05, 0.0],
             [0.7, 0.2, 0.05, 0.16, 0.2], 
             [0.0, -0.45, -0.2, 0.03, -0.3]])


def L_i(x, y, W):
    """
    unvectorized version. Compute the multiclass svm loss for a single example (x,y)
    - x is a column vector representing an image (e.g. 3073 x 1 in CIFAR-10)
        with an appended bias dimension in the 3073-rd position (i.e. bias trick)
    - y is an integer giving index of correct class (e.g. between 0 and 9 in CIFAR-10)
    - W is the weight matrix (e.g. 10 x 3073 in CIFAR-10)
    """
    delta = 1.0
    scores = W.dot(x)
    correct_class_score = scores[y]
    D = W.shape[0]
    loss_i = 0.0
    for j in range(D):
        if j == y:
            continue
        loss_i += max(0, scores[j] - correct_class_score + delta)
    return loss_i


def L_i_vectorized(x, y, W):
    """
    A faster half-vectorized implementation. half-vectorized
    refers to the fact that for a single example the implementation contains
    no for loops, but there is still one loop over the examples (outside this function)
    """
    delta = 1.0
    scores = W.dot(x)
    # compute the margins for all classes in one vector operation
    margins = np.maximum(0, scores - scores[y] + delta)
    # on y-th position scores[y] - scores[y] canceled and gave delta. We want
    # to ignore the y-th position and only consider margin on max wrong class
    margins[y] = 0
    loss_i = np.sum(margins)
    return loss_i


def L(X, Y, W):
  """
  fully-vectorized implementation :
  - X holds all the training examples as columns (e.g. 3073 x 50,000 in CIFAR-10)
  - y is array of integers specifying correct class (e.g. 50,000-D array)
  - W are weights (e.g. 10 x 3073)
  """
  # evaluate loss over all examples in X without using any for loops
  # left as exercise to reader in the assignment
  delta = 1.0
  score_array = W.dot(X)
  y_array_col = np.arange(Y.shape[0])
  ground_truth_score =  score_array[Y, y_array_col]
  margins = np.maximum(0, score_array - ground_truth_score + delta)
  margins[Y, y_array_col] = 0
  loss = np.sum(margins)
  return loss



if __name__=='__main__':
    loss_single = L_i_vectorized(x, y, W)
    print(loss_single)
    loss = L(x_array, y_array, W)

    print(loss)