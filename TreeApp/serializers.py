from rest_framework import serializers
# from rest_framework_recursive.fields import RecursiveField

from .models import LeveledTree, Categories, Parameters, ParametersTree

from ApartmentNumberApp.models import ApartmentNumber
from ApartmentNumberApp.serializers import ApartmentNumberSerializer


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        # fields = '__all__'
        fields = ['id', 'category_name', 'description']

        depth = 0


class CategoriesSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = Categories
        # fields = '__all__'
        fields = ['id', 'category_name', 'description']

        depth = 0


class ParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        # fields = '__all__'
        fields = ['id', 'variable_name', 'variable_category', 'description']

        depth = 0


class ParametersSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        # fields = '__all__'
        fields = ['id', 'variable_name', 'variable_category', 'description']

        depth = 0


class ParametersTreeSerializer(serializers.ModelSerializer):
    variable_name = ParametersSerializer(read_only=True)

    class Meta:
        model = ParametersTree
        # fields = '__all__'
        fields = ['id', 'variable_name', 'variable_value', 'fk', 'description']

        depth = 0


class ParametersTreeSerializerSet(serializers.ModelSerializer):
    variable_name = serializers.SlugRelatedField(queryset=Parameters.objects.all(), slug_field='variable_name')

    class Meta:
        model = ParametersTree
        # fields = '__all__'
        fields = ['id', 'variable_name', 'variable_value', 'fk', 'description']

        depth = 0


class LeveledTreeSerializer(DynamicFieldsModelSerializer):
    apartment_number = ApartmentNumberSerializer(read_only=True)

    parameters_leveled_tree = ParametersTreeSerializer(many=True, required=False)

    class Meta:
        model = LeveledTree
        # fields = '__all__'
        fields = ['id', 'name', 'apartment_number', 'description', 'parent',

                  'parameters_leveled_tree',
                  ]

        depth = 1


class LeveledTreeSerializerSet(DynamicFieldsModelSerializer):
    apartment_number = serializers.SlugRelatedField(queryset=ApartmentNumber.objects.all(), slug_field='name', required=False)

    parent = serializers.SlugRelatedField(queryset=LeveledTree.objects.all(), slug_field='name', required=False)

    parameters_leveled_tree = serializers.SlugRelatedField(queryset=ParametersTree.objects.all(), slug_field='variable_value', many=True, required=False)

    class Meta:
        model = LeveledTree
        # fields = '__all__'
        fields = ['id', 'name', 'apartment_number', 'description', 'parent',

                  'parameters_leveled_tree',
                  ]

        depth = 1
