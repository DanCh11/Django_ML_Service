from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.registry import MLRegistry
import inspect
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# ML registry

try:
    # create ML registry
    registry = MLRegistry()
    # random forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                           algorithm_object=rf,
                           algorithm_name="random forest",
                           algorithm_status="production",
                           algorithm_version="0.0.1a",
                           owner="Daycu_",
                           algorithm_description="description",
                           algorithm_code=inspect.getsource(RandomForestClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
