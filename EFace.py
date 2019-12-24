
from config import TEST_IMG
from matplotlib import image
from matplotlib import pyplot
import pylab
from time import time
from detector import Detector

start_time = time()

img = image.imread(TEST_IMG)
print(img)

if len(img.shape) == 3:
    imgSingleChannel = img[:,:, 1]
else:
    imgSingleChannel = img

det = Detector()

rectangles = det.scanImgOverScale(imgSingleChannel)

end_time = time()

print "Number of rectangles: ", len(rectangles)
print "Cost time: ", end_time - start_time

det.showResult(img, rectangles)
