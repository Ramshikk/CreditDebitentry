from django.shortcuts import render
from account.models import Entry
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def credit_debit_entry(request):
    message=""
    if request.method == 'POST':
        if request.POST.get("particulars") == "":
            message="please enter particulars"
        elif  request.POST.get("amount") == "":
            message="Please enter amount"
        else:
            todaysdate=request.POST.get("date")
            date_obj = datetime.strptime(todaysdate, "%Y-%m-%d")
            obj=Entry.objects.create(date=date_obj,
                    particulars=request.POST.get("particulars") ,
                    transaction_type=request.POST.get("transactionType"),
                    amount=request.POST.get("amount") )
            message="Details added successfully"
            




    return render(request,'credit_debit_entry.html',{'message':message})
@csrf_exempt
def  entry_view(request):
    entrydetails=""
    entrydetails=Entry.objects.all()
    if request.method == 'POST':
        entrydetails=Entry.objects.filter(date=request.POST.get("date"))
    else:
        entrydetails=Entry.objects.all()
    return render(request,'journal_entry_screen.html',{'entrydetails':entrydetails})
    
