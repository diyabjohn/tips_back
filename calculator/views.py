from rest_framework import generics
from .models import Tip
from .serializers import TipSerializer

class TipListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class TipRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Tip Calculator API!")

from django.shortcuts import render
from .models import Tip
from .forms import TipForm

def index(request):
    return render(request, 'index.html')

def tip_form(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            # Process form data and calculate tip
            bill_amount = form.cleaned_data['bill_amount']
            tip_percentage = form.cleaned_data['tip_percentage']
            total_tip = bill_amount * (tip_percentage / 100)
            total_amount = bill_amount + total_tip
            # Save the calculation to the database
            Tip.objects.create(
                bill_amount=bill_amount,
                tip_percentage=tip_percentage,
                total_tip=total_tip,
                total_amount=total_amount
            )
            return render(request, 'tip_detail.html', {'bill_amount': bill_amount, 'tip_percentage': tip_percentage, 'total_tip': total_tip, 'total_amount': total_amount})
    else:
        form = TipForm()
    return render(request, 'tip_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Tip

def tip_detail(request, pk):
    tip = get_object_or_404(Tip, pk=pk)
    return render(request, 'tip_detail.html', {'tip': tip})

# Create your views here.
