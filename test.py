import unittest
from A1 import preprocessing, train_and_evaluate_random_forest

class TestRandomForestClassifier(unittest.TestCase):
    def test_preprocessing(self):
        xtrain, xtest, ytrain, ytest = preprocessing()
        # Check if the data shapes are as expected
        self.assertEqual(xtrain.shape[0] + xtest.shape[0], len(ytrain) + len(ytest))
        # Add more specific checks if needed

    def test_train_and_evaluate_random_forest(self):
        xtrain, xtest, ytrain, ytest = preprocessing()
        acc_rf, f1_rf = train_and_evaluate_random_forest(xtrain, ytrain, xtest, ytest)
        # Check if accuracy and F1 score are within a reasonable range
        self.assertTrue(0 <= acc_rf <= 100)
        self.assertTrue(0 <= f1_rf <= 100)
        # Add more specific checks if needed

if __name__ == '__main__':
    unittest.main()
