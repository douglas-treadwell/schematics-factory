from schematics.models import Model, ModelMeta


def model(schema_dict):
    return ModelMeta('AnonymousModel', (Model,), schema_dict)


model_factory = model  # alternative import name
