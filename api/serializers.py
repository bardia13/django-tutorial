from rest_framework import serializers
from core.models import Person


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "age", "father_name"]


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=5, required=True, allow_blank=False)
    age = serializers.IntegerField(required=True, allow_null=False)
    father_name = serializers.CharField(max_length=200, required=False, allow_blank=True)

    def create(self, validated_data):
        instance = Person.objects.create(
            name=validated_data["name"],
            age=validated_data["age"],
            father_name=validated_data.get("father_name", ""),
        )
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.age = validated_data["age"]
        instance.father_name = validated_data.get("father_name", "")
        instance.save()
        return instance
    