from django.shortcuts import redirect, render, get_object_or_404
from app.models import Mutter


def mutter_list(request):

    if request.method == 'POST':
        mutter = Mutter.objects.create(content=request.POST.get("content", ""))
        mutter.save()
        redirect('mutter_list')

    keyword = request.GET.get(key="keyword", default=None)

    if keyword:
        mutters = Mutter.objects.filter(content__icontains=keyword).order_by("created_at")
    else:
        mutters = Mutter.objects.all().order_by("created_at")

    return render(request, 'mutter_list.html', dict(mutters=mutters))


def mutter_detail(request, mutter_id):

    # mutter_idが一致するつぶやきを取得する
    #mutter = Mutter.objects.get(id=mutter_id)
    mutter = get_object_or_404(Mutter, id=mutter_id)
    return render(request, 'mutter_detail.html', dict(mutter=mutter))
