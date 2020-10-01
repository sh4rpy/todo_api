from rest_framework import fields


class CustomChoiceField(fields.ChoiceField):
    def to_representation(self, value):
        return self._choices[value]
