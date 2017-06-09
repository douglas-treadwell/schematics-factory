from schematics.models import Model, ModelMeta
from schematics.types import ModelType


def model(_schema_dict=None, **kwargs):
    return ModelMeta('AnonymousModel', (Model,), _schema_dict or kwargs)


model_factory = model  # alternative import name


def nested(*args, **kwargs):
    return ModelType(model(*args, **kwargs))


nested_model = nested  # alternative import name
