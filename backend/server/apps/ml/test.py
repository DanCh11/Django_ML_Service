from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier


class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "gender": "male",
            "race/ethnicity": "group A",
            "parental level of education": "bachelor's degree",
            "lunch": "standard",
            "math score": 99,
            "reading score": 99,
            "writing score": 99
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertNotEqual('OK', response['status'])
        self.assertFalse('label' in response)
        #self.assertNotEqual('none', response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "income_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Piotr"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                               algorithm_status, algorithm_version, algorithm_owner,
                               algorithm_description, algorithm_code)

        self.assertEqual(len(registry.endpoints), 1)
