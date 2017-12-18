import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','chepane.settings')

import django
django.setup()

from mbt.models import *

def populate():
    res1=addmarket(name='BaTA',address='Bata,Kano.')
    res2 = addmarket(name='Yan kura',address='yan kura,kano')
    res3 = addmarket(name='Dawano',address='65,dawano, kano.')

    dish1=additem(name='afang',imageurl='mbt/media/dishes/afang-soup.jpg',market=res1,description='/bundle',price=750)
    dish2=additem(name='beef',imageurl='mbt/media/dishes/beef_steak.jpg',market=res2,description='/kg',price=600)
    dish3=additem(name='flour',imageurl='mbt/media/dishes/burger.jpg',market=res2,description='/mudu',price=450)
    dish4=additem(name='corn',imageurl='mbt/media/dishes/cake.jpg',market=res1,description='/mudu',price=550)
    dish5=additem(name='rice',imageurl='mbt/media/dishes/fried-rice.jpg',market=res3,description='/mudu',price=600)
    dish6=additem(name='fish',imageurl='mbt/media/dishes/fries_and_steak_on_plate.jpg',market=res3,description='/kg',price=650)
    dish7=additem(name='indomie',imageurl='mbt/media/dishes/indomie-recipe.jpg',market=res1,description='/carton',price=250)
    dish8=additem(name='tomatoes',imageurl='mbt/media/dishes/nicoise_salad .jpg',market=res1,description='/kwando',price=600)
    dish9=additem(name='pasta',imageurl='mbt/media/dishes/pasta_lg.jpg',market=res2,description='/carton',price=450)
    dish10=additem(name='smoked salmon slices',imageurl='mbt/media/dishes/smoked_salmon_slices.jpg',market=res1,description='/bundle',price=750)
    dish11=additem(name='macroni',imageurl='mbt/media/dishes/spaghetti_napolitana.jpg',market=res2,description='/carton',price=300)
    dish12=additem(name='eggs',imageurl='mbt/media/dishes/tortilleria.jpg',market=res2,description='/crate',price=850)

def addmarket(name,address):
    r= market.objects.create(name=name,address=address)
    return r

def additem(name,imageurl,market,description,price):
    i=item.objects.create(name=name,imageurl=imageurl,market=market,description=description,price=price)
    return i
if __name__ == '__main__':
    print 'starting chepane populating script'
    populate()
