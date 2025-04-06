from django.views.generic import (DetailView,
                                  ListView)
from home.models import (ProductModel,
                         BannerModel)


class IndexView(ListView):
    model = ProductModel
    template_name = "index/index.html"
    context_object_name = "products"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banner"] = BannerModel.objects.first()
        return context
    

class CategoriesView(ListView):
    model = ProductModel
    template_name = "index/all_items.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["platinum"] = ProductModel.objects.filter(type="Platinum").order_by("show_order")
        context["gold"] = ProductModel.objects.filter(type="Gold").order_by("show_order")
        context["silver"] = ProductModel.objects.filter(type="Silver").order_by("show_order")
        context["diamond"] = ProductModel.objects.filter(type="Diamond").order_by("show_order")
        return context


class DetailProductView(DetailView):
    model = ProductModel
    template_name = "index/product.html"
    context_object_name = "products"
    

class TypeView(ListView):
    model = ProductModel
    template_name = "index/category.html"
    context_object_name = "products"
    
    def get_queryset(self):
        category = self.kwargs["category"]
        # if category == "diamond":
        #     category = "bronze"
        return ProductModel.objects.filter(type=category.capitalize())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs["category"]
        context["type_name"] = category
        return context