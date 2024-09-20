from django import forms
from .models import Component, Attribute, Category, Threat, Control, ImplementedControl


class ComponentForm(forms.ModelForm):
    attributes = forms.ModelMultipleChoiceField(queryset=Attribute.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id', None)
        super().__init__(*args, **kwargs)

        if product_id:
            self.fields['product'].initial = product_id

    class Meta:
        model = Component
        fields = ['name', 'description', 'product']

    def save(self, commit=True):
        component = super().save(commit=False)
        if commit:
            component.save()
        if self.cleaned_data['attributes']:
            component.attributes.set(self.cleaned_data['attributes'])
        if self.cleaned_data['categories']:
            component.categories.set(self.cleaned_data['categories'])
        return component




class AttributeForm(forms.ModelForm):
    components = forms.ModelMultipleChoiceField(
        queryset=Component.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    threats = forms.ModelMultipleChoiceField(
        queryset=Threat.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    controls = forms.ModelMultipleChoiceField(
        queryset=Control.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Attribute
        fields = ['name', 'description', 'controls']

    def save(self, commit=True):
        attribute = super().save(commit=False)
        if commit:
            attribute.save()
        if self.cleaned_data['components']:
            attribute.components.set(self.cleaned_data['components'])
        if self.cleaned_data['threats']:
            attribute.threats.set(self.cleaned_data['threats'])
        if self.cleaned_data['controls']:
            attribute.controls.set(self.cleaned_data['controls'])
        return attribute


class ThreatForm(forms.ModelForm):
    controls = forms.ModelMultipleChoiceField(queryset=Control.objects.all(), required=False)
    attributes = forms.ModelMultipleChoiceField(queryset=Attribute.objects.all(), required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Threat
        fields = ['name', 'description']

    def save(self, commit=True):
        threat = super().save(commit=False)
        if commit:
            threat.save()
        if self.cleaned_data['controls']:
            threat.controls.set(self.cleaned_data['controls'])
        if self.cleaned_data['attributes']:
            threat.attributes.set(self.cleaned_data['attributes'])
        if self.cleaned_data['categories']:
            threat.categories.set(self.cleaned_data['categories'])
        return threat


class ControlForm(forms.ModelForm):
    implemented_controls = forms.ModelMultipleChoiceField(queryset=ImplementedControl.objects.all(), required=False)

    class Meta:
        model = Control
        fields = ['name', 'description', 'threats']

    def save(self, commit=True):
        control = super().save(commit=False)
        if commit:
            control.save()
        if self.cleaned_data['implemented_controls']:
            control.implemented_controls.set(self.cleaned_data['implemented_controls'])
        return control
