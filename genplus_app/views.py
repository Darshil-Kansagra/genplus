from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import user_master,component_master,order_master,card_payment,contactfrom,games,gamespc,city_master
# Create your views here.

productname=None
price=None
pm=None
success_message=None
error_message=None

# home function
def index(request):
    return render(request,'index.html')


# login function
def login(request):
    return_url=None
    login.return_url=request.GET.get('return_url')
    if request.method=="POST":
        uname=request.POST['username']
        pas=request.POST['password']
        error_message=None

        if user_master.objects.all().filter(username=uname,password=pas):
            request.session['username']=uname
            if login.return_url:
                return HttpResponseRedirect(login.return_url)
            else:
                login.return_url=None
                return redirect(index)
        else:
            error_message="Username or password is incorrect"
            return render(request,'login.html',{'error':error_message})
    elif request.method=="GET":
        return render(request,'login.html')
    else:
        error_message="Sorry Can't login Now"
        return render(request,'login.html',{'error':error_message})


# logout function
def logout(request):
    del request.session['username']
    request.session.clear()
    return redirect(login)


# signup function
def signup(request):
    if request.method=="POST":
        uname=request.POST['username']
        pas=request.POST['password']
        mail=request.POST['email']
        phone=request.POST['phone_no']
        name=request.POST['name']
        address=request.POST['address']
        pc=request.POST['postalcode']
        city=request.POST['city']
        error_message=None
        success_message=None


        if user_master.objects.all().filter(username=uname):
            error_message="Username is already taken"
            return render(request,'signup.html',{'error':error_message})

        elif user_master.objects.all().filter(email=mail):
            error_message="Email is already taken"
            return render(request,'signup.html',{'error':error_message})

        elif user_master.objects.all().filter(phone_no=phone):
            error_message="Phone Number is already taken"
            return render(request,'signup.html',{'error':error_message})
        else:
            temp=user_master(username=uname,name=name,password=pas,email=mail,phone_no=phone,address=address,postalcode=pc,city=city)
            temp.save()
            success_message="Signup Successfully"
            return render(request,'signup.html',{'success':success_message})
            
    elif request.method=="GET":
        show=city_master.objects.all()
        return render(request,'signup.html',{'city':show})
    else:
        error_message="Sorry Can't Signin Now"
        return render(request,'signup.html',{'error':error_message})


# profile page function
def profile(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):
        show=user_master.objects.all().filter(username=request.session.get('username'))
        return render(request,'profile.html',{'user':show})
    else:
        return redirect(f'login?return_url={return_url}')


# edit profile page function
def editprofile(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):   
        if request.method=="POST":
            name=request.POST['name']
            address=request.POST['address']
            pc=request.POST['postalcode']
            city=request.POST['city']

            user_master.objects.filter(username=request.session.get('username')).update(name=name,address=address,postalcode=pc,city=city)
            return redirect(profile)
        elif request.method=="GET":
            show=city_master.objects.all()
            return render(request,'editprofile.html',{'city':show})
        else:
            return render(request,'editprofile.html')
    else:
        return redirect(f'login?return_url={return_url}')


# contact page function
def contact(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'): 
        if request.method=="POST":
            name=request.POST['name']
            message=request.POST['message']
            success_message=None
            temp=contactfrom(username=request.session.get('username'),name=name,message=message)
            temp.save()
            success_message="Your Message is submited"
            return render(request,'contact.html',{'success':success_message})
        elif request.method=="GET":
            return render(request,'contact.html')
    else:
        return redirect(f'login?return_url={return_url}')


# display record in dropdown of custom page
def displaycon():
    cab=component_master.objects.all().filter(con_id=1)
    mb=component_master.objects.all().filter(con_id=2)
    pro=component_master.objects.all().filter(con_id=3)
    gc=component_master.objects.all().filter(con_id=4)
    smps=component_master.objects.all().filter(con_id=5)
    ram=component_master.objects.all().filter(con_id=6)
    ssd=component_master.objects.all().filter(con_id=7)
    hdd=component_master.objects.all().filter(con_id=8)
    return {"Cabinets":cab,"Motherboard":mb,"Processor":pro,"GraphicCard":gc,"SMPS":smps,"RAM":ram,"SSD":ssd,"HDD":hdd}


# custom page function
def custombuild(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):
        if request.method=="POST":
            def selectedcon():
                cab=request.POST['Cabinets']
                mb=request.POST['Motherboard']
                pro=request.POST['Processor']
                gc=request.POST['GraphicCard']
                smps=request.POST['SMPS']
                ram=request.POST['RAM'] 
                ssd=request.POST['SSD']
                hdd=request.POST['HDD']
                error_message=None                

                for cab_price in component_master.objects.all().filter(con_name=cab):
                    cab_price=cab_price.con_price

                for mb_price in component_master.objects.all().filter(con_name=mb):
                    mb_price=mb_price.con_price
              
                for pro_price in component_master.objects.all().filter(con_name=pro):
                    pro_price=pro_price.con_price
                      
                for gc_price in component_master.objects.all().filter(con_name=gc):
                    gc_price=gc_price.con_price
               
                for smps_price in component_master.objects.all().filter(con_name=smps):
                    smps_price=smps_price.con_price

                for ram_price in component_master.objects.all().filter(con_name=ram):
                    ram_price=ram_price.con_price

                for ssd_price in component_master.objects.all().filter(con_name=ssd):
                    ssd_price=ssd_price.con_price

                for hdd_price in component_master.objects.all().filter(con_name=hdd):
                    hdd_price=hdd_price.con_price

                total=cab_price+mb_price+pro_price+gc_price+smps_price+ram_price+ssd_price+hdd_price
                global price
                price=total

                global productname
                productname=cab

                for check in user_master.objects.all().filter(username=request.session.get('username')):
                    check=check.name
                if check==None:
                    error_message="Plz Enter Your Address To Checkout"

                return {"Cabinets":cab,"Motherboard":mb,"Processor":pro,"GraphicCard":gc,"SMPS":smps,"RAM":ram,"SSD":ssd,"HDD":hdd,
                "cab_price":cab_price,"mb_price":mb_price,"pro_price":pro_price,"gc_price":gc_price,"smps_price":smps_price,"ram_price":ram_price,"ssd_price":ssd_price,"hdd_price":hdd_price,
                'total':total,'error':error_message}
                  
            return render(request,'checkout.html',selectedcon())

        elif request.method=="GET":                               
            return render(request,'custombuild.html',displaycon())
        else:
            return render(request,'custombuild.html',displaycon())
    else:
        return redirect(f'login?return_url={return_url}')


def customgamingpc(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):
        if request.method=="POST":
            gn=request.POST['gp']
            pb=request.POST['pro']
            global price
            global productname

            if gamespc.objects.all().filter(gamename=gn,ProcessorBrand=pb):
                show=gamespc.objects.all().filter(gamename=gn,ProcessorBrand=pb)
                for s in show:
                    productname=s.Cabinets
                    price=s.price
                return render(request,'checkout.html',{'gp':show})
            else:
                return HttpResponse('Sorry Can not load the database')
        elif request.method=="GET":
            show=games.objects.all()
            return render(request,'customgamingpc.html',{'gp':show})
        else:
            return render(request,'customgamingpc.html')
    else:
        return redirect(f'login?return_url={return_url}')


# all product payment and checkout page
def checkout(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):
        if request.method=="POST":
            link=request.POST['link']
            global pm
            global productname
            global price
            global success_message
            global error_message
            cityname=None
            ordername=None
            orderprice=None
            name=None
            pm=link
            location=user_master.objects.all().filter(username=request.session.get('username'))
            for loc in location:
                cityname=loc.city
                name=loc.name

            if productname!=None:
                ordername=productname

            if price!=None:
                orderprice=price
            
            if link=='COD':
                temp=order_master(username=request.session.get('username'),order_name=ordername,name=name,order_price=orderprice,city=cityname,paymethod=link)
                temp.save()
                success_message="Your order has been received"
                return render(request,'ordersuccessfully.html',{'success':success_message})
            elif link=="CP":
                return redirect(card)
        elif request.method=="GET":
            return render(request,'checkout.html')
        else:
            return render(request,'checkout.html')
    else:
        return redirect(f'login?return_url={return_url}')

def card(request):
    if request.method=="POST":
        cardNo=request.POST['cn']
        cardHolder=request.POST['ch']
        expmonth=request.POST['month']
        expyear=request.POST['year']
        cvv=request.POST['cvv']
        cityname=None
        name=None
        ordername=None
        orderprice=None
        bal=None
        global productname
        global price
        global pm
        global success_message
        global error_message
        location=user_master.objects.all().filter(username=request.session.get('username'))
        for loc in location:
            cityname=loc.city
            name=loc.name

        if productname!=None:
            ordername=productname

        if price!=None:
            orderprice=price
        check=card_payment.objects.filter(CardNumber=cardNo,CardHolder=cardHolder,expiresmonth=expmonth,expiresyear=expyear,cvv=cvv)
        
        for bal in check:
            bal=bal.balance
        if check.exists():
            cp=card_payment.objects.filter(CardNumber=cardNo).update(balance=bal-orderprice)
            
            if cp!=None:
                temp=order_master(username=request.session.get('username'),order_name=ordername,name=name,order_price=orderprice,city=cityname,paymethod=pm)
                temp.save()
                success_message="Payment SuccessFully"
                return render(request,'ordersuccessfully.html',{'success':success_message})
            else:
                error_message="Payment Failed"
                return render(request,'ordersuccessfully.html',{'error':error_message})
        else:
            error_message="Card Not Found"
            return render(request,'ordersuccessfully.html',{'error':error_message})
            
    elif request.method=="GET":
        return render(request,'card.html')
    else:
        return render(request,'card.html')

def order(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):
        show=order_master.objects.all().filter(username=request.session.get('username'))
        return render(request,'order.html',{'order':show})
    else:
        return redirect(f'login?return_url={return_url}')    

def os(request):
    return_url=request.META['PATH_INFO']
    if request.session.get('username'):
        return render(request,'ordersuccessfully.html')   
    else:
        return redirect(f'login?return_url={return_url}')