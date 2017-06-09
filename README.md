Schematics Factory
==================


Inspired by [Voluptuous](https://github.com/alecthomas/voluptuous).

It's sometimes inconvenient to define
named [Schematics](https://github.com/schematics/schematics)
Models, especially when those models are deeply nested.

Example:

```
class InnerModel(Model):
    inner_bool = BooleanType()


class MiddleModel(Model):
    middle_int = IntType()
    middle_nested = ModelType(InnerModel)


class OuterModel(Model):
    outer_str = StringType()
    outer_nested = ModelType(MiddleModel)


model_instance = OuterModel(input_)
model_instance.validate()
```

So, this library provides a convenient syntax for defining
deeply nested Models.

```
OuterModel = model({
    'outer_str': StringType(),
    'outer_nested': ModelType(model({
        'middle_int': IntType(),
        'middle_nested': ModelType(model({
            'inner_bool': BooleanType()
        }))
    }))
})

model_instance = OuterModel(input_)
model_instance.validate()
```
