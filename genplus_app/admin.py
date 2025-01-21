from django.contrib import admin
from .models import user_master,category_master,component_master,order_master,card_payment,contactfrom,games,gamespc,city_master
# Register your models here.
class displayuser(admin.ModelAdmin):
    list_display=('username','name','email','phone_no','address','postalcode','city')
    search_fields=('username','name')

admin.site.register(user_master,displayuser)


class displaycat(admin.ModelAdmin):
    list_display=('cat_id','cat_name')
    search_fields=['cat_name']

admin.site.register(category_master,displaycat)

class displaycom(admin.ModelAdmin):
    list_display=('con_id','con_name','con_price','mp_date','exp_date')
    search_fields=['con_name']
    list_filter=['con_id']

admin.site.register(component_master,displaycom)


class displayorder(admin.ModelAdmin):
    list_display=('name','order_no','order_name','order_price','order_date','order_time','city','paymethod')
    search_fields=('order_no','name','order_name','username')
    list_filter=('username','city','paymethod')

admin.site.register(order_master,displayorder)

class displaycard(admin.ModelAdmin):
    list_display=('CardNumber','CardHolder','expiresmonth','expiresyear','cvv','balance')
    search_fields=('CardNumber','CardHolder')

admin.site.register(card_payment,displaycard)

class displaycontact(admin.ModelAdmin):
    list_display=('username','name','message','date','time')
    search_fields=('username','name')
    list_filter=('username','name')

admin.site.register(contactfrom,displaycontact)

class displayc(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']


admin.site.register(city_master,displayc)


class displayg(admin.ModelAdmin):
    list_display=['gamename']
    search_fields=['gamename']


admin.site.register(games,displayg)


class displaygp(admin.ModelAdmin):
    list_display=('gamename','Cabinets','Motherboard','Processor','GraphicCard','SMPS','RAM','SSD','HDD','price','ProcessorBrand')
    search_fields=['ProcessorBrand']
    list_filter=['ProcessorBrand']

admin.site.register(gamespc,displaygp)

