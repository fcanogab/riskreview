from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product, Component, Attribute, Threat, Control, ImplementedControl, Category
from .forms import ComponentForm, AttributeForm, ThreatForm, ControlForm


#### Product views ####
class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description']

    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Product.objects.filter(user=self.request.user)
        else:
            return Product.objects.none()

class ProductList(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductUpdate(LoginRequiredMixin,UpdateView):
    model = Product
    fields = ['name', 'description', 'components']

class ProductDelete(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


#### Component views ####
class ComponentCreate(LoginRequiredMixin, CreateView):
    model = Component
    form_class = ComponentForm

    success_url = reverse_lazy('component_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ComponentDetail(LoginRequiredMixin, DetailView):
    model = Component

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Component.objects.filter(user=self.request.user)
        else:
            return Component.objects.none()

class ComponentList(LoginRequiredMixin, ListView):
    model = Component

    def get_queryset(self):
        return Component.objects.filter(user=self.request.user)

class ComponentUpdate(LoginRequiredMixin,UpdateView):
    model = Component
    form_class = ComponentForm

    def get_initial(self):
        initial = super().get_initial()
        initial['attributes'] = self.object.attributes.all()
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.attributes.set(form.cleaned_data['attributes'])
        return response

class ComponentDelete(LoginRequiredMixin,DeleteView):
    model = Component
    success_url = reverse_lazy('component_list')


#### Attribute views ####
class AttributeCreate(LoginRequiredMixin, CreateView):
    model = Attribute
    form_class = AttributeForm

    success_url = reverse_lazy('attribute_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AttributeDetail(LoginRequiredMixin, DetailView):
    model = Attribute

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Attribute.objects.filter(user=self.request.user)
        else:
            return Attribute.objects.none()

class AttributeList(LoginRequiredMixin, ListView):
    model = Attribute

    def get_queryset(self):
        return Attribute.objects.filter(user=self.request.user)

class AttributeUpdate(LoginRequiredMixin,UpdateView):
    model = Attribute
    form_class = AttributeForm

    def get_initial(self):
        initial = super().get_initial()
        initial['controls'] = self.object.controls.all()
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.controls.set(form.cleaned_data['controls'])
        return response

class AttributeDelete(LoginRequiredMixin,DeleteView):
    model = Attribute
    success_url = reverse_lazy('attribute_list')


#### Threat views ####
class ThreatCreate(LoginRequiredMixin, CreateView):
    model = Threat
    form_class = ThreatForm

    success_url = reverse_lazy('threat_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ThreatDetail(LoginRequiredMixin, DetailView):
    model = Threat

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Threat.objects.filter(user=self.request.user)
        else:
            return Threat.objects.none()

class ThreatList(LoginRequiredMixin, ListView):
    model = Threat

    def get_queryset(self):
        return Threat.objects.filter(user=self.request.user)

class ThreatUpdate(LoginRequiredMixin,UpdateView):
    model = Threat
    form_class = ThreatForm

class ThreatDelete(LoginRequiredMixin,DeleteView):
    model = Threat
    success_url = reverse_lazy('threat_list')


#### Control views ####
class ControlCreate(LoginRequiredMixin, CreateView):
    model = Control
    form_class = ControlForm

    success_url = reverse_lazy('control_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ControlDetail(LoginRequiredMixin, DetailView):
    model = Control

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Control.objects.filter(user=self.request.user)
        else:
            return Control.objects.none()

class ControlList(LoginRequiredMixin, ListView):
    model = Control

    def get_queryset(self):
        return Control.objects.filter(user=self.request.user)

class ControlUpdate(LoginRequiredMixin,UpdateView):
    model = Control
    form_class = ControlForm

class ControlDelete(LoginRequiredMixin,DeleteView):
    model = Control
    success_url = reverse_lazy('control_list')


#### ImplementedControl views ####
class ImplementedControlCreate(LoginRequiredMixin, CreateView):
    model = ImplementedControl
    fields = ['name', 'description', 'control']

    success_url = reverse_lazy('implemented_control_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ImplementedControlDetail(LoginRequiredMixin, DetailView):
    model = ImplementedControl

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ImplementedControl.objects.filter(user=self.request.user)
        else:
            return ImplementedControl.objects.none()

class ImplementedControlList(LoginRequiredMixin, ListView):
    model = ImplementedControl

    def get_queryset(self):
        return ImplementedControl.objects.filter(user=self.request.user)

class ImplementedControlUpdate(LoginRequiredMixin,UpdateView):
    model = ImplementedControl
    fields = ['name', 'description', 'control']

class ImplementedControlDelete(LoginRequiredMixin,DeleteView):
    model = ImplementedControl
    success_url = reverse_lazy('implemented_control_list')



#### Category views ####
class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'description', 'components', 'threats']

    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Category.objects.filter(user=self.request.user)
        else:
            return Category.objects.none()

class CategoryList(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryUpdate(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name', 'description', 'components', 'threats']

class CategoryDelete(LoginRequiredMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
