from django.shortcuts import render
import razorepay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorepay.Client(
            auth=("rzp_test_2N4mcKG2I2htW3", "2ey41M3BdVB1IKwzOKtjjv3q"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')



@csrf_exempt
def success(request):
    return render(request, "success.html")