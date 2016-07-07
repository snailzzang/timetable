from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from timeline.models import *


@login_required
def account(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	timeline = get_object_or_404(Timeline, owner=user)

	same_user = request.user.pk == user.pk
	has_permission = timeline.viewers.filter(id=request.user.id).exists()

	if (not same_user) and (not has_permission):
		return render(request, '403.html')

	study_list = Study.objects.filter(user=user).order_by('-date')
	for study in study_list:
		# study.cat = [ each_cat.name for each_cat in study.category.all()]
		study.cat = study.get_category_names()
	
	categories = Category.objects.filter(user=user)

	context = {
		'study_list' : study_list,
		'categories' : categories,
		'user' : request.user,
	}
	return render(request, 'timeline/index.html', context)


@login_required
def add(request):
	timeline = get_object_or_404(Timeline, owner=request.user)
		
	user = request.user
	viewer_id = int(request.POST['viewer_id_to_add'])

	try:
		viewer = User.objects.get(pk=viewer_id)
		if viewer_id == request.user.id:
			pass
		elif not user.viewers.filter(id=viewer_id).exists():
			timeline.viewers.add(viewer)
	except: 
		pass

	return redirect(reverse('index'))


@login_required
def delete(request):
	viewer_id_list_to_del = request.POST.getlist('each_id_to_del')
	user = request.user
	timeline = Timeline.objects.get(owner=request.user)

	for each_id in viewer_id_list_to_del:
		viewer = User.objects.get(pk=int(each_id))
		timeline.viewers.remove(viewer)
		# timeline.viewers = timeline.viewers.exclude(id=viewer.id)  << 이렇게 해도 동일한 결과

		# each_viewer = timeline.viewers.get(id=int(each_id))
		# each_viewer.delete()  
		# : 이렇게 하면 user 인스턴스가 통째로 삭제됨. 본의 아니게 남의 계정을 삭제하는 부작용
	
	return redirect(reverse('index'))
