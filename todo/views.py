from django.shortcuts import render, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.shortcuts import redirect
# Create your views here.

def activity_list(request):
	posts = Todo.objects.all()
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.time.strftime("%d/%m/%y %H:%M") 
			post.save()
		return redirect('todo:activity_list')
	else:
		form = TodoForm()
	context_dict = {
		'todo': posts,
		'form': form
	}
	return render(request, 'todo/schedule_list.html', context_dict)

def del_activity(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    post.delete()
    return redirect('todo:activity_list')
