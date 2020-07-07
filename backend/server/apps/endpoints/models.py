from django.db import models

# Create your models here.
# Defining Database Models


class Endpoint(models.Model):
    """
    Attributes:
        name: the name of the endpoint what will be used in API URL
        owner: the string with owner name
        created_at: The date when endpoint was created

    """
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    """
    Attributes:
        name: name of the algorithm
        description: the short description of how the algorithm works
        code: the code of the algorithm
        version: the versiom of the algorithm similar to software versioning
        owner: the name of the owner
        created_at: the dare when MLAlgorithm was added
        parent_endpoint: the reference of the Endpoint
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    """
    Attributes:
        status: The status of algorithm in the endpoint. Ex: testing, staging
        active: The boolean flag which point to currently active status
        created_by: the name of creator
        created_at: the date of status creation
        parent_MLAlgorithm: The reference to corresponding MLAlgorithm
    """
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE, related_name='status')


class MLRequest(models.Model):
    """
    Atributes:
        input_data: the input data to ML algorithm in JSON format
        full_response: the response of the ML algorithm
        response: the response of the ML algorithm in JSON format
        feedback: the feedback about the response in JSON format
        created_at: the date when request was created
         parent_mlalgorithm: The reference to MLAlgorithm used to compute response
    """
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE)
