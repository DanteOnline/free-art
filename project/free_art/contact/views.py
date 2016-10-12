from django.shortcuts import render
from django.views.generic import FormView
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from contact.form import ContactForm
# Create your views here.

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        me = settings.EMAIL_HOST_USER
        recipients = [me]
        message += '\n from email: %s, name: %s'%(email, name)
        try:
            send_mail(subject, message, me, recipients)
            return render(self.request, 'message_good.html')
        except BadHeaderError:
            return HttpResponse('Bad header found')
        except:
            return render(self.request, 'message_error.html')