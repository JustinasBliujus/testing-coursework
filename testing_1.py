import unittest
from AI1 import activation, neuron, find_weights

class TestNeuronFunctions(unittest.TestCase):
    
    def test_activation_step_random_function(self):
        self.assertEqual(activation(1, 'a'), None)
        self.assertEqual(activation(0, 'a'), None)
        self.assertEqual(activation(-1, 'a'), None)
        
    def test_activation_step(self):
        self.assertEqual(activation(1, 'step'), 1)
        self.assertEqual(activation(0, 'step'), 1)
        self.assertEqual(activation(-1, 'step'), 0)

    def test_activation_sigmoid(self):
        self.assertEqual(activation(1, 'sigmoid'), 1)
        self.assertEqual(activation(10, 'sigmoid'), 1)
        self.assertEqual(activation(-10, 'sigmoid'), 0)
        
    def test_neuron_step(self):
        self.assertEqual(neuron(1, 1, 1, 1, -3, 'step'), 0)
        self.assertEqual(neuron(1, 1, 1, 1, 2, 'step'), 1)

    def test_neuron_sigmoid(self):
        self.assertEqual(neuron(1, 1, 1, 1, -2, 'sigmoid'), 0)
        self.assertEqual(neuron(1, 1, 1, 1, 2, 'sigmoid'), 1)

    def test_find_weights_step(self):
        weights = find_weights('step')
        self.assertEqual(len(weights), 3)
        for w1, w2, b in weights:
            self.assertIsInstance(w1, float)
            self.assertIsInstance(w2, float)
            self.assertIsInstance(b, float)

    def test_find_weights_sigmoid(self):
        weights = find_weights('sigmoid')
        self.assertEqual(len(weights), 3)
        for w1, w2, b in weights:
            self.assertIsInstance(w1, float)
            self.assertIsInstance(w2, float)
            self.assertIsInstance(b, float)

    def test_weight_range(self):
        weights = find_weights('step')
        for w1, w2, b in weights:
            self.assertGreaterEqual(w1, -5)
            self.assertLessEqual(w1, 5)
            self.assertGreaterEqual(w2, -5)
            self.assertLessEqual(w2, 5)
            self.assertGreaterEqual(b, -5)
            self.assertLessEqual(b, 5)
    
    def test_classification_step(self):
        weights = find_weights('step')[0]
        w1, w2, b = weights
        self.assertIn(neuron(1, 2, w1, w2, b, 'step'), [0, 1])
        self.assertIn(neuron(6, 7, w1, w2, b, 'step'), [0, 1])

    def test_classification_sigmoid(self):
        weights = find_weights('sigmoid')[0]
        w1, w2, b = weights
        self.assertIn(neuron(1, 2, w1, w2, b, 'sigmoid'), [0, 1])
        self.assertIn(neuron(6, 7, w1, w2, b, 'sigmoid'), [0, 1])
    
    def test_activation_sigmoid_rounding(self):
        self.assertEqual(activation(0.01, 'sigmoid'), 1)

    def test_find_weights_unique_sets(self):
        weights = find_weights('step')
        self.assertNotEqual(weights[0], weights[1])
        self.assertNotEqual(weights[1], weights[2])
        self.assertNotEqual(weights[0], weights[2])

    def test_find_weights_returns_exactly_three_sets(self):
        weights = find_weights('step')
        self.assertEqual(len(weights), 3, "Expected exactly 3 sets of weights.")
    
        weights = find_weights('sigmoid')
        self.assertEqual(len(weights), 3, "Expected exactly 3 sets of weights.")
        
    def test_neuron_zero_inputs(self):
        self.assertEqual(neuron(0, 0, 0, 0, 0, 'step'), 1)  
        self.assertEqual(neuron(0, 0, 0, 0, 0, 'sigmoid'), 1) 

    def test_classification_class_0(self):
        class_0 = [(1, 2), (2, 3), (1.5, 2.5), (3, 3), (2.5, 4)]
        
        weights = find_weights('step')[0] 
        w1, w2, b = weights
        
        for (x, y) in class_0:
            result = neuron(x, y, w1, w2, b, 'step') 
            self.assertEqual(result, 0, f"Point ({x}, {y}) was incorrectly classified as class 1.")
    
    def test_classification_class_1(self):
        class_1 = [(6, 7), (7, 6), (6.5, 6.5), (8, 7), (7.5, 8)]
        
        weights = find_weights('step')[0] 
        w1, w2, b = weights
        
        for (x, y) in class_1:
            result = neuron(x, y, w1, w2, b, 'step') 
            self.assertEqual(result, 1, f"Point ({x}, {y}) was incorrectly classified as class 0.")

    def test_activation_invalid_function(self):
        with self.assertRaises(ValueError):
            activation(1, 'invalid_function') 

        with self.assertRaises(ValueError):
            activation(-1, 'random_function') 

    def test_neuron_small_values(self):
        small_value = 1e-5
        self.assertEqual(neuron(small_value, small_value, 1, 1, 0, 'step'), 1)  
        self.assertEqual(neuron(-small_value, -small_value, 1, 1, 0, 'step'), 0) 
        self.assertEqual(neuron(small_value, small_value, 1, 1, 0, 'sigmoid'), 1) 
        self.assertEqual(neuron(-small_value, -small_value, 1, 1, 0, 'sigmoid'), 0)  
    
    def test_neuron_infinity(self):
        result_pos_inf = neuron(1, 1, float('inf'), float('inf'), float('inf'), 'step')
        self.assertEqual(result_pos_inf, 1, "Neuron output with positive infinity is incorrect.")

        result_neg_inf = neuron(1, 1, float('-inf'), float('-inf'), float('-inf'), 'step')
        self.assertEqual(result_neg_inf, 0, "Neuron output with negative infinity is incorrect.")

        result_large_pos = neuron(1, 1, 1e10, 1e10, 1e10, 'step')
        self.assertEqual(result_large_pos, 1, "Neuron output with large positive values is incorrect.")

        result_large_neg = neuron(1, 1, -1e10, -1e10, -1e10, 'step')
        self.assertEqual(result_large_neg, 0, "Neuron output with large negative values is incorrect.")

    def test_activation_invalid_function(self):
        with self.assertRaises(ValueError):
            find_weights('invalid_function') 

        with self.assertRaises(ValueError):
            find_weights('random_function') 

    def test_find_weights_classification_equivalence(self):
        step_weights = find_weights('step')
        sigmoid_weights = find_weights('sigmoid')

        for i in range(len(step_weights)):
            w1_step, w2_step, b_step = step_weights[i]
            w1_sigmoid, w2_sigmoid, b_sigmoid = sigmoid_weights[i]
            class_0 = [(1, 2), (2, 3), (1.5, 2.5), (3, 3), (2.5, 4)]
            class_1 = [(6, 7), (7, 6), (6.5, 6.5), (8, 7), (7.5, 8)]
            for (x, y) in class_0:
                self.assertEqual(neuron(x, y, w1_step, w2_step, b_step, 'step'), 0)
            for (x, y) in class_1:
                self.assertEqual(neuron(x, y, w1_step, w2_step, b_step, 'step'), 1)
            for (x, y) in class_0:
                self.assertEqual(neuron(x, y, w1_sigmoid, w2_sigmoid, b_sigmoid, 'sigmoid'), 0)
            for (x, y) in class_1:
                self.assertEqual(neuron(x, y, w1_sigmoid, w2_sigmoid, b_sigmoid, 'sigmoid'), 1)


if __name__ == '__main__':
    unittest.main()