from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import NameForm, ContactForm
from .models import Question, Choice
from django.core.cache import cache


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'polls/thanks.html', {'form': form})

    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})


def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except ConnectionRefusedError:
                return render(request, 'polls/thanks.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'polls/contact.html', {'form': form})


class ThanksView(generic.DetailView):
    model = Question
    template_name = 'polls/thanks.html'


@cache_page(60 * 15)
def my_view(request, code):
    # cache.add('code_cash', code, 30)
    # print(cache.get('code_cash'))
    return HttpResponse(f"Here's the response for {code}"
                        f"\nThe cache value of this was was added {cache.get('code_cash')}")
