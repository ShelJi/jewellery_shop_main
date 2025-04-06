from home.models import (GoldPrice,
                         CategoryModel,
                         ProductModel) 
 

def gold_prices(request):
    try:
        latest_prices = GoldPrice.objects.first()
        # categories = CategoryModel.objects.all()
        # available_categories = [category.type for category in categories]
        
        gold = ProductModel.objects.filter(type="Gold")
        available_categories_gold = [category.category.type for category in gold]
        available_categories_gold = list(set(available_categories_gold))
        
        platinum = ProductModel.objects.filter(type="Platinum")
        available_categories_platinum = [category.category.type for category in platinum]
        available_categories_platinum = list(set(available_categories_platinum))
        
        silver = ProductModel.objects.filter(type="Silver")
        available_categories_silver = [category.category.type for category in silver]
        available_categories_silver = list(set(available_categories_silver))
        
        diamond = ProductModel.objects.filter(type="Diamond")
        available_categories_diamond = [category.category.type for category in diamond]
        available_categories_diamond = list(set(available_categories_diamond))
        
        return {
            "gold_1g": latest_prices.gold_1g,
            "gold_8g": latest_prices.gold_8g,
            "silver_1g": latest_prices.silver_1g,
            "available_categories_gold": available_categories_gold,
            "available_categories_platinum": available_categories_platinum, 
            "available_categories_silver": available_categories_silver, 
            "available_categories_diamond": available_categories_diamond, 
        }
    except GoldPrice.DoesNotExist:
        return {
            "gold_1g": "N/A",
            "gold_8g": "N/A",
            "silver_1g": "N/A",
        }
