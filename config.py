
DEBUG_MODEL   = True
USING_CASCADE = False

# training set directory for face and non-face images
TRAINING_FACE    = "E:/FaceDetection-master/FaceDetection/TrainingImages/FACES/"
TRAINING_NONFACE = "E:/FaceDetection-master/FaceDetection/TrainingImages/NFACES/"

# test set directory for face and non-face images
TEST_FACE        = "./TrainingImages/FACES/"
TEST_NONFACE     = "./TrainingImages/NFACES/"

# single image for testing
TEST_IMG         = "./Test/chris.png"

FEATURE_FILE_TRAINING = "./features/features_train.cache"
FEATURE_FILE_TESTING  = "./features/features_test.cache"

FEATURE_FILE_SUBSET   = "./features/features_train_subset"
FEATURE_FILE_SUBSET_0 = "./features/features_train_subset0.cache"
FEATURE_FILE_SUBSET_1 = "./features/features_train_subset1.cache"

# For parallel
PROCESS_NUM = 2

ADABOOST_CACHE_FILE = "./model/adaboost_classifier.cache"
ROC_FILE            = "./model/roc.cache"

FIGURES             = "./figure/"

# image size in the training set 19 * 19
TRAINING_IMG_HEIGHT = 19
TRAINING_IMG_WIDTH  = 19

# How many different types of  Haar-feature
FEATURE_TYPE_NUM    = 5
# How many number of features that a single training image have
FEATURE_NUM = 37862
#FEATURE_NUM         = 16373
#FEATURE_NUM         = 49608

# number of positive and negative sample will be used in the training process
POSITIVE_SAMPLE     = 4800
NEGATIVE_SAMPLE     = 9000

SAMPLE_NUM = POSITIVE_SAMPLE + NEGATIVE_SAMPLE

TESTING_POSITIVE_SAMPLE = 20
TESTING_NEGATIVE_SAMPLE = 20

TESTING_SAMPLE_NUM = TESTING_NEGATIVE_SAMPLE + TESTING_POSITIVE_SAMPLE

LABEL_POSITIVE = +1
LABEL_NEGATIVE = -1

WHITE = 255
BLACK = 0

EXPECTED_TPR = 0.999
EXPECTED_FPR = 0.0005

# for CASCADE
EXPECTED_FPR_PRE_LAYYER = 0.1
EXPECTED_TPR_PRE_LAYYER = 0.999

# the threshold range of adaboost. (from -inf to +inf)
AB_TH_MIN   = -15
AB_TH_MAX   = +15

HAAR_FEATURE_TYPE_I     = "I"
HAAR_FEATURE_TYPE_II    = "II"
HAAR_FEATURE_TYPE_III   = "III"
HAAR_FEATURE_TYPE_IV    = "IV"
HAAR_FEATURE_TYPE_V     = "V"

AB_TH       = -3.
OVER_LAP_TH = 0.1

MAX_WEAK_NUM = 12

CASACADE_LIMIT = 3
ADABOOST_LIMIT = 150

SEARCH_WIN_STEP = 4

DETECT_START = 1.
DETECT_END   = 2.
DETECT_STEP  = 0.2
