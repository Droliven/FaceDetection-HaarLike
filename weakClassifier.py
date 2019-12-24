
from matplotlib import pyplot
import numpy

from config import LABEL_POSITIVE
from config import LABEL_NEGATIVE


class WeakClassifier:

    def __init__(self, Mat = None, Tag = None, W = None, train = True):

        if train == True:
            assert Mat.__class__ == numpy.ndarray
            assert Tag.__class__ == numpy.ndarray
            assert   W.__class__ == numpy.ndarray


            self._mat = Mat
            self._label = Tag

            # sampleDim == the number of features
            self.sampleDim, self.sampleNum = self._mat.shape

            if W == None:
                self.numPos = numpy.count_nonzero(self._label == LABEL_POSITIVE)
                self.numNeg = numpy.count_nonzero(self._label == LABEL_NEGATIVE)
                pos_W = [1.0/(2 * self.numPos) for i in xrange(self.numPos)]
                            
                neg_W = [1.0/(2 * self.numNeg) for i in xrange(self.numNeg)]
                self.weight = numpy.array(pos_W + neg_W)

            else:
                self.weight = W

            self.output = numpy.zeros(self.sampleNum, dtype = numpy.int)

            self.opt_errorRate = 1.
            self.opt_dimension = 0
            self.opt_threshold = None
            self.opt_direction = 0
            

    def optimal(self, d):

        # for positive sample
        idx = (self._label + LABEL_POSITIVE) / (LABEL_POSITIVE * 2)
        weight = self.weight  * idx
        vector = self._mat[d] * idx
        sumPos = weight.dot(vector)
        sumPosW= weight.sum()

        # for negative sample
        idx = (self._label + LABEL_NEGATIVE) / (LABEL_NEGATIVE * 2)
        weight = self.weight  * idx
        vector = self._mat[d] * idx
        sumNeg = weight.dot(vector)
        sumNegW= weight.sum()

                
        miuPos = sumPos / sumPosW
        miuNeg = sumNeg / sumNegW

        threshold = (miuPos + miuNeg)/2

        minErrRate    = numpy.inf
        bestDirection = None
        for direction in [-1, 1]:
            errorRate = 0.

            self.output[self._mat[d] * direction < threshold * direction]\
                    = LABEL_POSITIVE

            self.output[self._mat[d] * direction >= threshold * direction]\
                    = LABEL_NEGATIVE

            errorRate = self.weight[ self.output != self._label].sum()


            self.output *= 0 # reset the output
            if errorRate < minErrRate:
                minErrRate    = errorRate
                bestDirection = direction

        return minErrRate, threshold, bestDirection

    def train(self):

        for dim in xrange(self.sampleDim):
            err, threshold, direction = self.optimal(dim)
            if err < self.opt_errorRate:
                self.opt_errorRate = err
                self.opt_dimension = dim
                self.opt_threshold = threshold
                self.opt_direction = direction

        assert self.opt_errorRate < 0.5

        return self.opt_errorRate

    def prediction(self, Mat):
        sampleNum = Mat.shape[1]

        dim       = self.opt_dimension
        threshold = self.opt_threshold
        direction = self.opt_direction

        output = numpy.zeros(sampleNum, dtype = numpy.int)

        output[Mat[dim] * direction <  direction * threshold] = LABEL_POSITIVE
        output[Mat[dim] * direction >= direction * threshold] = LABEL_NEGATIVE

        return output

    def show(self, dim = None):

        if dim == None:
            dim = self.opt_dimension

        N = 10 # the number of center
        MaxVal = numpy.max(self._mat[dim])
        MinVal = numpy.min(self._mat[dim])

        scope = (MaxVal - MinVal) / N

        centers = [ (MinVal - scope/2)+ scope*i for i in xrange(N)]
        counter = [ [0, 0] for i in xrange(N)]

        for j in xrange(N):
            for i in xrange(self.sampleNum):
                if abs(self._mat[dim][i] - centers[j]) < scope/2:
                    if self._label[i] == LABEL_POSITIVE:
                        counter[j][1] += 1
                    else:
                        counter[j][0] += 1

        posVal, negVal = [], []

        for i in xrange(N):
            posVal.append(counter[i][1])
            negVal.append(counter[i][0])

        sumPosVal = sum(posVal)
        sumNegVal = sum(negVal)

        for i in xrange(len(posVal)): posVal[i] /= (1. * sumPosVal)
        for i in xrange(len(negVal)): negVal[i] /= (1. * sumNegVal)

        pyplot.title("A simple weak classifier")
        pyplot.plot(centers, posVal, "r-o", label = "Face class")
        pyplot.plot(centers, negVal, "b-o", label = "Non-Face class")
        pyplot.xlabel("feature response")
        pyplot.ylabel("frequency")

        # plot threshold line
        sumPosW = 0.
        sumNegW = 0.
        sumPos = 0.
        sumNeg = 0.
        for i in xrange(self.sampleNum):
            if self._label[i] == LABEL_POSITIVE:
                sumPos  += self.weight[i] * self._mat[dim][i]
                sumPosW += self.weight[i]
            else:
                sumNeg  += self.weight[i] * self._mat[dim][i]
                sumNegW += self.weight[i]
                
        miuPos = sumPos / sumPosW
        miuNeg = sumNeg / sumNegW

        threshold = (miuPos + miuNeg)/2
        pyplot.plot([threshold for i in xrange(10)], [i for i in numpy.arange(0.0, 0.5, 0.05)], label = "threshold")
        pyplot.legend()
        pyplot.show()

    def __str__(self):

        string  = "opt_errorRate:" + str(self.opt_errorRate) + "\n"
        string += "opt_threshold:" + str(self.opt_threshold) + "\n"
        string += "opt_dimension:" + str(self.opt_dimension) + "\n"
        string += "opt_direction:" + str(self.opt_direction) + "\n"
        string += "weights      :" + str(self.weight)        + "\n"
        return string

    def constructor(self, dimension, direction, threshold):
        self.opt_dimension = dimension
        self.opt_threshold = threshold
        self.opt_direction = direction

        return self
