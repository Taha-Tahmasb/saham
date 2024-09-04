from .serializer import InvestSerializer
from .models import Investment , Sandogh , User
from rest_framework.generics import ListAPIView ,CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import HttpResponse, JsonResponse



class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass


class NewInvestment(CreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestSerializer


class MyInvests(ListAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Investment.objects.filter(user = self.request.user)


@csrf_exempt
def prediction(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        sandogh = body['sandogh']
        start_month = body['start_month']
        finish_month = body['finish_month']
        invest = body['invest']
        start = Sandogh.objects.get(name = start_month)
        finish = Sandogh.objects.get(name = finish_month)

        if sandogh == "Gold":
            start_price = start.Gold
            finish_price = finish.Gold
        elif sandogh == "Silver":
            start_price = start.Silver
            finish_price = finish.Silver
        elif sandogh == "Copper":
            start_price = start.Copper
            finish_price = finish.Copper
        elif sandogh == "Oil":
            start_price = start.Oil
            finish_price = finish.Oil
        elif sandogh == "Steel":
            start_price = start.Steel
            finish_price = finish.Steel
        else:
            return HttpResponse("no boors found")
        
        sahm = invest / start_price
        net_profit = round((finish_price * sahm) - (invest) ,2)
        percent_profit = f"{round(net_profit / invest * 100 , 2)}%"

        profits = {
            "Gold":finish.Gold / start.Gold ,
            "Silver":finish.Silver / start.Silver,
            "Copper":finish.Copper / start.Copper,
            "Oil":finish.Oil / start.Oil,
            "Steel":finish.Steel / start.Steel
        }
        best_market = max(profits , key=profits.get)
        potential_profit = round((max(profits.values())-1)*invest , 2)
        return JsonResponse({
            "market name":sandogh,
            "your investment":f"{invest} $",
            "start month":start.name,
            "finish month":finish.name,
            "net profit":f"{net_profit} $",
            "percentage":percent_profit,
            "best market":best_market,
            "potential profit in best market":f"{potential_profit} $"
        },safe= False)
        




