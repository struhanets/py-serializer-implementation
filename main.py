import io

from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    json_data = JSONRenderer().render(serialized_car.data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    json_data = JSONParser().parse(stream)
    serializer = CarSerializer(data=json_data)
    if serializer.is_valid():
        return serializer.save()
    return serializer.errors

