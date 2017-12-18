from django.shortcuts import render
from django.db.models import Q
from models import market, item  # import the retaurannt database model
from functions import *
from django.http import HttpResponse


# Create your views here.


def markets(request):
    lst_markets = market.objects.all().order_by("name")
    context = {"lst_markets": lst_markets}
    template = "market.html"
    return render(request, template, context)


def items(request, r_id):
    lst_item = item.objects.filter(market_id=r_id)
    if len(lst_item) == 0:
        message = "No item yet for this market. kindly check back later"
        context = {"lst_item": lst_item,"message": message}
    else:

        # for dish in lst_item:
        #     td = "<td><img src={}></td>"
        #     lst_tds.append(td)
        result = myview(lst_item, 5)
        context = {"lst_item": lst_item, "lst_fobj": result}
    template = "market/item.html"
    return render(request, template, context)


def view_order(request,d_id):
    itm=item.objects.get(pk=d_id)
    r_id=itm.market_id
    maket=market.objects.get(pk=r_id)
    context={"item":itm,"market":maket}
    template="market/view.html"
    return render(request, template, context)


def search(request):
    query = request.GET.get('search','')
    if query:
        qset = (
                 Q(name__icontains=query) |
                 Q(price__icontains=query)|
                 Q(market__name__icontains=query)
                )
        results=item.objects.filter(qset)
        if len(results)==0:
            message="No item with your search parameter. Please search again."
            context={"message":message,"query":query}
        else:
            context={"results":results,"query":query}
    else:
        message="please type in a search string"

        context={"message":message,"query":query}


    template="search.html"
    return render(request,template,context)


def home(request):
    #generating random item and displaying them#

    dobj=[]             #empty list to hold random item
    pk_lst=[]           #list of primary keys
    likes=[]            #list for likes
    item_all=item.objects.all()
    last_ten = item_all[:10]
    try:
        for dish in item_all:
            pk_lst.append(dish.id)
            likes.append((dish.likes,dish.id))
        lst=random_lst_gen(pk_lst,6) #generating 6 rnadom numbers from pk list
        for i in lst:
            dish = item.objects.get(pk=i)
            dobj.append(dish)
            # if (dish):
            #     dobj.append(dish)
            # else:
            #     pass
        dishlst = myview(dobj,3)  #formarting dobj list for viewing

         #generating  most liked item#
        ordered_lst= sorted(likes,reverse=True) #sort the likes list in decending order
        most_liked=[]
        most_liked_obj=[]
        for i in range(4):
            most_liked.append(ordered_lst[i])
        for i in most_liked:
            dish=item.objects.get(id=i[1])
            most_liked_obj.append(dish)

        context={"dishlist":dishlst,"like":most_liked_obj,"table_items":last_ten}
    except IndexError:
        html="No data yet to be displayed. Kindly check back later."
        context={"emptyquery":html}
    template="home.html"
    return render(request,template,context)

def contactus(request):
    context={}
    template="contactus.html"
    return render(request,template,context)

def like_item(request):
    dish_id=None
    if request.method == 'GET':
        dish_id=request.GET['d_id']
    likes=0
    if dish_id:
        dish=item.objects.get(id=int(dish_id))
        if dish:
            likes = dish.likes + 1
            dish.likes=likes
            dish.save()
    return HttpResponse(likes)

def contactForm(request):
    name=request.GET.get('name','')
    email=request.GET.get('email','')
    feedback=request.GET.get('feedback','')
    message="Thank you"+name+" for your feedback."
    context={"message": message}
    template= "thanks.html"
    return render(request,template,context)
