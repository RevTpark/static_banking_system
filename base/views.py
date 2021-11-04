from django.shortcuts import render, get_object_or_404
from user.models import Account, User
from django.contrib import messages
from .models import LogTracker

def home_view(request):
    acc = Account.objects.all()
    context = {
        "accounts": acc
    }
    return render(request, "index.html", context)


def user_detail_view(request, **kwargs):
    user_det = get_object_or_404(User, username=kwargs.get("name"))
    acc_det = Account.objects.values().get(id=kwargs.get("id"))
    context = {
        "user": user_det,
        "acc": acc_det
    }
    return render(request, "detail.html", context)


def transfer_view(request):
    if request.method == "POST":
        data = request.POST
        sendFrom = Account.objects.get(user__username=data.get("sendFrom"))
        sendTo = Account.objects.get(user__username=data.get("sendTo"))
        amount = int(data.get("amount"))
        if sendFrom == sendTo:
            messages.error(request, "Transfer between same account is not allowed!")
        elif sendFrom.balance >= amount:
            sendFrom.balance -= amount
            sendFrom.save()
            sendTo.balance += amount
            sendTo.save()
            LogTracker.objects.create(isFrom=sendFrom, isTo=sendTo, ofAmount=amount, isSuccess=True)
            messages.success(request, f"Successfully transferred $ {amount} from {sendFrom} to {sendTo}!")
        else:
            LogTracker.objects.create(isFrom=sendFrom, isTo=sendTo, ofAmount=amount, isSuccess=False)
            messages.error(request, f"Not sufficient funds in {sendFrom} to make the transactions...")

    context = {
        "accounts": Account.objects.all()
    }
    return render(request, "transfer.html", context)


def log_tracker(request):
    logs = LogTracker.objects.all().order_by("-atTime")
    context = {
        "user_logs": logs
    }
    return render(request, "logs.html", context)
