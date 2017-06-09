from schematics.models import Model, ModelMeta


def model(_schema_dict=None, **kwargs):
    return ModelMeta('AnonymousModel', (Model,), _schema_dict or kwargs)


model_factory = model  # alternative import name
