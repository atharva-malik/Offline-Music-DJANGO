from django.utils import timezone
from django.core.exceptions import PermissionDenied, BadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.http import Http404
from .models import Choice, Question, UserDetails
from django.urls import reverse
# from django.template import loader
from django.views import generic
from .forms import SongNameForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('question_text')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        user_details = UserDetails.objects.filter(user_name=request.user)
        try:
            if user_details[0].has_voted:
                raise PermissionDenied(
                    "You have already voted!"
                )
        except IndexError:
            u = UserDetails(has_voted=True, user_name=request.user)
            u.save()
            selected_choice.votes += 1
            selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


@login_required
def new_question(request):
    if request.method == 'POST':
        form = SongNameForm(request.POST)
        if form.is_valid():
            q1 = Question.objects.filter(question_text=form.cleaned_data['song_name'])
            try:
                if q1[0] in Question.objects.all():
                    raise BadRequest(
                        "That question already exists!"
                    )
            except IndexError:
                q = Question(question_text=form.cleaned_data['song_name'], pub_date=timezone.now())
                q.save()
                q.choice_set.create(choice_text='Yes! Add this!', votes=0)
                return HttpResponseRedirect('/polls/')
    else:
        form = SongNameForm()
    return render(request, 'polls/new_question.html', context={"form": form})
