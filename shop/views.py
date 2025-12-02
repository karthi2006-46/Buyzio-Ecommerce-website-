from django.http import  JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from shop.form import CustomUserForm
from .models import category, Products,Cart,Favourite
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def home(request):
    products = Products.objects.filter(trending=True) 
    return render(request, "shop/index.html",{"products": products})

def favviewpage(request):
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        return render(request, "shop/fav.html", {"fav": fav})
    else:
        messages.warning(request, "Login required to view Favourite items!")
        return redirect('login')

 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

def cart_page(request):
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        return render(request, "shop/cart.html", {"cart": cart})
    else:
        messages.warning(request, "Login required to view Cart  items!")
        return redirect('login')


def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
 
def add_to_cart(request):
    # AJAX + POST only
    if request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "POST":

        # Not logged in
        if not request.user.is_authenticated:
            return JsonResponse(
                {
                    "status": "not_logged_in",
                    "message": "Please login to add items to cart.",
                    "redirect_url": reverse("login"),  # change if your login url name is different
                },
                status=401,
            )

        # Logged in: parse JSON
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid data."},
                status=400,
            )

        product_qty = int(data.get("product_qty", 0))
        product_id = data.get("pid")

        if product_qty <= 0 or not product_id:
            return JsonResponse(
                {"status": "error", "message": "Invalid quantity or product."},
                status=400,
            )

        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Product not found."},
                status=404,
            )

        # already in cart?
        if Cart.objects.filter(user=request.user, product_id=product_id).exists():
            return JsonResponse(
                {"status": "error", "message": "Product is already in your cart."},
                status=200,
            )

        # stock check
        if product.quantity < product_qty:
            return JsonResponse(
                {"status": "error", "message": "Product stock not available."},
                status=200,
            )

        Cart.objects.create(
            user=request.user,
            product_id=product_id,
            product_qty=product_qty,
        )

        return JsonResponse(
            {"status": "success", "message": "Product added to cart."},
            status=200,
        )

    return JsonResponse(
        {"status": "error", "message": "Invalid access."},
        status=400,
    )


def add_to_fav(request):
    # AJAX + POST only
    if request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "POST":

        # Not logged in
        if not request.user.is_authenticated:
            return JsonResponse(
                {
                    "status": "not_logged_in",
                    "message": "Please login to add items to favourites.",
                    "redirect_url": reverse("login"),
                },
                status=401,
            )

        # Logged in
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid data."},
                status=400,
            )

        product_id = data.get("pid")

        if not product_id:
            return JsonResponse(
                {"status": "error", "message": "Invalid product."},
                status=400,
            )

        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Product not found."},
                status=404,
            )

        # already in favourites
        if Favourite.objects.filter(user=request.user, product_id=product_id).exists():
            return JsonResponse(
                {"status": "error", "message": "Product already in favourites."},
                status=200,
            )

        Favourite.objects.create(
            user=request.user,
            product_id=product_id
        )

        return JsonResponse(
            {"status": "success", "message": "Product added to favourites."},
            status=200,
        )

    return JsonResponse(
        {"status": "error", "message": "Invalid access."},
        status=400,
    )


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect("/")

def login_page(request):
    # If already logged in, go to home
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('home')        # ✅ always return a response
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')       # ✅ return here too

    # For GET request just show login page
    return render(request, "shop/login.html")   # ✅ final return


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now..!")
            return redirect('/login')
    return render(request, "shop/register.html",{'form':form})


def collections(request):
    categories = category.objects.filter(status=0)
    return render(request, "shop/collections.html", {"category": categories})


def collectionsview(request, name):
    if category.objects.filter(name=name, status=0).exists():
        products = Products.objects.filter(category__name=name)
        return render(request, "shop/products/index.html", {"products": products, "category_name": name})
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')
    
def product_details(request, cname, pid):
    # cname -> category name from URL
    # pid   -> product id from URL (int)

    # 1) Check category
    try:
        cat = category.objects.get(name=cname, status=0)
    except category.DoesNotExist:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

    # 2) Check product in that category
    try:
        product = Products.objects.get(id=pid, category=cat, status=0)
    except Products.DoesNotExist:
        messages.error(request, "No such Product Found")
        return redirect('collections')

    # 3) Render details page
    return render(request, "shop/products/product_deatils.html", {"products": product})
# def product_details(request, cname, pname):
#     return HttpResponse("Product Details")
# def product_details(request, cname, pname):
#     if category.objects.filter(name=cname, status=0).exists():
#         if Products.objects.filter(name=pname, status=0).exists():
#             product = Products.objects.filter(name=pname, status=0).first()
#             return render(request, "shop/products/product_deatils.html", {"products": product})
#         else:
#             messages.error(request, "No such Product Found")
#             return redirect('collections')
#     else:
#         messages.warning(request, "No Such Category Found")
#         return redirect('collections')




    # for testing
    # return HttpResponse(f"{cname} - {pname}")
 

