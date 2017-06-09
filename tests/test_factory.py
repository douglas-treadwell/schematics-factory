from unittest import TestCase
from schematics.types import StringType, ModelType, IntType, BooleanType
from schematics_factory import model, nested


class TestFactory(TestCase):
    def test_simple_factory(self):
        my_model = model({
            'str': StringType()
        })

        my_instance = my_model({
            'str': 'str'
        })

        my_instance.validate()

    def test_alternative_syntax(self):
        Person = model(name=StringType(), age=IntType())

        person = Person(dict(name='Test', age=27))

        person.validate()

    def test_alternative_syntax_nesting(self):
        Person = model(name=StringType(), pet=nested(name=StringType()))

        person = Person(dict(name='Test', pet=dict(name='Rover')))

        person.validate()

    def test_nested_factory(self):
        my_model = model({
            'str': StringType(),
            'nested': ModelType(model({
                'nested_str': StringType()
            }))
        })

        my_instance = my_model({
            'str': 'str',
            'nested': {
                'nested_str': 'str'
            }
        })

        my_instance.validate()

    def test_nested_dict_literals(self):
        Person = model(name=StringType(),
                       pet=dict(name=StringType(required=True)))

        person = Person(dict(name='Test', pet=dict(name='Rover')))

        person.validate()

        Person = model({
            'name': StringType(),
            'pet': {
                'name': StringType(required=True)
            }
        })

        person = Person({
            'name': 'Test',
            'pet': {
                'name': 1
            }
        })

        person.validate()

    def test_readme_example(self):
        OuterModel = model({
            'outer_str': StringType(),
            'outer_nested': ModelType(model({
                'middle_int': IntType(),
                'middle_nested': ModelType(model({
                    'inner_bool': BooleanType()
                }))
            }))
        })

        input_ = {
            'outer_str': 'str',
            'outer_nested': {
                'middle_int': 1,
                'middle_nested': {
                    'inner_bool': True
                }
            }
        }

        model_instance = OuterModel(input_)
        model_instance.validate()
