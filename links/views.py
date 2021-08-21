from django.shortcuts import render, redirect
from .forms import AddLinkForm
from .models import Link

def home_view(request):
	no_discounted = 0
	error = None

	form = AddLinkForm(request.POST or None)

	if request.method == 'POST':
		try:
			if form.is_valid():
				form.save()
		except AttributeError:
			error = "Ups ... couldn't get the name or the price"
		except:
			error = "Ups ... something went wrong"

	form = AddLinkForm()

	qs = Link.objects.all()
	items_no = qs.count()

	if items_no > 0:
		discount_list = []
		for item in qs:
			if item.old_price > item.current_price:
				discount_list.append(item)
			no_discounted = len(discount_list)

	context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }

	return render(request, 'links/main.html', context)

def deleteLink(request, pk):
	link = Link.objects.get(id=pk)
	link.delete()
	return redirect('home')

def udateLinks(request):
	qs = Link.objects.all()
	for link in qs:
		link.save()

	return redirect('home')