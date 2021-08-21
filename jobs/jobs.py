from django.conf import settings
from links.models import Link

def schedule_db_update():
	qs = Link.objects.all()
	for link in qs:
		link.save()
	print('db updated')

