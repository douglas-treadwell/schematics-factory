from unittest import TestCase
from schematics.types import StringType, ModelType, IntType, BooleanType
from schematics_factory import model


class TestFactory(TestCase):
    def test_simple_factory(self):
        my_model = model({
            'str': StringType()
        })

        my_instance = my_model({
            'str': 'str'
        })

        my_instance.validate()

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
